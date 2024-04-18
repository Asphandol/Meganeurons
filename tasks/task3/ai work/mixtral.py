import time
start_time = time.time()


def create_acronym(input_sentence: str) -> str:
    if isinstance(input_sentence, str):
        if any(char.isdigit() for char in input_sentence):
            return

        sentences = input_sentence.split("\n")

        acronyms = []

        for i, sentence in enumerate(sentences):
            if sentence.isdigit():
                continue
        
            words = sentence.split()
        
            acronym = "".join(word[0].upper() for word in words)
        
            words = [acronym] + [' '.join(words)]
        
            words = " - ".join(words)
        
            if i < len(sentences) - 1:
                acronyms.append(words)
                acronyms.append("\n")
            else:
                acronyms.append(words)
        
        acronyms = "".join(acronyms)

        return acronyms
    

end_time = time.time()

print("Execution Time: ", end_time - start_time)