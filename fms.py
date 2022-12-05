# Import the necessary libraries
import os
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import sqlite3

# Create a GUI window
root = Tk()
root.title("File Management System")

# Connect to the database
conn = sqlite3.connect("files.db")
cursor = conn.cursor()

# Create the database table (if it doesn't already exist)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        path TEXT
    )
""")


# Define the function for uploading files
def upload_file():
    # Use the file selection dialog to choose a file
    filepath = filedialog.askopenfilename()

    # Extract the file name and path from the filepath
    filename = os.path.basename(filepath)
    filepath = os.path.dirname(filepath)

    # Insert the file name and path into the database
    cursor.execute("""
        INSERT INTO files (name, path) VALUES (?, ?)
    """, (filename, filepath))
    conn.commit()

    # Show a message to confirm that the file was uploaded successfully
    tkinter.messagebox.showinfo("File Uploaded", "The file was uploaded successfully!")


# Create a button for uploading files
upload_button = Button(root, text="Upload File", command=upload_file)
upload_button.pack()

# Run the GUI
root.mainloop()

