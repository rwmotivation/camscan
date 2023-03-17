import sqlite3

# Create a database connection
conn = sqlite3.connect('scanned_images.db')

# Create a table to store the scanned images
conn.execute('''
CREATE TABLE IF NOT EXISTS images (
    id INTEGER PRIMARY KEY,
    plate_number TEXT NOT NULL,
    image BLOB NOT NULL
);
''')

# Insert the scanned image into the database
with open('image.jpg', 'rb') as f:
    image_data = f.read()
    plate_number = 'ABC123'  # Replace with the actual plate number
    conn.execute('INSERT INTO images (plate_number, image) VALUES (?, ?)', (plate_number, image_data))
    conn.commit()

# Close the database connection
conn.close()
