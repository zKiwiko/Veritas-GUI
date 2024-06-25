
from customtkinter import *
import customtkinter as tk
from bin.config import Operators
from PIL import Image
import json
import os
import datetime
import importlib.util
import sys
import shutil

version_num = "1.01 | 9.1.0"
img_veritas = CTkImage(Image.open("bin/veritas.png"), size=(200, 200))
ico_veritas = CTkImage(Image.open("bin/veritas.ico"), size=(20,20))
changeLog = f"re:Veritas GUI {version_num}.\n\nThis Version includes:\n Anti Recoil : For all Operators\n Configuring All Mods, as well as presetting them\n Presetting Layouts\n Presetting Profiles\n Easy Config Sharing, Importing, and Resetting\n\nPlanned Features:\n Layout Customization\n Operator Icons\n Weapon Icons\n\n\n\n\nYou can support my work here:\n CashApp - $zKiwiko\n Github - https://github.com/zKiwiko "

# Veritas Stuff
attackers = "bin/scripts/Attackers.gpc"
defenders = "bin/scripts/Defenders.gpc"
output_a = "Attackers.gpc"
output_b = "Defenders.gpc"

veritas_blue = "#0a7cbf"
r6_Operators = list(Operators.keys())
r6_weapons = []
for op in Operators.values():
    r6_weapons.extend(op["weapons"])
weapon_dict = {}
weapon_values = ""

successful_login = False
username = ""
password = ""

script_mods = {
    "CROUCH_SPAM": (60, 0),
    "STRAFE": (200, 0),
    "SHAIKO_LEAN": (120, 0),
    "LEAN_SPAM": (95, 0),
    "PRONE_SHOT": (250, 0),
    "TEA_BAG_LOL": (10, 1),
    "RAPID_FIRE": (20, 1),
    "DEAD_ZONE": (12, 0),
    "ON_CAMS": (0, 0),
    "RAPID_FIRE_FOR_ALL": (0, 0),
    "AUTO_LEAN": (0, 0),
    "HIP_LEAN": (0, 0),
    "PIN_ON_SHOT": (0, 0),
    "AUTO_SCAN": (0, 1),
    "INVERTED": (0, 0),
    "ABILITIES": (0, 1),
    "SKELETON_KEY_RF": (0, 0)
}

script_layouts = ["Default", "Lefty", "SouthPaw", "SouthPaw Lefty", "Bumper Swap", "Enhanced Bumper Leaner", "LB L1", "RB R1", "RT R2"]
script_profiles = ["Controller", "Zen MNK", "Xim"]

current_layout = 0
current_profile = 0

attacker_operators = [
    "Sledge", "Thatcher", "Ash", "Thermite", "Twitch", "Montagne", "Glaz", "Fuze", "Blitz", "IQ",
    "Buck", "Blackbeard", "Capitao", "Hibana", "Jackal", "Ying", "Zofia", "Dokkaebi", "Lion",
    "Finka", "Maverick", "Nomad", "Gridlock", "Nokk", "Amaru", "Kali", "Iana", "Ace", "Zero",
    "Flores", "Osa", "Sens", "Grim", "Brava", "Ram", "Deimos", "Striker"
]

defender_operators = [
    "Smoke", "Mute", "Castle", "Pulse", "Doc", "Rook", "Kapkan", "Tachanka", "Jager", "Bandit",
    "Frost", "Valkyrie", "Caveira", "Echo", "Mira", "Lesion", "Ela", "Vigil", "Maestro", "Alibi",
    "Clash", "Kaid", "Mozzie", "Warden", "Goyo", "Wamai", "Oryx", "Melusi", "Aruni", "Thunderbird",
    "Thorn", "Azami", "Solis", "Fenrir", "Tubarao", "Sentry"
]

# End

root = tk.CTk()

root.title(f"Veritas GUI {version_num}")
root.geometry("640x480")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.resizable(False, False)
tk.set_default_color_theme("dark-blue")
tk.set_appearance_mode("dark")
black = "black"

frame = CTkFrame(root)
frame.pack(fill="both", expand=True)

def clear_frame():
    if frame.winfo_children():
        for widget in frame.winfo_children():
            widget.destroy()

def validate_login(event=None):
    global successful_login
    successful_login = True
    if successful_login:
        main_page()

def Login_View():
    global etr_password, etr_username

    clear_frame()

    box_ChangeLog = CTkTextbox(frame, width = 620, height=320)
    box_ChangeLog.insert("0.0", changeLog)
    box_ChangeLog.configure(state="disabled")
    box_ChangeLog.pack(pady=10)

    btn_continue = CTkButton(frame,
                              text="Continue",
                              fg_color="transparent",
                              border_color="white",
                              border_width=2,
                              corner_radius=12,
                              width=120,
                              command=main_page
                              )
    btn_continue.pack(anchor="s")

    label_credits = CTkLabel(frame, 
                             text="Created by @Kiwiko - © 2024",
                             text_color="black"
                             )
    
    label_credits.pack(side="bottom")
