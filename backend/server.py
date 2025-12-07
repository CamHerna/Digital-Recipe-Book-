from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import recipe_backend as backend
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"  # folder to save uploaded images
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # make sure folder exists

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.get("/recipes")
def api_view_all():
    result = backend.view_all_recipes()
    return jsonify(result)

@app.get("/recipes/<int:recipe_id>")
def api_view_one(recipe_id):
    result = backend.view_recipe(recipe_id)
    return jsonify(result)

@app.post("/add_recipe")
def api_add_recipe():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()

    # Combine ingredients and instructions into strings
    ingredients_list = request.form.getlist("ingredients[]")
    instructions_list = request.form.getlist("instructions[]")
    ingredients = "\n".join(ingredients_list)
    instructions = "\n".join(instructions_list)

    # Handle uploaded image
    image_file = request.files.get("image")
    image_path = None
    if image_file:
        filename = secure_filename(image_file.filename)
        image_file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        image_path = f"uploads/{filename}"

    # Add recipe via backend
    result = backend.add_recipe(title, description, ingredients, instructions, image_path)

    return jsonify({
        "success": result["success"],
        "message": result["message"],
        "recipe_id": result.get("recipe_id")
    })


@app.put("/recipes/<int:recipe_id>")
def api_edit_recipe(recipe_id):
    data = request.get_json()
    result = backend.edit_recipe(
        recipe_id,
        new_title=data.get("title"),
        new_description=data.get("description"),
        new_ingredients=data.get("ingredients"),
        new_instructions=data.get("instructions")
    )
    return jsonify({"message": result})

@app.delete("/recipes/<int:recipe_id>")
def api_delete_recipe(recipe_id):
    result = backend.delete_recipe(recipe_id)
    return jsonify({"message": result})

@app.get("/search")
def api_search():
    keyword = request.args.get("q", "")
    result = backend.search_recipe(keyword)
    return jsonify(result)


@app.route('/uploads/<path:filename>')
def serve_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == "__main__":
    app.run(debug=True)
