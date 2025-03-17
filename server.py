from flask import Flask, request, jsonify
from ytmusicapi import YTMusic

app = Flask(__name__)

# Инициализация ytmusicapi
ytmusic = YTMusic()  # Создайте headers_auth.json через ytmusicapi oauth

# Роут для поиска треков
@app.route('/api/search', methods=['GET'])
def search_tracks():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Запрос не указан'}), 400

    try:
        # Поиск треков через ytmusicapi
        results = ytmusic.search(query, filter='songs', limit=10)
        tracks = [
            {
                'title': item['title'],
                'artist': item['artists'][0]['name'] if item['artists'] else 'Unknown',
                'videoId': item['videoId']
            }
            for item in results
        ]
        return jsonify(tracks)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=3000)