from random import choice

class markov_chain(object):

    def __init__(self, ft={}):
        """Frequency Table: ft."""
        self.ft = ft
        self.separators = "!?."

    def __siw(self, word):
        """Check if separator occurs in word."""
        for separator in self.separators:
            if separator in word:
                return True

        return False

    def learn(self, text):
        """Learn from a text."""
        words = text.split()

        pw = words[0]
        for word in words[1:]:
            if pw in self.ft:
                if word in self.ft[pw]:
                    self.ft[pw][word] += 1
                else:
                    self.ft[pw][word] = 1

                self.ft[pw]["total"] += 1
            else:
                self.ft[pw] = {}
                self.ft[pw]["total"] = 1
                self.ft[pw][word] = 1

    def _get_sentence(self, start):
        """
        Generate one sentence.
        
        A sentence is defined as a sequence
        that ends in a separator.
        """
        sentence = [start]
        pos = start
        while not self.__siw(pos):
            if pos in self.ft:
                pos = get_successor(self.ft[pos])
                sentence.append(pos)
            else:
                sentence.append("\n")
                break

        
        next_start = None
        if pos in self.ft:
            next_start = get_successor(pos)

        return next_start, sentence

    def generate(self, sentences=2):
        """Generate a Text."""
        
        """position in chain."""

        start = choice(self.ft.keys())
        text = []
        while sentences:
            next_start, sentence = self._get_sentence(start)
            text.extend(sentence)

            if next_start is 




def get_successor(stats):
    """Get successor of chain."""

    """This might be used to effectivice."""
    total = stats["total"]


    """Naive Solution."""
    freq = []
    for k, v in stats.items():
        freq.extend([k] * v)

    return choice(freq)



