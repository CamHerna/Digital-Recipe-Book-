from datetime import datetime

recipes = []
recipe_id_counter = 1

def add_recipe(title, description, ingredients, instructions, is_user_made=True):
    global recipe_id_counter, recipes

    if not title or not ingredients or not instructions:
        return "Error: Title, ingredients, and instructions are required."

    recipe = {
        "id": recipe_id_counter,
        "title": title.strip(),
        "description": description.strip(),
        "ingredients": ingredients.strip(),
        "instructions": instructions.strip(),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "is_user_made": bool(is_user_made)
    }

    recipes.append(recipe)
    recipe_id_counter += 1
    return "Recipe added successfully!"

def view_all_recipes():
    return recipes if recipes else []

def view_recipe(recipe_id):
    for r in recipes:
        if r["id"] == recipe_id:
            return r
    return "Recipe not found."
