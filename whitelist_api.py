from flask import Flask, request, jsonify

app = Flask(__name__)

# Fake whitelist for testing
whitelist = {"12345678": True}  # Replace with actual Roblox IDs

@app.route("/check_whitelist", methods=["GET"])
def check_whitelist():
    user_id = request.args.get("user_id")
    is_whitelisted = whitelist.get(user_id, False)
    return jsonify({"whitelisted": is_whitelisted})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Use a high port (Render requires it)


