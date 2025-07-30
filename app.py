import time
import os
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

clear()

# Header
print("=" * 50)
print("🎩 MAGIC NUMBER GAME 🎩")
print("👨‍💻 Created with magic by Rayyan Iqbal(fusion fc player btw)")
print("=" * 50)
time.sleep(2)

# Intro
typewriter("\nWelcome, bitch 👁️")
typewriter("You're about to witness real magic...")
time.sleep(1.5)

# ASCII Magic Hat
print(r"""
             _____
            /     \
           /       \ 
           \       /
            \_____/
             ( . .)  
        ---oOO-(_)-OOo---
""")
time.sleep(2)

typewriter("\nStep 1: Think of a number in your mind 🧠")
time.sleep(2)
typewriter("Step 2: Now type that number below 👇")
number = input("Enter your number: ")

typewriter("\nHold on... I'm entering the mind  🌀")
time.sleep(1.5)
typewriter("Reading your thoughts...")
time.sleep(1.5)
typewriter("why u thinking about me tho...")
time.sleep(1.5)
typewriter("cmonnnnnnnn...")
time.sleep(2)
typewriter("Almost there...")
time.sleep(1)

# Dramatic Reveal
typewriter(f"\nThe number you were thinking of is... {number} 😲", delay=0.05)
time.sleep(1)

typewriter("\nWhoa! HAHA BITCH 😉")
typewriter("Thanks!")

# Outro
print("\n✨splendid ✨")
