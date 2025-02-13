import tkinter as tk
from PIL import Image, ImageTk  # Import the Image module from the Pillow library
import webbrowser
from MusicApp import main
from PyQt5.QtWidgets import QApplication


def open_spotify():
    # URL for the Spotify web player
    spotify_url = "https://open.spotify.com/"

    # Open the Spotify web player in the default web browser
    webbrowser.open(spotify_url)


def open_local_music_player():
    # Replace the file path with the path to your local music player script
    local_music_player_path = r"C:/Users/HP/PycharmProjects/MusicApp/main.py"

    # Open the local music player using the default Python interpreter
    webbrowser.open(local_music_player_path)


# Create the main GUI window
root = tk.Tk()
root.title("MusicWindow")

# Load images for buttons (replace with your image file paths)
spotify_image_path = "C:/Users/HP/PycharmProjects/Stress_debuster/MusicApp/img.png"
local_music_player_image_path = "C:/Users/HP/PycharmProjects/Stress_debuster/MusicApp/img_1.png"

# Open the images using the Pillow library for resizing
spotify_image = Image.open(spotify_image_path)
spotify_image = ImageTk.PhotoImage(
    spotify_image.resize((200, 200), Image.BICUBIC))  # Use BICUBIC for older Pillow versions

local_music_player_image = Image.open(local_music_player_image_path)
local_music_player_image = ImageTk.PhotoImage(
    local_music_player_image.resize((200, 200), Image.BICUBIC))  # Use BICUBIC for older Pillow versions

# Set the window size
window_width = 700
window_height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Add a label with the specified text
label_text = "Time to groove and let the beats sprinkle funk in your day! Let the rhythm hijack your mood, making every note a burst of energy – press play and let the music takeover the excitement!"
label = tk.Label(root, text=label_text, font=("Helvetica", 15), wraplength=600, justify=tk.CENTER)
label.pack(pady=50)

# Create a frame to hold the buttons and center it in the window
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create a button to open Spotify with an image
spotify_button = tk.Button(frame, image=spotify_image, command=open_spotify, width=200, height=250)
spotify_button.pack(side=tk.LEFT, padx=30)  # Adjust padx to add space

# Create a button to open the local music player with an image
local_music_player_button = tk.Button(frame, image=local_music_player_image, command=open_local_music_player, width=200,
                                      height=250)
local_music_player_button.pack(side=tk.LEFT, padx=20)  # Adjust padx to add space

# Run the GUI application
root.mainloop()
