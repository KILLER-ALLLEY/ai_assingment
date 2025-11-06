from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
from playwright.sync_api import sync_playwright
import time

app = Flask(__name__)
CORS(app)


HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LinkedIn Scraper</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { font-family: system-ui, -apple-system, sans-serif; }
    </style>
</head>
<body class="bg-gradient-to-br from-blue-50 to-indigo-100 min-h-screen p-8">
    <div class="max-w-5xl mx-auto">
        <div class="bg-white rounded-lg shadow-lg p-6 mb-6">
            <h1 class="text-3xl font-bold text-gray-800 mb-2">🔍 LinkedIn Profile Scraper</h1>
            <p class="text-gray-600">Extract profile information from LinkedIn URLs</p>
        </div>

        <div class="bg-white rounded-lg shadow-lg p-6 mb-6">
            <h2 class="text-xl font-semibold mb-4">🔐 Login Credentials</h2>
            <div class="space-y-4">
                <div>
                    <label class="block text-sm font-medium mb-2">LinkedIn Email</label>
                    <input type="email" id="email" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500" placeholder="your.email@example.com">
                </div>
                <div>
                    <label class="block text-sm font-medium mb-2">LinkedIn Password</label>
                    <input type="password" id="password" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500" placeholder="••••••••">
                </div>
            </div>
        </div>

        <div class="bg-white rounded-lg shadow-lg p-6 mb-6">
            <h2 class="text-xl font-semibold mb-4">📝 Profile URLs (one per line)</h2>
            <textarea id="urls" rows="12" class="w-full p-3 border border-gray-300 rounded-lg font-mono text-sm focus:ring-2 focus:ring-blue-500" 
                placeholder="https://www.linkedin.com/in/username1/
https://www.linkedin.com/in/username2/
https://www.linkedin.com/in/username3/"></textarea>
            <div class="mt-4 flex justify-between items-center">
                <span id="urlCount" class="text-sm text-gray-600">0 URLs entered</span>
                <button id="scrapeBtn" class="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white font-semibold py-3 px-6 rounded-lg transition-colors">
                    Start Scraping
                </button>
            </div>
        </div>

        <div id="errorMsg" class="hidden bg-red-50 border border-red-200 rounded-lg p-4 mb-6">
            <p class="text-red-800"></p>
        </div>

        <div id="loading" class="hidden bg-white rounded-lg shadow-lg p-8 text-center mb-6">
            <div class="animate-spin rounded-full h-16 w-16 border-b-4 border-blue-600 mx-auto"></div>
            <p class="mt-4 text-gray-600 font-medium">Scraping profiles... This may take a while.</p>
        </div>

        <div id="results" class="bg-white rounded-lg shadow-lg p-6 hidden">
            <div class="flex justify-between items-center mb-4">
                <h2 class="text-xl font-semibold">✅ Results (<span id="resultCount">0</span>)</h2>
                <button id="copyBtn" class="bg-green-600 hover:bg-green-700 text-white font-semibold py-2 px-4 rounded-lg transition-colors">
                    📋 Copy All Data
                </button>
            </div>
            <div id="resultsContainer" class="space-y-4 max-h-[600px] overflow-y-auto"></div>
        </div>
    </div>

    <script>
        const urlsTextarea = document.getElementById('urls');
        const urlCount = document.getElementById('urlCount');
        const scrapeBtn = document.getElementById('scrapeBtn');
        const resultsDiv = document.getElementById('results');
        const resultsContainer = document.getElementById('resultsContainer');
        const resultCount = document.getElementById('resultCount');
        const loading = document.getElementById('loading');
        const errorMsg = document.getElementById('errorMsg');
        const copyBtn = document.getElementById('copyBtn');
        
        let scrapedData = [];

        urlsTextarea.addEventListener('input', () => {
            const urls = urlsTextarea.value.split('\\n').filter(u => u.trim());
            urlCount.textContent = `${urls.length} URLs entered`;
        });

        scrapeBtn.addEventListener('click', async () => {
            const email = document.getElementById('email').value.trim();
            const password = document.getElementById('password').value.trim();
            const urls = urlsTextarea.value.split('\\n').filter(u => u.trim());

            errorMsg.classList.add('hidden');

            if (!email || !password) {
                showError('Please enter your LinkedIn credentials');
                return;
            }

            if (urls.length === 0) {
                showError('Please enter at least one LinkedIn profile URL');
                return;
            }

            scrapeBtn.disabled = true;
            scrapeBtn.textContent = 'Scraping...';
            loading.classList.remove('hidden');
            resultsDiv.classList.add('hidden');
            resultsContainer.innerHTML = '';
            scrapedData = [];

            try {
                const response = await fetch('/scrape', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password, urls })
                });

                const data = await response.json();
                
                if (!response.ok) {
                    throw new Error(data.error || 'Failed to scrape profiles');
                }

                loading.classList.add('hidden');
                resultsDiv.classList.remove('hidden');
                resultCount.textContent = data.results.length;
                scrapedData = data.results;

                data.results.forEach((result, index) => {
                    const card = document.createElement('div');
                    card.className = 'border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow';
                    
                    if (result.status === 'success') {
                        card.innerHTML = `
                            <div class="flex items-start justify-between mb-2">
                                <h3 class="font-semibold text-lg text-gray-800">${result.name}</h3>
                                <span class="text-green-500">✓</span>
                            </div>
                            <p class="text-gray-700 mb-2"><strong>💼</strong> ${result.headline}</p>
                            <p class="text-gray-600 mb-3"><strong>📍</strong> ${result.location}</p>
                            <a href="${result.url}" target="_blank" class="text-blue-600 text-sm hover:underline break-all">${result.url}</a>
                        `;
                    } else {
                        card.className += ' bg-red-50';
                        card.innerHTML = `
                            <div class="flex items-start justify-between mb-2">
                                <h3 class="font-semibold text-lg text-red-600">❌ Error</h3>
                            </div>
                            <p class="text-red-700 mb-2">${result.error || 'Failed to scrape profile'}</p>
                            <a href="${result.url}" target="_blank" class="text-blue-600 text-sm hover:underline break-all">${result.url}</a>
                        `;
                    }
                    
                    resultsContainer.appendChild(card);
                });

            } catch (error) {
                loading.classList.add('hidden');
                showError('Error: ' + error.message);
            }

            scrapeBtn.disabled = false;
            scrapeBtn.textContent = 'Start Scraping';
        });

        copyBtn.addEventListener('click', () => {
            let output = '';
            scrapedData.forEach((result, index) => {
                if (result.status === 'success') {
                    output += `Profile ${index + 1}:\\n`;
                    output += `Name: ${result.name}\\n`;
                    output += `Headline: ${result.headline}\\n`;
                    output += `Location: ${result.location}\\n`;
                    output += `URL: ${result.url}\\n`;
                    output += `\\n${'='.repeat(60)}\\n\\n`;
                }
            });
            
            navigator.clipboard.writeText(output).then(() => {
                copyBtn.textContent = '✓ Copied!';
                copyBtn.classList.remove('bg-green-600', 'hover:bg-green-700');
                copyBtn.classList.add('bg-green-700');
                setTimeout(() => {
                    copyBtn.textContent = '📋 Copy All Data';
                    copyBtn.classList.remove('bg-green-700');
                    copyBtn.classList.add('bg-green-600', 'hover:bg-green-700');
                }, 2000);
            });
        });

        function showError(message) {
            errorMsg.classList.remove('hidden');
            errorMsg.querySelector('p').textContent = message;
        }
    </script>
