class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        super().__init__("En", letters)

    def is_en_letter(self, letter):
        return letter in self.letters

    def letters_num(self):
        return EngAlphabet.__letters_num
   
    @staticmethod
    def example():
        return "I want to see Lasha tumbai"

if __name__ == "__main__":
    ea = EngAlphabet()

    ea.print()
    print(ea.letters_num())
    print(ea.is_en_letter("L"))
    print(ea.is_en_letter("П"))
    print(EngAlphabet.example())
