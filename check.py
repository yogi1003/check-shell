from requests import get, exceptions
import argparse
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

parser = argparse.ArgumentParser(description='Check Your Shell')
parser.add_argument('infile', type=str, help='List Name')
parser.add_argument('-r', '--replace', help='Save and Replace List', action='store_true')
args = parser.parse_args()

try:
    #x = input('your file: ')
    file = open(args.infile, "r")
except:
    print("CHECK YOUR FILE")
    exit()
###############################
nr = "\033[0;37m"
gr = "\033[1;32m"
red = "\033[1;31m"
###############################
fail = 0
success = 0
isi = []
#file = open('shell-10.txt', 'r')
lines = file.readlines()
for line in lines:
    ganti = line.replace("\n", "")
    if len(ganti) < 3:
        continue
    try:
        cek = get(ganti, headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"}, verify=False)
        if cek.status_code == 200:
        #    isi.append(line)
        #    print(line, "success")
            if cek.text.lower().find('shell') > 1 or cek.text.lower().find('anonsec') > 1:
                print(f"{ganti} -> {cek.status_code} {gr}success{nr}")
                success+=1
                isi.append(line)
            else:
                print(f"{ganti} -> {red}EXPIRED{nr}")
                fail+=1
        else:
            print(f"{ganti} -> {cek.status_code} {red}fail{nr}")
            fail+=1
    #except exceptions.ConnectionError:
    #    print('CEK KONEKSINYA!!')
    #    break
    except KeyboardInterrupt:
        print("\nTERIMA KASIH >///<")
        break
    except Exception as ex:
        print(f"{ganti} -> {cek.status_code} {red}{ex}{nr}")
        fail+=1
file.close()
print(f"success     = {gr}{success}{nr}")
print(f"fail        = {red}{fail}{nr}")
if args.replace:
	hasil = open(args.infile, 'w')
	hasil.writelines(isi)
	hasil.close()
else:
	sinmpan = input('simpan? y/t: ')
	if sinmpan == 'y':
		hasil = open(input('result: '), 'a+')
		hasil.writelines(isi)
		hasil.close()
