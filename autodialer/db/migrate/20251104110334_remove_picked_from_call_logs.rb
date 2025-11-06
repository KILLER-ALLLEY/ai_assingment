class RemovePickedFromCallLogs < ActiveRecord::Migration[8.1]
  def change
    remove_column :call_logs, :picked, :boolean
  end
end
