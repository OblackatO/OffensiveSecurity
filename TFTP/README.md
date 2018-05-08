## Get_Banners.py 
### **Description:**
Gets the banners of the hosts which have ports 21,22 or 23 opened.
The banners will be saved in a txt file in the current folder.
The user can then use the banners to get the hosts' names and finally use them in Get_Backup.py. See the script for more details.

## Get_Backup.py
### **Description:**
If there are tftp services on the network, the script looks for backup files on hosts that have (21 || 22 || 23) services on. 
Often administrators do back-ups using the TFTP service(ot they used to) appending to the name of the host to be backed-up a '-' or '_' following the number of the backup. For example : SSH_serverD_01. This program will try to download those back-up files using the names the user specify that were previously obtained using the Get_Banners.py program



