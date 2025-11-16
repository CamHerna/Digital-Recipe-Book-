from datetime import datetime
from db import get_db_connection


def add_recipe(title, description, ingredients, instructions, is_user_made=True):
    if not title or not ingredients or not instructions:
        return "Error: Title, ingredients, and instructions are required."

    conn = get_db_connection()
    if not conn:
        return "Database connection failed."

    cursor = conn.cursor()

    sql = """
        INSERT INTO recipes (title, description, ingredients, instructions, created_at, is_sample_data)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    created_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    values = (title, description, ingredients, instructions, created_time, 0)

    cursor.execute(sql, values)
    conn.commit()

    cursor.close()
    conn.close()

    return f"Recipe '{title}' added successfully!"


def view_all_recipes():
    conn = get_db_connection()
    if not conn:
        return "Database connection failed."

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM recipes ORDER BY recipe_id;")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    if not rows:
        return "No recipes found."

    return rows


def view_recipe(recipe_id):
    conn = get_db_connection()
    if not conn:
        return "Database connection failed."

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM recipes WHERE recipe_id = %s;", (recipe_id,))
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    return row if row else "Recipe not found."


def edit_recipe(recipe_id, new_title=None, new_description=None, new_ingredients=None, new_instructions=None):
    conn = get_db_connection()
    if not conn:
        return "Database connection failed."

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

    return f"Recipe ID {recipe_id} updated successfully."


def delete_recipe(recipe_id):
    conn = get_db_connection()
    if not conn:
        return "Database connection failed."

    cursor = conn.cursor()
    cursor.execute("DELETE FROM recipes WHERE recipe_id = %s;", (recipe_id,))
    conn.commit()

    cursor.close()
    conn.close()

    return f"Recipe ID {recipe_id} deleted successfully."


def search_recipe(keyword):
    conn = get_db_connection()
    if not conn:
        return "Database connection failed."

    cursor = conn.cursor(dictionary=True)
    search_term = f"%{keyword}%"
    cursor.execute("SELECT * FROM recipes WHERE title LIKE %s;", (search_term,))
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows if rows else "No matching recipes found."