def update_AR_values():
    global Operators, selected_operator, selected_weapon
    
    selected_operator = drop_Operators.get() 
    selected_weapon = drop_Weapons.get()
    vertical_value = sldr_vertical.get()
    horizontal_value = sldr_horizontal.get()  
    percentadj_value = sldr_percentAdjustment.get()
    
    if selected_operator not in Operators:
        Operators[selected_operator] = {"weapons": [], "values": {}}

    if selected_weapon not in Operators[selected_operator]["weapons"]:
        Operators[selected_operator]["weapons"].append(selected_weapon)
    
    Operators[selected_operator]["values"][selected_weapon] = {
        'vertical': round(vertical_value),
        'horizontal': round(horizontal_value),

    }
def update_sliders(event=None):
    selected_operator = drop_Operators.get()
    selected_weapon = drop_Weapons.get()

    if selected_operator and selected_weapon:
        adjustments = Operators[selected_operator]["values"].get(selected_weapon, {})
        vertical = adjustments.get("vertical", 0)
        horizontal = adjustments.get("horizontal", 0)
        percent = sldr_percentAdjustment.get()

        sldr_vertical.set(vertical)
        sldr_horizontal.set(horizontal)

        update_vertical_label(vertical)
        update_horizontal_label(horizontal)
        update_percentadj_label(percent)
    else:
        
        sldr_vertical.set(0)
        sldr_horizontal.set(0)
        sldr_percentAdjustment.set(0)

        update_vertical_label(0)
        update_horizontal_label(0)
        update_percentadj_label(0)

def update_vertical_label(value):
    vertical_value = value
    lbl_vertical_value.configure(text=round(vertical_value))
    update_AR_values()

def update_horizontal_label(value):
    horizontal_value = value
    lbl_horizontal_value.configure(text=round(horizontal_value))
    update_AR_values()

def update_percentadj_label(value):
    percentAdjustment = value
    lbl_percentadj_value.configure(text=round(percentAdjustment))
    update_AR_values()

def update_deadzone_label(value):
    deadzone = value
    lbl_deadzone_value.configure(text=round(deadzone))


def update_weapon_box(event=None):
    global selected_operator, weapon_values

    selected_operator = drop_Operators.get()

    weapon_values = [weapon for weapon in Operators[selected_operator]["weapons"] if weapon != "None"]

    drop_Weapons.configure(values=weapon_values) 

    current_weapon = drop_Weapons.get()
    if current_weapon not in weapon_values:
        if weapon_values:
            drop_Weapons.set(weapon_values[0])
        else:
            drop_Weapons.set('')  

    update_sliders()
def increment_entry(var, op, incre, min, max):
    if op == "+" and min is not None and max is not None:
        temp = var.get()
        if int(temp) > max:
            var.delete(0, "end")
            var.insert(0, max)
            return True
        elif int(temp) < min:
            var.delete(0, "end")
            var.insert(0, min)
            return True
        elif int(temp) < max:
            var.delete(0, "end")
            var.insert(0, int(temp) + incre)
    if op == '-' and min is not None and max is not None:
        temp = var.get()
        if int(temp) > max:
            var.delete(0, "end")
            var.insert(0, max)
            return True
        elif int(temp) < min:
            var.delete(0, "end")
            var.insert(0, min)
            return True
        elif int(temp) > min:
            var.delete(0, "end")
            var.insert(0, int(temp) - incre)
def increment_label(var, op, incre, min, max):
    if op == '+' and min is not None and max is not None:
        temp = var.get()
        if int(temp) > max:
            var.set(max)
            return True
        elif int(temp) < min:
            var.set(min)
            return True
        elif int(temp) < max:
            var.set(int(temp) + incre)

def layout_description(value):
    if value == "Default":
        current_layout = 1
    elif value == "Lefty":
        current_layout = 2
    elif value == "SouthPaw":
        current_layout = 3
    elif value == "SouthPaw Lefty":
        current_layout = 4
    elif value == "Bumper Swap":
        current_layout = 5
    elif value == "Enhanced Bumper Leaner":
        current_layout = 6
    elif value == "LB L1":
        current_layout = 7
    elif value == "RB R1": 
        current_layout = 8
    elif value == "RT R2":
        current_layout = 9
    else:
        current_layout = None
    return current_layout

def profile_description(value):
    if value == "Controller":
        profile = "PROFILE_CONTROLLER"
    elif value == "Zen MNK":
        profile = "PROFILE_MNK"
    elif value == "Xim":
        profile = "PROFILE_XIM"
    else:
        profile = None
    return profile

