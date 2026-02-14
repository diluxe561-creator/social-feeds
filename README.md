# social-feeds

# Real-Time Social Feed App (Flask)

A lightweight real-time social timeline application built with Flask and SQLite. Users can create posts, like posts, and see updates automatically refresh on the feed. Designed to demonstrate structured backend routing, database models, and dynamic frontend updates.

## Features

* Create short text posts
* Like posts
* Auto-refreshing feed (near real-time)
* Structured Flask blueprints
* SQLite database
* Clean, responsive UI
* REST-style API endpoints

## Tech Stack

* Python
* Flask
* Flask-SQLAlchemy
* SQLite
* HTML/CSS/JavaScript

## Project Structure

backend/

* app.py — main Flask app
* models.py — database models
* routes/posts.py — post endpoints
* routes/likes.py — like endpoints
* templates/ — HTML templates
* static/ — CSS styles

## Installation

1. Clone the repo
2. Create virtual environment

python -m venv venv
source venv/bin/activate (or venv\Scripts\activate on Windows)

3. Install dependencies

pip install flask flask_sqlalchemy

4. Run app

python app.py

5. Open browser at:
   http://127.0.0.1:5000

## API Endpoints

POST /post — create a post
GET /posts — list posts
POST /like/<id> — like a post

## Learning Goals

* Backend routing with Flask blueprints
* Database modeling
* JSON APIs
* Dynamic frontend updates

## Future Improvements

* User accounts
* Comments
* WebSocket real-time updates
* Image uploads
* Follow system
