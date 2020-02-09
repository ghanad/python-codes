from configparser import ConfigParser
from pathlib import Path
import os


TOKEN_FILE = 'tokens.ini'

class Tokens:
    def __init__(self):
        pass
    # True = continue 
    # False = create new file 
    def getUserAnswer(self, tokenFile=TOKEN_FILE):
        if os.path.isfile(tokenFile):
            user_answer = input('{} file is available. do you want to continue?[Y/N]'.format(tokenFile))
            if user_answer == 'Y' or user_answer == 'y':
                return True
            else:
                return False
        else:
            return False
    
    def touchFile(self, userAnswer):
        if userAnswer == False:
            with open(TOKEN_FILE, 'w') as tmpinifile:
                tmpinifile.write()

a = Tokens()
a.touchFile(a.getUserAnswer())