def write_defenders(filename, operators):
    
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    
    def get_replacement_values(operator):
        start_index = None
        end_index = None
        for i, line in enumerate(lines):
            if "const int8  GunAntiRecoil[][]  = {" in line:
                start_index = i
            if start_index is not None and "};" in line:
                end_index = i
                break

        new_values = []
        for weapon in Operators[operator]["weapons"]:
            values = Operators[operator]["values"][weapon]  
            vertical = values["vertical"]
            horizontal = values["horizontal"]
            percent = round(sldr_percentAdjustment.get())
            new_values.append(f"{vertical},{horizontal},{percent}")

        while len(new_values) < 6:  
            new_values.append("0,0,80")

        new_values_str = ",".join(new_values[:6])  
        return f'{{{new_values_str}}}'

    del lines[101:121]

    
    const_int8_lines = ["const int8 GunAntiRecoil[][] = {"]
    for i, operator in enumerate(operators):
        comma = "," if i < len(operators) - 1 else ""  
        const_int8_lines.append(f"\t{get_replacement_values(operator)}{comma}\t/* {operator.upper()} */")
    const_int8_lines.append("};")
    lines.insert(102, "\n".join(const_int8_lines) + "\n")

    
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines)
def write_attackers(filename, operators): 
    
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    
    def get_replacement_values(operator):
        start_index = None
        end_index = None
        for i, line in enumerate(lines):
            if "const int8  GunAntiRecoil[][]  = {" in line:
                start_index = i
            if start_index is not None and "};" in line:
                end_index = i
                break

        new_values = []
        for weapon in Operators[operator]["weapons"]:
            values = Operators[operator]["values"][weapon]  
            vertical = values["vertical"]
            horizontal = values["horizontal"]
            percent = round(sldr_percentAdjustment.get())
            new_values.append(f"{vertical},{horizontal},{percent}")

        while len(new_values) < 6:  
            new_values.append("0,0,80")

        new_values_str = ",".join(new_values[:6]) 
        return f'{{{new_values_str}}}'

    del lines[103:123]
    const_int8_lines = ["const int8 GunAntiRecoil[][] = {"]
    for i, operator in enumerate(operators):
        comma = "," if i < len(operators) - 1 else ""  
        const_int8_lines.append(f"\t{get_replacement_values(operator)}{comma}\t/* {operator.upper()} */")
    lines.insert(103, "\n".join(const_int8_lines) + "\n")
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines)

def write_quicktoggles_attack(file_path, script_mods):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if "const int16 quickToggleMinMaxDef[][]= {" in line:
            start_index = i
        if start_index is not None and "};" in line:
            end_index = i
            break

    if start_index is None or end_index is None:
        raise ValueError("Array definition not found in the file")
        
    new_array_content = "const int16 quickToggleMinMaxDef[][]= {\n"

    for i, line in enumerate(lines[start_index + 1:end_index]):
        parts = line.split(',')
        if len(parts) >= 4:
            min_val = parts[0].strip()
            max_val = parts[1].strip()
            def_val = parts[2].strip()
            def_status = parts[3].strip().split(',')[0]  # Remove any additional content after the fourth value
            key = line.split('//')[1].strip().replace(",", "").replace(" ", "_").upper()
            if key != "SKELETON_KEY_RF":
                mod_values = script_mods[key]
                new_line = f"{min_val},{max_val},{mod_values[0]},{mod_values[1]}}}, //{key}\n"
            else:
                new_line = f"{min_val},{max_val},{mod_values[0]},{mod_values[1]}}} // SKELETON_KEY_RF\n"
        else:
            new_line = line.strip() + "\n"
        new_array_content += new_line
        
    new_array_content = new_array_content.rstrip(',\n') + "\n};\n"

    new_lines = lines[:start_index] + [new_array_content] + lines[end_index + 1:]

    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(new_lines)
def write_quicktoggles_defense(file_path, script_mods):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if "const int16 quickToggleMinMaxDef[][]= {" in line:
            start_index = i
        if start_index is not None and "};" in line:
            end_index = i
            break

    if start_index is None or end_index is None:
        raise ValueError("Array definition not found in the file")
        
    new_array_content = "const int16 quickToggleMinMaxDef[][]= {\n"

    for i, line in enumerate(lines[start_index + 1:end_index]):
        parts = line.split(',')
        if len(parts) >= 4:
            min_val = parts[0].strip()
            max_val = parts[1].strip()
            def_val = parts[2].strip()
            def_status = parts[3].strip().split(',')[0]  # Remove any additional content after the fourth value
            key = line.split('//')[1].strip().replace(",", "").replace(" ", "_").upper()
            if key != "ABILITIES":
                mod_values = script_mods[key]
                new_line = f"{min_val},{max_val},{mod_values[0]},{mod_values[1]}}}, //{key}\n"
            else:
                new_line = f"{min_val},{max_val},{mod_values[0]},{mod_values[1]}}} // ABILITIES\n"
        else:
            new_line = line.strip() + "\n"
        new_array_content += new_line
        
    new_array_content = new_array_content.rstrip(',\n') + "\n};\n"

    new_lines = lines[:start_index] + [new_array_content] + lines[end_index + 1:]

    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(new_lines)
def write_layout(filename):
    # Read the contents of the source file with UTF-8 encoding
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    layout_val = layout_description(drop_Layouts.get())
    profile_val = profile_description(drop_Profiles.get())

    modified_lines = []
    found_string = False

    # Process each line
    for line in lines:
        if "int gameLayout 	= 0;" in line:
            modified_lines.append(f"int gameLayout = {layout_val};\n")
            found_string = True
        else:
            modified_lines.append(line)

    # Write the updated content back to the source file
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(modified_lines)

def write_profile(filename):
    # Read the contents of the source file with UTF-8 encoding
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    layout_val = layout_description(drop_Layouts.get())
    profile_val = profile_description(drop_Profiles.get())

    modified_lines = []
    found_string = False

    # Process each line
    for line in lines:
        if "int profile		= 0;" in line:
            modified_lines.append(f"int profile = {profile_val};\n")
            found_string = True
        else:
            modified_lines.append(line)

    # Write the updated content back to the source file
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(modified_lines)
def copy_from_bin():
    if os.path.exists(attackers):
        shutil.copy(attackers, output_a)
    else:
        print("Error: A001")

    if os.path.exists(defenders):
        shutil.copy(defenders, output_b)
    else:
        print("Error: A002")

