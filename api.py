import os
import json
from flask import Blueprint, jsonify
from flask_cors import CORS

api_bp = Blueprint('api', __name__)
CORS(api_bp) 
# Function to load blogs from a JSON file in the 'data' directory
def load_blogs_from_file():
    file_path = os.path.join('data', 'db.json')
    with open(file_path, 'r') as file:
        blogs = json.load(file)
    return blogs

# API endpoint to get all blogs
@api_bp.route('/blogs', methods=['GET'])
def get_blogs():
    blogs = load_blogs_from_file()
    return jsonify(blogs)

# API endpoint to get a specific blog by ID
@api_bp.route('/blogs/<int:blog_id>', methods=['GET'])
def get_blog(blog_id):
    blogs = load_blogs_from_file()
    blog = next((blog for blog in blogs if blog['id'] == blog_id), None)
    if blog:
        return jsonify(blog)
    else:
        return jsonify({"error": "Blog not found"}), 404
