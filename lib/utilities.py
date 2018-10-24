from lib import parameters as pars
import datetime


def setupLogFile():
    pars.logFile = (pars.logFile[:-3] + '-' + (datetime.datetime.now().strftime("%y%m%d-%Hh%M")) + '.log')
    return True


def log(message):
    if message == '':
        print(message)
        file = open(pars.logFile, 'a', encoding='utf-8')
        file.write('\n')
        file.close()
    else:
        print((datetime.datetime.now().strftime("%H:%M ")) + message)
        file = open(pars.logFile, 'a', encoding='utf-8')
        file.write((datetime.datetime.now().strftime("%H:%M ")) + message + '\n')
        file.close()
