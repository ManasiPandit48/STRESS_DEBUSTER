import os
import random
import tkinter as tk
from PIL import Image, ImageTk
import requests
import io
import pymysql


class MemeViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Meme Viewer")

        screen_width = root.winfo_screenwidth()
        window_width = int(screen_width / 2)
        window_height = 500
        self.root.geometry(f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+0")

        self.db = pymysql.connect(
            host="localhost",
            user="root",
            password="Manasi@123",
            database="meme_viewer"
        )
        self.cursor = self.db.cursor()

        self.meme_data = []  # Initialize meme_data as an empty list
        self.load_meme_data()

        # Convert tuples to lists and shuffle
        self.meme_data = [list(item) for item in self.meme_data]
        random.shuffle(self.meme_data)  # Shuffle the list randomly

        self.current_index = 0

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        self.create_navigation_buttons()

        # Delay the execution of show_current_image by 100 milliseconds
        self.root.after(100, self.show_current_image)

    def load_meme_data(self):
        self.cursor.execute("SELECT name, image_url FROM memes")
        self.meme_data = self.cursor.fetchall()

    def create_navigation_buttons(self):
        navigation_frame = tk.Frame(self.root)
        navigation_frame.pack(side=tk.BOTTOM, pady=10)

        prev_button = tk.Button(navigation_frame, text="Previous", command=self.show_previous)
        prev_button.pack(side=tk.LEFT, padx=10)

        next_button = tk.Button(navigation_frame, text="Next", command=self.show_next)
        next_button.pack(side=tk.RIGHT, padx=10)

    import random

    # ...

    def show_current_image(self):
        if 0 <= self.current_index < len(self.meme_data):
            meme_name, image_url = self.meme_data[self.current_index]

            try:
                # Add a random parameter to the image URL to make it unique
                random_param = random.randint(1, 1000000)  # Adjust the range as needed
                image_url = f"{image_url}?r={random_param}"

                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
                response = requests.get(image_url, headers=headers)
                response.raise_for_status()

                image_data = io.BytesIO(response.content)
                image = Image.open(image_data)

                # Resize the image to 500x500 pixels (increased size)
                resized_image = image.resize((430, 430))
                tk_image = ImageTk.PhotoImage(resized_image)

                # Set the label image to the resized image
                self.image_label.config(image=tk_image)
                self.image_label.image = tk_image

                # Place the image in the center with some space from the top
                window_width = self.root.winfo_width()
                window_height = self.root.winfo_height()
                image_width = 430  # Adjusted size
                image_height = 430  # Adjusted size

                x_position = (window_width - image_width) // 2
                y_position = (window_height - image_height) // 4  # Adjust the divisor for more or less space

                self.image_label.place(x=x_position, y=y_position)

            except Exception as e:
                print(f"Error loading image: {e}")

    def show_previous(self):
        if self.meme_data:
            self.current_index = (self.current_index - 1) % len(self.meme_data)
            self.show_current_image()

    def show_next(self):
        if self.meme_data:
            self.current_index = (self.current_index + 1) % len(self.meme_data)
            self.show_current_image()


if __name__ == "__main__":
    root = tk.Tk()
    meme_viewer = MemeViewer(root)
    root.mainloop()
