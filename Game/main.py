import tkinter as tk
from PIL import Image, ImageTk
import os


class GameLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Launcher")
        self.root.geometry("700x700")

        # Create a frame to hold the buttons grid
        frame = tk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # List of games with corresponding image paths
        self.games = [
            ("Breakout", "E:\Stress_debuster\Game\\breakout.py", "E:\Stress_debuster\Game\imgicon\\breakout.png"),
            ("Flappy Bird", "E:\Stress_debuster\Game\\flappy.py", "E:\Stress_debuster\Game\imgicon\\flappy.png"),
            ("Snake", "E:\Stress_debuster\Game\\snake.py", "E:\Stress_debuster\Game\imgicon\\snake.png"),
            ("Tic Tac Toe", "E:\Stress_debuster\Game\\tictactoe.py", "E:\Stress_debuster\Game\imgicon\\tictactoe.png"),
        ]

        # Create buttons for each game in a grid layout
        for index, (game_name, game_script, image_path) in enumerate(self.games):
            button_image = self.load_button_image(image_path)
            button = tk.Button(frame, text=game_name, image=button_image, compound=tk.TOP,
                               command=lambda script=game_script: self.run_game(script))
            button.image = button_image
            button.grid(row=index // 2, column=index % 2, padx=10, pady=10)

        # Add a label with the specified text
        label_text = "Dance into relaxation with the funky beats of gaming: where pixels play the rhythm of pure joy!"
        label = tk.Label(root, text=label_text, font=("Helvetica", 12), wraplength=600, justify=tk.CENTER)
        label.pack(pady=50)

    def load_button_image(self, image_path):
        if os.path.exists(image_path):
            image = Image.open(image_path)
            image = image.resize((150, 150),
                                 resample=Image.LANCZOS)
            return ImageTk.PhotoImage(image)
        return None

    def run_game(self, script):
        os.system(f'python {script}')


if __name__ == "__main__":
    root = tk.Tk()
    app = GameLauncher(root)
    root.mainloop()
