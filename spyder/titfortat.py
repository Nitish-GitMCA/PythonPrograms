def tit_for_tat(player_moves, opponent_moves):
    if len(opponent_moves) == 0:
        # Start by cooperating
        return 'cooperate'
    else:
        # Mirror opponent's last move
        return opponent_moves[-1]

# Example of playing the Tit-for-Tat game for 5 rounds
num_rounds = 5
player_history = []
opponent_history = []

for i in range(num_rounds):
    player_move = tit_for_tat(player_history, opponent_history)
    opponent_move = 'cooperate' if input(f"Round {i + 1}: Your move? Type 'cooperate' or 'defect': ") == 'cooperate' else 'defect'

    player_history.append(player_move)
    opponent_history.append(opponent_move)

    print(f"Player move: {player_move}, Opponent move: {opponent_move}")

# Print the final outcome
player_score = sum(1 for p, o in zip(player_history, opponent_history) if p == 'cooperate' and o == 'cooperate')
opponent_score = sum(1 for p, o in zip(player_history, opponent_history) if p == 'defect' and o == 'cooperate')

print(f"\nFinal Scores - Player: {player_score}, Opponent: {opponent_score}")
if player_score > opponent_score:
    print("Player wins!")
elif player_score < opponent_score:
    print("Opponent wins!")
else:
    print("It's a tie!")
