from flask import Flask, render_template
from models import db
from routes.posts import posts_bp
from routes.likes import likes_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///feed.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(posts_bp)
app.register_blueprint(likes_bp)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
