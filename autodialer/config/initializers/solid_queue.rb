# config/initializers/solid_queue.rb
if defined?(SolidQueue)
  SolidQueue::Engine.configure do
    config.active_record.database = :primary
  end
end
