__author__ = 'brycedcarter'

filename = "sampleData/data_test.dat"

packetStream = []  # this will contain the final list of packet objects

# this is the preamble and address that should be used for matching a valid packet
preambleAndAddress = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0,
                      1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0]


# Class to represent data packets
class Packet(object):
    def __init__(self, preBits, pcBits, payloadBits):
        self.address = preBits[8:]
        self.dataLength = self.getPayloadLength(pcBits)
        self.data = payloadBits[0:self.dataLength * 8]

    # TODO implement use of the rest of the packet control bits other than just the packet length

    # TODO implement CRC check

    @staticmethod
    def getPayloadLength(pcBits):  # gives the payload length given a set of (9) packet control bits
        payloadLength = int("".join(str(i) for i in pcBits[0:6]), 2)
        return payloadLength


# Open the target file and start reading bits out of it
with open(filename, 'r') as f:
    preBits = []  # this holds the set of preamble and address bits
    pcBits = []  # this holds the packet control bits
    payloadBits = []  # this holds the payload and crc bits
    lockIndex = 0  # this is the index below which we know there is no data or the data has already been processed
    lockCount = 0  # this is the index of the preamble and address stream that we have match up to... if this reached the length of the preamble and address it means that we have successfully matched a packet
    payloadLength = None  # this is the length of the payload read from the pc bits

    for bitByte in f.read():
        bit = ord(bitByte)  # the newest bit read from the file

        if lockCount == len(
                preambleAndAddress):  # if we have matched the full preamble and address then we can collect the rest of the packet bits
            if len(pcBits) < 9:  # read 9 bits into the set of packet control bits
                pcBits.append(bit)
                continue  # don't move on with processing until we have all of the pc bits

            if len(
                    pcBits) == 9 and payloadLength is None:  # if we have all of the pc bits but have not determined the length of the payload, do so...
                payloadLength = Packet.getPayloadLength(pcBits)

            if len(payloadBits) < payloadLength * 8 + 15:  # collect the payload and the crc bits
                payloadBits.append(bit)
                continue

            payloadBits.append(bit)  # grab the last straggler bit that was missed by the last if

            packetStream.append(Packet(preBits, pcBits, payloadBits))  # build a packet and add it to the packet stream

            # reset all of the buffers and indexes to look for the next buffer
            preBits = []
            pcBits = []
            payloadBits = []
            lockIndex = 0
            lockCount = 0
            payloadLength = None


        # if we did not continue on the loop before, try to match the current position of the preamble and address
        if bit == preambleAndAddress[lockCount]:
            lockCount += 1
            preBits.append(bit)
        # if we cant match it... reset and start again
        else:
            lockIndex += 1
            lockCount = 0
            preBits = []

print packetStream[0].data  # print the data of the first packet
