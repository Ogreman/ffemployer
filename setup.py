import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
	base = "Win32GUI"

setup(name="Final Fantasy Employer", version="0.1",description="Final Fantasy Employer", executables = [Executable("ffiii_job_roll.py", base=base)])