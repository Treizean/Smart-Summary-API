from flask import Flask, request, jsonify
from utils import summarize_text
import logging
import os

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='requests.log', level=logging.INFO)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        summary = summarize_text(text)
        logging.info(f"Summary created for input length {len(text)}")
        return jsonify({'summary': summary})
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return jsonify({'error': 'Failed to generate summary'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)