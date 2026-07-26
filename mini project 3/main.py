import time # time module is imported and used for time related functions.
import random 

sentences = [
    "The quick brown fox jumped over the lazy dog near the river bank.",
    "Learning to code every day helps improve problem solving and logical thinking skills.",
    "A gentle breeze moved through the trees while birds sang in the morning sunlight.",
    "She packed her backpack with books, snacks, and a water bottle before leaving home."

]

def measure_accuracy(user_input, test_sentences):
    correct_chars = sum(1 for a, b in zip(user_input, test_sentences) if a==b)
    accuracy = (correct_chars / len(test_sentences)) * 100 if test_sentences else 0
    return accuracy

def typing_test():
    test_sentences = random.choice(sentences)
    print("Type the following sentence as fast as you can:")
    print(test_sentences)
    input("Press Enter when you are ready...")
    start_time = time.time() # Measure  the start time
    user_input = input("\nStart Typing:\n")
    end_time = time.time() # Measure the end time
    time_taken = end_time - start_time
    word_count = len(test_sentences.split(" "))

    print("Results:")
    print(f"Time taken: {time_taken} seconds")
    print(f"Words typed: {word_count}")
    print(f"Typing Speed: {word_count} / {(time_taken / 60):.2f} words per minute")
    accuracy = measure_accuracy(user_input, test_sentences)
    print(f"Accuracy: {accuracy:.2f}%")

typing_test()

#overall flow of code 
# Program Starts
#       │
#       ▼
# Import Modules
#       │
#       ▼
# Choose Random Sentence
#       │
#       ▼
# Display Sentence
#       │
#       ▼
# Wait for Enter
#       │
#       ▼
# Start Timer
#       │
#       ▼
# User Types Sentence
#       │
#       ▼
# Stop Timer
#       │
#       ▼
# Calculate Time
#       │
#       ▼
# Calculate WPM
#       │
#       ▼
# Calculate Accuracy
#       │
#       ▼
# Display Results
#       │
#       ▼
# Program Ends
