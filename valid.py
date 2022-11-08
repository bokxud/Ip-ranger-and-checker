import socket
from multiprocessing.dummy import Pool


def checker(i) :
    try :
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((i,80))
        if result == 0:
            print ('valid   == '+i)
            open('valids.txt','a').write(i+'\n')
        else:
            print ('No valid == '+i)
    except :
        pass
def main():
    ad = input('Enter ip : ')
    opp = open(ad, 'r', errors='ignore').read().splitlines()
    pp= Pool(100)
    pp.map(checker, opp)
main()