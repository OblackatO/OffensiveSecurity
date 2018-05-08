from ftplib import FTP 
0 - ftpi = FTP_TLS(host,user,passwd....) : connect with TLS security
0.1 ftpi.proto_p() : data in the connection gets secured
1:OK-FTP(host='', user='', passwd='', acct=\
	'', timeout=None, source_address=None)
source_address : tuple option, a source address and b destination port 

2:OK- FTP.getwelcome() : get welcome message from the server once connection is estasblished

3- FTP.abort() : aborts file transfer, sometimes does not work, but it's worth trying.

4- FTP.retrlines(cmd, callback=None)
Retrieve a file or directory listing in ASCII transfer mode. cmd should be an 
appropriate RETR command (see retrbinary()) or a command such as LIST or NLST 
(usually just the string 'LIST'). LIST retrieves a list of files and information 
about those files. NLST retrieves a list of file names. The callback function is 
called for each line with a string argument containing the line with the trailing 
CRLF stripped. The default callback prints the line to sys.stdout.

5- FTP.retrbinary(cmd, callback, blocksize=8192, rest=None)
cmd : command, should be : "RETR filename"
blocksize : specifies the maximum chunk size to read 
rest : Not import I guess 
 
6-FTP.storbinary(cmd, fp, blocksize=8192, callback=None, rest=None) :OK
Store a file in binary transfer mode. cmd should be an appropriate STOR command: 
"STOR filename". fp is a file object (opened in binary mode) which is read until 
EOF using its read() method in blocks of size blocksize to provide the data to be 
stored. The blocksize argument defaults to 8192. callback is an optional single 
parameter callable that is called on each block of data after it is sent. rest means
the same thing as in the transfercmd() method.

7-FTP.storlines(cmd, fp, callback=None)
Store a file in ASCII transfer mode. cmd should be an appropriate STOR command 
(see storbinary()). Lines are read until EOF from the file object fp 
(opened in binary mode) using its readline() method to provide the data to be stored. callback is an optional single parameter callable that is called on each line after it is sent.

8- FTP.mlsd(path="", facts=[])
List a directory in a standardized format by using MLSD command (RFC 3659). If path 
is omitted the current directory is assumed. facts is a list of strings representing
the type of information desired (e.g. ["type", "size", "perm"]). Return a generator
object yielding a tuple of two elements for every file found in path. First element
is the file name, the second one is a dictionary containing facts about the file 
name. Content of this dictionary might be limited by the facts argument but server
is not guaranteed to return all requested facts.

9- FTP.dir(argument[, ...])
Produce a directory listing as returned by the LIST command, printing it to standard 
output. The optional argument is a directory to list (default is the current server 
directory). Multiple arguments can be used to pass non-standard options to the 
LIST command. If the last argument is a function, it is used as a callback function 
as for retrlines(); the default prints to sys.stdout. This method returns None.

10-FTP.rename(fromname, toname)
Rename file fromname on the server to toname.

11-FTP.delete(filename) :OK
Remove the file named filename from the server. If successful, returns the text of 
the response, otherwise raises error_perm on permission errors or error_reply on 
other errors.

12-FTP.cwd(pathname)
Set the current directory on the server.

13-FTP.mkd(pathname)
Create a new directory on the server.

14-FTP.pwd()
Return the pathname of the current directory on the server.

15-FTP.rmd(dirname)
Remove the directory named dirname on the server.

16-FTP.size(filename)
Request the size of the file named filename on the server. On success, the size of 
the file is returned as an integer, otherwise None is returned. Note that the SIZE 
command is not standardized, but is supported by many common server implementations.

17-FTP.quit()
Send a QUIT command to the server and close the connection. This is the “polite” way to 
close a connection, but it may raise an exception if the server responds with an 
error to the QUIT command. This implies a call to the close() method which renders 
the FTP instance useless for subsequent calls (see below).

FTP.close()
Close the connection unilaterally. This should not be applied to an already closed 
connection such as after a successful call to quit(). After this call the FTP 
instance should not be used any more (after a call to close() or quit() you 
cannot reopen the connection by issuing another login() method).