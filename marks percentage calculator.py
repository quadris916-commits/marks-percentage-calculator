import tkinter as tk
from tkinter import messagebox

def calculate_result():
    try:
        marks = [
            float(entry1.get()),
            float(entry2.get()),
            float(entry3.get()),
            float(entry4.get()),
            float(entry5.get())
        ]

        for mark in marks:
            if mark < 0 or mark > 100:
                messagebox.showerror("Invalid Input", "Marks must be between 0 and 100.")
                return

        total = sum(marks)
        average = total / 5
        percentage = (total / 500) * 100

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        if all(mark >= 35 for mark in marks):
            status = "Pass"
        else:
            status = "Fail"

        total_value.config(text=f"{total:.2f}")
        average_value.config(text=f"{average:.2f}")
        percentage_value.config(text=f"{percentage:.2f}%")
        grade_value.config(text=grade)
        status_value.config(text=status)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric marks in all fields.")

def clear_all():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    entry5.delete(0, tk.END)

    total_value.config(text="")
    average_value.config(text="")
    percentage_value.config(text="")
    grade_value.config(text="")
    status_value.config(text="")

root = tk.Tk()
root.title("Marks Percentage Calculator")
root.geometry("500x550")
root.config(bg="#1e1e2f")

title = tk.Label(
    root,
    text="Student Marks Calculator",
    font=("Arial", 20, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=15)

frame = tk.Frame(root, bg="#2b2b40", padx=20, pady=20)
frame.pack(pady=10)

label_style = {
    "font": ("Arial", 12),
    "bg": "#2b2b40",
    "fg": "white",
    "anchor": "w",
    "width": 18
}

entry_style = {
    "font": ("Arial", 12),
    "width": 20
}

tk.Label(frame, text="Subject 1 Marks:", **label_style).grid(row=0, column=0, pady=8, sticky="w")
entry1 = tk.Entry(frame, **entry_style)
entry1.grid(row=0, column=1, pady=8)

tk.Label(frame, text="Subject 2 Marks:", **label_style).grid(row=1, column=0, pady=8, sticky="w")
entry2 = tk.Entry(frame, **entry_style)
entry2.grid(row=1, column=1, pady=8)

tk.Label(frame, text="Subject 3 Marks:", **label_style).grid(row=2, column=0, pady=8, sticky="w")
entry3 = tk.Entry(frame, **entry_style)
entry3.grid(row=2, column=1, pady=8)

tk.Label(frame, text="Subject 4 Marks:", **label_style).grid(row=3, column=0, pady=8, sticky="w")
entry4 = tk.Entry(frame, **entry_style)
entry4.grid(row=3, column=1, pady=8)

tk.Label(frame, text="Subject 5 Marks:", **label_style).grid(row=4, column=0, pady=8, sticky="w")
entry5 = tk.Entry(frame, **entry_style)
entry5.grid(row=4, column=1, pady=8)

btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=15)

calc_btn = tk.Button(
    btn_frame,
    text="Calculate",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=12,
    command=calculate_result
)
calc_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(
    btn_frame,
    text="Clear",
    font=("Arial", 12, "bold"),
    bg="#f44336",
    fg="white",
    width=12,
    command=clear_all
)
clear_btn.grid(row=0, column=1, padx=10)

result_frame = tk.Frame(root, bg="#2b2b40", padx=20, pady=20)
result_frame.pack(pady=10)

tk.Label(result_frame, text="Total Marks:", **label_style).grid(row=0, column=0, pady=8, sticky="w")
total_value = tk.Label(result_frame, text="", font=("Arial", 12, "bold"), bg="#2b2b40", fg="#00ffcc", width=20, anchor="w")
total_value.grid(row=0, column=1, pady=8)

tk.Label(result_frame, text="Average:", **label_style).grid(row=1, column=0, pady=8, sticky="w")
average_value = tk.Label(result_frame, text="", font=("Arial", 12, "bold"), bg="#2b2b40", fg="#00ffcc", width=20, anchor="w")
average_value.grid(row=1, column=1, pady=8)

tk.Label(result_frame, text="Percentage:", **label_style).grid(row=2, column=0, pady=8, sticky="w")
percentage_value = tk.Label(result_frame, text="", font=("Arial", 12, "bold"), bg="#2b2b40", fg="#00ffcc", width=20, anchor="w")
percentage_value.grid(row=2, column=1, pady=8)

tk.Label(result_frame, text="Grade:", **label_style).grid(row=3, column=0, pady=8, sticky="w")
grade_value = tk.Label(result_frame, text="", font=("Arial", 12, "bold"), bg="#2b2b40", fg="#00ffcc", width=20, anchor="w")
grade_value.grid(row=3, column=1, pady=8)

tk.Label(result_frame, text="Status:", **label_style).grid(row=4, column=0, pady=8, sticky="w")
status_value = tk.Label(result_frame, text="", font=("Arial", 12, "bold"), bg="#2b2b40", fg="#00ffcc", width=20, anchor="w")
status_value.grid(row=4, column=1, pady=8)

root.mainloop()