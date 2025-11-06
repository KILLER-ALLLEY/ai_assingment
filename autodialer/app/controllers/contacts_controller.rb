class ContactsController < ApplicationController
  require 'twilio-ruby'
  require 'csv'

  def index
    @contacts = Contact.all
  end

  def new
    @contact = Contact.new
  end

  def create
    @contact = Contact.new(contact_params)
    if @contact.save
      redirect_to contacts_path, notice: "Contact added successfully!"
    else
      render :new
    end
  end

  # 🔹 Upload CSV
  def upload
    if params[:file].present?
      begin
        CSV.foreach(params[:file].path, headers: true) do |row|
          Contact.create!(
            name: row['Name'],
            phone: row['Phone'],
            status: "Pending"
          )
        end
        flash[:notice] = "Contacts uploaded successfully!"
      rescue => e
        flash[:alert] = "Error reading CSV: #{e.message}"
      end
    else
      flash[:alert] = "Please upload a CSV file."
    end
    redirect_to contacts_path
  end

  # 🔹 Autodial all contacts
  def autodial
    @contacts = Contact.all
    account_sid = ENV['TWILIO_ACCOUNT_SID']
    auth_token  = ENV['TWILIO_AUTH_TOKEN']
    from_number = ENV['TWILIO_PHONE_NUMBER']
    client = Twilio::REST::Client.new(account_sid, auth_token)

    @contacts.each do |contact|
      begin
        call = client.calls.create(
          from: from_number,
          to: contact.phone,
          url: "https://demo.twilio.com/docs/voice.xml"
        )

        contact.update(status: "Call Initiated")
        CallLog.create!(
          phone_number: contact.phone,
          status: "Success",
          message: "Autodial initiated successfully",
          sid: call.sid
        )
      rescue Twilio::REST::RestError => e
        contact.update(status: "Failed: #{e.message}")
        CallLog.create!(
          phone_number: contact.phone,
          status: "Failed",
          message: e.message
        )
        Rails.logger.error("❌ Twilio autodial failed for #{contact.phone}: #{e.message}")
        next  # ✅ Continue to next contact even if this one fails
      rescue => e
        contact.update(status: "Error: #{e.message}")
        Rails.logger.error("⚠️ Unexpected error on autodial: #{e.message}")
        next
      end
    end

    redirect_to contacts_path, notice: "Autodial initiated for all contacts."
  end

  # 🔹 Reset all contacts (Clear DB)
  def reset
    Contact.destroy_all
    CallLog.delete_all
    redirect_to contacts_path, notice: "All contacts and logs cleared."
  end

  private

  def contact_params
    params.require(:contact).permit(:name, :phone)
  end
end
