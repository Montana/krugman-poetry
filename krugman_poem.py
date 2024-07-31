import time
import random

def type_numbers():
    print("Typing numbers into spreadsheet...")
    for _ in range(3):
        print(f"{random.randint(1000, 9999)}", end=" ")
        time.sleep(0.5)
    print()

def drink_coffee():
    print("Sipping coffee from NYT mug...")
    time.sleep(1)

def tweet():
    print("Tweeting about tariffs...")
    tweets = [
        "Tariffs are not the answer! #FreeTrade",
        "Why do we still debate the benefits of global trade?",
        "Protectionism hurts more than it helps. Let's talk data."
    ]
    print(f"Tweet: {random.choice(tweets)}")
    time.sleep(1)

def krugman_routine():
    poem = """
    Paul Krugman
    economist
    sits at desk
    types numbers into spreadsheet
    frowns slightly
    thinks about global trade
    drinks coffee from mug with faded New York Times logo
    sighs
    opens X
    tweets about tariffs
    closes X
    stares out window
    wonders if anyone reads his columns anymore
    remembers he won Nobel Prize
    feels momentary satisfaction
    returns to spreadsheet
    cycle repeats
    """
    
    print(poem)
    print("\nSimulating Paul Krugman's day:\n")
    
    for cycle in range(5):
        print(f"Cycle {cycle + 1}:")
        print("Paul sits at his desk.")
        time.sleep(1)
        
        type_numbers()
        print("Paul frowns slightly.")
        time.sleep(1)
        
        print("Thinking about global trade...")
        time.sleep(2)
        
        drink_coffee()
        print("Paul sighs.")
        time.sleep(1)
        
        print("Opening X...")
        tweet()
        print("Closing X.")
        time.sleep(1)
        
        print("Staring out the window...")
        time.sleep(2)
        
        print("Paul wonders if anyone reads his columns anymore.")
        time.sleep(1)
        
        print("Remembering Nobel Prize...")
        print("Paul feels momentary satisfaction.")
        time.sleep(1)
        
        print("Returning to spreadsheet.")
        if cycle < 4:
            print("\nCycle repeats...\n")
        time.sleep(2)

    print("\nPaul Krugman's day simulation completed.")

if __name__ == "__main__":
    try:
        krugman_routine()
    except KeyboardInterrupt:
        print("\nExiting Paul Krugman simulation.")
