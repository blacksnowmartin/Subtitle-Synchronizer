import tkinter as tk
from tkinter import filedialog, messagebox
import moviepy.editor as mp
import pysrt

def synchronize_subtitles(video_path, subtitle_path, output_subtitle_path, delay_seconds):
    # Load video
    video = mp.VideoFileClip(video_path)
    
    # Load subtitles
    subs = pysrt.open(subtitle_path)
    
    # Adjust subtitles timing
    for sub in subs:
        sub.start.shift(seconds=delay_seconds)
        sub.end.shift(seconds=delay_seconds)
    
    # Save synchronized subtitles
    subs.save(output_subtitle_path, encoding='utf-8')

def open_file_dialog(file_type):
    if file_type == "video":
        return filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.mkv;*.avi")])
    elif file_type == "subtitle":
        return filedialog.askopenfilename(filetypes=[("Subtitle Files", "*.srt")])

def synchronize():
    video_path = entry_video.get()
    subtitle_path = entry_subtitle.get()
    delay_seconds = float(entry_delay.get())
    
    if not video_path or not subtitle_path:
        messagebox.showwarning("Input Error", "Please select both video and subtitle files.")
        return
    
    output_subtitle_path = filedialog.asksaveasfilename(defaultextension=".srt", filetypes=[("Subtitle Files", "*.srt")])
    
    try:
        synchronize_subtitles(video_path, subtitle_path, output_subtitle_path, delay_seconds)
        messagebox.showinfo("Success", f"Subtitles synchronized and saved to {output_subtitle_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create main window
root = tk.Tk()
root.title("Subtitle Synchronizer")

# Video file selection
lbl_video = tk.Label(root, text="Video File:")
lbl_video.grid(row=0, column=0, padx=10, pady=10)

entry_video = tk.Entry(root, width=50)
entry_video.grid(row=0, column=1, padx=10, pady=10)

btn_video = tk.Button(root, text="Browse", command=lambda: entry_video.insert(0, open_file_dialog("video")))
btn_video.grid(row=0, column=2, padx=10, pady=10)

# Subtitle file selection
lbl_subtitle = tk.Label(root, text="Subtitle File:")
lbl_subtitle.grid(row=1, column=0, padx=10, pady=10)

entry_subtitle = tk.Entry(root, width=50)
entry_subtitle.grid(row=1, column=1, padx=10, pady=10)

btn_subtitle = tk.Button(root, text="Browse", command=lambda: entry_subtitle.insert(0, open_file_dialog("subtitle")))
btn_subtitle.grid(row=1, column=2, padx=10, pady=10)

# Delay input
lbl_delay = tk.Label(root, text="Delay (seconds):")
lbl_delay.grid(row=2, column=0, padx=10, pady=10)

entry_delay = tk.Entry(root, width=10)
entry_delay.grid(row=2, column=1, padx=10, pady=10)

# Synchronize button
btn_sync = tk.Button(root, text="Synchronize", command=synchronize)
btn_sync.grid(row=3, column=0, columnspan=3, pady=20)

# Start the GUI event loop
root.mainloop()
