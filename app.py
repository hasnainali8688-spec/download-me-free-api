from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def is_link_active(url):
    try:
        res = requests.head(url, timeout=5, allow_redirects=True)
        return res.status_code == 200
    except:
        return False

@app.route('/search', methods=['GET'])
def search():
    movie = request.args.get('name', '')
    
    sample_links = [
        {"site": "VegaMovies", "quality": "1080p", "url": "https://www.google.com"},
        {"site": "SSRmovies", "quality": "720p", "url": "https://invalid-link-test-123.com"}
    ]
    
    active_results = []
    for item in sample_links:
        if is_link_active(item['url']):
            active_results.append(item)
            
    return jsonify({
        "app_name": "download me free",
        "movie": movie,
        "links": active_results
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

