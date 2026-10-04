"""
Program - word analyzer
Author - Bernard Paul
Purpose- scans the 4 text files and states how often each word is said alphabetically 
10/4/26

"""
from pathlib import Path
import string


#class to analyze word frequencies of a text file
class WordAnalyzer:

    def __init__(self, filepath):
        self.file_path = Path(filepath)
        self.word_counts = {}


    #function to read teh file and count how often each word appears
    def process_file(self):

        try:   #make sure that there is a file to try 
            if not self.file_path.exists():
                raise FileNotFoundError


            with self.__filepath.open("r") as file:

                for line in file:

                    line = line.lower() #make everything lower case

                    line = line.translate(str.maketrans("", "", string.punctuation)) #remove punctuation

                    words = line.split() #split the line into words

                    #adds word to the word count 
                    for word in words:
                        if word in self.word_counts:
                            self.word_counts[word] += 1
                        else:
                            self.word_counts[word] = 1
            return True
        #message for it the file isnt found 
        except FileNotFoundError:
            print(f"File could not be found.")
            return False