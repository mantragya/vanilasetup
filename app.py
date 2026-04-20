from flask import Flask, jsonify
import logging
from src.github_api import fetch_user_gists
from src.logging_config import setup_logger

app = Flask(__name__)
logger = setup_logger("github_api_server", logging.INFO)

@app.route('/<username>')
def get_user_gists(username):
    try:
        gists = fetch_user_gists(username)
        return jsonify(gists)
    except Exception as e:
        logger.error(f"Error fetching gists for {username}: {str(e)}")
        return jsonify({"error": str(e)}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
