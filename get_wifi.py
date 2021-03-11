import os

sum = ""
a = 1

os.system('netsh wlan show interfaces > tmp')
file_1 = open("tmp", "r+")
data = file_1.readlines()

for i in data[19]:
    a += 1
    if a > 30:
        sum += i

sum_mod =  sum.strip()

os.system(f'netsh wlan show profile {sum_mod} key=clear > data.txt')








