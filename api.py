import os
import json
from flask import Blueprint, jsonify
from flask_cors import CORS

api_bp = Blueprint('api', __name__)
CORS(api_bp) 
# Function to load blogs from a JSON file in the 'data' directory
def load_blogs_from_file():
    file_path = os.path.join('data', 'db.json')
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if 'blogs' in data and isinstance(data['blogs'], list):
                return data
            else:
                raise ValueError("INVALID DATA STRUCTURE: MISSING OR INVALID 'BLOGS' KEY")
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON data in file '{file_path}'.")


# API endpoint to get all blogs
@api_bp.route('/blogs', methods=['GET'])
def get_blogs():
    blogs = load_blogs_from_file()
    return jsonify(blogs)

# API endpoint to get a specific blog by ID
@api_bp.route('/blogs/<int:blog_id>', methods=['GET'])
def get_blog(blog_id):
    blogs = load_blogs_from_file()
    blog = next((blog for blog in blogs['blogs'] if blog['id'] == blog_id), None)
    if blog:
        return jsonify(blog)
    else:
        return jsonify({"error": "Blog not found"}), 404

