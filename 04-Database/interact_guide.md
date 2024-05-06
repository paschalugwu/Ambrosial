# Here's a guide on how you can use sqlite3 to interact with your database:

```python
# Import necessary packages
from flask_ambrosial import db, app
from flask_ambrosial.models import User, Post

# Set up an application context using app.app_context()
with app.app_context():
    # Create the database tables
    db.create_all()

import os
import sqlite3

# Specify the path to the 'instance' directory
db_path = os.path.join(os.getcwd(), "instance/site.db")

# Connect to the database
conn = sqlite3.connect(db_path)
c = conn.cursor()

# To search for all your posts
c.execute("SELECT * FROM post WHERE user_id = ?", (your_user_id,))
print(c.fetchall())

# To list all registered users
c.execute("SELECT * FROM user")
print(c.fetchall())

# To retrieve the dates posts were made
c.execute("SELECT date_posted FROM post")
print(c.fetchall())

# To list images
c.execute("SELECT image_file FROM user")
print(c.fetchall())

# Populate the Database
# Insert data into the 'user' table
c.execute("INSERT INTO user (username, email, image_file, password) VALUES (?, ?, ?, ?)", ('Ugwu Paschal', 'ugwu@example.com', 'default.jpg', 'password123'))

# Insert data into the 'post' table
c.execute("INSERT INTO post (title, date_posted, content, user_id) VALUES (?, ?, ?, ?)", ('How to prepare Jollof Rice.', '2022-04-18', 'Jollof rice, a beloved West African dish...', 1))

# Commit the changes
conn.commit()

# Query the Database
# Retrieve data from the 'user' table
c.execute("SELECT * FROM user")
print(c.fetchall())

# Update the Database
# Update a record in the 'user' table
c.execute("UPDATE user SET username = ? WHERE username = ?", ('Paschal Ugwu', 'Ugwu Paschal'))
conn.commit()

# Delete from the Database
# Delete a record from the 'user' table
c.execute("DELETE FROM user WHERE username = ?", ('Paschal Ugwu',))
conn.commit()

# Drop All Content
# Delete all records from the 'user' and 'post' tables
c.execute("DELETE FROM user")
c.execute("DELETE FROM post")
conn.commit()

# Close the Connection
# Don't forget to close the connection once you're done
conn.close()
```

# This script demonstrates how to connect to a SQLite database, insert data into tables, retrieve data from tables, update records in a table, delete a record from a table, delete all records from tables, and close the database connection.

# Other queries:
### Example 1: Retrieve all users
```python
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('instance/site.db')
c = conn.cursor()

# Execute SQL query to select all users
c.execute("SELECT * FROM user")

# Fetch all rows
users = c.fetchall()

# Print user information
for user in users:
    print(f"Username: {user[1]}, Email: {user[2]}")
```

### Example 2: Retrieve a specific user by ID
```python
# Execute SQL query to select a user by ID
c.execute("SELECT * FROM user WHERE id=?", (1,))  # Replace 1 with the ID of the user you want to retrieve

# Fetch the user
user = c.fetchone()

# Print user information
print(f"Username: {user[1]}, Email: {user[2]}")
```

### Example 3: Retrieve all posts
```python
# Execute SQL query to select all posts
c.execute("SELECT * FROM post")

# Fetch all rows
posts = c.fetchall()

# Print post information
for post in posts:
    print(f"Title: {post[1]}, Content: {post[3]}")
```

### Example 4: Retrieve posts by a specific user
```python
# Execute SQL query to select posts by a specific user
c.execute("SELECT * FROM post WHERE user_id=?", (1,))  # Replace 1 with the ID of the user you want to retrieve posts for

# Fetch all rows
posts = c.fetchall()

# Print post information
for post in posts:
    print(f"Title: {post[1]}, Content: {post[3]}")
```

### Example 5: Retrieve posts by filtering with conditions
```python
# Execute SQL query to select posts based on conditions
c.execute("SELECT * FROM post WHERE title LIKE ?", ('%example%',))

# Fetch all rows
filtered_posts = c.fetchall()

# Print filtered post information
for post in filtered_posts:
    print(f"Title: {post[1]}, Content: {post[3]}")
```

### Example 6: Retrieve the most recent posts
```python
# Execute SQL query to select the most recent posts
c.execute("SELECT * FROM post ORDER BY date_posted DESC LIMIT 10")

# Fetch all rows
recent_posts = c.fetchall()

# Print recent post information
for post in recent_posts:
    print(f"Title: {post[1]}, Date Posted: {post[2]}")
```
