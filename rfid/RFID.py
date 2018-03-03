import RPi.GPIO as GPIO
import MFRC522

mfrc = MFRC522.MFRC522()
cardKey = [0x95, 0x35, 0xEF, 0x2B, 0x64]

def dis_CommandLine():
    print("RC522>")

def dis_CardID(cardID):
    print("%2X%2X%2X%2X%2X>"%(cardID[0], cardID[1], cardID[2], cardID[3], cardID[4]))

def setup():
    print("Program starting")

def loop():
    while(True):
        dis_CommandLine()
        inCmd = raw_input()
        print inCmd
        if(inCmd == "scan"):
            print("Scanning...")
            isScan = True
            while isScan:
                (status, TagType) = mfrc.MFRC522_Request(mfrc.PICC_REQIDL)
                if(status == mfrc.MI_OK):
                    print("Card detected")
                (status, uid) = mfrc.MFRC522_Anticoll()
                if(status == mfrc.MI_OK):
                    print("Card UID: " + str(map(hex, uid)))
                    if(mfrc.MFRC522_SelectTag(uid) == 0):
                        print("MFRC522 select tag failed")
                    if(cmdloop(uid) < 1):
                        isScan = False
        elif(inCmd == "quit"):
            destroy()
            exit(0)
        else:
            print("Unknown command\nscan: scan card and dump\nquit: exit program")

def cmdloop(cardId):
    while True:
        dis_CommandLine()
        dis_CardID(cardId)
        inCmd = raw_input()
        cmd = inCmd.split(" ")
        print(cmd)
        if(cmd[0] == "read"):
            blockAddr = int(cmd[1])
            if((blockAddr < 0) or (blockAddr > 63)):
                print("Invalid address")
            #key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
            status = mfrc.MFRC522_Auth(mfrc.PICC_AUTHENT1A, blockAddr, cardKey, cardId)
            if(status == mfrc.MI_OK):
                mfrc.MFRC522_Readstr(blockAddr)
            else:
                print(status)
                print("Authentication error")
                return 0
        elif(cmd[0] == "dump"):
            #Default key for authentication
            #key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
            mfrc.MFRC522_Dump_Str(cardKey, cardId)

        elif(cmd[0] == "write"):
            blockAddr = int(cmd[1])
            if((blockAddr < 0) or (blockAddr > 63)):
                print("Invalid address")
            data = [0]*16
            if(len(cmd) < 2):
                data = [0]*16
            else:
                data = cmd[2][0:17]
                data = map(ord, data)
                if(len(data) < 16):
                    data += [0]*(16 - len(data))
                #key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
                status = mfrc.MFRC522_Auth(mfrc.PICC_AUTHENT1A, blockAddr, cardKey, cardId)
                if(status == mfrc.MI_OK):
                    print("Before writing, the data in block %d is: "%(blockAddr))
                    mfrc.MFRC522_Readstr(blockAddr)
                    mfrc.MFRC522_Write(blockAddr, data)
                    print("After written, the data in block %d is: "%(blockAddr))
                    mfrc.MFRC522_Readstr(blockAddr)
                else:
                    print("Authentication error")
                    return 0
        elif(cmd[0] == "clean"):
            blockAddr = int(cmd[1])
            if((blockAddr < 0) or (blockAddr > 63)):
                print("Invalid address")
            data = [0]*16
            #key =[0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
            status = mfrc.MFRC522_Auth(mfrc.PICC_AUTHENT1A, blockAddr, cardKey, cardId)
            if(status == mfrc.MI_OK):
                print("Before cleaning, the data in block %d is: "%(blockAddr))
                mfrc.MFRC522_Readstr(blockAddr)
                mfrc.MFRC522_Write(blockAddr, data)
                print("After cleaned, the data in block %d is: "%(blockAddr))
                mfrc.MFRC522_Readstr(blockAddr)
            else:
                print("Authentication error")
                return 0
        elif(cmd[0] == "halt"):
            return 0
        else:
            print("Usage:\r\n\tread <blockstart>\r\n\tdump\r\n\thalt\r\n\tclean <blockaddr>\r\n\twrite <blockaddr> <data>")

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
