class AddPickedToCallLogs < ActiveRecord::Migration[8.1]
  def change
    add_column :call_logs, :picked, :boolean
  end
end