def Script_Generation():
    copy_from_bin()
    if os.path.exists(defenders) and os.path.exists(attackers):
        write_defenders(output_b, defender_operators)
        write_attackers(output_a, attacker_operators)
        write_quicktoggles_attack(output_a, script_mods)
        write_quicktoggles_defense(output_b, script_mods)
        write_layout(output_a)
        write_profile(output_a)
        write_layout(output_b)
        write_profile(output_b)
        print(f"Attackers and Defenders Generated Successfully. You can find them in the same folder this app is.")
    else:
        print("Error: A001x2")

def create_config():
    with open("exported_config.py", "w") as file:
        file.write("Operators = ")
        json.dump(Operators, file, indent = 4)

def import_config():
    spec = importlib.util.spec_from_file_location("exported_config", "exported_config.py")
    exported_config = importlib.util.module_from_spec(spec)
    sys.modules["exported_config"] = exported_config
    spec.loader.exec_module(exported_config)
    
    op_import = exported_config.Operators
    original = Operators

    def deep_update(original, updates):
        for key, value in updates.items():
            if isinstance(value, dict):
                original[key] = deep_update(original.get(key, {}), value)
            else:
                original[key] = value
        return original
    deep_update(original, op_import)
    update_sliders()
def reset_config(d):
    if isinstance(d, dict):
        for key, value in d.items():
            if isinstance(value, dict):
                reset_config(value)
            elif isinstance(value, list):
                for i in range(len(value)):
                    value[i] = 0
            else:
                d[key] = 0
    elif isinstance(d, list):
        for i in range(len(d)):
            d[i] = 0
    update_sliders()
    
def check_toggles():
    if check_OnCams.get() == 1:
        script_mods['ON_CAMS'] = (0, 1)
    else:
        script_mods['ON_CAMS'] = (0, 0)
    if check_RF4ALL.get() == 1:
        script_mods['RAPID_FIRE_FOR_ALL'] = (0, 1)
    else:
        script_mods['RAPID_FIRE_FOR_ALL'] = (0, 0)
    if check_AutoLean.get() == 1:
        script_mods['AUTO_LEAN'] = (0, 1)
    else:
        script_mods['AUTO_LEAN'] = (0, 0)
    if check_HipLean.get() == 1:
        script_mods['HIP_LEAN'] = (0, 1)
    else:
        script_mods['HIP_LEAN'] = (0, 0)
    if check_PingOnFire.get() == 1:
        script_mods['PIN_ON_SHOT'] = (0, 1)
    else:
        script_mods['PIN_ON_SHOT'] = (0, 0)
    if check_AutoScan.get() == 1:
        script_mods['AUTO_SCAN'] = (0, 1)
    else:
        script_mods['AUTO_SCAN'] = (0, 0)
    if check_Abilities.get() == 1:
        script_mods['ABILITIES'] = (0, 1)
    else:
        script_mods['ABILITIES'] = (0, 0)
    if check_BuckRF.get() == 1:
        script_mods['SKELETON_KEY_RF'] = (0, 1)
    else:
        script_mods['SKELETON_KEY_RF'] = (0, 0)

def generate_log():
    with open(f"Log.txt", "w") as log:
        log.write(f"Version: {version_num}\n")
        log.write(f"Date: {datetime.datetime.now()}\n")
        log.write(f"Attackers: {attacker_operators}\n")
        log.write(f"Defenders: {defender_operators}\n")
        log.write(f"Script Mods: {list(script_mods)}\n")
        log.write(f"Layout: {drop_Layouts.get()}\n")
        log.write(f"Profile: {drop_Profiles.get()}\n")
        if os.path.exists(attackers):
            log.write("Attackers FOUND\n")
        else:
            log.write("Error: A00x1\n")

        if os.path.exists(defenders):
            log.write("Defenders FOUND\n")
        else:
            log.write("Error: A00x2\n")

