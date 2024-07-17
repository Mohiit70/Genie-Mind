from flask import request, jsonify
from app import app
from app.utils import simplify_text, analyze_sentiment

@app.route('/simplify', methods=['POST'])
def simplify():
    data = request.json
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    simplified = simplify_text(data['text'])
    sentiment = analyze_sentiment(data['text'])
    
    return jsonify({
        'simplified': simplified,
        'sentiment': sentiment
    })

@app.route('/')
def hello():
    return "Hello, World!"
