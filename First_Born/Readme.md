# KeyLogger_CC.py
## **Description**

First of all note that I did this keylogger when I was a begginer in python and in hacking, years ago. 
It is here because it is my very first malware, my very first born, and I learned many things while developping it.
At the end of the description a list may be found containing what I would have done better, if I wrote it today.

It all started when I tried to transfer the cookies of Mozilla FireFox from one friend's computer 
to mine manually. We both noticied that the cookies were encrypted, but when I opened the browser in my PC using his cookies I could see them anyway, because suprisingly the browser did not recognize that those were not my cookies. I tried this with different browsers, on different OSs , and more surprisingly yet, the same thing happened, cookies from anyone from a browser X could be opened in within that browser X interface (but not in plain text) on any computer. 

This meant that if I went to configurations and checked for saved passwords for instance, I would see any password that the user saved in his browser, only having the small size file of its cookies && saved password file, which was also stored in the same folder of the cookies file for all the tested browsers. 

I also noticed that some information such credit card numbers were stored in cookies, perhaps not the information of credit cards, but information if the credit cards were already stored for a Y website. For instance if you shop online, you do not need to type your credit card number by hand if it is stored already. On the site DB ? On the browser cookies file ? I did not know, but what I knew is that, if the cookies file was deleted one had to reinput the credit card information again, this was several times tested, even for amazon.

Finally I thought about this keylogger. 

In the 1st phase it would check for the OS of the victim, and the installed browsers. 

In the 2nd phase it would then try to gain persistence, so when the victim logs-off/shuts down the system the keylogger keeps listen for key strokes when the new login happens. 

In the 3th and last phase phase, the keylogger uploaded the cookies' files of the installed browsers to a ftp server, and delete them on the machine afterwards to force the victim to input again his credit card information when he/she buys something online. 

When he/she buys something online the keylogger would recognize that a credit card number was tapped using regex expressions. The keylogger is adapted for the following credit cards : 
    American Card
    Mastercard 
    Visa card
    Diners Club(3 different type of cards)
    Discover (2 different type of cards)
    JBCcard (3 different types)

Note that the 3 || 4 digits required to make payments online would also be recorded. Furthermore, the expiration date of the card as well, using an approximation to the current date because most sites give the option to select the month and year of expiration date using a selection list.

Apart from all this, the keylogger worked also as stealer (1st phase), and I would get all the saved password/information on the browsers installed in the victim's machine.

### **A few points that I have done better/changed today (10th april 2018):**

1st of all, I would have not, at all, written a malware with so poor functionalities. With some adaptations, the idea behind this keylogger could be perhaps 5% of a decent malware. Here are some things that I would have done (differently || changed)

...

I would have used OOP, and treat every victim has an object. (a struct in case of a none OOP languages like C)

I would have written proper logging functions

I would have put in place a C2C to change the behaviour of the malware or get additional information of the victim if needed. 

I would have encrypted all the gathered information and I would not kept it in the victim's machine, instead I would upload it directly to either a ftps || encrypted anonymous cloud|| some other victim's machine || ...

I would have built a network with the infected victims and treat them as zombies, to make for instance DDoS attacks. (Using the C2C to launch a DDoS attack on demand)

I would have used other programming languages to write the different phases of the attack, for instance javascript to spread the malware, or C to write the whole malware instead of python.

I would have have taken in consideration processing management && rights to make sure the malware would stay undectected, with the necessary right to run.

I would have added automatical spread functions in the internal network of the victim && on the rest of the internet using the victim's machine.


...The list goes on.
    




