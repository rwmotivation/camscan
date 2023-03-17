# camscan
cross platform app to scan vehicle registration numbers from cctv cameras 


# in dbcon.py file 
In dbconnection.py file , we first create a database connection to a file named 'scanned_images.db'. We then create a table named 'images' to store the scanned images, with columns for an ID (which will be automatically generated), the plate number, and the image data.

To insert a scanned image into the database, we first read the image file into memory as binary data, and then use a parameterized SQL query to insert the plate number and image data into the 'images' table. Finally, we commit the transaction and close the database connection.

Note that in a real-world app, you may want to handle errors and use best practices for database access, such as using a context manager to ensure proper resource management.
