from configparser import ConfigParser
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor 
import os


TOKEN_FILE = 'tokens.ini'
INI_GROUP_NAME = 'tokens'

class Tokens:
    def __init__(self, tokenNumber, tokenFile=TOKEN_FILE, GroupName=INI_GROUP_NAME):
        self.tokenFile = tokenFile
        self.GroupName = GroupName
        self.tokenNumber = tokenNumber

    def checkFileExist(self):
        if os.path.exists(self.tokenFile):
            user_answer = input('{} file is available. do you want to continue?[Y/N]'.format(self.tokenFile))
            if user_answer == 'Y' or user_answer == 'y':
                return self.loadINIfile()
            else:
                os.remove(self.tokenFile)
                for k,v in self.tokenCreator().items():
                    self.saveToINI(k,v)
                # print(self.tokenCreator())
                return self.tokenCreator()
        else:
            for k,v in self.tokenCreator().items():
                    self.saveToINI(k,v)
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
            # rangeList.append('{},{},{}'.format(startRange, endRange,num))
            rangeList['{},{},{}'.format(num, startRange, endRange)] = 'None'
            startRange = endRange  
        return rangeList

    def loadINIfile(self):
        config = ConfigParser()
        config.read(self.tokenFile)
        return {k:v for k,v in config.items(self.GroupName)}

    def saveToINI(self, token, status):
        config = ConfigParser()
        config.read(self.tokenFile)
        if not config.has_section(self.GroupName):
            config.add_section(self.GroupName)
        config.set(self.GroupName, token, status)
        with open(self.tokenFile, 'w') as configfile:
            config.write(configfile)

# a = Tokens(100)
# tokensDict = a.checkFileExist()

def testfunction(a):
    print('{}   {}'.format(os.getpid(), a))



if __name__ == "__main__":
    a = Tokens(100)
    tokensDict = a.checkFileExist()
    noneTokenList = [x for x in tokensDict.keys()  if tokensDict[x] != 'Success']
    with ProcessPoolExecutor(max_workers=10) as executor:
        executor.map(testfunction, noneTokenList)