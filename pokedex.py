from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox

# Create initial window
root = Tk()
root.title("Pokédex")
root.iconbitmap("pokeball.ico")
root.geometry("425x600")


# Stats bar function
def stats_bar(stat):
    global stats_bar_img
    if stat <= 25:
        stat_bar_img = "stats_bar_red.png"
    elif stat in range(25, 51):
        stat_bar_img = "stats_bar_orange.png"
    elif stat in range(51, 76):
        stat_bar_img = "stats_bar_yellow.png"
    elif stat in range(76, 101):
        stat_bar_img = "stats_bar_green.png"
    elif stat in range(101, 126):
        stat_bar_img = "stats_bar_teal.png"
    elif stat >= 126:
        stat_bar_img = "stats_bar_blue.png"
    return stat_bar_img


name_label_stats = ""

# SEARCH BY NUMBER FUNCTION
def search_by_number():
    # Get number
    row_number = number_box.get()
    # Create connection to database
    conn = sqlite3.connect('pokedex.db')
    # Create cursor
    c = conn.cursor()
    # Query Database
    c.execute("SELECT * FROM pokedex WHERE rowid = " + row_number)
    # Assign data to a variable
    stats = c.fetchone()
    # Assign values to variable names
    stats_name = stats[0]
    stats_type = stats[1]
    stats_height = stats[2]
    stats_weight = stats[3]
    stats_hp = stats[4]
    stats_attack = stats[5]
    stats_defense = stats[6]
    stats_spatk = stats[7]
    stats_spdef = stats[8]
    stats_speed = stats[9]
    stats_img = stats[10]

    # Display name
    name_label_stats = Label(root, text=f"{stats_img}  {stats_name}")
    name_label_stats.grid(row=2, column=0, columnspan=3, ipadx=10, pady=(20, 0))

    # Create image box
    image1 = ImageTk.PhotoImage(Image.open(f"img/{stats_img}.jpg").resize((200, 200)))
    image_box = Label(root, image=image1)
    image_box.grid(row=5, column=0, columnspan=3, pady=(10, 0))

    # Display stats
    # TYPE
    stats_type_label = Label(root, text=f"Type: {stats_type}")
    stats_type_label.grid(row=4, column=0, ipadx=10, pady=(10, 0), sticky="w")

    # HEIGHT
    stats_height_label = Label(root, text=f"Height: {stats_height}")
    stats_height_label.grid(row=4, column=1, ipadx=10, pady=(10, 0))

    # HEIGHT
    stats_weight_label = Label(root, text=f"Weight: {stats_weight}")
    stats_weight_label.grid(row=4, column=2, ipadx=10, pady=(10, 0), sticky="w")

    # HP
    stats_hp_label = Label(root, text=f"HP:         {stats_hp}")
    stats_hp_label.grid(row=6, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=6, column=1, pady=(10, 0), sticky="w")
    hp_value = int(stats_hp)
    hp_stat_bar_color = stats_bar(hp_value)
    hp_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{hp_stat_bar_color}").resize((hp_value, 20)))
    hp_stats_bar_pack = Label(root, image=hp_stats_bar)
    hp_stats_bar_pack.grid(row=6, column=1, pady=(10, 0), sticky="w")

    # ATK
    stats_attack_label = Label(root, text=f"ATK:       {stats_attack}")
    stats_attack_label.grid(row=7, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=7, column=1, pady=(10, 0), sticky="w")
    attack_value = int(stats_attack)
    attack_stat_bar_color = stats_bar(attack_value)
    attack_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{attack_stat_bar_color}").resize((attack_value, 20)))
    attack_stats_bar_pack = Label(root, image=attack_stats_bar)
    attack_stats_bar_pack.grid(row=7, column=1, pady=(10, 0), sticky="w")

    # DEF
    stats_defense_label = Label(root, text=f"DEF:       {stats_defense}")
    stats_defense_label.grid(row=8, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=8, column=1, pady=(10, 0), sticky="w")
    defense_value = int(stats_defense)
    defense_stat_bar_color = stats_bar(defense_value)
    defense_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{defense_stat_bar_color}").resize((attack_value, 20)))
    defense_stats_bar_pack = Label(root, image=defense_stats_bar)
    defense_stats_bar_pack.grid(row=8, column=1, pady=(10, 0), sticky="w")

    # SP-ATK
    stats_spatk_label = Label(root, text=f"SP-ATK: {stats_spatk}")
    stats_spatk_label.grid(row=9, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=9, column=1, pady=(10, 0), sticky="w")
    spatk_value = int(stats_spatk)
    spatk_stat_bar_color = stats_bar(spatk_value)
    spatk_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{spatk_stat_bar_color}").resize((spatk_value, 20)))
    spatk_stats_bar_pack = Label(root, image=spatk_stats_bar)
    spatk_stats_bar_pack.grid(row=9, column=1, pady=(10, 0), sticky="w")

    # SP-DEF
    stats_spdef_label = Label(root, text=f"SP-DEF: {stats_spdef}")
    stats_spdef_label.grid(row=10, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=10, column=1, pady=(10, 0), sticky="w")
    spdef_value = int(stats_spdef)
    spdef_stat_bar_color = stats_bar(spdef_value)
    spdef_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{spdef_stat_bar_color}").resize((spdef_value, 20)))
    spdef_stats_bar_pack = Label(root, image=spdef_stats_bar)
    spdef_stats_bar_pack.grid(row=10, column=1, pady=(10, 0), sticky="w")

    # SPEED
    stats_speed_label = Label(root, text=f"SPEED:   {stats_speed}")
    stats_speed_label.grid(row=11, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=11, column=1, pady=(10, 0), sticky="w")
    speed_value = int(stats_speed)
    speed_stat_bar_color = stats_bar(speed_value)
    speed_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{speed_stat_bar_color}").resize((speed_value, 20)))
    speed_stats_bar_pack = Label(root, image=speed_stats_bar)
    speed_stats_bar_pack.grid(row=11, column=1, pady=(10, 0), sticky="w")

    root.mainloop()


