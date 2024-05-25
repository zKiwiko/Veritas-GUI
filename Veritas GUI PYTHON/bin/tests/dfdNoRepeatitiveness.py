GunName = [
    "L85A2", "M590A1", "P226 MK 25", "SMG-11", "USP40", "ARX200", "G36C", "MK1 9MM", "AUG A2", "P12",
    "CSRX 300", "C75 Auto", "G8A1", "SUPERNOVA", "P229", "FMG-9", "SIX12 SD", "5.7 USG", "D-50", "SMG-12",
    "SUPER SHO..", "R4-C", "M45 MEUSOC", "M1014", "P9", "LFP586", "MP7", "PMM", "GSH-18", "556XI",
    "AR33", "F2", "417", "SG-CQB", "CAMRS", "C8-SFW", "M249", "PARA-308", "PRB92", "552COMMANDO",
    "OTS-03", "AK-12", "6P41", "SR-25", "MK17 CQB", "TYPE-89", "C7E", "ITA12S", "ITA12L", "PDW9",
    ".44MAG SEMI", "Q-929", "T-95 LSW", "BEARING 9", "SIX12", "RG15", "BOSG.12.2", "SPSMG9", "LMG-E", "M762",
    "Mk 14 EBR", "V308", "SPEAR .308", "AR-15.50", "M4", "1911 TACOPS", "AK-74M", "F90", "SC3000K", "Shield",
    "Gonne-6", "SASG-12", "SPAS-12", "MP5", "Bailiff 410", "MP5K", "VECTOR .45", "TCSG12", "MPX", "P-10C",
    "COMMANDO 9", "P10 RONI", "SDP 9mm", "UMP45", "P90", "M870", "416CCARBINE", "9X19VSN", "9MM C1", "SUPER90",
    "AUG A3", "T-5 SMG", "M12", "SPAS-15", "LUISON", "MP5SD", "SCORPION", "FO-12", "K1A", "ALDA 5.56",
    "ACS12", "KERATOS.357", "Mx4 Storm", "DP27", "UZK50GI", "POF-9", ".44VENDETTA", ""
]

GunAssignment = [
    [15, 1, -1, 3, 2, -1],  # SMOKE
    [75, 1, -1, 3, 2, -1],  # MUTE
    [83, 23, -1, 20, 17, 22],  # CASTLE
    [83, 23, -1, 17, 22, -1],  # PULSE
    [73, 33, 84, 24, 25, 74],  # DOC
    [73, 33, 84, 24, 25, -1],  # ROOK
    [87, 71, -1, 27, 28, -1],  # KAPKAN
    [87, 103, -1, 27, 28, 53],  # TACHANKA
    [86, 85, -1, 9, -1, -1],  # JAGER
    [26, 85, -1, 9, -1, -1],  # BANDIT
    [88, 89, -1, 7, 47, -1],  # FROST
    [78, 72, -1, 18, -1, -1],  # VALKYRIE
    [92, 93, -1, 94, -1, -1],  # CAVEIRA
    [95, 13, -1, 53, 14, -1],  # ECHO
    [76, 48, -1, 47, 4, -1],  # MIRA
    [91, 54, -1, 51, 20, -1],  # LESION
    [96, 97, -1, 55, -1, -1],  # ELA
    [98, 56, -1, 11, 19, -1],  # VIGIL
    [99, 100, -1, 74, 101, -1],  # MAESTRO
    [102, 100, -1, 101, 74, -1],  # ALIBI
    [57, 20, 79, -1, -1, -1],  # CLASH
    [90, 77, -1, 25, 50, -1],  # KAID
    [80, 81, -1, 82, -1, -1],  # MOZZIE
    [78, 1, -1, 19, 79, -1],  # WARDEN
    [76, 77, -1, 14, -1, -1],  # GOYO
    [8, 75, -1, 101, 9, -1],  # WAMAI
    [91, 72, -1, 74, 4, -1],  # ORYX
    [73, 89, -1, 55, -1, -1],  # Melusi
    [81, 60, -1, 38, -1, -1],  # ARUNI
    [62, 93, -1, 53, 51, -1],  # THUNDERBIRD
    [104, 85, -1, 11, 65, -1],  # THORN
    [87, 100, -1, 18, -1, -1],  # AZAMI
    [84, 48, -1, 3, -1, -1],  # SOLIS
    [26, 71, -1, 74, 17, -1],  # FENRIR
    [78, 63, -1, 2, -1, -1]  # TUBARAO
]

Operators = {}

OperatorNames = [
    "Smoke", "Mute", "Castle", "Pulse", "Doc", "Rook", "Kapkan", "Tachanka", "Jager", "Bandit",
    "Frost", "Valkyrie", "Caveira", "Echo", "Mira", "Lesion", "Ela", "Vigil", "Maestro", "Alibi",
    "Clash", "Kaid", "Mozzie", "Warden", "Goyo", "Wamai", "Oryx", "Melusi", "Aruni", "Thunderbird",
    "Thorn", "Azami", "Solis", "Fenrir", "Tubarao"
]
for operator_name in OperatorNames:
    index = OperatorNames.index(operator_name)
    weapons = [GunName[gun] if gun != -1 else None for gun in GunAssignment[index]]
    weapons_dict = {}
    for weapon in weapons:
        weapons_dict[weapon] = {"vertical": 0, "horizontal": 0, "percent": 0}
    Operators[operator_name] = {"weapons": weapons, "values": weapons_dict}

# Print the Operators dictionary in the specified format
with open("config.py", "a") as file:
    # Write the beginning of the dictionary
    file.write("Operators = {\n")
    
    # Iterate through the Operators dictionary
    for operator_name, data in Operators.items():
        # Write operator name and beginning of its data
        file.write(f'    "{operator_name}": {{\n')
        file.write(f'        "weapons": {data["weapons"]},\n')
        file.write("        \"values\": {\n")
        
        # Write weapon values
        for weapon, values in data["values"].items():
            file.write(f'            "{weapon}": {values},\n')
        
        # Write the end of the operator data
        file.write("        }\n")
        file.write("    },\n")
    
    # Write the end of the dictionary
    file.write("}\n")