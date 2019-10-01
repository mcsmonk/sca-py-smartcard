
from smartcard.System import readers
from smartcard.util import toHexString
from config import *

class scasc:
    
    def __init__(self):
        self.set_reader = False
        self.set_connect = False
    
    def set_sc_reader(self):
        r = readers()
        r2 = ['%2d : %s' % (i,j) for i,j in zip(range(len(r)),r)]
        print('sc readers:')
        for i in r2:
            print(i)
        rn = int(input('Enter number of reader for connection : '))
        if rn < 0 or rn > len(r)-1 :
            print('Error : inccorect reader number')
            return
        self.reader = r[rn].createConnection()
        self.set_reader = True

    def connect(self):
        if self.set_reader:
            if self.set_connect == False:
                self.reader.connect()
                self.set_connect = True
            else:
                print('Error : Already connected')
        else:
            print('Error : need te set sc reader')

    def disconnect(self):
        if self.set_reader:
            if self.set_connect == True:
                self.reader.disconnect()
                self.set_connect = False
            else:
                print('Error : not connected')
        else:
            print('Error : need te set sc reader')

    def print_ATR(self):
        atr = self.reader.getATR()
        print('ATR : ', ['%02X' % i for i in atr])

    def print_APDU(self, apdustr, apdu):
        apdu1 = apdu[0:5]
        apdu2 = apdu[5:]
        print(apdustr, ':', end=' ')
        print(''.join(['%02X' % i for i in apdu1]), end=' ')
        print(''.join(['%02X' % i for i in apdu2]))

    def print_APDU2(self, apdu):
        apdu1 = apdu[0:5]
        apdu2 = apdu[5:]
        print(''.join(['%02X' % i for i in apdu1]), end=' ')
        print(''.join(['%02X' % i for i in apdu2]))

    def print_DATAwithSW(self, datastr, data, sw1, sw2):
        print(datastr, ':', end=' ')
        if len(data) > 0:
            print(''.join(['%02X' % i for i in data]), end=' ')
        print('%02X%02X' % (sw1, sw2))

    def print_DATAwithSW2(self, data, sw1, sw2):
        if len(data) > 0:
            print(''.join(['%02X' % i for i in data]), end=' ')
        print('%02X%02X' % (sw1, sw2))

    def send_APDU_lc(self, apdu):
        print('>> ', end='')
        self.print_APDU2(apdu)
        ins = apdu[0:5]
        data = apdu[5:]
        l = int(ins[-1])
        if l != len(data):
            print('Error : inccorect APDU')
            print('\t -> ', end='')
            self.print_APDU('APDU', apdu)
            return
        data, sw1, sw2 = self.reader.transmit(apdu)
        print('>> ', end='')
        self.print_DATAwithSW2(data, sw1, sw2)
        return data, sw1, sw2

    def send_APDU_le(self, apdu):
        print('>> ', end='')
        self.print_APDU2(apdu)
        apdu = apdu[0:5]
        data, sw1, sw2 = self.reader.transmit(apdu)
        print('>> ', end='')
        self.print_DATAwithSW2(data, sw1, sw2)
        return data, sw1, sw2

    '''
    def select_DF(self):
        print('>> ', end='')
        self.print_APDU('selectDF', SELECTDF)
        data, sw1, sw2 = self.send_APDU_lc(SELECTDF)
        print('<< ', end='')
        # self.print_DATAwithSW('response', data, sw1, sw2)
        self.print_DATAwithSW2(data, sw1, sw2)

    def get_ENCIPHER_APDU(self, text):
        GE = GETENCIPHER + [len(text)] + text
        print('>> ', end='')
        self.print_APDU('getEncipher', GE)
        data, sw1, sw2 = self.send_APDU_lc(GE)
        print('<< ', end='')
        # self.print_DATAwithSW('response', data, sw1, sw2)
        self.print_DATAwithSW2(data, sw1, sw2)
        return data, sw1, sw2
        
    def get_RESPONSE_APDU(self, length):
        GR = GETRESPONSE + [length]
        print('>> ', end='')
        self.print_APDU('getResponse', GR)
        data, sw1, sw2 = self.send_APDU_le(GR)
        print('<< ', end='')
        # self.print_DATAwithSW('response', data, sw1, sw2)
        self.print_DATAwithSW2(data, sw1, sw2)
        return data, sw1, sw2
    '''

