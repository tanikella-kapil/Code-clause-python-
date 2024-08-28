from flask import Flask, redirect
import hashlib
app = Flask(__name__)

class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.base_url = "http://localhost:4234/"

    def shorten_url(self, original_url):
        url_hash = hashlib.md5(original_url.encode()).hexdigest()[:6]
        short_url = self.base_url + url_hash
        self.url_map[url_hash] = original_url
        return short_url

    def retrieve_url(self, short_code):
        return self.url_map.get(short_code, "URL not found.")

shortener = URLShortener()# This create an instance of the above class

original_url = "https://internship.codeclause.com/"
short_url = shortener.shorten_url(original_url)
print(f"Shortened URL: {short_url}")

@app.route('/<short_code>')
def redirect_short_url(short_code):
    # Retrieve the original URL
    original_url = shortener.retrieve_url(short_code)
    if original_url == "URL not found.":
        return "Error: URL not found.", 404
    else:
        return redirect(original_url)

if __name__ == '__main__':
    app.run(port=4234, debug=True)
