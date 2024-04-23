# Here's a guide on how you can use sqlite3 to interact with your database:

```python
import os
import sqlite3

# Specify the path to the 'instance' directory
db_path = os.path.join(os.getcwd(), "instance/site.db")

# Connect to the database
conn = sqlite3.connect(db_path)
c = conn.cursor()

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
