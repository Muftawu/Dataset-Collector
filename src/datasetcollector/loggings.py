from termcolor import cprint
import sys 

color_error = "red"
color_info = "yellow"
color_success = "green"

def warning_error(msg: str):
    try:
        cprint(f"ERROR: {msg}", color_error, end=' ')
        sys.stdout.flush()
    except:
        pass 

def warning_info(msg):
    try:
        cprint(f"INFO: {msg}", color_info, end=' ')
        sys.stdout.flush()
    except:
        pass 

def warning_success(msg):
    try:
        cprint(f"\nSUCCESS: {msg}", color_success)
    except:
        pass 