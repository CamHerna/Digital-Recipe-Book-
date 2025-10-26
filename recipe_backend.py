"""
Digital Recipe Book - Backend Logic (Python Functions Only)

"""

from datetime import datetime

# --- In-memory recipe "database" ---
# For now, we store recipes in a Python list instead of a real SQL database
recipes = []
recipe_id_counter = 1


def add_recipe(title, description, ingredients, instructions):
    """
    Adds a new recipe to the list.
    Checks if title, ingredients, and instructions are not empty.
    Returns a success message or an error message.
    """
    global recipe_id_counter

    if not title or not ingredients or not instructions:
        return "Error: Title, ingredients, and instructions are required."

    recipe = {
        "id": recipe_id_counter,
        "title": title.strip(),
        "description": description.strip(),
        "ingredients": ingredients.strip(),
        "instructions": instructions.strip(),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    recipes.append(recipe)
    recipe_id_counter += 1
    return f"Recipe '{title}' added successfully!"


def view_all_recipes():
    """
    Returns all recipes currently saved in the list.
    If there are no recipes, returns a message saying so.
    """
    if not recipes:
        return "No recipes found."
    return recipes


def view_recipe(recipe_id):
    """
    Finds and returns a specific recipe by its ID.
    If the recipe is not found, returns an error message.
    """
    for recipe in recipes:
        if recipe["id"] == recipe_id:
            return recipe
    return "Recipe not found."


def edit_recipe(recipe_id, new_title=None, new_description=None, new_ingredients=None, new_instructions=None):
    """
    Updates an existing recipe by its ID.
    Only updates the fields that are provided (others stay the same).
    Returns a confirmation or error message.
    """
    for recipe in recipes:
        if recipe["id"] == recipe_id:
            if new_title:
                recipe["title"] = new_title.strip()
            if new_description:
                recipe["description"] = new_description.strip()
            if new_ingredients:
                recipe["ingredients"] = new_ingredients.strip()
            if new_instructions:
                recipe["instructions"] = new_instructions.strip()
            return f"Recipe ID {recipe_id} updated successfully."
    return "Recipe not found."


def delete_recipe(recipe_id):
    """
    Deletes a recipe from the list by its ID.
    Returns a confirmation message or an error if not found.
    """
    global recipes
    for recipe in recipes:
        if recipe["id"] == recipe_id:
            recipes = [r for r in recipes if r["id"] != recipe_id]
            return f"Recipe ID {recipe_id} deleted successfully."
    return "Recipe not found."


def search_recipe(keyword):
    """
    Searches for recipes whose title includes the given keyword.
    Returns a list of matching recipes or a message if none found.
    """
    results = [r for r in recipes if keyword.lower() in r["title"].lower()]
    if not results:
        return "No matching recipes found."
    return results