def main_page():
    global sldr_percentAdjustment, sldr_horizontal, sldr_vertical # Sliders
    global lbl_deadzone_value, lbl_AntiRecoil,lbl_percentadj_value,lbl_vertical_value,lbl_horizontal_value # Labels and Buttons
    global etr_TbagLol # Entries
    global percentAdjustment # Variables
    global check_OnCams, check_RF4ALL, check_AutoLean, check_HipLean, check_PingOnFire, check_AutoScan, check_Abilities, check_BuckRF 
    global drop_Weapons, drop_Operators, drop_Layouts, drop_Profiles # Drop/CheckBox
    percentAdjustment = 0
    clear_frame()

    # Create the Tabview
    tabview = CTkTabview(frame, 
                         width=680,
                        height=480,
                        fg_color="transparent",
                        border_color=veritas_blue,
                        border_width=2,
                        segmented_button_selected_color=veritas_blue,
                        corner_radius=12,
                        )
    tabview.pack(expand=True, fill='both')

    # Add tabs to the Tabview
    tab_anti_recoil = tabview.add("Anti Recoil")
    tab_mods = tabview.add("Mods")
    tab_layout = tabview.add("Layouts")
    tab_profiles = tabview.add("Profiles")
    tab_settings = tabview.add("Settings")
    # Anti Recoil tab content
    lbl_AntiRecoil = CTkButton(tab_anti_recoil, 
                               text="Anti Recoil", 
                               fg_color="transparent", 
                               hover=False, 
                               border_color="white", 
                               border_width=2, 
                               corner_radius=12, 
                               width=120
                               )
    lbl_AntiRecoil.grid(row=0, column=0, padx=10)

    drop_Operators = tk.CTkOptionMenu(tab_anti_recoil, 
                                  width=200,
                                  values=r6_Operators, 
                                  command=update_weapon_box,
                                  hover = False,
                                 )
    drop_Operators.grid(row=0, column=1, sticky="n")
    drop_Operators.bind("<<OptionMenuSelected>>", update_sliders)

    drop_Weapons = CTkOptionMenu(tab_anti_recoil,
                               values=r6_weapons,
                               bg_color="transparent",
                               command=update_sliders,
                               hover=False,
                               width=180
                               )
    drop_Weapons.grid(row=0, column=2)
    drop_Weapons.bind("<<OptionMenuSelected>>", update_sliders)

    lbl_Vertical = CTkButton(tab_anti_recoil,
                            text="Vertical",
                            fg_color="transparent",
                            border_color="white",
                            border_width=2,
                            width=80,
                            corner_radius=12,
                            hover=False,
                            )
    lbl_Vertical.grid(row=1, column=0)

    sldr_vertical = CTkSlider(tab_anti_recoil, 
                              from_=0, 
                              to=100,
                              width=400,
                              progress_color=veritas_blue,
                              command=update_vertical_label
                              )
    sldr_vertical.grid(row=1, column=1, columnspan=4, pady=10)

    lbl_vertical_value = CTkButton(tab_anti_recoil,
                                   text=sldr_vertical.get(),
                                   fg_color="transparent",
                                   border_color="white",
                                   border_width=2,
                                   corner_radius=12,
                                   width=20,
                                   hover=False
                                   )
    lbl_vertical_value.grid(row=1, column=5,padx=10,sticky="e")

    lbl_horizontal = CTkButton(tab_anti_recoil,
                               text="Horizontal",
                               fg_color="transparent",
                               border_color="white",
                               border_width=2,
                               width=80,
                               corner_radius=12,
                               hover=False
                               )
    lbl_horizontal.grid(row=2, column=0)

    sldr_horizontal = CTkSlider(tab_anti_recoil,
                                from_=-20,
                                to=20,
                                width=400,
                                progress_color=veritas_blue,
                                command=update_horizontal_label
                                )
    sldr_horizontal.grid(row=2, column=1, columnspan=4, pady=10)

    lbl_horizontal_value = CTkButton(tab_anti_recoil,
                                     text=sldr_horizontal.get(),
                                     fg_color="transparent",
                                     border_color="white",
                                     border_width=2,
                                     width=20,
                                     corner_radius=12,
                                     hover=False
                                    )
    lbl_horizontal_value.grid(row=2, column=5, padx=10, sticky="e")

    lbl_percentAdjustment = CTkButton(tab_anti_recoil,
                                      hover=False,
                                      text="Percent Adj",
                                      fg_color="transparent",
                                      border_color="white",
                                      border_width=2,
                                      width=80,
                                      corner_radius=12
                                    )
    lbl_percentAdjustment.grid(row=3, column=0)

    sldr_percentAdjustment = CTkSlider(tab_anti_recoil,
                                       from_=0,
                                       to=100,
                                       width=400,
                                       progress_color="#0a7cbf",
                                       command=update_percentadj_label
                                       )
    sldr_percentAdjustment.grid(row=3, column=1, columnspan=4)
    sldr_percentAdjustment.set(80)
    

    lbl_percentadj_value = CTkButton(tab_anti_recoil,
                                    text=sldr_percentAdjustment.get(),
                                    fg_color="transparent",
                                    border_color="white",
                                    border_width=2,
                                    width=20,
                                    corner_radius=12,
                                    hover=False
                                    )
    lbl_percentadj_value.grid(row=3, column=5, padx=10, sticky="e")

    lbl_deadzone = CTkButton(tab_anti_recoil,
                            text="Deadzone",
                            fg_color="transparent",
                            border_color="white",
                            border_width=2,
                            corner_radius=12,
                            width=80,
                            hover=False
    )
    lbl_deadzone.grid(row=4, column=0)

    sldr_deadzone = CTkSlider(tab_anti_recoil,
                              from_=1,
                              to=100,
                              width=400,
                              progress_color=veritas_blue,
                              command=update_deadzone_label
    )
    sldr_deadzone.grid(row=4, column=1, columnspan=4, pady=10)
    sldr_deadzone.set(12)

    lbl_deadzone_value = CTkButton(tab_anti_recoil,
                                   text=(sldr_deadzone.get()),
                                   fg_color="transparent",
                                   border_color="white",
                                   border_width=2,
                                   hover = False,
                                   width=20,
                                   corner_radius=12,                   
    )
    lbl_deadzone_value.grid(row=4, column=5, padx=10, sticky="e")

    btn_generate_Script = CTkButton(tab_anti_recoil,
                                    text="Generate Script",
                                     fg_color="transparent",
                                     border_color="white",
                                     border_width=2,
                                     corner_radius=12,
                                     width=120,
                                     hover = True,
                                     command=Script_Generation
    )
    btn_generate_Script.grid(row=5, column=1, padx=(100, 0), pady=(80,0))

    update_weapon_box()

    # Mods tab content ###############################################

    lbl_tbagLol = CTkButton(tab_mods,
                            text="TbagLol",
                            fg_color="transparent",
                            border_color="white",
                            border_width=2,
                            corner_radius=12,
                            width=120,
                            hover=False
                            )
    lbl_tbagLol.grid(row=0, column=0, padx=(0,10), pady=10,sticky='w')
    etr_TbagLol = CTkEntry(tab_mods,
                            width=30,
                            )
    etr_TbagLol.grid(row=0, column=2, padx=(5, 10), pady=10,sticky="w")
    etr_TbagLol.insert(0, script_mods["TEA_BAG_LOL"][0])
    incre_tbagLol = CTkButton(tab_mods,
                              text="+",
                              fg_color="transparent",
                              border_color="white",
                              border_width=2,
                              corner_radius=12,
                              hover=True,
                              width=20,
                              command=lambda: increment_entry(etr_TbagLol, "+", 1, 0, 20)  # Use lambda to pass arguments
                            )
    incre_tbagLol.grid(row=0, column=2, padx=(40, 10), pady=10,sticky="w")
    decre_tbagLol = CTkButton(tab_mods,
                              text="-",
                              fg_color="transparent",
                              border_color="white",
                              border_width=2,
                              corner_radius=12,
                              hover=True,
                              width=20,
                              command=lambda: increment_entry(etr_TbagLol, "-", 1, 0, 20)
                            )
    decre_tbagLol.grid(row=0,column=1)

