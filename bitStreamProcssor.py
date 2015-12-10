__author__ = 'brycecater'

from bitstring import BitStream

filename = "sampleData/data_test.dat"


packetStream = []
preambleAndAddress = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,0,1,0,0,0,0,1,0,0,1,0,0,1,1,1,0]

class Packet(object):
    def __init__(self, preBits, pcBits, payloadBits):
        self.address = preBits[8:]
        self.dataLength = self.getPayloadLength(pcBits)
        print payloadBits
        self.data = payloadBits[0:self.dataLength*8]

    @staticmethod
    def getPayloadLength(pcBits):
        payloadLength = int("".join(str(i) for i in pcBits[0:6]), 2)
        return payloadLength


with open(filename, 'r') as f:
    preBits = []
    pcBits = []
    payloadBits = []
    lockIndex = 0
    lockCount = 0
    payloadLength = None

    for bitByte in f.read():
        bit = ord(bitByte)

        if lockCount == len(preambleAndAddress):
            if len(pcBits) < 9:
                pcBits.append(bit)
                continue

            if len(pcBits) == 9 and payloadLength is None:
                payloadLength = Packet.getPayloadLength(pcBits)

            if len(payloadBits) < payloadLength*8+15:
                payloadBits.append(bit)
                continue

            payloadBits.append(bit)
            packetStream.append(Packet(preBits, pcBits, payloadBits))
            preBits = []
            pcBits = []
            payloadBits = []
            lockIndex = 0
            lockCount = 0
            payloadLength = None


        if bit == preambleAndAddress[lockCount]:
            lockCount += 1
            preBits.append(bit)
        else:
            lockIndex += 1
            lockCount = 0
            preBits = []


print packetStream[0].data