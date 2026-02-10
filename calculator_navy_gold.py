import tkinter as tk

# =========================
# Main Window
# =========================
main_window = tk.Tk()
main_window.title("Anamika Rani Calculator")
main_window.geometry("400x530")
main_window.configure(bg="#1a365d")  # Navy blue - Professional, trustworthy

# =================================================
# Click Function (supports multi-step expressions)
# =================================================
def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            expression = display_format.get().strip()

            # allow only safe characters
            allowed = "0123456789+-*/.() "
            if any(ch not in allowed for ch in expression):
                raise ValueError("Invalid characters")

            result = eval(expression, {"__builtins__": None}, {})
            display_format.delete(0, tk.END)
            display_format.insert(tk.END, str(result))

        except Exception:
            display_format.delete(0, tk.END)
            display_format.insert(tk.END, "Error")

    elif text == "Clear":
        display_format.delete(0, tk.END)

    elif text == "⌫":
        current = display_format.get()
        display_format.delete(0, tk.END)
        display_format.insert(tk.END, current[:-1])

    else:
        display_format.insert(tk.END, text)

# =========================
# Display
# =========================
display_format = tk.Entry(
    main_window,
    font=("Consolas", 22, "bold"),
    justify="right",
    fg="#ffffff",              # White text
    bg="#2d3748",              # Dark gray background
    relief="sunken",           # Sunken for realistic display screen
    bd=5,
    insertbackground="#f59e0b"  # Gold cursor - Premium accent
)
display_format.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

# =================================
# Make columns expand equally
# =================================
for col in range(4):
    main_window.grid_columnconfigure(col, weight=1)

# =========================
# Button Style Helper
# =========================
def make_button(text, r, c, colspan=1, sticky="nsew", is_operator=False):
    if is_operator:
        # Operator buttons - Gold/Amber (draws attention to key functions)
        fg_color = "#1a365d"  # Navy text for contrast
        bg_color = "#f59e0b"  # Gold - Premium, important actions
    elif text in ["Clear", "⌫"]:
        # Special function buttons - Red (universal for delete/clear)
        fg_color = "#ffffff"
        bg_color = "#dc2626"  # Red - Warning/action color
    else:
        # Number buttons - Steel Blue (neutral, professional)
        fg_color = "#ffffff"
        bg_color = "#475569"  # Steel blue - Professional, readable
    
    btn = tk.Button(
        main_window,
        text=text,
        font=("Consolas", 18, "bold"),
        fg=fg_color,
        bg=bg_color,
        activebackground="#64748b",
        activeforeground="#ffffff",
        relief="sunken",          # Sunken - Looks like pressed buttons
        bd=4,                     # Border depth for 3D effect
        height=2,
        cursor="hand2"
    )
    btn.grid(row=r, column=c, columnspan=colspan, padx=5, pady=5, sticky=sticky)
    btn.bind("<Button-1>", click)
    return btn

# =========================
# Buttons Layout
# =========================

# Row 1
make_button("7", 1, 0)
make_button("8", 1, 1)
make_button("9", 1, 2)
make_button("/", 1, 3, is_operator=True)

# Row 2
make_button("4", 2, 0)
make_button("5", 2, 1)
make_button("6", 2, 2)
make_button("*", 2, 3, is_operator=True)

# Row 3
make_button("1", 3, 0)
make_button("2", 3, 1)
make_button("3", 3, 2)
make_button("-", 3, 3, is_operator=True)

# Row 4
make_button("0", 4, 0)
make_button(".", 4, 1)
make_button("=", 4, 2, is_operator=True)
make_button("+", 4, 3, is_operator=True)

# Row 5 (extra useful buttons)
make_button("(", 5, 0)
make_button(")", 5, 1)
make_button("⌫", 5, 2)
make_button("Clear", 5, 3)

main_window.mainloop()
