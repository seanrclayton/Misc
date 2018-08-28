import requests
import smtplib
import os.path

fromaddr = 'seancvolusion@gmail.com'
toaddrs  = 'sean.r.clayton@gmail.com'
msg = requests.get('http://icanhazip.com').text
username = 'seancvolusion@gmail.com'
password = '********'

fname = '/home/clayton/ip.txt'

if os.path.isfile(fname):
  ip = open(fname,'r').read()
  print(ip)
  if ip == msg:
    print('ip is the same')
  else:
    print(msg)
    rename = open(fname, 'w')
    rename.write(msg)
    rename.close()

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

