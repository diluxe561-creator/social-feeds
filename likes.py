from flask import Blueprint, jsonify
from models import db, Post

likes_bp = Blueprint("likes", __name__)

@likes_bp.route("/like/<int:id>", methods=["POST"])
def like(id):
    p = Post.query.get(id)
    p.likes += 1
    db.session.commit()
    return jsonify({"likes": p.likes})
