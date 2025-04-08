# webhook_server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def receive_webhook():
    data = request.json
    print("📩 Получен webhook от ComfyOnline:")
    print(data)

    task_id = data.get("task_id")
    status = data.get("status")
    output = data.get("output", {})
    urls = output.get("output_url_list", [])

    if status == "COMPLETED" and urls:
        print(f"✅ Задача {task_id} завершена. Ссылка на изображение: {urls[0]}")
    elif status == "FAILED":
        print(f"❌ Задача {task_id} не удалась. Ошибка: {data.get('error_message')}")
    else:
        print(f"ℹ️ Задача {task_id} в статусе: {status}")

    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
