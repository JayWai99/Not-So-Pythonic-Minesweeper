import customtkinter as ctk

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

app = ctk.CTk()
app.geometry('1280x720')

# four frames needed for the entire operation of the game
start_frame = ctk.CTkFrame(app)
difficulty_frame = ctk.CTkFrame(app)
stats_frame = ctk.CTkFrame(app)
game_frame = ctk.CTkFrame(app)

# always initialise with the start frame first, can be abstracted into a function
start_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor='center')

# grid configuration for all the frames to ensure everything fits as intended
start_frame.grid_columnconfigure(0, weight=1)
difficulty_frame.grid_columnconfigure(0, weight=1)
stats_frame.grid_columnconfigure(0, weight=1)
game_frame.grid_columnconfigure(0, weight=1)

# functions for switching between frames, there is a method called tkraise, potentially better
def start_to_difficulty():
    print('load game frame')
    start_frame.place_forget()
    difficulty_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor='center')

def start_easy():
    print('load easy mode')


def start_normal():
    print('load normal mode')


def start_hard():
    print('load hard mode')


def start_hell():
    print('load hell mode')


def start_steven_he():
    print('load steven he mode')


def back_to_start():
    difficulty_frame.place_forget()
    start_frame.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor='center')

def player_stats():
    print('load stats frame')

# widgets for start frame
label = ctk.CTkLabel(start_frame, text="A Not So Pythonic Minesweeper", font=('Arial Bold', 50))
label.grid(column=0, row=0, padx=200, pady=150, sticky='ew')

start_button = ctk.CTkButton(start_frame, text='Start Game', command=start_to_difficulty, font=('Arial', 30), hover_color='purple')
stats_button = ctk.CTkButton(start_frame, text='Player Statistics', command=player_stats, font=('Arial', 30), hover_color='purple')
quit_button = ctk.CTkButton(start_frame, text='Quit', command=app.destroy, font=('Arial', 30), hover_color='purple')

start_button.grid(column=0, row=1, padx=200, pady=100, sticky='ew')
stats_button.grid(column=0, row=2, padx=200, pady=10, sticky='ew')
quit_button.grid(column=0, row=3, padx=200, pady=10, sticky='ew')

# widgets for difficulty frame
label = ctk.CTkLabel(difficulty_frame, text="A Not So Pythonic Minesweeper", font=('Arial Bold', 50))
label.grid(column=0, row=0, padx=200, pady=150, sticky='ew')

easy_button = ctk.CTkButton(difficulty_frame, text='Easy mode', command=start_easy, font=('Arial', 30), hover_color= 'purple')
normal_button = ctk.CTkButton(difficulty_frame, text='Normal mode', command=start_normal, font=('Arial', 30), hover_color= 'purple')
hard_button = ctk.CTkButton(difficulty_frame, text='Hard mode', command=start_hard, font=('Arial', 30), hover_color= 'purple')
hell_button = ctk.CTkButton(difficulty_frame, text='Hell mode', command=start_hell, font=('Arial', 30), hover_color= 'purple')
steven_he_button = ctk.CTkButton(difficulty_frame, text='Steven He mode', command=start_steven_he, font=('Arial', 30), hover_color= 'purple')
back_to_start_button = ctk.CTkButton(difficulty_frame, text='Back', command=back_to_start, font=('Arial', 30), hover_color='purple')

easy_button.grid(column=0, row=1 , padx=200, pady=10, sticky='ew')
normal_button.grid(column=0, row=2 , padx=200, pady=10, sticky='ew')
hard_button.grid(column=0, row=3 , padx=200, pady=10, sticky='ew')
hell_button.grid(column=0, row=4 , padx=200, pady=10, sticky='ew')
steven_he_button.grid(column=0, row=5 , padx=200, pady=10, sticky='ew')
back_to_start_button.grid(column=0, row=6 , padx=200, pady=10, sticky='ew')

# widgets for stats frame


# widgets for game frame

app.mainloop()