# interpreter.py
class Interpreter:
    def __init__(self, language="python", theme="light"):
        self.language = language
        self.theme = theme

    def set_language(self, language):
        self.language = language

    def set_theme(self, theme):
        self.theme = theme

    def execute_code(self, code):
        # Logika wykonania kodu dla każdego języka
        pass

    def display_theme(self):
        # Logika wyświetlenia motywu
        pass
