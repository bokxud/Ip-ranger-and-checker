import socket
from multiprocessing.dummy import Pool


def checker(i) :
    try :
        ip_hada = i.split('.')
        for kin in range(0,255) :
            new = '{0}.{1}.{2}.{3}'.format(ip_hada[0],ip_hada[1],ip_hada[2],str(kin))
            print(new)
            open('ip_ranged.txt','a').write(new+'\n')
    except :
        pass
def main():
    ad = input('Enter ip : ')
    opp = open(ad, 'r', errors='ignore').read().splitlines()
    pp= Pool(100)
    pp.map(checker, opp)
main()