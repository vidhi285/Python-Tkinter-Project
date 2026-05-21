from tkinter import Tk, Button, Label, filedialog
from pygame import mixer pygame

pygame.mixer.init()

current_song = None

def exit_window():
    mixer.stop()
    w.destroy()
    
def play_music():
    global current_song
    current_song = "your_song.mp3"  # Placeholder for current song
    mixer.music.load(current_song)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def resume_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

def browse_music():
    global current_song
    current_song = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    if current_song:
        mixer.music.load(current_song)

w = Tk()
w.title('Music Player')
w.geometry('500x300')
w.iconbitmap('icon.ico')

L1 = Label(w, text='Music Player', font=('cambria', 20))
L1.pack(pady=10)

B1 = Button(w, text='Play', height=2, width=15, font=('cambria', 20), command=play_music)
B1.pack(pady=10)

B2 = Button(w, text='Pause', height=2, width=15, font=('cambria', 20), command=pause_music)
B2.pack(pady=10)

B3 = Button(w, text='Resume', height=2, width=15, font=('cambria', 20), command=resume_music)
B3.pack(pady=10)

B4 = Button(w, text='Stop', height=2, width=15, font=('cambria', 20), command=stop_music)
B4.pack(pady=10)

B5 = Button(w, text='Browse', height=2, width=15, font=('cambria', 20), command=browse_music)
B5.pack(pady=10)

B6 = Button(w, text='Exit', height=2, width=15, font=('cambria', 20), command=exit_window)
B6.pack(pady=10)

w.mainloop()
