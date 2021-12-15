from trainedData import TrainedData

class Trainer(object):

    """docstring for Trainer"""
    def __init__(self, tokenizer):
        super(Trainer, self).__init__()
        self.tokenizer = tokenizer
        self.data = TrainedData()

    def train(self, text, className):
        """
        enhances trained data using the given text and class
        """
        self.data.increaseClass(className)

        tokens = self.tokenizer.tokenize(text)
        for token in tokens:
            token = self.tokenizer.remove_stop_words(token)
            token = self.tokenizer.remove_punctuation(token)
            self.data.increaseToken(token, className)
