
from flask import Flask, request, jsonify

app = Flask(__name__)

bookmarks = [{
    "id": 1,
    "title": "OpenAI",
    "url": "https://chat.openai.com",
    "category": "AI",
    "favourite": True
}]

@app.get("/")
def home():
    return jsonify({
        "status": "Bookmarks Manager API running successfully"
    })

@app.get("/bookmarks")
def get_all():
    return jsonify(bookmarks)

@app.get("/bookmarks/<int:id>")
def get_one(id):
    for b in bookmarks:
        if b["id"] == id:
            return jsonify(b)
    return jsonify({"error": "Bookmark not found"}), 404

@app.post("/bookmarks")
def add():
    d = request.get_json()
    b = {
        "id": max([x["id"] for x in bookmarks], default=0) + 1,
        "title": d["title"],
        "url": d["url"],
        "category": d["category"],
        "favourite": d["favourite"]
    }
    bookmarks.append(b)
    return jsonify({
        "status": "Bookmark added successfully",
        "bookmark": b
    }), 201

@app.patch("/bookmarks/<int:id>")
def update(id):
    for b in bookmarks:
        if b["id"] == id:
            b.update(request.get_json())
            return jsonify({
                "status": "Bookmark updated successfully",
                "bookmark": b
            })
    return jsonify({"error": "Bookmark not found"}), 404

@app.delete("/bookmarks/<int:id>")
def delete(id):
    for b in bookmarks:
        if b["id"] == id:
            bookmarks.remove(b)
            return jsonify({
                "status": "Bookmark deleted successfully",
                "bookmark": b
            })
    return jsonify({"error": "Bookmark not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
