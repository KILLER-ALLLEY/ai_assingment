class CallsController < ApplicationController
  require 'twilio-ruby'
  skip_before_action :verify_authenticity_token, only: [:create_via_ai]

  # 📞 Manual call
  def create
    phone_number = params[:phone_number] || params[:phone]
    if phone_number.blank?
      flash[:alert] = "Phone number missing!"
      return redirect_to contacts_path
    end

    initiate_call(phone_number, source: "manual")
    redirect_to contacts_path
  end

  # 🤖 AI-triggered call
  def create_via_ai
    phone_number = params[:phone_number]
    initiate_call(phone_number, source: "AI")
    head :ok
  end

  # 🧹 Clear logs
  def reset_logs
    CallLog.delete_all
    flash[:notice] = "✅ All call logs cleared successfully."
    redirect_to contacts_path
  end

  def initiate_call(phone_number, source: "manual")
    contact = Contact.find_by(phone: phone_number)
    account_sid = ENV['TWILIO_ACCOUNT_SID']
    auth_token  = ENV['TWILIO_AUTH_TOKEN']
    from_number = ENV['TWILIO_PHONE_NUMBER']

    client = Twilio::REST::Client.new(account_sid, auth_token)

    begin
      call = client.calls.create(
        from: from_number,
        to: phone_number,
        url: "https://handler.twilio.com/twiml/EH268f2c1bd6c5981a14a41b57b10567da"
      )

      contact&.update(status: "Success")
      CallLog.create!(
        phone_number: phone_number,
        status: "Success",
        message: "#{source.capitalize} call initiated successfully",
        sid: call.sid
      )

      Rails.logger.info("📞 #{source.upcase} call to #{phone_number} successful")
    rescue StandardError => e
      contact&.update(status: "Failed: #{e.message}")
      CallLog.create!(
        phone_number: phone_number,
        status: "Failed",
        message: e.message
      )

      Rails.logger.error("❌ Call failed: #{e.message}")
    end
  end
end