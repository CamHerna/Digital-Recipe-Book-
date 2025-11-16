from datetime import datetime
from db import get_db_connection



# ADD RECIPE (SQL INSERT)

def add_recipe(title, description, ingredients, instructions, is_user_made=True):
    if not title or not ingredients or not instructions:
        return "Error: Title, ingredients, and instructions are required."

    conn = get_db_connection()
    if not conn:
        return "Database connection failed."

    cursor = conn.cursor()

    sql = """
    INSERT INTO recipes (title, description, ingredients, instructions, is_sample_data)
    VALUES (%s, %s, %s, %s, %s)
    """
    
    values = (title, description, ingredients, instructions, int(is_user_made))
    cursor.execute(sql, values)
    
    conn.commit()
    new_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return f"Recipe {new_id} added successfully!"



# VIEW ALL RECIPES (SQL SELECT)

def view_all_recipes():
    conn = get_db_connection()
    if not conn:
        return []

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM recipes ORDER BY recipe_id DESC")
    
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return rows



# VIEW SINGLE RECIPE (SQL SELECT WHERE)

def view_recipe(recipe_id):
    conn = get_db_connection()
    if not conn:
        return "Connection failed."

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM recipes WHERE recipe_id = %s", (recipe_id,))
    
    recipe = cursor.fetchone()

    cursor.close()
    conn.close()

    return recipe if recipe else "Recipe not found."



# EDIT RECIPE (SQL UPDATE)

def edit_recipe(recipe_id, new_title=None, new_description=None, new_ingredients=None, new_instructions=None):
    conn = get_db_connection()
    if not conn:
        return "Connection failed."

    cursor = conn.cursor()

    updates = []
    values = []

    if new_title:
        updates.append("title = %s")
        values.append(new_title)

    if new_description:
        updates.append("description = %s")
        values.append(new_description)

    if new_ingredients:
        updates.append("ingredients = %s")
        values.append(new_ingredients)

    if new_instructions:
        updates.append("instructions = %s")
        values.append(new_instructions)

    if not updates:
        return "Nothing to update."

    values.append(recipe_id)

    sql = "UPDATE recipes SET " + ", ".join(updates) + " WHERE recipe_id = %s"

    cursor.execute(sql, values)
    conn.commit()

    cursor.close()
    conn.close()

    return f"Recipe {recipe_id} updated successfully."



# DELETE RECIPE (SQL DELETE)

def delete_recipe(recipe_id):
    conn = get_db_connection()
    if not conn:
        return "Connection failed."

    cursor = conn.cursor()
    cursor.execute("DELETE FROM recipes WHERE recipe_id = %s", (recipe_id,))
    conn.commit()

    cursor.close()
    conn.close()

    return f"Recipe {recipe_id} deleted successfully."



# SEARCH RECIPE (SQL SELECT LIKE)

def search_recipe(keyword):
    conn = get_db_connection()
    if not conn:
        return []

    cursor = conn.cursor(dictionary=True)
    search_term = f"%{keyword}%"
    
    cursor.execute("SELECT * FROM recipes WHERE title LIKE %s", (search_term,))
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results if results else []
