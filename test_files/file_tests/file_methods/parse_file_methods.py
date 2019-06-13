import os.path

class parse_file_methods(object):
    def __init__(self):
        pass

    def check_file_type(self, filepath):
        # Parameters: filepath
        # filepath = path of the file to check
        # Description: check if the file exists
        if os.path.isfile(filepath):
            if filepath.endswith('.dat') or filepath.endswith('.txt'):
                return "True"
            else:
                return "File format is invalid. Only accepts .dat and .txt"
        else:
            return "File '%s' not exist" % filepath

    def get_lines_from_file(self, input_file):
        # Parameters:
        # input_file = file path of the file to read
        # Description: open the file, readlines and store them in a list.
        # Return: list of lines from the file
        with open(input_file) as f:
            lines = f.read().splitlines()

        return lines

    def get_largest_word(self, lines):
        # Parameters:
        # lines = lines to parse
        temp_largest_word = ""
        largest_words = []
        for line in lines:
            temp_words = line.split(" ")
            for temp_word in temp_words:
                if len(temp_word) > len(temp_largest_word):
                    largest_words = [temp_word]
                    temp_largest_word = temp_word
                elif len(temp_word) == len(temp_largest_word):
                    largest_words.append(temp_word)
        return largest_words

    def reverse_words(self, words_list):
        # Parameters:
        # words_list = list of words to reverse
        reversed_words = []
        for word in words_list:
            reversed_words.append(word[::-1])
        return reversed_words


