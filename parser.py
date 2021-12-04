class Parser:
    def __init__(self, file):
        self.file = file
        self.snt = []

    def parsing(self):
        snt_count = 0
        char_count = 0
        for line in self.file:
            if line !="\n":
                line = line.strip("\n")
                self.snt.append(line)
                snt_count += 1
                for char in line:
                    if char !=' ':
                        char_count += 1

        return {'sentences': self.snt, 'stats': {'total_sentences': snt_count, 'total_chars': char_count }}, snt_count, char_count



