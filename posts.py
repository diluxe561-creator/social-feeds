from flask import Blueprint, request, jsonify
from models import db, Post

posts_bp = Blueprint("posts", __name__)

@posts_bp.route("/post", methods=["POST"])
def create_post():
    text = request.json["content"]
    p = Post(content=text)
    db.session.add(p)
    db.session.commit()
    return jsonify({"status": "ok"})

@posts_bp.route("/posts")
def get_posts():
    posts = Post.query.order_by(Post.created.desc()).all()
    return jsonify([
        {"id": p.id, "content": p.content, "likes": p.likes}
        for p in posts
    ])
