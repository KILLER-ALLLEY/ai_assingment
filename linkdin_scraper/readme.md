# 🔍 LinkedIn Profile Scraper

A powerful web-based tool to scrape LinkedIn profile information with real-time updates and a beautiful user interface.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![Playwright](https://img.shields.io/badge/Playwright-Latest-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 🚀 **Real-time scraping** - See results appear instantly as each profile is scraped
- 📊 **Progress tracking** - Live progress bar and profile counter
- 🎨 **Beautiful UI** - Modern, responsive interface with Tailwind CSS
- 📋 **Copy to clipboard** - Export all scraped data with one click
- ⚡ **Fast & efficient** - Uses Playwright for reliable browser automation
- 🔐 **Secure** - Your credentials are only used locally and never stored

## 📋 What Data Gets Scraped

For each LinkedIn profile, the scraper extracts:
- ✅ Full Name
- ✅ Professional Headline
- ✅ Location
- ✅ Profile URL

## 🚀 How to Run

### 1. Start the Server
```bash
python app.py
```

You should see:
```
==================================================
🚀 LinkedIn Scraper Server Starting...
==================================================
📍 Open your browser and go to: http://localhost:5000
==================================================
```

### 2. Open Your Browser

Navigate to: **http://localhost:5000**

### 3. Enter Your Credentials

- Enter your LinkedIn email
- Enter your LinkedIn password

⚠️ **Note:** Your credentials are used only to log into LinkedIn via the automated browser and are never stored.

### 4. Add Profile URLs

Paste LinkedIn profile URLs (one per line) in the text area. Example:
```
https://www.linkedin.com/in/username1/
https://www.linkedin.com/in/username2/
https://www.linkedin.com/in/username3/
```

### 5. Start Scraping

Click **"Start Scraping"** and watch the magic happen! ✨

- Progress bar shows real-time completion status
- Each profile appears instantly as it's scraped
- Total count updates automatically

### 6. Export Data

Click **"📋 Copy All Data"** to copy all scraped information to your clipboard in a formatted text format.

## 📸 Screenshots

### Main Interface
```
┌─────────────────────────────────────────────┐
│  🔍 LinkedIn Profile Scraper                │
│  Extract profile information from URLs      │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  🔐 Login Credentials                       │
│  Email: [your.email@example.com]            │
│  Password: [••••••••]                       │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  📝 Profile URLs                            │
│  [Text area for URLs]                       │
│  3 URLs entered    [Start Scraping Button]  │
└─────────────────────────────────────────────┘
```

### Real-time Results
```
┌─────────────────────────────────────────────┐
│  Scraping Progress: 5 / 10                  │
│  Currently scraping: linkedin.com/in/john   │
│  ████████████░░░░░░░ 50%                    │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  ✅ Results (5)          [📋 Copy All Data] │
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │ John Doe                          ✓ │   │
│  │ 💼 Software Engineer at Tech Co     │   │
│  │ 📍 San Francisco, CA                │   │
│  │ linkedin.com/in/johndoe             │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  [More results appear here in real-time...] │
└─────────────────────────────────────────────┘
```

## 🔧 Configuration

### Change Port

Edit the last line in `app.py`:
```python
app.run(debug=True, port=5000, host='0.0.0.0')
#                      ^^^^
#                      Change this to your desired port
```

### Headless Mode

To run the browser in headless mode (no visible window), change:
```python
browser = playwright.chromium.launch(headless=True, slow_mo=200)
#                                              ^^^^
#                                              Set to True
```

### Scraping Speed

Adjust the `slow_mo` parameter (milliseconds):
```python
browser = playwright.chromium.launch(headless=True, slow_mo=200)
#                                                        ^^^
#                                                        Lower = faster
```

## ⚠️ Important Notes

### LinkedIn Terms of Service

- This tool is for **educational purposes only**
- Respect LinkedIn's Terms of Service
- Don't scrape at scale or use for commercial purposes
- Use rate limiting to avoid being blocked
- Consider using LinkedIn's official API for production use

### Rate Limiting

LinkedIn may temporarily block your account if you scrape too many profiles too quickly. Recommendations:

- Scrape in small batches (10-20 profiles at a time)
- Add delays between batches
- Don't run the scraper continuously

### Security

- **Never share your LinkedIn credentials**
- The tool runs locally on your machine
- No data is sent to external servers
- Your credentials are only used to log into LinkedIn

## 🐛 Troubleshooting

### "Email or Phone" field not found

LinkedIn's login page structure may have changed. Update the selector:
```python
page.get_by_label("Email or Phone").fill(email)
```

### Profiles not loading

- Check your internet connection
- LinkedIn may be rate-limiting you
- Try increasing the `time.sleep()` values
- Verify the profile URLs are correct

### Browser won't open

Reinstall Playwright browsers:
```bash
playwright install chromium --force
```

### Port already in use

Change the port number in `app.py` or run:
```bash
# Linux/Mac
PORT=8080 python app.py
```

## 📝 Sample URLs for Testing
```
https://www.linkedin.com/in/williamhgates/
https://www.linkedin.com/in/jeffweiner08/
https://www.linkedin.com/in/reidhoffman/
https://www.linkedin.com/in/satyanadella/
https://www.linkedin.com/in/johnlegere/
```

## ⚡ Performance Tips

- Use **headless mode** for faster scraping
- Reduce `slow_mo` value for speed (but may be less stable)
- Scrape during off-peak hours
- Use a stable internet connection

## 🔮 Future Enhancements

Potential features for future versions:

- [ ] Export to CSV/Excel
- [ ] Support for company pages
- [ ] Skills and experience extraction
- [ ] Database integration
- [ ] Batch processing with scheduling
- [ ] Proxy support
- [ ] Multi-account support
- [ ] API endpoints

## 📄 License

This project is licensed under the MIT License.
```
MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

**⚠️ Disclaimer:** This tool is for educational purposes only. Users are responsible for complying with LinkedIn's Terms of Service and applicable laws. The authors are not responsible for any misuse of this tool.

---

Made with ❤️

**Star ⭐ this repo if you find it helpful!**
