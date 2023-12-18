import random
import keyboard
from prompts import prompts
import tkinter as tk

def count_words():
    input_text = input_field.get()  # Get the text from the input field
    word_count = len(input_text.split())  # Split the text into words and count them
    word_count_label.config(text=f"Speed: {word_count} WPM")

def start_countdown():
    countdown(60)
    start_button.config(state=tk.DISABLED)
    input_field.config(state=tk.NORMAL)
    input_field.focus_set()
    text_field.config(state=tk.NORMAL)
    text_field.delete("1.0", tk.END)  # Clear the text field
    text_field.insert(tk.END, prompt_text)

def check_accuracy():
    input_text = input_field.get()
    text_field_text = text_field.get("1.0", tk.END).strip()

    if input_text == text_field_text:
        accuracy_level.config(text="100%")
    else:
        input_words = input_text.split()
        text_field_words = text_field_text.split()
        wrong_words = []

        for i in range(len(input_words)):
            if i >= len(text_field_words) or input_words[i] != text_field_words[i]:
                start_index = f"1.{len(' '.join(input_words[:i]))}"
                end_index = f"1.{len(' '.join(input_words[:i+1]))}"
                text_field.tag_add("highlight", start_index, end_index)
                wrong_words.append(i)
        accuracy_grade = (len(input_words) - len(wrong_words)) / len(input_words) * 100
        accuracy_level.config(text=f"Accuracy: {accuracy_grade:.2f}%")

def countdown(seconds):
    if seconds >= 0:
        countdown_label.config(text=f"Time remaining: {seconds} seconds")
        window.after(1000, countdown, seconds - 1)
    else:
        keyboard.press('enter')
        countdown_label.config(text="Time's up!")
        check_accuracy()
        count_words()
        start_button.config(state=tk.NORMAL)
        input_field.config(state=tk.DISABLED)


# Create the main window
window = tk.Tk()
window.title("WPM Calculator")
window.geometry("800x600")

# Create the countdown timer label
countdown_label = tk.Label(window, text="Time remaining:")
countdown_label.grid(row=0, column=1)

# Create the input field
input_field = tk.Entry(window, width=100, state=tk.DISABLED)
input_field.grid(row=4, column=1, columnspan=1)

# Typing prompt text
prompt_text = random.choice(prompts)

# Create the text field
text_field = tk.Text(window, height=8, width=90, state=tk.DISABLED)
text_field.grid(row=3, column=1, columnspan=3)
text_field.config(state=tk.DISABLED, bd=1, relief=tk.SOLID)

# Create the word count label
word_count_label = tk.Label(window, text="Word count: 0")
word_count_label.grid(column=1, row=2)

# Create the accuracy label
accuracy_level = tk.Label(window, text="Accuracy:")
accuracy_level.grid(column=1, row=1)

# Configure the tag for highlighting
text_field.tag_configure("highlight", background="yellow")

# Create the start button
start_button = tk.Button(window, text="Start", command=start_countdown)
start_button.grid(row=5, column=1)

# Start the Tkinter event loop
window.mainloop()