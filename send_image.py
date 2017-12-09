import os
from os import walk
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def SendMail(ImgFileName):
    print(ImgFileName)
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'subject'
    msg['From'] = 'e@mail.cc'
    msg['To'] = 'e@mail.cc'

    text = MIMEText("Motion Images")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("bunnyeater3000@gmail.com", "xxx")
    s.sendmail("bunnyeater3000@gmail.com", "bunnyeater3000@gmail.com", msg.as_string())
    s.quit()

dir_path = os.path.dirname(os.path.realpath(__file__)) + "\img\\"

f = []
for (dirpath, dirnames, filenames) in walk(dir_path):
    file = dirpath + filenames[0]
    print(file)
    f.append(file)
    break



me = "bunnyeater3000@gmail.com"

you = "karlis.vigulis@city.ac.uk"