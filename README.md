# Veritas GUI
Veritas Script Generation and Anti Recoil config sharing.

# How To Use

Simply run the `veritas.exe` file to open the GUI.
In the Anti Recoil tab you can edit the Anti Recoil settings for every operator and their weapons.
In the Mods tab, you can change certain values of mods or faster updating, or convinience. Same with toggling mods on the right side of that tab.
In the Layout tab, you can change the default Layout the script will be compiled with. Same with the Profiles tab.

In the Settigns tab, you can Export, Import, and Reset your Anti Recoil Configuration. Exported configs will be named "exported_config.py"
and must remain this way when sharing/Importing.

If youre going to import a config, make sure to export your own as a back up.

# Compiling from Source

To compile from source, you must first install [python](https://www.python.org/downloads/). Make sure to check the option to add it to your system's PATH.
After installing python, i would recommend installing [Visual Studio Code](https://code.visualstudio.com/) if youd want to look at the source code, and verify
it before compiling.
Open your windows command prompt ( Win + R, "cmd" ) and type `pip install customtkinter` to install the GUI Framework this uses.
after letting customtkinter install, now type `pip install auto-py-to-exe` to be able to convert it to a .EXE file.
You can do the same this with [CX Freeze](https://cx-freeze.readthedocs.io/en/stable/overview.html) but i feel its easier to use py to exe.

run the command `auto-py-to-exe` to open the compilier.
Inside of autopy, choose the option for the .exe to be "windows based" so the program doesnt
open with a cmd window behind it. **Note** compiling this way will false flag as a trojan. it is not, it is simply how auto-py-to-exe  compilies scripts,
as you wont get this error if you choose "console based", if you dont want the console window, simply disable your anti virus when converting.

After so, go back into CMD and type `pip show customtkinter` and copy that directory.
In Auto-Py click the "Additional Files" drop down menu, and click "Add folder" and paste
the directory into the search bar at the bottom. 

Now click "CONVERT .PY TO .EXE" and wait.

Open the output folder and copy the contents of the "veritas" folder to the source folder.

And boom, all done

# Credits

VeritasCGD -> Creating the Scripts, and allowing me to dev along side him.

Tom Schimansky -> [For creating customtkiner, and making this possible](https://github.com/TomSchimansky/CustomTkinter)

Brent Vollebregt -> [For maintaining Auto-Py-To-Exe](https://pypi.org/project/auto-py-to-exe/)

# Donations

You can donate to me here :
> CashApp : $zKiwiko ( American Residents )

> BuyMeACoffee : https://buymeacoffee.com/kiwiko ( International Residents )