# Rapid Fire
    lbl_rapidfire = CTkButton(tab_mods,
                              text="Rapid Fire",
                              fg_color="transparent",
                              border_color="white",
                              border_width=2,
                              corner_radius=12,
                              width=120,
    )
    lbl_rapidfire.grid(row=1, column=0, padx=(0,10), pady=10,sticky='w')
    etr_rapidfire = CTkEntry(tab_mods,
                              width=30,
                              )
    etr_rapidfire.grid(row=1, column=2, padx=(5, 10), pady=10,sticky="w")
    etr_rapidfire.insert(0, script_mods["RAPID_FIRE"][0])
    decre_rapidFire = CTkButton(tab_mods,
                                text='-',
                                fg_color="transparent",
                                border_color='white',
                                border_width=2,
                                corner_radius=12,
                                hover=True,
                                width=20,
                                command=lambda: increment_entry(etr_rapidfire, "-", 2, 10, 100)
                                )
    decre_rapidFire.grid(row=1,column=1)
    incre_rapidFire = CTkButton(tab_mods,
                                text='+',
                                fg_color="transparent",
                                border_color='white',
                                border_width=2,
                                hover=False,
                                width=20,
                                corner_radius=12,
                                command=lambda: increment_entry(etr_rapidfire, "+", 2, 10, 100)
    )
    incre_rapidFire.grid(row=1,column=2, padx=(40, 10), pady=10,sticky="w")

# Prone Shot
    lbl_proneShot = CTkButton(tab_mods,
                              text="Prone Shot",
                              fg_color="transparent",
                              border_color="white",
                              border_width=2,
                              corner_radius=12,
                              width=120,
                              hover = False,
    )
    lbl_proneShot.grid(row=2, column=0, padx=(0,10), pady=10,sticky='w')
    etr_proneShot = CTkEntry(tab_mods,
                              width=35,
                              )
    etr_proneShot.grid(row=2, column=2, padx=(5, 20), pady=10,sticky="w")
    etr_proneShot.insert(0, script_mods["PRONE_SHOT"][0])
    incre_proneShot = CTkButton(tab_mods,
                                text="+",
                                fg_color="transparent",
                                border_color="white",
                                border_width=2,
                                corner_radius=12,
                                hover=True,
                                width=20,
                                command=lambda: increment_entry(etr_proneShot, "+", 5, 100, 400)  # Use lambda to pass arguments
                                )
    incre_proneShot.grid(row=2, column=2, padx=(45, 10), pady=10,sticky="w")
    decre_proneShot = CTkButton(tab_mods,
                                text="-",
                                fg_color="transparent",
                                border_color="white",
                                border_width=2,
                                corner_radius=12,
                                hover=True,
                                width=20,
                                command=lambda: increment_entry(etr_proneShot, "-", 5, 100, 400)
    )
    decre_proneShot.grid(row=2,column=1)
# lean Spam
    lbl_leanSpam = CTkButton(tab_mods,
                              text="Lean Spam",
                              fg_color="transparent",
                              border_color="white",
                              border_width=2,
                              corner_radius=12,
                              width=120,
                              hover = False,
    )
    lbl_leanSpam.grid(row=3, column=0, padx=(0,10), pady=10,sticky='w')
    etr_leanSpam = CTkEntry(tab_mods,
                              width=35,
                              )
    etr_leanSpam.grid(row=3, column=2, padx=(5, 20), pady=10,sticky="w")
    etr_leanSpam.insert(0, script_mods["LEAN_SPAM"][0])
    incre_leanSpam = CTkButton(tab_mods,
                                text="+",
                                fg_color="transparent",
                                border_color="white",
                                border_width=2,
                                corner_radius=12,
                                hover=True,
                                width=20,
                                command=lambda: increment_entry(etr_leanSpam, "+", 5, 30, 200)  # Use lambda to pass arguments
    )
    incre_leanSpam.grid(row=3, column=2, padx=(45, 10), pady=10,sticky="w")
    decre_leanSpam = CTkButton(tab_mods,
                                text="-",
                                fg_color="transparent",
                                border_color="white",
                                border_width=2,
                                corner_radius=12,
                                hover=True,
                                width=20,
                                command=lambda: increment_entry(etr_leanSpam, "-", 5, 30, 200)
    )
    decre_leanSpam.grid(row=3,column=1)
