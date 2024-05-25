
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
    [0, 1, -1, 2, -1, -1],  # SLEDGE
    [30, 0, 1, 2, -1, -1],  # THATCHER
    [21, 6, -1, 17, 22, -1],  # Ash
    [29, 23, -1, 17, 22, -1],  # THERMITE
    [31, 32, 33, 24, 25, -1],  # TWITCH
    [69, -1, -1, 24, 25, -1],  # MONTAGNE
    [40, -1, -1, 27, 70, 53],  # GLAZ
    [41, 42, 69, 27, 28, -1],  # FUZE
    [69, -1, -1, 9, -1, -1],  # BLITZ
    [12, 8, 39, 9, -1, -1],  # IQ
    [35, 34, -1, 7, 70, -1],  # BUCK
    [44, 43, -1, 18, -1, -1],  # BLACKBEARD
    [36, 37, -1, 38, 70, -1],  # CAPITÃO
    [45, 13, -1, 53, 14, -1],  # HIBANA
    [46, 49, 48, 4, 47, -1],  # JACKAL
    [52, 54, -1, 51, -1, -1],  # YING
    [59, 58, -1, 55, -1, -1],  # ZOFIA
    [60, 56, -1, 19, 70, 11],  # DOKKAEBI
    [61, 32, 33, 25, -1, 24],  # LION
    [42, 62, 71, 27, -1, 28],  # FINKA
    [63, 64, -1, 65, -1, -1],  # MAVERICK
    [66, 5, -1, 38, 50, -1],  # NOMAD
    [36, 67, -1, 20, 70, 82],  # GRIDLOCK
    [15, 16, -1, 18, 17, -1],  # NOKK
    [12, 13, -1, 3, 70, 47],  # Amaru
    [10, -1, -1, 57, 11, 2],  # KALI
    [5, 6, -1, 7, 70, -1],  # IANA
    [41, 23, -1, 24, -1, -1],  # ACE
    [26, 68, -1, 17, 70, -1],  # ZERO
    [30, 43, -1, 28, -1, -1],  # FLORES
    [29, 49, -1, 27, -1, -1],  # OSA
    [105, 32, -1, 82, -1, -1],  # SENSE
    [39, 33, -1, 14, 74, -1],  # GRIM
    [37, 34, -1, 4, 20, -1],  # BRAVA
    [21, 58, -1, 47, 7, -1],  # RAM
    [66, 1, -1, 106, -1, -1]  # DEIMOS
]

OperatorNames = [
    "Sledge", "Thatcher", "Ash", "Thermite", "Twitch", "Montagne", "Glaz", "Fuze", "Blitz", "Iq",
    "Buck", "Blackbeard", "Capitão", "Hibana", "Jackal", "Ying", "Zofia", "Dokkaebi", "Lion", "Finka",
    "Maverick", "Nomad", "Gridlock", "Nokk", "Amaru", "Kali", "Iana", "Ace", "Zero", "Flores",
    "Osa", "Sense", "Grim", "Brava", "Ram", "Deimos"
]

config = "config.py"

Operators = {}

for operator_name in OperatorNames:
    index = OperatorNames.index(operator_name)
    weapons = [GunName[gun] if gun != -1 else None for gun in GunAssignment[index]]
    weapons_dict = {}
    for weapon in weapons:
        weapons_dict[weapon] = {"vertical": 0, "horizontal": 0, "percent": 0}
    Operators[operator_name] = {"weapons": weapons, "values": weapons_dict}

# Print the Operators dictionary in the specified format
with open("config.py", "w") as file:
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





