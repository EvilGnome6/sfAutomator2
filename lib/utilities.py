from lib import parameters as pars
import datetime


def init(parameters):
    pars.logFile = (parameters['testName'] + (datetime.datetime.now().strftime("%y%m%d-%Hh%M")) + '.log')
    pars.resultsFile = pars.logFile.replace('.log', '.csv')
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


def results(results):
    if results == '':
        file = open(pars.resultsFile, 'a', encoding='utf-8')
        file.write('\n')
        file.close()
    else:
        file = open(pars.resultsFile, 'a', encoding='utf-8')
        file.write(results + '\n')
        file.close()
