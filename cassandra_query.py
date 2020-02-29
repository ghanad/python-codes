from configparser import ConfigParser
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor 
import os
import logging


TOKEN_FILE = 'tokens.ini'
INI_GROUP_NAME = 'tokens'
LOG_FILE_NAME = 'info.log'
TOKEN_NUMBER = 100000

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler_streamer = logging.FileHandler('logfile.log')
# Console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
handler_streamer.setFormatter(formatter)
logger.addHandler(handler_streamer)


class Tokens:
    def __init__(self, tokenNumber=None, tokenFile=None, GroupName=None):
        self.tokenFile = tokenFile
        self.GroupName = GroupName
        self.tokenNumber = tokenNumber

    def checkFileExist(self):
        if os.path.exists(self.tokenFile):
            user_answer = input('{} file is available. do you want to continue?[Y/N]'.format(self.tokenFile))
            if user_answer == 'Y' or user_answer == 'y':
                return self.loadINIfile()
            else:
                logger.info('Remove old {} file'.format(self.tokenFile))
                os.remove(self.tokenFile)
                tDict = self.tokenCreator()
                self.saveToINI(tDict)
                return self.tokenCreator()
        else:
            tDict = self.tokenCreator()
            self.saveToINI(tDict)
            return self.tokenCreator()

    def tokenCreator(self):
        rangeList = dict()
        start = -9223372036854775808
        end = 9223372036854775807
        startRange = start
        rangeSize = int((end - start) / self.tokenNumber)
        for num,i in enumerate(range(0, self.tokenNumber)):
            endRange = startRange + rangeSize
            if i == (self.tokenNumber - 1):
                endRange = end
            rangeList['{},{},{}'.format(num, startRange, endRange)] = 'None'
            startRange = endRange  
        return rangeList

    def loadINIfile(self):
        config = ConfigParser()
        config.read(self.tokenFile)
        return {k:v for k,v in config.items(self.GroupName)}

    def saveToINI(self, token, status='None'):
        if isinstance(token, (int, str)):
            token_dict = dict()
            token_dict[token] = status
            self._saveHelper(token_dict)        
        elif isinstance(token, dict):
            self._saveHelper(token)
        elif isinstance(token, list):
            token_dict = dict()
            token_dict = {k:'None' for k in token}
            self._saveHelper(token_dict)

    def _saveHelper(self, tokenDictionary):
        config = ConfigParser()
        config.read(self.tokenFile)
        if not config.has_section(self.GroupName):
            config.add_section(self.GroupName)
        for key,value in tokenDictionary.items():
            config.set(self.GroupName, key, value)
            logger.info('token_{} status= {} saved to file'.format(key, value))
        try:
            with open(self.tokenFile, 'w') as configfile:
                config.write(configfile)
            
        except Exception as err:
            logger.error('could not save token to file. {}'.format( err ))



class query:
    pass

def worker():
    pass


if __name__ == "__main__":
    a = Tokens(TOKEN_NUMBER, TOKEN_FILE, INI_GROUP_NAME)
    tokensDict = a.checkFileExist()
#     noneTokenList = [x for x in tokensDict.keys()  if tokensDict[x] != 'Success']
#     with ProcessPoolExecutor(max_workers=10) as executor:
#         executor.map(worker, noneTokenList)