import tkinter as tk

def create_gui(start_bot, stop_bot):
    root = tk.Tk()
    root.title("BOE KING")

    start_button = tk.Button(root, text="Start", command=start_bot)
    start_button.pack(pady=10)

    stop_button = tk.Button(root, text="Stop", command=stop_bot)
    stop_button.pack(pady=10)

    root.mainloop()
