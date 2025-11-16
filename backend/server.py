from flask import Flask, request, jsonify
from flask_cors import CORS
import recipe_backend as backend

app = Flask(__name__)
CORS(app)

@app.get("/recipes")
def api_view_all():
    result = backend.view_all_recipes()
    return jsonify(result)

@app.get("/recipes/<int:recipe_id>")
def api_view_one(recipe_id):
    result = backend.view_recipe(recipe_id)
    return jsonify(result)

@app.post("/recipes")
def api_add_recipe():
    data = request.get_json()  # read JSON
    title = data.get("title", "").strip()
    ingredients = data.get("ingredients", "").strip()
    instructions = data.get("instructions", "").strip()
    description = data.get("description", "").strip()
    is_user_made = data.get("is_user_made", True)

    if not title or not ingredients or not instructions:
        return jsonify({"error": "Title, ingredients, and instructions are required."}), 400

    result = backend.add_recipe(title, description, ingredients, instructions, is_user_made)
    return jsonify({"message": result})

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


if __name__ == "__main__":
    app.run(debug=True)
