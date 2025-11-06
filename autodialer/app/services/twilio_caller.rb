require 'twilio-ruby'

class TwilioCaller
  def initialize
    @client = Twilio::REST::Client.new(
      ENV['TWILIO_ACCOUNT_SID'],
      ENV['TWILIO_AUTH_TOKEN']
    )
  end

  def make_call(to)
    @client.calls.create(
      from: ENV['TWILIO_PHONE_NUMBER'],
      to: to,
      url: 'http://demo.twilio.com/docs/voice.xml'
    )
  end
end
