ANIMAL_N = "ANIMAL_N"
ANIMAL_N_1 = "ANIMAL_N_1"
FINAL_LINES = "I don't know why she swallowed a fly - perhaps she'll die!\n"
REPEATING_LINE = "She swallowed the " + ANIMAL_N + " to catch the " + ANIMAL_N_1

class my_class(object):
    def __init__(self, name, optionalText, includeRepeater, includeLastLine):
        self.name = name
        self.optionalText = optionalText
        self.includeRepeater = bool(includeRepeater)
        self.includeLastLine = bool(includeLastLine)
    




