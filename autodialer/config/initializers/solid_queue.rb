# config/initializers/solid_queue.rb
# Force SolidQueue to use the primary ActiveRecord database in production

if defined?(SolidQueue)
  SolidQueue::Record.connects_to database: { writing: :primary }
end
