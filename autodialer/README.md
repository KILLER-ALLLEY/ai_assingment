# 📞 Ruby Contact Management & Blog Platform

A comprehensive Ruby web application for managing contacts, auto-dialing, and AI-powered blog generation.

![Ruby](https://img.shields.io/badge/Ruby-3.0+-red.svg)
![Rails](https://img.shields.io/badge/Rails-7.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### 📇 Contact Management
- 📤 **CSV Upload** - Bulk import contacts from CSV files
- ✍️ **Manual Entry** - Add individual contacts through an intuitive form
- 📊 **Contact List** - View and manage all your contacts in one place
- 🔍 **Search & Filter** - Quickly find specific contacts

### 📞 Auto-Dialing System
- 🤖 **Automated Calling** - Auto-dial all contacts in your database
- 📋 **Call Queue Management** - Organize and prioritize calls
- 📈 **Call Tracking** - Monitor call status and history
- ⏱️ **Scheduling** - Set up automated calling campaigns

### 📝 Blog Management
- 🤖 **AI Blog Generation** - Automatically generate blog posts
- ✏️ **Rich Text Editor** - Create and edit blogs with ease
- 📚 **Blog Library** - Manage all your published content
- 🔖 **Categories & Tags** - Organize blogs by topic
- 👁️ **Preview Mode** - Review blogs before publishing

## 🚀 Getting Started

### Prerequisites

- Ruby 3.0 or higher
- Rails 7.0 or higher
- PostgreSQL (or your preferred database)
- Node.js and Yarn
- Twilio account (for auto-dialing features)
- OpenAI API key (for blog generation)

### Installation

1. **Install Dependencies**
```bash
bundle install
yarn install
```

2. **Database Setup**
```bash
rails db:create
rails db:migrate
rails db:seed
```

3. **Environment Variables**

Create a `.env` file in the root directory:
```env
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=your_database_url
```

### Running the Application
```bash
rails server
```

Then open your browser and navigate to: **http://localhost:3000**

## 📋 How to Use

### Contact Management

#### Uploading Contacts via CSV

1. Navigate to **Contacts** → **Upload CSV**
2. Click **Choose File** and select your CSV file
3. Ensure your CSV has the following columns:
```
   first_name,last_name,email,phone_number
```
4. Click **Upload** to import contacts

**Sample CSV Format:**
```csv
name,phone_number
John Doe,+1234567890
Jane Smith,+0987654321
```

#### Adding Contacts Manually

1. Navigate to **Contacts** → **Add New Contact**
2. Fill in the contact details:
   - First Name
   - Last Name
   - Email Address
   - Phone Number
   - Company (optional)
   - Notes (optional)
3. Click **Save Contact**

#### Managing Contacts

- **View All Contacts**: Navigate to **Contacts** → **All Contacts**
- **Edit Contact**: Click the **Edit** button next to any contact
- **Delete Contact**: Click the **Delete** button and confirm
- **Export Contacts**: Click **Export to CSV** to download all contacts

### Auto-Dialing

#### Setting Up a Call Campaign

1. Navigate to **Dialer** → **New Campaign**
2. Configure your campaign:
   - Campaign Name
   - Select Contacts (or use filters)
   - Call Script/Message
   - Schedule (immediate or future)
3. Click **Start Campaign**

#### Monitoring Calls

1. Navigate to **Dialer** → **Call History**
2. View call status for each contact:
   - ✅ Completed
   - 📞 In Progress
   - ❌ Failed
   - ⏳ Scheduled
3. Filter by date, status, or contact

#### Managing Call Queue

- **Pause Campaign**: Click **Pause** to temporarily stop dialing
- **Resume Campaign**: Click **Resume** to continue
- **Stop Campaign**: Click **Stop** to end the campaign permanently

### Blog Management

#### Auto-Generating Blogs

1. Navigate to **Blogs** → **Generate New Blog**
2. Enter blog parameters:
   - **Topic/Title**: Main subject of the blog
   - **Keywords**: Relevant SEO keywords (comma-separated)
   - **Tone**: Professional, Casual, Technical, etc.
   - **Length**: Short (500 words), Medium (1000 words), Long (2000 words)
3. Click **Generate Blog**
4. Wait for AI to create your content (usually 10-30 seconds)
5. Review and edit if needed
6. Click **Publish** or **Save as Draft**

#### Creating Blogs Manually

1. Navigate to **Blogs** → **New Blog Post**
2. Fill in the details:
   - Title
   - Content (using rich text editor)
   - Featured Image
   - Categories
   - Tags
   - Meta Description (for SEO)
3. Click **Publish** or **Save as Draft**

#### Managing Blogs

- **View All Blogs**: Navigate to **Blogs** → **All Posts**
- **Edit Blog**: Click on any blog title or the **Edit** button
- **Delete Blog**: Click **Delete** and confirm
- **Unpublish Blog**: Change status from **Published** to **Draft**

## 🎨 User Interface

### Dashboard
```
┌─────────────────────────────────────────────────┐
│  📊 Dashboard                                   │
├─────────────────────────────────────────────────┤
│  📇 Contacts: 1,234     📞 Calls Today: 56     │
│  📝 Blogs: 48          🤖 AI Generated: 32     │
└─────────────────────────────────────────────────┘
```

### Contact List
```
┌─────────────────────────────────────────────────┐
│  📇 All Contacts                    [+ Add New] │
│  [Search...] [Filter] [Export CSV]             │
├─────────────────────────────────────────────────┤
│  Name          Email              Phone         │
│  John Doe      john@example.com   +1234567890  │
│  Jane Smith    jane@example.com   +0987654321  │
└─────────────────────────────────────────────────┘
```

### Blog Editor
```
┌─────────────────────────────────────────────────┐
│  ✏️ Create New Blog                             │
├─────────────────────────────────────────────────┤
│  Title: [Enter blog title...]                  │
│  [Rich Text Editor Area]                        │
│  Categories: [Technology] [+]                   │
│  [🤖 Auto Generate] [💾 Save] [📤 Publish]     │
└─────────────────────────────────────────────────┘
```

## 📁 Project Structure
```
app/
├── controllers/
│   ├── contacts_controller.rb
│   ├── dialer_controller.rb
│   └── blogs_controller.rb
├── models/
│   ├── contact.rb
│   ├── call.rb
│   └── blog.rb
├── services/
│   ├── csv_import_service.rb
│   ├── auto_dialer_service.rb
│   └── blog_generator_service.rb
├── jobs/
│   ├── auto_dial_job.rb
│   └── blog_generation_job.rb
└── views/
    ├── contacts/
    ├── dialer/
    └── blogs/
```

## 🔧 Configuration

### Twilio Setup (Auto-Dialing)

1. Sign up for a Twilio account at https://www.twilio.com
2. Get your Account SID and Auth Token from the dashboard
3. Purchase a phone number for making calls
4. Add credentials to your `.env` file

### OpenAI Setup (Blog Generation)

1. Create an account at https://platform.openai.com
2. Generate an API key from the API settings
3. Add the key to your `.env` file
4. Choose your preferred model (GPT-4 recommended for best results)

### Database Configuration

Edit `config/database.yml`:
```yaml
development:
  adapter: postgresql
  database: your_app_development
  pool: 5
  timeout: 5000

test:
  adapter: postgresql
  database: your_app_test
  pool: 5
  timeout: 5000

production:
  url: <%= ENV['DATABASE_URL'] %>
```

### CSV Upload Settings

Maximum file size and allowed formats can be configured in `config/initializers/csv_upload.rb`:
```ruby
CSV_UPLOAD = {
  max_file_size: 10.megabytes,
  allowed_extensions: ['.csv', '.txt'],
  max_rows: 10_000
}
```

## 🐛 Troubleshooting

### CSV Upload Issues

**Problem**: CSV upload fails or imports incorrect data

**Solutions**:
- Ensure CSV is UTF-8 encoded
- Check that column headers match exactly: `first_name,last_name,email,phone_number`
- Remove any special characters or extra spaces
- Verify file size is under 10MB

### Auto-Dialer Not Working

**Problem**: Calls are not being placed

**Solutions**:
- Verify Twilio credentials in `.env` file
- Check Twilio account balance
- Ensure phone numbers are in E.164 format (e.g., +1234567890)
- Check that contacts have valid phone numbers
- Review Twilio error logs in the dashboard

### Blog Generation Fails

**Problem**: AI blog generation times out or produces errors

**Solutions**:
- Verify OpenAI API key is valid
- Check API usage limits on your OpenAI account
- Try generating shorter content first
- Ensure stable internet connection
- Check background job queue is running: `rails jobs:work`

### Database Connection Errors

**Problem**: Cannot connect to database

**Solutions**:
- Ensure PostgreSQL is running: `pg_ctl status`
- Check database credentials in `config/database.yml`
- Run migrations: `rails db:migrate`
- Reset database if needed: `rails db:reset`

## 📊 Database Schema

### Contacts Table
```ruby
create_table "contacts" do |t|
  t.string "first_name"
  t.string "status"
  t.string "phone_number"
end
```

### Calls Table
```ruby
create_table "calls" do |t|
  t.references "contact"
  t.string "status"
  t.string "twilio_sid"
end
```

### Blogs Table
```ruby
create_table "blogs" do |t|
  t.string "title"
  t.text "content"
  t.boolean "ai_generated"
end
```

## ⚡ Performance Tips

### Contact Management
- Import contacts in batches of 1,000 or less for optimal performance
- Use background jobs for large CSV imports
- Regularly clean up duplicate contacts

### Auto-Dialing
- Limit concurrent calls to 5-10 to avoid rate limiting
- Schedule calls during business hours for better response rates
- Use call queues to prioritize important contacts

### Blog Generation
- Generate blogs during off-peak hours to reduce wait time
- Cache generated content to avoid regenerating similar blogs
- Use background jobs for multiple blog generation requests

## 🔒 Security Best Practices

- Never commit `.env` file to version control
- Use strong passwords for database access
- Regularly rotate API keys
- Implement rate limiting on CSV uploads
- Sanitize all user inputs
- Enable HTTPS in production
- Regularly backup your database

## 📈 API Integration

### Twilio (Voice Calls)
- Uses Twilio Voice API for automated calling
- Supports call recording and transcription
- Webhook endpoints for call status updates

### OpenAI (Blog Generation)
- Uses GPT-4 or GPT-3.5-turbo models
- Customizable prompts for different blog styles
- Token usage tracking and optimization

## 🆘 Support

For issues, questions, or feature requests:

1. Check the troubleshooting section above
2. Review the application logs: `tail -f log/development.log`
3. Check background jobs: `rails console` → `Delayed::Job.last`

## 📄 License

This project is licensed under the MIT License.

---

**⚠️ Important Compliance Notes:**

- **TCPA Compliance**: Ensure you have proper consent before auto-dialing contacts
- **CAN-SPAM**: Include unsubscribe options in automated communications
- **GDPR/Privacy**: Respect data protection laws when storing contact information
- **Twilio ToS**: Follow Twilio's acceptable use policy for calling features

---

Made with ❤️ using Ruby on Rails

**Star ⭐ this repo if you find it helpful!**
