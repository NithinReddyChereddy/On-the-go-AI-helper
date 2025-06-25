from tkinterdnd2 import DND_FILES, DND_TEXT, TkinterDnD
import tkinter as tk
import requests
import threading
import keyboard
import os
from tkinter import filedialog

API_KEY = "AIzaSyANHT6hb02ukh7HbgBzxIG-f_k1wDqyIxM"  # Replace with your API key

# Window settings
is_visible = True
current_alpha = 0.92  # Default transparency

def toggle_visibility():
    global is_visible
    is_visible = not is_visible
    if is_visible:
        root.deiconify()
        root.attributes('-alpha', current_alpha)
        root.lift()
        root.focus_force()
    else:
        root.withdraw()
    print(f"F2 pressed → {'Shown' if is_visible else 'Hidden'}")

def adjust_transparency():
    global current_alpha
    current_alpha = max(0.1, min(1.0, current_alpha + 0.1))
    if current_alpha >= 0.95:
        current_alpha = 0.1
    root.attributes('-alpha', current_alpha)
    print(f"F3 pressed → Transparency: {int(current_alpha*100)}%")

def get_gemini_response(prompt, output_box):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?key={API_KEY}"
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        content = response.json()['candidates'][0]['content']['parts'][0]['text']
        output_box.config(state='normal')
        output_box.insert(tk.END, f"You: {prompt}\n\nAI: {content}\n\n")
        output_box.see(tk.END)
        output_box.config(state='disabled')
    except Exception as e:
        output_box.config(state='normal')
        output_box.insert(tk.END, f"Error: {e}\n")
        output_box.config(state='disabled')

def send_prompt(entry, output_box):
    prompt = entry.get()
    if prompt:
        entry.delete(0, tk.END)
        threading.Thread(target=get_gemini_response, args=(prompt, output_box), daemon=True).start()

def clear_chat(output_box):
    output_box.config(state='normal')
    output_box.delete("1.0", tk.END)
    output_box.config(state='disabled')

def on_enter_key(event, entry, output_box):
    send_prompt(entry, output_box)

def handle_drop(event):
    """Handle dropped text into the entry widget"""
    try:
        # Get the dropped data
        data = event.data
        
        # For Windows, remove curly braces that might be added
        if data.startswith('{') and data.endswith('}'):
            data = data[1:-1]
        
        # Insert the text at cursor position
        entry.insert(tk.INSERT, data)
    except Exception as e:
        print(f"Drop error: {e}")

def browse_files(entry):
    """Open file dialog to select a file"""
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            entry.insert(tk.END, f"File content from {os.path.basename(file_path)}:\n{content}")
        except Exception as e:
            entry.insert(tk.END, f"Couldn't read file: {e}")

# Create root window with enhanced drag and drop support
root = TkinterDnD.Tk()
root.title("Mini AI Helper")

# --- Window Settings ---
root.overrideredirect(True)
root.attributes("-topmost", True)
root.attributes("-alpha", current_alpha)
root.geometry("300x400+100+100")

# Draggable window functionality
def start_move(event):
    root.x = event.x
    root.y = event.y

def stop_move(event):
    root.x = None
    root.y = None

def do_move(event):
    delta_x = event.x - root.x
    delta_y = event.y - root.y
    x = root.winfo_x() + delta_x
    y = root.winfo_y() + delta_y
    root.geometry(f"+{x}+{y}")

root.bind("<ButtonPress-1>", start_move)
root.bind("<ButtonRelease-1>", stop_move)
root.bind("<B1-Motion>", do_move)

# --- UI Elements ---
frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.X)

# Entry widget with enhanced drag and drop support
entry = tk.Entry(frame, font=("Arial", 12))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
entry.bind("<Return>", lambda event: on_enter_key(event, entry, output_box))

# Configure drag and drop for the entry widget (both files and text)
entry.drop_target_register(DND_FILES, DND_TEXT)
entry.dnd_bind('<<Drop>>', handle_drop)

# Right-click context menu for the entry
entry_menu = tk.Menu(root, tearoff=0)
entry_menu.add_command(label="Paste", command=lambda: entry.insert(tk.INSERT, root.clipboard_get()))
entry_menu.add_command(label="Browse File", command=lambda: browse_files(entry))
entry_menu.add_separator()
entry_menu.add_command(label="Clear", command=lambda: entry.delete(0, tk.END))

def show_entry_menu(event):
    try:
        entry_menu.tk_popup(event.x_root, event.y_root)
    finally:
        entry_menu.grab_release()

entry.bind("<Button-3>", show_entry_menu)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

send_button = tk.Button(button_frame, text="Ask", command=lambda: send_prompt(entry, output_box))
send_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear Chat", command=lambda: clear_chat(output_box))
clear_button.pack(side=tk.LEFT, padx=5)

# Output text box
output_box = tk.Text(root, height=15, wrap=tk.WORD, font=("Arial", 10))
output_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
output_box.config(state='disabled')

# --- Hotkeys ---
try:
    keyboard.add_hotkey("F2", toggle_visibility)
    keyboard.add_hotkey("F3", adjust_transparency)
except Exception as e:
    print(f"Hotkey registration failed: {e}")
    print("You may need to run as Administrator for hotkeys to work")

# --- Run the App ---
entry.focus()
root.mainloop()