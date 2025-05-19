import tkinter as tk
from tkinter import messagebox
import random

class FarkleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Farkle Game")
        self.geometry("800x600")
        self.bg_color = '#ffffff'
        self.fg_color = '#222222'
        self.dice_bg = '#dddddd'
        self.configure(bg=self.bg_color)
        self.players = []
        self.num_players = 0
        self.target_score = 10000
        self.scores = []
        self.banked_points = 0
        self.current_player_index = 0
        self.dice = []
        self.dice_buttons = []
        self.kept_dice = []
        self.remaining_dice = 6
        self._build_splash_screen()

    def _clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def _build_splash_screen(self):
        self._clear_screen()
        title_label = tk.Label(self, text="Welcome to Farkle!", font=("Arial", 20, "bold"), bg=self.bg_color, fg=self.fg_color)
        title_label.pack(pady=20)

        self.rules_var = tk.BooleanVar()
        rules_check = tk.Checkbutton(self, text="Show game rules", variable=self.rules_var, bg=self.bg_color, fg=self.fg_color, selectcolor=self.bg_color)
        rules_check.pack()

        tk.Label(self, text="Number of Players (1-6):", bg=self.bg_color, fg=self.fg_color).pack(pady=10)
        self.num_players_entry = tk.Entry(self, justify='center', bg=self.bg_color, fg=self.fg_color)
        self.num_players_entry.pack()

        tk.Label(self, text="Target Score (Default 10000):", bg=self.bg_color, fg=self.fg_color).pack(pady=10)
        self.target_score_entry = tk.Entry(self, justify='center', bg=self.bg_color, fg=self.fg_color)
        self.target_score_entry.pack()

        start_btn = tk.Button(self, text="Continue", command=self._on_start)
        start_btn.pack(pady=20)

    def _on_start(self):
        try:
            self.num_players = int(self.num_players_entry.get())
            if not (1 <= self.num_players <= 6):
                raise ValueError("Player count must be 1 to 6")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number of players (1-6).")
            return

        target_score_text = self.target_score_entry.get()
        if target_score_text.strip():
            try:
                self.target_score = int(target_score_text)
            except ValueError:
                messagebox.showerror("Invalid Input", "Target score must be a number.")
                return

        if self.rules_var.get():
            self._show_rules()

        self._build_player_setup()

    def _show_rules(self):
        rules = (
            "Object: Reach the highest score above 10,000 in the final round!\n\n"
            "- Roll six dice. Earn points for 1s, 5s, triples, etc.\n"
            "- Farkle = no scoring dice. Lose turn and points from that turn.\n"
            "- You may keep scoring dice and re-roll the rest.\n"
            "- Hot Dice = use all dice for scoring, re-roll all 6 again.\n"
            "- Three Farkles in a row: -1000 points penalty.\n"
            "- Final round starts when a player reaches 10,000 points."
        )
        messagebox.showinfo("Farkle Rules", rules)

    def _build_player_setup(self):
        self._clear_screen()
        tk.Label(self, text="Enter Player Names:", font=("Arial", 14), bg=self.bg_color, fg=self.fg_color).pack(pady=10)
        self.player_name_vars = []
        for i in range(self.num_players):
            frame = tk.Frame(self, bg=self.bg_color)
            frame.pack(pady=5)
            tk.Label(frame, text=f"Player {i + 1}:", bg=self.bg_color, fg=self.fg_color).pack(side=tk.LEFT, padx=10)
            name_var = tk.StringVar()
            tk.Entry(frame, textvariable=name_var, bg=self.bg_color, fg=self.fg_color).pack(side=tk.LEFT)
            self.player_name_vars.append(name_var)

        tk.Button(self, text="Start Game", command=self._start_game).pack(pady=20)

    def _start_game(self):
        self.players = [var.get().strip() or f"Player {i + 1}" for i, var in enumerate(self.player_name_vars)]
        self.scores = [0] * self.num_players
        self._build_game_window()

    def _build_game_window(self):
        self._clear_screen()
        self.banked_points = 0
        self.remaining_dice = 6

        self.scoreboard = tk.Label(self, text="", font=("Arial", 12), bg=self.bg_color, fg=self.fg_color, justify=tk.LEFT)
        self.scoreboard.pack(pady=10)

        self.info_label = tk.Label(self, text=f"{self.players[self.current_player_index]}'s Turn", font=("Arial", 16), bg=self.bg_color, fg=self.fg_color)
        self.info_label.pack(pady=10)

        self.dice_frame = tk.Frame(self, bg=self.bg_color)
        self.dice_frame.pack(pady=10)
        self.dice_buttons = []
        for i in range(6):
            btn = tk.Button(self.dice_frame, text="", font=("Arial", 24), width=3, height=2, bg=self.dice_bg, command=lambda i=i: self._toggle_keep(i))
            btn.grid(row=0, column=i, padx=5)
            self.dice_buttons.append(btn)

        self.bank_button = tk.Button(self, text="Bank Selected Points", command=self._bank_points)
        self.bank_button.pack(pady=5)

        self.roll_button = tk.Button(self, text="Roll Remaining Dice", command=self._roll_dice)
        self.roll_button.pack(pady=5)

        self.end_turn_button = tk.Button(self, text="End Turn (Add Banked Points)", command=self._end_turn)
        self.end_turn_button.pack(pady=5)

        self.status_label = tk.Label(self, text="", bg=self.bg_color, fg=self.fg_color)
        self.status_label.pack(pady=10)

        self._roll_dice()

    def _roll_dice(self):
        if self.remaining_dice == 0:
            self.remaining_dice = 6  # Hot Dice reset
        self.dice = [random.randint(1, 6) for _ in range(self.remaining_dice)]
        for i in range(6):
            if i < len(self.dice):
                self.dice_buttons[i].config(text=str(self.dice[i]), state=tk.NORMAL, relief=tk.RAISED)
            else:
                self.dice_buttons[i].config(text="", state=tk.DISABLED)
        self.kept_dice.clear()
        self.status_label.config(text="Select dice to keep.")
        self._update_scoreboard()

    def _toggle_keep(self, index):
        if index not in self.kept_dice:
            self.kept_dice.append(index)
            self.dice_buttons[index].config(relief=tk.SUNKEN)
        else:
            self.kept_dice.remove(index)
            self.dice_buttons[index].config(relief=tk.RAISED)

    def _bank_points(self):
        score = sum(100 if self.dice[i] == 1 else 50 if self.dice[i] == 5 else 0 for i in self.kept_dice)
        if score == 0:
            self.status_label.config(text="No valid scoring dice selected.")
            return
        self.banked_points += score
        self.remaining_dice -= len(self.kept_dice)
        if self.remaining_dice == 0:
            self.remaining_dice = 6  # Hot dice reset
        self.status_label.config(text=f"Banked {score} points! Roll again or end turn.")
        self.kept_dice.clear()
        self._update_scoreboard()

    def _end_turn(self):
        self.scores[self.current_player_index] += self.banked_points
        if self.scores[self.current_player_index] >= self.target_score:
            messagebox.showinfo("Game Over", f"{self.players[self.current_player_index]} wins with {self.scores[self.current_player_index]} points!")
            self.destroy()
            return
        self.current_player_index = (self.current_player_index + 1) % self.num_players
        self._build_game_window()

    def _update_scoreboard(self):
        board = "\n".join(f"{name}: {score} pts" for name, score in zip(self.players, self.scores))
        board += f"\n\nBanked Points: {self.banked_points}"
        self.scoreboard.config(text=board)

if __name__ == "__main__":
    app = FarkleApp()
    app.mainloop()
