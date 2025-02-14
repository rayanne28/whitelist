from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def check_whitelist(user_id):
    conn = sqlite3.connect("whitelist.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM whitelist WHERE script = ?", (str(user_id),))
    result = cursor.fetchone()
    conn.close()
    return result is not None

@app.route('/check_whitelist', methods=['GET'])
def whitelist():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400
    
    if check_whitelist(user_id):
        return jsonify({"whitelisted": True})
    else:
        return jsonify({"whitelisted": False})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

