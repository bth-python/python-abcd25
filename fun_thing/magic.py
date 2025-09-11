import random
import time

answers = [
    "Yes, absolutely! 🎉",
    "Nope, try again later. ❌",
    "Hmm... maybe 🤔",
    "Ask me after coffee ☕",
    "Definitely YES 🚀",
    "99% chance of success 🌟",
]

print("🎱 Welcome to the Magic 8-Ball 🎱")
question = input("Ask me anything: ")

print("Thinking...")
time.sleep(2)  # pause for effect
print(random.choice(answers))