</body>
</html>
"""

def scrape_profile(url, page):
    """Scrape a single LinkedIn profile - EXACT SAME METHOD AS YOUR WORKING CODE"""
    print(f"\n🔗 Visiting: {url}")
    page.goto(url)
    time.sleep(3)

    
    try:
        name = page.locator("h1").first.inner_text() if page.locator("h1").count() else "N/A"
    except:
        name = "N/A"

    try:
        headline = page.locator(".text-body-medium.break-words").first.inner_text() if page.locator(".text-body-medium.break-words").count() else "N/A"
    except:
        headline = "N/A"

    try:
        location = page.locator(".text-body-small.inline.t-black--light.break-words").first.inner_text() if page.locator(".text-body-small.inline.t-black--light.break-words").count() else "N/A"
    except:
        location = "N/A"

    print(f"✅ Name: {name.strip()}")
    print(f"🧠 Headline: {headline.strip()}")
    print(f"📍 Location: {location.strip()}")

    return {
        "url": url,
        "name": name.strip(),
        "headline": headline.strip(),
        "location": location.strip(),
        "status": "success"
    }

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/scrape', methods=['POST'])
def scrape_profiles():
    data = request.json
    urls = data.get('urls', [])
    email = data.get('email')
    password = data.get('password')

    if not urls:
        return jsonify({"error": "No URLs provided"}), 400
    
    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    results = []
    
    try:
        with sync_playwright() as playwright:
            
            browser = playwright.chromium.launch(headless=True, slow_mo=200)
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                extra_http_headers={
                    "Accept-Language": "en-US,en;q=0.9",
                    "Referer": "https://www.google.com/"
                },
                viewport={"width": 1280, "height": 800}
            )
            page = context.new_page()

            
            page.goto("https://www.linkedin.com/login")
            page.wait_for_load_state("networkidle")
            page.get_by_label("Email or Phone").fill(email)
            page.get_by_label("Password").fill(password)
            page.get_by_role("button", name="Sign in", exact=True).click()
            time.sleep(5)

            
            for url in urls:
                try:
                    profile_data = scrape_profile(url, page)
                    results.append(profile_data)
                except Exception as e:
                    print(f"❌ Error scraping {url}: {str(e)}")
                    results.append({
                        "url": url,
                        "status": "error",
                        "error": str(e)
                    })

            context.close()
            browser.close()
            
    except Exception as e:
        return jsonify({"error": f"Scraping failed: {str(e)}"}), 500

    return jsonify({"results": results})

if __name__ == '__main__':
    print("="*50)
    print("🚀 LinkedIn Scraper Server Starting...")
    print("="*50)
    print("📍 Open your browser and go to: http://localhost:5000")
    print("="*50)
    app.run(debug=True, port=5000, host='0.0.0.0')

