
CREATE USER 'recipe_app_user'@'localhost' IDENTIFIED BY 'Kz8gnHfufP4b';


GRANT SELECT, INSERT, UPDATE, DELETE ON recipebox.recipes
TO 'recipe_app_user'@'localhost';


FLUSH PRIVILEGES;
