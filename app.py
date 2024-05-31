import ftplib
# alireza@liliyome.com 123456789@Mf
server = ftplib.FTP()
server.connect('liliyome.com', 21)
server.login('alireza','123456789@Mf')
server.dir()
print("End")