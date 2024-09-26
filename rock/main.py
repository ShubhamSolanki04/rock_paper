import random
import streamlit as st

# Streamlit UI
st.title("Stone, Paper, Scissors Game")
st.write("Choose your move:")

# Player's choice
player_choice = st.selectbox("Your move", ["Stone", "Paper", "Scissors"])

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Stone" and computer_choice == "Scissors") or \
         (player_choice == "Scissors" and computer_choice == "Paper") or \
         (player_choice == "Paper" and computer_choice == "Stone"):
        return "You win!"
    else:
        return "You lose!"
   
    # Determine the winner
    # Button to submit the choice
if st.button("Play"):
    computer_choice = random.choice(["Stone", "Paper", "Scissors"])
    st.write(f"Computer chose: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)
    st.write(result)
