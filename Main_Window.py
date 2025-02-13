import tkinter as tk
from PIL import Image, ImageTk
import os
import subprocess
from subprocess import call
from Game.main import GameLauncher


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Stress De-buster")
        self.root.geometry("700x700")

        label_text = "🌟  Attention Team!!!!   Time for a screen break!   Let's recharge our minds for 10 minutes and come back with refreshed brilliance! 🚀 #TakeABreak   #RefreshAndRevive 🌟"
        label = tk.Label(root, text=label_text, font=("Helvetica", 15), wraplength=600, justify=tk.CENTER)
        label.pack(pady=50)

        # Create a frame to hold the buttons grid
        frame = tk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # List of games with corresponding image paths
        self.options = [
            ("Listen Music", "C:/Users/HP/PycharmProjects/Stress_debuster/MusicApp/MusicWindow.py", "music-maker-app.png"),
            ("Watch Memes ", "C:/Users/HP/PycharmProjects/Stress_debuster/memes/main.py", "joking.png"),
            ("Play Games ", "C:/Users/HP/PycharmProjects/Stress_debuster/Game/main.py", "arcade-game.png"),
        ]

        # Create buttons for each game in a grid layout
        for index, (option_name, option_script, image_path) in enumerate(self.options):
            button_image = self.load_button_image(image_path)
            button = tk.Button(frame, text=option_name, image=button_image, compound=tk.TOP,
                               command=lambda script=option_script: self.run_option(script))
            button.image = button_image
            button.grid(row=index // 3, column=index % 3, padx=10, pady=10)


    def load_button_image(self, image_path):
        if os.path.exists(image_path):
            image = Image.open(image_path)
            image = image.resize((150, 150),
                                 resample=Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BILINEAR)
            return ImageTk.PhotoImage(image)
        return None

    def run_option(self, script):
        try:
            if script:
                if os.path.exists(script):
                    subprocess.run(['python', script], shell=True, check=True)
                else:
                    print(f"Error: {script} not found")
            else:
                print("Selected option has no associated script.")
        except subprocess.CalledProcessError as e:
            print(f"Error running script: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()