# Shaiiko Lean
    lbl_shaiikoLean = CTkButton(tab_mods,
                                text="Shaiiko Lean",
                                fg_color="transparent",
                                border_color="white",
                                border_width=2,
                                corner_radius=12,
                                width=120,
                                hover=False,
    )
    lbl_shaiikoLean.grid(row=4, column=0, padx=(0,10), pady=10,sticky='w')
    etr_shaiikoLean = CTkEntry(tab_mods,
                                width=35,
                                )
    etr_shaiikoLean.grid(row=4, column=2, padx=(5, 20), pady=10,sticky="w")
    etr_shaiikoLean.insert(0, script_mods["SHAIKO_LEAN"][0])
    incre_shaiikoLean = CTkButton(tab_mods,
                                text="+",
                                fg_color="transparent",
                                border_color="white",
                                border_width=2,
                                corner_radius=12,
                                hover=True,
                                width=20,
                                command=lambda: increment_entry(etr_shaiikoLean, "+", 5, 100, 200)  # Use lambda to pass arguments
    )
    incre_shaiikoLean.grid(row=4, column=2, padx=(45, 10), pady=10,sticky="w")
    decre_shaiikoLean = CTkButton(tab_mods,
                                text="-",
                                fg_color="transparent",
                                border_color="white",
                                border_width=2,
                                corner_radius=12,
                                hover=True,
                                width=20,
                                command=lambda: increment_entry(etr_shaiikoLean, "-", 5, 100, 200)
    )
    decre_shaiikoLean.grid(row=4,column=1)
# Auto Strafe
    lbl_autoStrafe = CTkButton(tab_mods,
                                text="Auto Strafe",
                                fg_color="transparent",
                                border_color="white",
                                border_width=2,
                                corner_radius=12,
                                width=120,
                                hover=False,
    )
    lbl_autoStrafe.grid(row=5, column=0, padx=(0,10), pady=10,sticky='w')
    etr_autoStrafe = CTkEntry(tab_mods,
                                width=35,
                                )
    etr_autoStrafe.grid(row=5, column=2, padx=(5, 20), pady=10,sticky="w")
    etr_autoStrafe.insert(0, script_mods["STRAFE"][0])
    incre_autoStrafe = CTkButton(tab_mods,
                                text="+",
                                fg_color="transparent",
                                border_color="white",
                                border_width=2,
                                corner_radius=12,
                                hover=True,
                                width=20,
                                command=lambda: increment_entry(etr_autoStrafe, "+", 5, 100, 200)  # Use lambda to pass arguments
    )
    incre_autoStrafe.grid(row=5, column=2, padx=(45, 10), pady=10,sticky="w")
    decre_autoStrafe = CTkButton(tab_mods,
                                text="-",
                                fg_color="transparent",
                                border_color="white",
                                border_width=2,
                                corner_radius=12,
                                hover=True,
                                width=20,
                                command=lambda: increment_entry(etr_autoStrafe, "-", 5, 100, 200)
    )
    decre_autoStrafe.grid(row=5,column=1)
# Crouch Spam
    lbl_crouchSpam = CTkButton(tab_mods,
                                text="Crouch Spam",
                                fg_color="transparent",
                                border_color="white",
                                border_width=2,
                                corner_radius=12,
                                width=120,
                                hover=False,
    )
    lbl_crouchSpam.grid(row=6, column=0, padx=(0,10), pady=10,sticky='w')
    etr_crouchSpam = CTkEntry(tab_mods,
                                width=35,
                                )
    etr_crouchSpam.grid(row=6, column=2, padx=(5, 20), pady=10,sticky="w")
    etr_crouchSpam.insert(0, script_mods["CROUCH_SPAM"][0])
    incre_crouchSpam = CTkButton(tab_mods,
                                text="+",
                                fg_color="transparent",
                                border_color="white",
                                border_width=2,
                                corner_radius=12,
                                hover=True,
                                width=20,
                                command=lambda: increment_entry(etr_crouchSpam, "+", 5, 10, 200)  # Use lambda to pass arguments
    )
    incre_crouchSpam.grid(row=6, column=2, padx=(45, 10), pady=10,sticky="w")
    decre_crouchSpam = CTkButton(tab_mods,
                                text="-",
                                fg_color="transparent",
                                border_color="white",
                                border_width=2,
                                corner_radius=12,
                                hover=True,
                                width=20,
                                command=lambda: increment_entry(etr_crouchSpam, "-", 5, 10, 200)
    )
    decre_crouchSpam.grid(row=6,column=1)
# check Boxes
    global OnCams, RF4All, AutoLean, HipLean, PingOnFire, AutoScan, Abilities, BuckRF
    OnCams = None
    RF4All = None
    AutoLean = None
    HipLean = None
    PingOnFire = None
    AutoScan = None
    Abilities = None
    BuckRF = None
    