# SEARCH BY NAME FUNCTION
def search_by_name():
    # Get number
    name = name_box.get()
    # Create connection to database
    # Create connection to database
    conn = sqlite3.connect('pokedex.db')
    # Create cursor
    c = conn.cursor()
    # Query Database
    c.execute(f"SELECT * FROM pokedex WHERE name = '{name}'")
    # Assign data to a variable
    stats = c.fetchone()
    # Assign values to variable names
    stats_name = stats[0]
    stats_type = stats[1]
    stats_height = stats[2]
    stats_weight = stats[3]
    stats_hp = stats[4]
    stats_attack = stats[5]
    stats_defense = stats[6]
    stats_spatk = stats[7]
    stats_spdef = stats[8]
    stats_speed = stats[9]
    stats_img = stats[10]

    # Display name
    name_label_stats = Label(root, text=f"{stats_img}  {stats_name}")
    name_label_stats.grid(row=2, column=0, columnspan=3, ipadx=10, pady=(20, 0))

    # Create image box
    image1 = ImageTk.PhotoImage(Image.open(f"img/{stats_img}.jpg").resize((200, 200)))
    image_box = Label(root, image=image1)
    image_box.grid(row=5, column=0, columnspan=3, pady=(10, 0))

    # Display stats
    # TYPE
    stats_type_label = Label(root, text=f"Type: {stats_type}")
    stats_type_label.grid(row=4, column=0, ipadx=10, pady=(10, 0), sticky="w")

    # HEIGHT
    stats_height_label = Label(root, text=f"Height: {stats_height}")
    stats_height_label.grid(row=4, column=1, ipadx=10, pady=(10, 0))

    # HEIGHT
    stats_weight_label = Label(root, text=f"Weight: {stats_weight}")
    stats_weight_label.grid(row=4, column=2, ipadx=10, pady=(10, 0), sticky="w")

    # HP
    stats_hp_label = Label(root, text=f"HP:         {stats_hp}")
    stats_hp_label.grid(row=6, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=6, column=1, pady=(10, 0), sticky="w")
    hp_value = int(stats_hp)
    hp_stat_bar_color = stats_bar(hp_value)
    hp_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{hp_stat_bar_color}").resize((hp_value, 20)))
    hp_stats_bar_pack = Label(root, image=hp_stats_bar)
    hp_stats_bar_pack.grid(row=6, column=1, pady=(10, 0), sticky="w")

    # ATK
    stats_attack_label = Label(root, text=f"ATK:       {stats_attack}")
    stats_attack_label.grid(row=7, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=7, column=1, pady=(10, 0), sticky="w")
    attack_value = int(stats_attack)
    attack_stat_bar_color = stats_bar(attack_value)
    attack_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{attack_stat_bar_color}").resize((attack_value, 20)))
    attack_stats_bar_pack = Label(root, image=attack_stats_bar)
    attack_stats_bar_pack.grid(row=7, column=1, pady=(10, 0), sticky="w")

    # DEF
    stats_defense_label = Label(root, text=f"DEF:       {stats_defense}")
    stats_defense_label.grid(row=8, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=8, column=1, pady=(10, 0), sticky="w")
    defense_value = int(stats_defense)
    defense_stat_bar_color = stats_bar(defense_value)
    defense_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{defense_stat_bar_color}").resize((defense_value, 20)))
    defense_stats_bar_pack = Label(root, image=defense_stats_bar)
    defense_stats_bar_pack.grid(row=8, column=1, pady=(10, 0), sticky="w")

    # SP-ATK
    stats_spatk_label = Label(root, text=f"SP-ATK: {stats_spatk}")
    stats_spatk_label.grid(row=9, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=9, column=1, pady=(10, 0), sticky="w")
    spatk_value = int(stats_spatk)
    spatk_stat_bar_color = stats_bar(spatk_value)
    spatk_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{spatk_stat_bar_color}").resize((spatk_value, 20)))
    spatk_stats_bar_pack = Label(root, image=spatk_stats_bar)
    spatk_stats_bar_pack.grid(row=9, column=1, pady=(10, 0), sticky="w")

    # SP-DEF
    stats_spdef_label = Label(root, text=f"SP-DEF: {stats_spdef}")
    stats_spdef_label.grid(row=10, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=10, column=1, pady=(10, 0), sticky="w")
    spdef_value = int(stats_spdef)
    spdef_stat_bar_color = stats_bar(spdef_value)
    spdef_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{spdef_stat_bar_color}").resize((spdef_value, 20)))
    spdef_stats_bar_pack = Label(root, image=spdef_stats_bar)
    spdef_stats_bar_pack.grid(row=10, column=1, pady=(10, 0), sticky="w")

    # SPEED
    stats_speed_label = Label(root, text=f"SPEED:   {stats_speed}")
    stats_speed_label.grid(row=11, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=11, column=1, pady=(10, 0), sticky="w")
    speed_value = int(stats_speed)
    speed_stat_bar_color = stats_bar(speed_value)
    speed_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{speed_stat_bar_color}").resize((speed_value, 20)))
    speed_stats_bar_pack = Label(root, image=speed_stats_bar)
    speed_stats_bar_pack.grid(row=11, column=1, pady=(10, 0), sticky="w")

    root.mainloop()

