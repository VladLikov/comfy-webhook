import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def receive_webhook():
    data = request.json
    print("📩 Получен webhook от ComfyOnline:")
    print(data)

    # Логика обработки webhook
    task_id = data.get("task_id")
    status = data.get("status")
    output = data.get("output", {})
    error_message = data.get("error_message")

    print(f"📦 Task ID: {task_id}")
    print(f"🧩 Status: {status}")
    print(f"🖼️ Output: {output.get('output_url_list')}")
    if error_message:
        print(f"❌ Ошибка: {error_message}")

    return jsonify({"success": True})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway автоматически задаёт PORT
    app.run(host="0.0.0.0", port=port)
