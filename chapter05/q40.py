class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def is_end_of_sentence(self) -> bool: return self.pos1 == '句点'

    def __str__(self) -> str: return 'surface: {}, base: {}, pos: {}, pos1: {}'.format(self.surface, self.base, self.pos, self.pos1)
    
def make_morph_list(analyzed_file_name: str) -> list:
    sentences = []
    sentence = []
    with open(analyzed_file_name, encoding='utf-8') as input_file:
        for line in input_file:
            line_list = line.split()
            if (line_list[0] == '*') | (line_list[0] == 'EOS'):
                pass
            else:
                line_list = line_list[0].split(',') + line_list[1].split(',')
                _morph = Morph(surface=line_list[0], base=line_list[7], pos=line_list[1], pos1=line_list[2])

                sentence.append(_morph)

                if _morph.is_end_of_sentence():
                    sentences.append(sentence)
                    sentence = []

    return sentences

morphed_sentences = make_morph_list('neko.txt.cabocha')

print(morphed_sentences)
# for morph in morphed_sentences[2]:
#     print(str(morph))