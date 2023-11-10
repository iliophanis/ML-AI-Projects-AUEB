class Vocabulary:

    def __init__(self, vocabulary_file=None):
        self.id_to_word = {}
        self.word_to_id = {}
        self.locked = False
        self.next_id = 0
        if vocabulary_file:
            for row in open(vocabulary_file):
                row = row.rstrip('\n')
                (word, wid) = row.split('\t')
                self.word_to_id[word] = int(wid)
                self.id_to_word[wid] = word
                self.next_id = max(self.next_id, int(wid)+1)


    def lock(self):
        self.locked = True

    def get_id(self, word):
        if not word in self.word_to_id:
            if self.locked:
                return -1
            else:
                self.word_to_id[word] = self.next_id
                self.id_to_word[self.word_to_id[word]] = word
                self.next_id += 1
        return self.word_to_id[word]

    def get_word(self, wid):
        return self.id_to_word[wid]

    def get_words(self):
        return self.word_to_id.keys()

    def has_word(self, word):
        return word in self.word_to_id

    def get_size_vocabulary(self):
        return self.next_id

    def has_id(self, id):
        return id in self.id_to_word

    def save_vocabulary(self, vocabulary_file):
        out_file = open(vocabulary_file, 'w')
        for word in self.word_to_id.keys():
            out_file.write("%s\t%s\n" % (word, self.word_to_id[word]))

