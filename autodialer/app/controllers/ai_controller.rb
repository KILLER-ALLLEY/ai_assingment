class AiController < ApplicationController
  skip_before_action :verify_authenticity_token, only: [:command]

  def command
    prompt = params[:prompt]
    return render json: { error: "Prompt cannot be empty" }, status: 400 if prompt.blank?

    begin
      require 'openai'
      require 'net/http'
      require 'json'
      require 'uri'
      
      # Make direct HTTP request to OpenAI API
      uri = URI('https://api.openai.com/v1/chat/completions')
      http = Net::HTTP.new(uri.host, uri.port)
      http.use_ssl = true
      
      request = Net::HTTP::Post.new(uri.path, {
        'Content-Type' => 'application/json',
        'Authorization' => "Bearer #{ENV.fetch('OPENAI_API_KEY')}"
      })
      
      request.body = {
        model: "gpt-4o-mini",
        messages: [
          {
            role: "system",
            content: "You are an assistant that converts plain English into structured JSON commands for an autodialer app. You only respond with JSON. Example: {\"action\": \"make_call\", \"number\": \"+919876543210\"}"
          },
          { role: "user", content: prompt }
        ],
        temperature:0,
        top_p: 1
      }.to_json
      
      response = http.request(request)
      response_body = JSON.parse(response.body)
      
      result = JSON.parse(response_body.dig("choices", 0, "message", "content")) rescue {}

      case result["action"]
      when "make_call"
        CallsController.new.initiate_call(result["number"], source: "AI")
        render json: { message: "📞 Calling #{result['number']}..." }

      when "clear_logs"
        CallLog.delete_all
        render json: { message: "🧹 All call logs cleared." }

      else
        render json: { message: "❓ Unknown action or invalid command." }
      end

    rescue => e
      Rails.logger.error("AIController error: #{e.message}")
      Rails.logger.error("Error backtrace: #{e.backtrace.first(5).join("\n")}")
      render json: { error: e.message }, status: 500
    end
  end
end