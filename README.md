

````markdown
# Game Launch Argument Tool (GLAT)

GLAT is a no-nonsense Python tool that lets you launch old-school games (especially DVD or DRM-free ones) with custom command-line arguments. No launcher required.

It's great for running legacy .exe files with specific commands, skipping intros, setting memory pool sizes, or launching games exactly how you want.

## Features

- Launch any .exe file with custom command-line arguments
- Runs in an invisible CMD window
- Designed for games without traditional launchers
- Useful for modders, retro gamers, and power users

## Requirements

- Python 3.x
- Windows (tested on Windows 10 and 11)

## Installation

Clone the repository or download the script manually:

```bash
git clone https://github.com/your-username/glat.git
cd glat
````

Or just download `glat.py` and run it directly.

## Usage

Run the script from the terminal or double-click if Python is associated with .py files:

```bash
python glat.py
```

Then follow the prompts:

```
Insert full path to EXE: C:/Games/ATS/bin/win_x64/ats.exe
Insert launch arguments (if any): -nointro -64bit
Launching the game...
```

## Example Launch Options for American Truck Simulator

```
-nointro            Skips intro videos  
-64bit              Forces 64-bit mode  
-mm_pool_size 4000  Allocates 4 GB to the engine's memory pool
```

## License

This project is licensed under the GNU General Public License v3.0.
See the LICENSE file for full details.

## Credits

Created by crabtech1
GLAT is free software. Use it, share it, improve it.


