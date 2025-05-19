import random
import time
from collections import Counter
import os

class Colors:
    # ANSI color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class FarkleGame:
    def __init__(self, num_players=2, target_score=10000):
        self.num_players = num_players
        self.target_score = target_score
        self.scores = [0 for _ in range(num_players)]
        self.round_scores = [0 for _ in range(num_players)] # Track scores for the current round
        self.current_player = 0
        self.final_round = False
        self.consecutive_farkles = [0 for _ in range(num_players)]
        # Player colors for scoreboard
        self.player_colors = [
            Colors.RED,
            Colors.GREEN,
            Colors.YELLOW,
            Colors.BLUE,
            Colors.MAGENTA,
            Colors.CYAN
        ]
        
    def roll_dice(self, num_dice):
        """Roll the specified number of dice"""
        print(f"\n{Colors.BOLD}Rolling dice...{Colors.END}")
        # Visual rolling effect
        for _ in range(3):
            temp_roll = [random.randint(1, 6) for _ in range(num_dice)]
            self.display_roll(temp_roll, highlight_scorable=False)
            time.sleep(0.3)
            if os.name == 'posix':  # For Unix/Linux/Mac
                os.system('clear')
            else:  # For Windows
                os.system('cls')
                
        # Final roll
        final_roll = [random.randint(1, 6) for _ in range(num_dice)]
        return final_roll
    
    def calculate_score(self, dice):
        """Calculate the score for a given dice combination"""
        if not dice:
            return 0, 0
            
        dice_counter = Counter(dice)
        total_score = 0
        scorable_dice = 0
        
        # Check for straight (1-2-3-4-5-6)
        if len(dice) == 6 and sorted(dice) == [1, 2, 3, 4, 5, 6]:
            return 6, 1500
            
        # Check for three pairs (requires exactly 6 dice)
        if len(dice) == 6:
            values = list(dice_counter.values())
            if sorted(values) == [2, 2, 2] and len(dice_counter) == 3:
                return 6, 1500
                
        # Check for two triplets (requires exactly 6 dice)
        if len(dice) == 6:
            values = list(dice_counter.values())
            if sorted(values) == [3, 3] and len(dice_counter) == 2:
                return 6, 2500
        
        # Check for 4, 5, or 6 of a kind
        for num, count in dice_counter.items():
            if count >= 4:
                if count == 4:
                    # 4 of a kind
                    total_score += 1000
                    scorable_dice += 4
                elif count == 5:
                    # 5 of a kind
                    total_score += 2000
                    scorable_dice += 5
                elif count == 6:
                    # 6 of a kind
                    total_score += 3000
                    scorable_dice += 6
                continue
                
            if count >= 3:
                # Three of a kind
                if num == 1:
                    total_score += 1000
                else:
                    total_score += num * 100
                scorable_dice += 3
                
                # Count remaining 1's and 5's separately
                remaining = count - 3
            else:
                remaining = count
                
            # Add individual 1's and 5's (that aren't part of 3+ of a kind)
            if num == 1:
                total_score += remaining * 100
                scorable_dice += remaining
            elif num == 5:
                total_score += remaining * 50
                scorable_dice += remaining
                
        return scorable_dice, total_score
    
    def identify_scorable_dice(self, dice):
        """Returns possible scoring combinations from the dice"""
        if not dice:
            return []
            
        dice_counter = Counter(dice)
        combinations = []
        
        # Check for straight (1-2-3-4-5-6)
        if len(dice) == 6 and sorted(dice) == [1, 2, 3, 4, 5, 6]:
            combinations.append(("Straight", 1500, dice.copy()))
            
        # Check for three pairs
        if len(dice) == 6:
            values = list(dice_counter.values())
            if sorted(values) == [2, 2, 2] and len(dice_counter) == 3:
                combinations.append(("Three Pairs", 1500, dice.copy()))
                
        # Check for two triplets
        if len(dice) == 6:
            values = list(dice_counter.values())
            if sorted(values) == [3, 3] and len(dice_counter) == 2:
                combinations.append(("Two Triplets", 2500, dice.copy()))
                
        # Check for 4, 5, or 6 of a kind
        for num, count in dice_counter.items():
            if count == 6:
                combinations.append((f"Six {num}'s", 3000, [num] * 6))
            elif count == 5:
                combinations.append((f"Five {num}'s", 2000, [num] * 5))
            elif count == 4:
                combinations.append((f"Four {num}'s", 1000, [num] * 4))
            elif count == 3:
                if num == 1:
                    combinations.append((f"Three {num}'s", 1000, [num] * 3))
                else:
                    combinations.append((f"Three {num}'s", num * 100, [num] * 3))
                    
        # Individual 1's and 5's
        if 1 in dice_counter and dice_counter[1] < 3:
            for _ in range(dice_counter[1]):
                combinations.append(("Single 1", 100, [1]))
                
        if 5 in dice_counter and dice_counter[5] < 3:
            for _ in range(dice_counter[5]):
                combinations.append(("Single 5", 50, [5]))
                
        return combinations
    
    def get_scorable_dice(self, dice):
        """Return which dice positions are scorable"""
        scorable = []
        
        # Check for straight, three pairs, or two triplets
        if len(dice) == 6:
            if sorted(dice) == [1, 2, 3, 4, 5, 6]:
                return list(range(len(dice)))
                
            dice_counter = Counter(dice)
            
            values = list(dice_counter.values())
            if sorted(values) == [2, 2, 2] and len(dice_counter) == 3:
                return list(range(len(dice)))
                
            if sorted(values) == [3, 3] and len(dice_counter) == 2:
                return list(range(len(dice)))
        
        # Check for 4, 5, or 6 of a kind
        dice_counter = Counter(dice)
        for value, count in dice_counter.items():
            if count >= 3:
                positions = [i for i, die in enumerate(dice) if die == value]
                scorable.extend(positions[:count])  # Take only the count we need
                
        # Check individual 1's and 5's
        for i, die in enumerate(dice):
            if i not in scorable:  # Avoid counting dice twice
                if die == 1 or die == 5:
                    scorable.append(i)
                    
        return sorted(scorable)
    
    def check_farkle(self, dice):
        """Check if the roll is a Farkle (no scoring dice)"""
        scorable = self.get_scorable_dice(dice)
        return len(scorable) == 0
    
    def select_dice(self, dice, selected_indices):
        """Return the selected dice and the remaining dice"""
        selected = [dice[i] for i in selected_indices]
        remaining = [d for i, d in enumerate(dice) if i not in selected_indices]
        return selected, remaining
    
    def display_roll(self, dice, highlight_scorable=True):
        """Display the dice roll in a friendly format with improved visibility"""
        dice_faces = {
            1: "⚀",
            2: "⚁",
            3: "⚂",
            4: "⚃",
            5: "⚄",
            6: "⚅"
        }
        
        # Get scorable indices if highlighting
        scorable_indices = self.get_scorable_dice(dice) if highlight_scorable else []
        
        # Display dice with appropriate colors
        dice_display = []
        for i, d in enumerate(dice):
            if i in scorable_indices:
                # Highlight scorable dice in bright green
                dice_display.append(f"{Colors.GREEN}{Colors.BOLD}{dice_faces[d]}{Colors.END}")
            else:
                # Normal dice in white
                dice_display.append(f"{Colors.WHITE}{dice_faces[d]}{Colors.END}")
        
        print(f"Dice: {' '.join(dice_display)}")
        
        # Display position numbers in cyan for better visibility
        position_display = []
        for i in range(len(dice)):
            position_display.append(f"{Colors.CYAN}{Colors.BOLD}{i+1}{Colors.END}")
        
        print(f"Pos:  {' '.join(position_display)}")
    
    def display_scoreboard(self):
        """Display a colorful scoreboard with player scores"""
        print(f"\n{Colors.BOLD}{Colors.UNDERLINE}SCOREBOARD{Colors.END}")
        print(f"{Colors.BOLD}{'Player':<10} {'Round':<10} {'Total':<10}{Colors.END}")
        print("-" * 30)
        
        for i in range(self.num_players):
            player_color = self.player_colors[i % len(self.player_colors)]
            print(f"{player_color}Player {i+1}:{Colors.END} {self.round_scores[i]:<10} {self.scores[i]:<10}")
            
        print("-" * 30)
    
    def play_turn(self, player_index):
        """Play a turn for the specified player"""
        player_color = self.player_colors[player_index % len(self.player_colors)]
        print(f"\n{player_color}{Colors.BOLD}Player {player_index + 1}'s turn{Colors.END}")
        print(f"Current score: {self.scores[player_index]}")
        
        # Reset round score for this player
        self.round_scores[player_index] = 0
        
        remaining_dice = 6
        turn_score = 0
        roll_again = True
        
        input(f"{player_color}Press Enter to start your turn...{Colors.END}")
        
        while roll_again and remaining_dice > 0:
            # Automatic dice rolling
            current_roll = self.roll_dice(remaining_dice)
            
            print(f"\n{player_color}Player {player_index + 1}{Colors.END} rolled:")
            self.display_roll(current_roll)
            
            if self.check_farkle(current_roll):
                print(f"\n{Colors.RED}{Colors.BOLD}FARKLE!{Colors.END} You lose all points from this turn.")
                self.consecutive_farkles[player_index] += 1
                
                if self.consecutive_farkles[player_index] >= 3:
                    print(f"{Colors.RED}{Colors.BOLD}Three Farkles in a row! You lose 1000 points.{Colors.END}")
                    self.scores[player_index] = max(0, self.scores[player_index] - 1000)
                    self.consecutive_farkles[player_index] = 0
                    
                # Update round score to zero for this player
                self.round_scores[player_index] = 0
                self.display_scoreboard()    
                input("Press Enter to continue...")
                return False
            else:
                self.consecutive_farkles[player_index] = 0
                
            scorable_indices = self.get_scorable_dice(current_roll)
            scorable_combinations = self.identify_scorable_dice(current_roll)
            
            print(f"\n{Colors.BOLD}Scoring combinations available:{Colors.END}")
            for i, (name, points, dice_combo) in enumerate(scorable_combinations):
                dice_str = ", ".join([str(d) for d in dice_combo])
                print(f"{i+1}. {name}: {Colors.YELLOW}{points} points{Colors.END} ({dice_str})")
            
            valid_selection = False
            selected_indices = []
            
            while not valid_selection:
                try:
                    selection = input(f"\n{Colors.CYAN}Choose dice positions to keep (separated by spaces, e.g. '1 3 4'):{Colors.END} ")
                    if selection.strip():
                        selected_indices = [int(pos) - 1 for pos in selection.split()]
                        
                        # Validate selection
                        if not all(0 <= idx < len(current_roll) for idx in selected_indices):
                            print(f"{Colors.RED}Invalid positions. Please choose positions between 1 and {len(current_roll)}{Colors.END}")
                            continue
                            
                        if not all(idx in scorable_indices for idx in selected_indices):
                            print(f"{Colors.RED}Invalid selection. You can only select scorable dice.{Colors.END}")
                            continue
                            
                        if not selected_indices:
                            print(f"{Colors.RED}You must select at least one die.{Colors.END}")
                            continue
                            
                        # Make sure the selection is valid scoring-wise
                        selected_dice, _ = self.select_dice(current_roll, selected_indices)
                        scorable_count, score = self.calculate_score(selected_dice)
                        
                        if scorable_count != len(selected_dice):
                            print(f"{Colors.RED}Your selection is not a valid scoring combination.{Colors.END}")
                            continue
                            
                        valid_selection = True
                    else:
                        print(f"{Colors.RED}You must select at least one die.{Colors.END}")
                except ValueError:
                    print(f"{Colors.RED}Invalid input. Please enter numbers separated by spaces.{Colors.END}")
            
            selected_dice, remaining_dice_list = self.select_dice(current_roll, selected_indices)
            _, score = self.calculate_score(selected_dice)
            
            turn_score += score
            self.round_scores[player_index] = turn_score  # Update round score
            
            print(f"\nSelected dice: {selected_dice}")
            print(f"Score from this selection: {Colors.YELLOW}{score}{Colors.END}")
            print(f"Turn score so far: {Colors.YELLOW}{turn_score}{Colors.END}")
            
            # Display current scoreboard
            self.display_scoreboard()
            
            remaining_dice = len(remaining_dice_list)
            
            # If all dice have been used, player gets all 6 back
            if remaining_dice == 0:
                print(f"\n{Colors.GREEN}{Colors.BOLD}Hot dice!{Colors.END} You've used all dice and get to roll all 6 dice again!")
                remaining_dice = 6
            
            if remaining_dice > 0:
                choice = input(f"\n{Colors.CYAN}You have {remaining_dice} dice remaining. Roll again? (y/n):{Colors.END} ").strip().lower()
                roll_again = choice == 'y'
            else:
                roll_again = False
                
            if not roll_again:
                self.scores[player_index] += turn_score
                print(f"\n{Colors.GREEN}Banking {turn_score} points. New total: {self.scores[player_index]}{Colors.END}")
                
                # Check if player has reached target score to initiate final round
                if not self.final_round and self.scores[player_index] >= self.target_score:
                    print(f"\n{Colors.MAGENTA}{Colors.BOLD}Player {player_index + 1} has reached {self.target_score}! Final round begins!{Colors.END}")
                    self.final_round = True
        
        # Reset round score for next turn
        self.round_scores[player_index] = 0
        
        input("Press Enter to continue...")
        return True
    
    def play_game(self):
        """Play the full game of Farkle"""
        print(f"\n{Colors.BOLD}{Colors.YELLOW}===== WELCOME TO FARKLE ====={Colors.END}")
        print(f"First player to reach {Colors.GREEN}{self.target_score}{Colors.END} points triggers the final round!")
        
        game_over = False
        starting_player = 0
        round_number = 1
        
        while not game_over:
            print(f"\n{Colors.BOLD}{Colors.YELLOW}===== ROUND {round_number} ====={Colors.END}")
            self.display_scoreboard()
                
            for i in range(self.num_players):
                current_player_idx = (starting_player + i) % self.num_players
                print("\n" + "="*40)
                
                self.play_turn(current_player_idx)
                
                # Check if we're in the final round and have completed a full cycle
                if self.final_round and current_player_idx == (starting_player - 1) % self.num_players:
                    game_over = True
                    break
            
            round_number += 1
            
            if game_over:
                break
        
        # Determine winner
        max_score = max(self.scores)
        winners = [i+1 for i, score in enumerate(self.scores) if score == max_score]
        
        print(f"\n{Colors.BOLD}{Colors.YELLOW}===== GAME OVER ====={Colors.END}")
        self.display_scoreboard()
        
        if len(winners) == 1:
            winner_color = self.player_colors[(winners[0]-1) % len(self.player_colors)]
            print(f"\n{winner_color}{Colors.BOLD}Player {winners[0]} wins with {max_score} points!{Colors.END}")
        else:
            print(f"\n{Colors.BOLD}It's a tie between Players {', '.join(map(str, winners))} with {max_score} points!{Colors.END}")

