Rails.application.routes.draw do
  get "voice/speak"

  # 🧠 AI Command Route
  post "/ai/command", to: "ai#command"

  # 📝 Blog routes
  resources :blogs do
    collection do
      post :generate_ai   # For AI-based blog generation
    end
  end

  # ☎️ Contact management
  resources :contacts, only: [:index, :new, :create] do
    collection do
      post :upload
      post :autodial
      delete :reset
    end
  end

  # 📞 Call logs
  resources :calls, only: [:index, :create] do
    collection do
      post :status_callback   # ✅ Twilio call status tracking
      delete :reset_logs
    end
  end

  # 🏠 Default page
  root "contacts#index"
end
