import random

def diceRoll():
    rollDice = random.randint(1,6)
    return rollDice
# testing the dice
# x = 0
# while x < 100:
#     outcome = diceRoll()
#     print(outcome)
#     x += 1
def monte_carlo_simulation(num_simulations):
    results = [0, 0, 0, 0, 0, 0]
    for _ in range(num_simulations):
            roll = diceRoll()
            results[roll - 1] += 1  
    probabilities = [count / num_simulations for count in results]
    return probabilities

num_simulations = 1000000  
probabilities = monte_carlo_simulation(num_simulations)


for i, probability in enumerate(probabilities):
        print(f"Face {i + 1}: Probability = {probability:.2%}")