# Create Entry Boxes
# Create text boxes
number_box = Entry(root, width=30)
number_box.grid(row=0, column=1, pady=(15, 0))

name_box = Entry(root, width=30)
name_box.grid(row=1, column=1, pady=(15, 0))

# Create text box labels
number_label = Label(root, text="Number")
number_label.grid(row=0, column=0, pady=(15, 0))

name_label = Label(root, text="Name")
name_label.grid(row=1, column=0, pady=(15, 0))

# Create buttons
search_number_button = Button(root, text="Search by Number", command=search_by_number)
search_number_button.grid(row=0, column=2, pady=(15, 0))

search_name_button = Button(root, text="Search by Name", padx=8, command=search_by_name)
search_name_button.grid(row=1, column=2, pady=(15, 0))


# Menu Functions
def exit():
    root.quit()

def edit_pokemon():
    # Get Input
    if number_box.get() == "":
        messagebox.showerror(title="Input Error", message="Please enter a Pokemon number in the number box.")
    else:
        row_number = number_box.get()

        # Create Edit Pokemon Window
        edit_pokemon_window = tk.Toplevel()
        edit_pokemon_window.title("Edit Pokemon")
        edit_pokemon_window.iconbitmap("pokeball.ico")
        edit_pokemon_window.geometry("190x370")
        edit_pokemon_window.attributes("-topmost", True)

        # Create connection to database
        conn = sqlite3.connect('pokedex.db')
        # Create cursor
        c = conn.cursor()
        # Query Database
        c.execute("SELECT * FROM pokedex WHERE rowid = " + row_number)
        # Assign data to a variable
        stats = c.fetchone()
        # Assign values to variable names
        stats_name = stats[0]
        stats_type = stats[1]
        stats_height = stats[2]
        stats_weight = stats[3]
        stats_hp = stats[4]
        stats_attack = stats[5]
        stats_defense = stats[6]
        stats_spatk = stats[7]
        stats_spdef = stats[8]
        stats_speed = stats[9]
        stats_img = stats[10]
        edit_number = int(stats_img)

        # Close Connection
        conn.close()

        # Number and Name Label
        pokemon_name_label = Label(edit_pokemon_window, text=f"{stats_img} {stats_name}", font=("Arial", 20))
        pokemon_name_label.grid(row=0, column=0, columnspan=2)

        # Labels and Entry Boxes
        # Type
        type_label = Label(edit_pokemon_window, text="Type: ")
        type_label.grid(row=1, column=0, pady=5, sticky="w")
        type_entry = Entry(edit_pokemon_window, width=15)
        type_entry.grid(row=1, column=1, pady=5, sticky="w")
        type_entry.insert(0, stats_type)
        type_entry.focus_set()

        # Height
        height_label = Label(edit_pokemon_window, text="Height: ")
        height_label.grid(row=2, column=0, pady=5, sticky="w")
        height_entry = Entry(edit_pokemon_window, width=15)
        height_entry.grid(row=2, column=1, pady=5, sticky="w")
        height_entry.insert(0, stats_height)

        # Height
        weight_label = Label(edit_pokemon_window, text="Weight: ")
        weight_label.grid(row=3, column=0, pady=5, sticky="w")
        weight_entry = Entry(edit_pokemon_window, width=15)
        weight_entry.grid(row=3, column=1, pady=5, sticky="w")
        weight_entry.insert(0, stats_weight)

        # Weight
        hp_label = Label(edit_pokemon_window, text="HP: ")
        hp_label.grid(row=4, column=0, pady=5, sticky="w")
        hp_entry = Entry(edit_pokemon_window, width=15)
        hp_entry.grid(row=4, column=1, pady=5, sticky="w")
        hp_entry.insert(0, stats_hp)

        # Attack
        attack_label = Label(edit_pokemon_window, text="Attack: ")
        attack_label.grid(row=5, column=0, pady=5, sticky="w")
        attack_entry = Entry(edit_pokemon_window, width=15)
        attack_entry.grid(row=5, column=1, pady=5, sticky="w")
        attack_entry.insert(0, stats_attack)

        # Defense
        defense_label = Label(edit_pokemon_window, text="Defense: ")
        defense_label.grid(row=6, column=0, pady=5, sticky="w")
        defense_entry = Entry(edit_pokemon_window, width=15)
        defense_entry.grid(row=6, column=1, pady=5, sticky="w")
        defense_entry.insert(0, stats_defense)

        # SP ATK
        spatk_label = Label(edit_pokemon_window, text="SP ATK: ")
        spatk_label.grid(row=7, column=0, pady=5, sticky="w")
        spatk_entry = Entry(edit_pokemon_window, width=15)
        spatk_entry.grid(row=7, column=1, pady=5, sticky="w")
        spatk_entry.insert(0, stats_spatk)

        # SP DEF
        spdef_label = Label(edit_pokemon_window, text="SP DEF: ")
        spdef_label.grid(row=8, column=0, pady=5, sticky="w")
        spdef_entry = Entry(edit_pokemon_window, width=15)
        spdef_entry.grid(row=8, column=1, pady=5, sticky="w")
        spdef_entry.insert(0, stats_spdef)

        # SP DEF
        speed_label = Label(edit_pokemon_window, text="Speed: ")
        speed_label.grid(row=9, column=0, pady=5, sticky="w")
        speed_entry = Entry(edit_pokemon_window, width=15)
        speed_entry.grid(row=9, column=1, pady=5, sticky="w")
        speed_entry.insert(0, stats_speed)


        # Validate and Get Entry Data
        def edit():
            # Validate Entry Boxes
            if type_entry.get() == "":
                messagebox.showerror(title="Input Error", message="Type cannot be blank")
                type_entry.focus_set()
                return
            else:
                edit_type = type_entry.get()

            if height_entry.get() == "":
                messagebox.showerror(title="Input Error", message="Height cannot be blank")
                height_entry.focus_set()
                return
            else:
                edit_height = height_entry.get()

            if weight_entry.get() == "":
                messagebox.showerror(title="Input Error", message="Weight cannot be blank")
                weight_entry.focus_set()
                return
            else:
                edit_weight = weight_entry.get()

            if hp_entry.get() == "":
                messagebox.showerror(title="Input Error", message="HP cannot be blank")
                hp_entry.focus_set()
                return
            else:
                edit_hp = hp_entry.get()

            if attack_entry.get() == "":
                messagebox.showerror(title="Input Error", message="Attack cannot be blank")
                attack_entry.focus_set()
                return
            elif attack_entry.get().isdigit() and len(defense_entry.get()) <= 3 and int(attack_entry.get()) < 200:
                edit_attack = attack_entry.get()
            else:
                messagebox.showerror(title="Input Error", message="Attack must be an 1 - 3 digit integer between 1 and 200")
                attack_entry.focus_set()
                return

            if defense_entry.get() == "":
                messagebox.showerror(title="Input Error", message="Defense cannot be blank")
                defense_entry.focus_set()
                return
            elif defense_entry.get().isdigit() and len(defense_entry.get()) <= 3 and int(defense_entry.get()) < 200:
                edit_defense = defense_entry.get()
            else:
                messagebox.showerror(title="Input Error", message="Attack must be an 1 - 3 digit integer between 1 and 200")
                defense_entry.focus_set()
                return

            if spatk_entry.get() == "":
                messagebox.showerror(title="Input Error", message="SP ATK cannot be blank")
                spatk_entry.focus_set()
                return
            elif spatk_entry.get().isdigit() and len(spatk_entry.get()) <= 3 and int(spatk_entry.get()) < 200:
                edit_spatk = spatk_entry.get()
            else:
                messagebox.showerror(title="Input Error", message="SP ATK must be an 1 - 3 digit integer between 1 and 200")
                spatk_entry.focus_set()
                return

            if spdef_entry.get() == "":
                messagebox.showerror(title="Input Error", message="SP DEF cannot be blank")
                spdef_entry.focus_set()
                return
            elif spdef_entry.get().isdigit() and len(spdef_entry.get()) <= 3 and int(spdef_entry.get()) < 200:
                edit_spdef = spdef_entry.get()
            else:
                messagebox.showerror(title="Input Error", message="SP DEF must be an 1 - 3 digit integer between 1 and 200")
                spdef_entry.focus_set()
                return

            if speed_entry.get() == "":
                messagebox.showerror(title="Input Error", message="Speed cannot be blank")
                speed_entry.focus_set()
                return
            elif speed_entry.get().isdigit() and len(speed_entry.get()) <= 3 and int(speed_entry.get()) < 200:
                edit_speed = speed_entry.get()
            else:
                messagebox.showerror(title="Input Error", message="Speed must be an 1 - 3 digit integer between 1 and 200")
                speed_entry.focus_set()
                return

            # Update Pokedex.db
            # Create connection to database
            conn = sqlite3.connect('pokedex.db')

            # Create cursor
            c = conn.cursor()

            # Update Entry
            c.execute(f"""UPDATE pokedex SET
                name = '{stats_name}',
                type = '{edit_type}',
                height = '{edit_height}',
                weight = '{edit_weight}',
                hp = '{edit_hp}',
                attack = '{edit_attack}',
                defense = '{edit_defense}',
                spatk = '{edit_spatk}',
                spdef = '{edit_spdef}',
                speed = '{edit_speed}',
                img = '{stats_img}'

                WHERE rowid = {edit_number}
                """)

            conn.commit()
            conn.close()


        # Edit Button
        edit_button = Button(edit_pokemon_window, text="Edit", command=edit)
        edit_button.grid(row=10, column=0, columnspan=2, ipadx=30, ipady=10)

