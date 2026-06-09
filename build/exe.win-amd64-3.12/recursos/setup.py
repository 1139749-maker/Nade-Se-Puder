import sys
import cx_Freeze

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executaveis = [ 
    cx_Freeze.Executable(
        script="main.py", 
        icon="bases/icone.png", 
        target_name="NadeSePuder.exe",
        base=base
    ) 
]

cx_Freeze.setup(
    name="Nade Se Puder",
    version="1.0",
    description="Jogo Nade Se Puder",
    options={
        "build_exe": {
           
            "packages": ["pygame", "pyttsx3"], 
            
            "include_files": [
                ("bases/", "bases/"),
                ("recursos/", "recursos/")
            ]
        }
    }, 
    executables=executaveis
)