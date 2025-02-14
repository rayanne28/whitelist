from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/check_whitelist', methods=['GET'])
def check_whitelist():
    user_id = request.args.get('user_id')

    conn = sqlite3.connect("whitelist.db")
    cursor = conn.cursor()

    # Debugging: Print user_id received
    print(f"🔎 Checking whitelist for user ID: {user_id}")

    cursor.execute("SELECT * FROM whitelist WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()

    conn.close()

    # Debugging: Print if user is whitelisted
    if result:
        print(f"✅ User {user_id} is whitelisted")
    else:
        print(f"❌ User {user_id} is NOT whitelisted")

    return jsonify({"whitelisted": bool(result)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