def print_rules():
    """Display the rules of Farkle"""
    print(f"\n{Colors.BOLD}{Colors.YELLOW}===== FARKLE RULES ====={Colors.END}")
    print(f"{Colors.BOLD}Object:{Colors.END} The player with the highest score above 10,000 points on the final round wins!")
    print(f"\n{Colors.BOLD}How to Play:{Colors.END}")
    print("- Each player takes turns rolling six dice")
    print("- Points are earned for 1's, 5's, three-of-a-kind, etc.")
    print("- If no dice score points, that's a Farkle! You lose your turn and any points accumulated this turn")
    print("- You can bank your points at any time and pass to the next player")
    print("- If you use all six dice in scoring combinations, you get to roll all six again ('Hot Dice')")
    print("- The final round begins when a player reaches 10,000 points")
    print(f"\n{Colors.BOLD}Scoring:{Colors.END}")
    print(f"- Single 1: {Colors.YELLOW}100 points{Colors.END}")
    print(f"- Single 5: {Colors.YELLOW}50 points{Colors.END}")
    print(f"- Three 1's: {Colors.YELLOW}1000 points{Colors.END}")
    print(f"- Three 2's: {Colors.YELLOW}200 points{Colors.END}")
    print(f"- Three 3's: {Colors.YELLOW}300 points{Colors.END}")
    print(f"- Three 4's: {Colors.YELLOW}400 points{Colors.END}")
    print(f"- Three 5's: {Colors.YELLOW}500 points{Colors.END}")
    print(f"- Three 6's: {Colors.YELLOW}600 points{Colors.END}")
    print(f"- Four of a kind: {Colors.YELLOW}1000 points{Colors.END}")
    print(f"- Five of a kind: {Colors.YELLOW}2000 points{Colors.END}")
    print(f"- Six of a kind: {Colors.YELLOW}3000 points{Colors.END}")
    print(f"- Straight (1-2-3-4-5-6): {Colors.YELLOW}1500 points{Colors.END}")
    print(f"- Three pairs: {Colors.YELLOW}1500 points{Colors.END}")
    print(f"- Two triplets: {Colors.YELLOW}2500 points{Colors.END}")
    print(f"- Three Farkles in a row: {Colors.RED}Lose 1000 points{Colors.END}")
    print("\n=======================")

if __name__ == "__main__":
    print(f"{Colors.BOLD}{Colors.GREEN}Welcome to Farkle!{Colors.END}")
    
    show_rules = input("Would you like to see the rules? (y/n): ").strip().lower()
    if show_rules == 'y':
        print_rules()
    
    num_players = 0
    while num_players < 1:
        try:
            num_players = int(input("\nEnter number of players (1-6): "))
            if num_players < 1 or num_players > 6:
                print(f"{Colors.RED}Number of players must be between 1 and 6.{Colors.END}")
                num_players = 0
        except ValueError:
            print(f"{Colors.RED}Please enter a valid number.{Colors.END}")
    
    target = input("Enter target score (default 10000): ")
    target_score = 10000 if not target.strip() else int(target)
    
    game = FarkleGame(num_players, target_score)
    game.play_game()
