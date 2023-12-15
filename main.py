import time
from keyboard import press
import tkinter as tk

def count_words():
    input_text = input_field.get()  # Get the text from the input field
    word_count = len(input_text.split())  # Split the text into words and count them
    word_count_label.config(text=f"Word count: {word_count}")

def start_countdown():
    countdown(60)

def countdown(seconds):
    if seconds >= 0:
        countdown_label.config(text=f"Time remaining: {seconds} seconds")
        window.after(1000, countdown, seconds - 1)
    else:
        countdown_label.config(text="Time's up!")


# Create the main window
window = tk.Tk()
window.title("Countdown Timer")
window.geometry("800x600")

# Create the countdown timer label
countdown_label = tk.Label(window, text="Countdown Timer")
countdown_label.grid(row=0, column=1)

# Create the input field
input_field = tk.Entry(window, width=50)
input_field.grid(row=2, column=1)

# Create the text field
text_field = tk.Text(window, height=8, width=50)
text = "Rectal prolapse is a condition in which part of the wall or the entire wall of the rectum falls out of place. Rectal prolapse can be a medical emergency. In some cases, the rectum may protrude."
text_field.grid(row=1, column=1)
text_field.insert(tk.END, text)
text_field.config(state=tk.DISABLED)

# Create the word count label
word_count_label = tk.Label(window, text="Word count: 0")
word_count_label.grid(column=2, row=3)

# Create the start button
start_button = tk.Button(window, text="Start", command=start_countdown)
start_button.grid(row=2, column=2)

# Start the Tkinter event loop
window.mainloop()