#Apa Tod Mau Recode?
#Tinggal Pake aja ribet_-
import os,sys,time
from time import sleep

def load(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./12)
os.system('clear')
sleep(1)
os.system("chmod 777 Add-button.py")
os.system("pkg install figlet")
os.system('clear')
os.system("figlet -f small HomeTermux")
banner = """
\033[90m==============================================
\n\x1b[1;100m\x1b[1;97m* Creator \x1b[1;96m:\x1b[1;100m Md.SomRaAt Hossain[Black Hacker]\x1b[1;97m\n\x1b[1;93m* \x1b[1;96mSupport \x1b[1;91m: \x1b[1;97mBD Cyber Hacker TeM\x1b[1;96m\x1b[1;97m/ \x1b[1;96m\n\x1b[1;97m* \x1b[1;97mGitHub  \x1b[1;91m: \x1b[1;92m\x1b[4mhttps://github.com/StHackerFake424\x1b[0m\n\033[1;33m[INFO]\033[1;37mThis Tool Made For Just To Add Default Button   In your Termux Home Enjoy Now..\n==============================================
"""
print (banner)
print('\n\033[90m[\033[1;91m!\033[90m] \033[1;96mRetrieving File Default Termux\033[1;97m')
sleep(1)
load("\033[90m[\033[1;92m•\033[90m] \033[1;96mLoading\033[90m............\033[1;97m")
sleep (2)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print('\033[90m[\033[1;92m+\033[90m] \033[1;92mSuccess\033[1;97m')
sleep(2)
print('\n\033[90m[\033[1;91m!\033[90m] \033[1;96mTermux Add Button\033[1;97m')
sleep(1)
load("\033[90m[\033[1;92m•\033[90m] \033[1;96mLoading\033[90m............\033[1;97m")

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
xmanz = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
xmanz.write(key)
xmanz.close()
sleep (2)
os.system('termux-reload-settings')
print ("\033[90m[\033[1;92m+\033[90m] \033[1;92mSuccess\033[1;97m")
sleep (2)
tod = input("\033[90mSubscribe To Channel Admin?\033[1;96m (y/t)\033[90m: \033[1;96m")
if tod == "y":
   print ("\033[90m[\033[1;91m!\033[90m] \033[1;96mWaiting\033[90m...\033[1;97m")
   sleep (2)
   os.system("xdg-open https://www.youtube.com/c/HackerFake424")
   sleep (4)
   print ("\033[90m[\033[1;92m+\033[90m]\033[1;92m Thanks You Brothers\033[90m:)\033[1;97m")
elif tod == "t":
     print ("\033[90m[\033[1;91m!\033[90m]\033[1;91mExit\033[1;97m")
     sleep (1)
     sys.exit()
