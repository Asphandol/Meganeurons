def create_acronym(input_sentence: str) -> str:
    if isinstance(input_sentence, str):
        if any(char.isdigit() for char in input_sentence):
            return

        sentences = input_sentence.split("\n")

        acronyms = []

        if len(sentences) > 1:
            for sentence in sentences:
                words = sentence.split()

                acronym = "".join(word[0].upper() for word in words)

                words = [acronym] + [' '.join(words)]

                words = " - ".join(words)

                acronyms.append(words)

                if sentence != sentences[-1]:
                    acronyms.append("\n")

            acronyms = "".join(acronyms)

        elif len(sentences) == 1:
            sentence = sentences[0]

            words = sentence.split()

            acronym = ""

            for word in words:
                acronym += word[0]

            acronym = acronym.upper()

            acronym += " -"

            words.insert(0, acronym)

            acronyms = words

            acronyms = " ".join(acronyms)

        return acronyms