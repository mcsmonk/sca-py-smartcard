
from scasc import scasc
from lecroywin32com import LeCroyScope
from lecroysocket import LeCroyScope


def main():
    sc = scasc()
    sc.set_sc_reader()
    sc.connect()
    sc.print_ATR()
    sc.select_DF()
    data, sw1, sw2 = sc.get_ENCIPHER_APDU(list(range(32)))
    data, sw1, sw2 = sc.get_RESPONSE_APDU(sw2)
    sc.disconnect()


if __name__ == '__main__':
    main()
