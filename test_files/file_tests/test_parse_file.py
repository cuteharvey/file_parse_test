from file_methods.parse_file_methods import parse_file_methods as pfms
from utils.setup_teardown import setup_teardown as st
from utils import log
import unittest
'''

     1. Read input from a file of words;

    2. Find the largest word in the file

    3. Transpose the letters in the largest word

    4. Show the largest word and the largest word transposed

    5. Demonstrate positive and negative test cases

    6. Ensure you document code and instructions for building and running based on the response best practices above


Assumptions (in real projects, QA would have to clarify these assumptions from PMs or Project Leads):
1. Duplicates are shown
2. Transponse letters == Reverse word
3. Special characters are part of a word eg. ", ., !, ....
4. File type extensions accepted are .txt, .dat
'''

class test_parse_file(unittest.TestCase):
    def setUp(self):
        st().setup_steps()
        self.pfm = pfms()

    def test_happy_path(self):
        log.info("*** Happy path test *** ../files/testFile.txt")
        filename = "../files/testFile.txt"
        assert self.parse_file(filename), "Expecting file to be found and valid. Check if file %s actually exists with correct format" % filename

    def test_empty_file(self):
        log.info("*** Empty file test *** ../files/testEmptyFile.txt")
        filename = "../files/testEmptyFile.txt"
        assert self.parse_file(filename), "Expecting file to be found and valid. Check if file %s actually exists with correct format" % filename

    def test_sentences_in_file(self):
        log.info("*** Sentences in File test *** ../files/testSentencesFile.txt")
        filename = "../files/testSentencesFile.txt"
        assert self.parse_file(filename), "Expecting file to be found and valid. Check if file %s actually exists with correct format" % filename

    def test_file_does_not_exist(self):
        log.info("*** File Does Not Exist test *** ../files/testFileDoesNotExist.txt")
        filename = "../files/testFileDoesNotExist.txt"
        #filename = "../files/testFile.txt"        #enable this line to check if test will fail if file exists (testing your method actually works if file actually exists)
        assert self.parse_file(filename) is False, "Expecting file DOES NOT EXIST. File %s is found" % filename

    def test_file_invalid_format(self):
        log.info("*** Invalid file format test *** ../files/testImageFile.png")
        filename = "../files/testImageFile.png"
        assert self.parse_file(filename) is False, "Expecting file DOES NOT EXIST. File %s is found with valid format" % filename

    def parse_file(self, test_file):
        check_file = self.pfm.check_file_type(test_file)
        if check_file == "True":
            lines_in_file = self.pfm.get_lines_from_file(test_file)
            log.info("Lines in File: %s" % lines_in_file)
            largest_words = self.pfm.get_largest_word(lines_in_file)
            log.info("Largest words: %s" % largest_words)
            reversed_words = self.pfm.reverse_words(largest_words)
            log.info("Reversed words: %s" % reversed_words)
            return True
        else:
            log.info(check_file)
            return False

    def tearDown(self):
        st().teardown_steps()


# if __name__ == '__main__':
#     tfm = test_parse_file()
#     tfm.test_happy_path()
#     tfm.test_empty_file()
#     tfm.test_sentences_in_file()
#     tfm.test_file_does_not_exist()
#     tfm.test_file_invalid_format()


