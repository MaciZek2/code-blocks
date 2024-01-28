# main.py
from interpreter import Interpreter
from languages.python import PythonInterpreter
from themes.dark import DarkTheme

# Inicjalizacja interpretera
interpreter = Interpreter(language="python", theme="light")

# Zmiana języka
interpreter.set_language("cpp")

# Zmiana motywu
interpreter.set_theme("dark")

# Wykonanie kodu
code = 'print("Hello, World!")'
interpreter.execute_code(code)

# Wyświetlenie motywu
interpreter.display_theme()

