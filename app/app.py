from flask import Flask, jsonify
import os
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Cofre Digital Online!",
        "version": os.getenv('APP_VERSION', '1.0.0')
    })

@app.route('/database')
def database_info():
    db_password = os.getenv('DB_PASSWORD', 'NAO_CONFIGURADA')
    logger.info("Acesso ao banco solicitado")
    return jsonify({
        "status": "connected" if db_password != 'NAO_CONFIGURADA' else "offline",
        "password_configured": db_password != 'NAO_CONFIGURADA'
    })