def add_pokemon():
    # Create Add Pokemon Window
    add_pokemon_window = tk.Toplevel()
    add_pokemon_window.title("Add Pokemon")
    add_pokemon_window.iconbitmap("pokeball.ico")
    add_pokemon_window.geometry("170x400")
    add_pokemon_window.attributes("-topmost", True)

    # Get Pokemon Number
    # Create connection to database
    conn = sqlite3.connect('pokedex.db')

    # Create cursor
    c = conn.cursor()

    # Get Last Row ID
    c.execute("SELECT rowid from pokedex")

    # Get Last Row ID
    last_rowid = c.fetchall()

    conn.close()

    last_row_id_str = str(last_rowid[-1])

    # Define Current Row ID
    current_row_id = int(last_row_id_str[1:4]) + 1

    current_row_id_str = str(current_row_id)


    # Labels and Entry Boxes
    # Number Label
    number_label = Label(add_pokemon_window, text="Number: ")
    number_label.grid(row=0, column=0, pady=5)
    pokedex_number_label = Label(add_pokemon_window, text=f"{current_row_id_str}")
    pokedex_number_label.grid(row=0, column=1, pady=5, sticky="w")


    # Name
    name_label = Label(add_pokemon_window, text="Name: ")
    name_label.grid(row=1, column=0, pady=5, sticky="w")
    name_entry = Entry(add_pokemon_window, width=15)
    name_entry.grid(row=1, column=1, pady=5, sticky="w")

    # Type
    type_label = Label(add_pokemon_window, text="Type: ")
    type_label.grid(row=2, column=0, pady=5, sticky="w")
    type_entry = Entry(add_pokemon_window, width=15)
    type_entry.grid(row=2, column=1, pady=5, sticky="w")

    # Height
    height_label = Label(add_pokemon_window, text="Height: ")
    height_label.grid(row=3, column=0, pady=5, sticky="w")
    height_entry = Entry(add_pokemon_window, width=15)
    height_entry.grid(row=3, column=1, pady=5, sticky="w")

    # Height
    weight_label = Label(add_pokemon_window, text="Weight: ")
    weight_label.grid(row=4, column=0, pady=5, sticky="w")
    weight_entry = Entry(add_pokemon_window, width=15)
    weight_entry.grid(row=4, column=1, pady=5, sticky="w")

    # Weight
    hp_label = Label(add_pokemon_window, text="HP: ")
    hp_label.grid(row=5, column=0, pady=5, sticky="w")
    hp_entry = Entry(add_pokemon_window, width=15)
    hp_entry.grid(row=5, column=1, pady=5, sticky="w")

    # Attack
    attack_label = Label(add_pokemon_window, text="Attack: ")
    attack_label.grid(row=6, column=0, pady=5, sticky="w")
    attack_entry = Entry(add_pokemon_window, width=15)
    attack_entry.grid(row=6, column=1, pady=5, sticky="w")

    # Defense
    defense_label = Label(add_pokemon_window, text="Defense: ")
    defense_label.grid(row=7, column=0, pady=5, sticky="w")
    defense_entry = Entry(add_pokemon_window, width=15)
    defense_entry.grid(row=7, column=1, pady=5, sticky="w")

    # SP ATK
    spatk_label = Label(add_pokemon_window, text="SP ATK: ")
    spatk_label.grid(row=8, column=0, pady=5, sticky="w")
    spatk_entry = Entry(add_pokemon_window, width=15)
    spatk_entry.grid(row=8, column=1, pady=5, sticky="w")

    # SP DEF
    spdef_label = Label(add_pokemon_window, text="SP DEF: ")
    spdef_label.grid(row=9, column=0, pady=5, sticky="w")
    spdef_entry = Entry(add_pokemon_window, width=15)
    spdef_entry.grid(row=9, column=1, pady=5, sticky="w")

    # SP DEF
    speed_label = Label(add_pokemon_window, text="Speed: ")
    speed_label.grid(row=10, column=0, pady=5, sticky="w")
    speed_entry = Entry(add_pokemon_window, width=15)
    speed_entry.grid(row=10, column=1, pady=5, sticky="w")


    # Validate and Get Entry Data
    def add():
        # Validate Entry Boxes
        if name_entry.get() == "":
            messagebox.showerror(title="Input Error", message="Name cannot be blank")
            name_entry.focus_set()
            return
        else:
            name_add = name_entry.get()

        if type_entry.get() == "":
            messagebox.showerror(title="Input Error", message="Type cannot be blank")
            type_entry.focus_set()
            return
        else:
            type_add = type_entry.get()

        if height_entry.get() == "":
            messagebox.showerror(title="Input Error", message="Height cannot be blank")
            height_entry.focus_set()
            return
        else:
            height_add = height_entry.get()

        if weight_entry.get() == "":
            messagebox.showerror(title="Input Error", message="Weight cannot be blank")
            weight_entry.focus_set()
            return
        else:
            weight_add = weight_entry.get()

        if hp_entry.get() == "":
            messagebox.showerror(title="Input Error", message="HP cannot be blank")
            hp_entry.focus_set()
            return
        else:
            hp_add = hp_entry.get()

        if attack_entry.get() == "":
            messagebox.showerror(title="Input Error", message="Attack cannot be blank")
            attack_entry.focus_set()
            return
        elif attack_entry.get().isdigit() and len(defense_entry.get()) <= 3 and int(attack_entry.get()) < 200:
            attack_add = attack_entry.get()
        else:
            messagebox.showerror(title="Input Error", message="Attack must be an 1 - 3 digit integer between 1 and 200")
            attack_entry.focus_set()
            return

        if defense_entry.get() == "":
            messagebox.showerror(title="Input Error", message="Defense cannot be blank")
            defense_entry.focus_set()
            return
        elif defense_entry.get().isdigit() and len(defense_entry.get()) <= 3 and int(defense_entry.get()) < 200:
            defense_add = defense_entry.get()
        else:
            messagebox.showerror(title="Input Error", message="Attack must be an 1 - 3 digit integer between 1 and 200")
            defense_entry.focus_set()
            return

        if spatk_entry.get() == "":
            messagebox.showerror(title="Input Error", message="SP ATK cannot be blank")
            spatk_entry.focus_set()
            return
        elif spatk_entry.get().isdigit() and len(spatk_entry.get()) <= 3 and int(spatk_entry.get()) < 200:
            spatk_add = spatk_entry.get()
        else:
            messagebox.showerror(title="Input Error", message="SP ATK must be an 1 - 3 digit integer between 1 and 200")
            spatk_entry.focus_set()
            return

        if spdef_entry.get() == "":
            messagebox.showerror(title="Input Error", message="SP DEF cannot be blank")
            spdef_entry.focus_set()
            return
        elif spdef_entry.get().isdigit() and len(spdef_entry.get()) <= 3 and int(spdef_entry.get()) < 200:
            spdef_add = spdef_entry.get()
        else:
            messagebox.showerror(title="Input Error", message="SP DEF must be an 1 - 3 digit integer between 1 and 200")
            spdef_entry.focus_set()
            return

        if speed_entry.get() == "":
            messagebox.showerror(title="Input Error", message="Speed cannot be blank")
            speed_entry.focus_set()
            return
        elif speed_entry.get().isdigit() and len(speed_entry.get()) <= 3 and int(speed_entry.get()) < 200:
            speed_add = speed_entry.get()
        else:
            messagebox.showerror(title="Input Error", message="Speed must be an 1 - 3 digit integer between 1 and 200")
            speed_entry.focus_set()
            return


        # Update Current Row ID
        # Create connection to database
        conn = sqlite3.connect('pokedex.db')

        # Create cursor
        c = conn.cursor()

        # Get Last Row ID
        c.execute("SELECT rowid from pokedex")

        # Get Last Row ID
        last_rowid = c.fetchall()

        c.close()

        last_row_id_str = str(last_rowid[-1])

        # Define Current Row ID
        current_row_id = int(last_row_id_str[1:4]) + 1

        current_row_id_str = str(current_row_id)

        # Assign Img Number
        img_number = current_row_id

        # Insert Values into Pokedex.db
        # Create connection to database
        conn = sqlite3.connect('pokedex.db')

        # Create cursor
        c = conn.cursor()

        # Insert Values
        c.execute(f"""INSERT INTO pokedex VALUES (
            '{name_add}',
            '{type_add}',
            '{height_add}',
            '{weight_add}',
            '{hp_add}',
            '{attack_add}',
            '{defense_add}',
            '{spatk_add}',
            '{spdef_add}',
            '{speed_add}',
            '{img_number}'
            )""")

        # Commit and Close
        conn.commit()
        conn.close()

        # Reset Window
        add_pokemon_window.destroy()

        add_pokemon()


        # Add Record to Pokedex.db


    # Add Button
    add_button = Button(add_pokemon_window, text="Add Pokemon", command=add)
    add_button.grid(row=11, column=0, columnspan=2, padx=(10, 0), ipadx=20, ipady=10)



# ROOT MENU
root_menu = Menu(root, tearoff=False)
root.config(menu=root_menu)

file_menu = Menu(root_menu, tearoff=False)
root_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Add Pokemon", command=add_pokemon)
file_menu.add_command(label="Edit Pokemon", command=edit_pokemon)
file_menu.add_command(label="Exit", command=exit)



# Run startscreen mainloop
root.mainloop()
