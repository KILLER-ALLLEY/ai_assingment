class CreateCallLogs < ActiveRecord::Migration[8.1]
  def change
    create_table :call_logs do |t|
      t.string :phone_number
      t.string :status
      t.text :message
      t.string :sid

      t.timestamps
    end
  end
end