# On Cams
    check_OnCams = CTkCheckBox(tab_mods,
                               text="On Cams",
                               fg_color=veritas_blue,
                               border_color="white",
                               border_width=2,
                               corner_radius=12,
                               width=120,
                               variable=OnCams,
                               onvalue=1,
                               offvalue=0,
                               command=check_toggles
    )
    check_OnCams.grid(row=0, column=4, padx=(250,10), pady=10,sticky='e')
# RapidFire 4 All
    check_RF4ALL = CTkCheckBox(tab_mods,
                               text="RF 4 All",
                               fg_color=veritas_blue,
                               border_color="white",
                               border_width=2,
                               corner_radius=12,
                               width=120,
                               variable=RF4All,
                               onvalue="on",
                               offvalue="off"
    )
    check_RF4ALL.grid(row=1, column=4, padx=(250,10), pady=10,sticky='e')
# Auto Lean
    check_AutoLean = CTkCheckBox(tab_mods,
                               text="Auto Lean",
                               fg_color=veritas_blue,
                               border_color="white",
                               border_width=2,
                               corner_radius=12,
                               width=120,
                               variable=AutoLean,
                               onvalue="on",
                               offvalue="off"
    )
    check_AutoLean.grid(row=2, column=4, padx=(250,10), pady=10,sticky='e')
# Hip Lean
    check_HipLean = CTkCheckBox(tab_mods,
                               text="Hip Lean",
                               fg_color=veritas_blue,
                               border_color="white",
                               border_width=2,
                               corner_radius=12,
                               width=120,
                               variable=HipLean,
                               onvalue="on",
                               offvalue="off"
    )
    check_HipLean.grid(row=3, column=4, padx=(250,10), pady=10,sticky='e')
# Ping On Fire
    check_PingOnFire = CTkCheckBox(tab_mods,
                               text="Ping On Fire",
                               fg_color=veritas_blue,
                               border_color="white",
                               border_width=2,
                               corner_radius=12,
                               width=120,
                               variable=PingOnFire,
                               onvalue="on",
                               offvalue="off"
    )
    check_PingOnFire.grid(row=4, column=4, padx=(250,10), pady=10,sticky='e')
# Auto Scan
    check_AutoScan = CTkCheckBox(tab_mods,
                               text="Auto Scan",
                               fg_color=veritas_blue,
                               border_color="white",
                               border_width=2,
                               corner_radius=12,
                               width=120,
                               variable=AutoScan,
                               onvalue="on",
                               offvalue="off"
    )
    check_AutoScan.grid(row=5, column=4, padx=(250,10), pady=10,sticky='e')
# Abilities 
    check_Abilities = CTkCheckBox(tab_mods,
                               text="Abilities",
                               fg_color=veritas_blue,
                               border_color="white",
                               border_width=2,
                               corner_radius=12,
                               width=120,
                               variable=Abilities,
                               onvalue="on",
                               offvalue="off"
    )
    check_Abilities.grid(row=6, column=4, padx=(250,10), pady=10,sticky='e')
# Buck RF
    check_BuckRF = CTkCheckBox(tab_mods,
                               text="Buck RF",
                               fg_color=veritas_blue,
                               border_color="white",
                               border_width=2,
                               corner_radius=12,
                               width=120,
                               variable=BuckRF,
                               onvalue="on",
                               offvalue="off",
    )
    check_BuckRF.grid(row=7, column=4, padx=(250,10), pady=10,sticky='e')

# Tab - Layouts
    drop_Layouts = CTkOptionMenu(tab_layout,
                               values=script_layouts,
                               width = 240,
                               command=layout_description
    )
    drop_Layouts.grid(row=0, column=0, padx=(0,10), pady=10,sticky='w')

# Tab - Profiles
    drop_Profiles = CTkOptionMenu(tab_profiles,
                               values=script_profiles,
                               width = 240,
                               command=profile_description
    )
    drop_Profiles.grid(row=0, column=0, padx=(0,10), pady=10,sticky='w')

# Tab - Settings
    btn_generate_log = CTkButton(tab_settings,
                                 text="Generate Log",
                                 fg_color="transparent",
                                 border_color="white",
                                 border_width=2,
                                 corner_radius=12,
                                 width=120,
                                 command=generate_log
    )
    btn_generate_log.grid(row=0, column=0, padx=(0,10), pady=10,sticky='w')
    btn_share_config = CTkButton(tab_settings,
                                 text="Export Config",
                                 fg_color="transparent",
                                 border_color="white",
                                 border_width=2,
                                 corner_radius=12,
                                 width=120,
                                 command=create_config
    )
    btn_share_config.grid(row=1, column=0, padx=(0,10), pady=10,sticky='w')
    btn_import_config = CTkButton(tab_settings,
                                 text="Import Config",
                                 fg_color="transparent",
                                 border_color="white",
                                 border_width=2,
                                 corner_radius=12,
                                 width=120,
                                 command=import_config
    )
    btn_import_config.grid(row=2, column=0, padx=(0,10), pady=10,sticky='w')

    btn_reset_config = CTkButton(tab_settings,
                                 text="Reset Config",
                                 fg_color="transparent",
                                 border_color="white",
                                 border_width=2,
                                 corner_radius=12,
                                 width=120,
                                 command=lambda: reset_config(Operators)
    )
    btn_reset_config.grid(row=3, column=0, padx=(0,10), pady=10,sticky='w')

# Misc
def main():
    if not successful_login:
        Login_View()
    else:
        update_sliders()
        main_page()
main()
root.mainloop()