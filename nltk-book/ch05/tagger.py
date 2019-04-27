import nltk, re, pprint
from nltk import word_tokenize


def test_connect():
    """
    prints to make sure file is connect
    """
    print("Connected")


class Tagger:
    """docstring for Tagger"""

    def __init__(self, arg):
        """
        Begin Setup
        """
        self.raw_string = arg
        self.tokenize = word_tokenize(arg)

        """
        Part of Speech
        """
        self.speech_tag = None

        """
        Tagged Corpora
        """

        self.string_tuple = None
        self.common_part_speech = None


    def print_init(self):
        """
        prints raw string
        """

        print(self.raw_string)


    """
    Part of Speech
    """


    def pos_tagger(self):
        """
        saves part of speech
        """
        self.speech_tag = nltk.pos_tag(self.tokenize)


    """
    Tagged Corpora
    """


    def tuple_to_string(self):
        """
        Saves a tuple to a string format of : the/DET hello/NN
        :return: string
        """
        raw_string = """"""
        for item in self.speech_tag:
            raw_string += item[0] + '/' + item[1] + " "

        self.string_tuple = raw_string


    def most_common_tag(self):
        """
        Returns a common part of speech tag list
        :return: list
        """

        self.common_part_speech = nltk.FreqDist(tag for (word, tag) in self.speech_tag)

    """
    Return Commands
    """


    def return_value(self, keyword):
        """
        Returns the value in the keyword
        """

        init_value = {
            'speech_tag': self.speech_tag,
            'string_tuple': self.string_tuple,
            'common_part_speech': self.common_part_speech
        }

        return init_value[keyword]
