from urllib.request import urlopen as html
print('''\033[31;1m
  ____    _    ____   _____           _
 |  _ \  (_)  / ___| |_   _|__   ___ | |
 | | | | | | | |  _    | |/ _ \ / _ \| |
 | |_| | | | | |_| |   | | (_) | (_) | |
 |____/  |_|  \____|   |_|\___/ \___/|_|
\033[0m''')
print("\033[32;1m[!]Dark Information Gathering Tool for Web Application Pentesting ^_^ by D4rk h7ml")
def usage():
    print("\033[32;1m[+]Choose Method from List eg: 1 or 2 or 3")
    print("\033[32;1m[-]Enter target site name without http or https")
def id():
    print("\033[36;1mwww.facebook.com/uiddarkhtml")
    print("\033[36;1mwww.darkerror.net")
    print("\033[36;1mwww.youtube.com/DarkError")
    print("\033[36mGreetz:All muslim hackers")
    print("\033[36;1m~Nothing is True,Everything is permitted~")
id()
def menu():
    print("\033[34;1m [1]Whois Lookup")
    print("\033[34;1m [2]Port Scan")
    print("\033[34;1m [3]Geo Ip")
    print("\033[34;1m [4]DNS lookup")
    print("\033[34;1m [5]Subnet Calc..")
    print("\033[34;1m [6]Subdomains")
    print("\033[34;1m [7]Link Crawlers")
    print("\033[34;1m [8]Traceroute")
    print("\033[34;1m [9]Exit")
menu()
def who():
    domain = input("\033[34mEnter Site Name plz:")
    who =("http://api.hackertarget.com/whois/?q="+domain)
    wip =html(who).read().decode('utf-8')
    print(wip)
def ip():
    site = input("\033[32mEnter Site Name plz:")
    nip =("http://api.hackertarget.com/nmap/?q="+site)
    pip = html(nip).read().decode('utf-8')
    print(pip)
def sub():
    subi =input("\033[36mEnter site name plz:")
    subl =("https://api.hackertarget.com/hostsearch/?q="+subi)
    subo =html(subl).read().decode('utf-8')
    print(subo)
def geo():
    geoi =input("\033[31mEnter site name plz:")
    geol =("https://api.hackertarget.com/geoip/?q="+geoi)
    geoo =html(geol).read().decode('utf-8')
    print(geoo)
def mtr():
    mtri =input("\033[32mEnter site name plz:")
    mtrl =("https://api.hackertarget.com/mtr/?q="+mtri)
    mtro =html(mtrl).read().decode('utf-8')
    print(mtro)
def subnet():
    snti =input("\033[33mEnter site name plz:")
    sntl =("https://api.hackertarget.com/subnetcalc/?q="+snti)
    snto =html(sntl).read().decode('utf-8')
    print(snto)
def dlook():
    dli =input("\033[34mEnter site name plz:")
    dll =("http://api.hackertarget.com/dnslookup/?q="+dli)
    dlo =html(dll).read().decode('utf-8')
    print(dlo)
def crwl():
    cli =input("\033[36mEnter site name plz:")
    cll =("https://api.hackertarget.com/pagelinks/?q="+cli)
    clo =html(cll).read().decode('utf-8')
    print(clo)
methods = input("\033[37mInput Methods plz:")
if methods== "1":
   who()
elif methods== "2":
   ip()
elif methods== "3":
   geo()
elif methods== "4":
   dlook()
elif methods== "5":
   subnet()
elif methods== "6":
   sub()
elif methods== "7":
   crwl()
elif methods== "8":
   mtr()
if methods== "9":
   print("./ Exit Success ")

   
