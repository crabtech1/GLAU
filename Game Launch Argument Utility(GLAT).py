import subprocess
import os

print("Welcome to GLAT")
def launch_game():
    exe_path = input("Insert full path to EXE: ").strip('" ')
    if not os.path.exists(exe_path):
        print("EXE not found. Check the path and try again.")
        return

    args = input("Insert launch arguments (if any): ")
    command = f'"{exe_path}" {args}'

    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    try:
        subprocess.Popen(command, startupinfo=startupinfo, shell=True)
        print("Launching the game...")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    launch_game()
    print("Success!")
