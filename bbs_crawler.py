# -*- coding: utf-8 -*-

import getpass
import sys
import telnetlib
import os
import re

p = re.compile("[0-9]/[0-9]")
print p.match('�� 1/3 ��')

HOST = "ptt2.cc"
user = "gsrr"
password = "1128"

tn = telnetlib.Telnet(HOST)

tn.read_until("�п�J�N��")
tn.write(user + "\r\n")
if password:
    tn.read_until("�п�J�z���K�X: ")
    tn.write(password + "\r\n")

print "login ok"
tn.read_until("�Ы����N���~��")
tn.write("\r\n")
tn.read_until("�I�s��")
tn.write("sWebMining\r\n")
#tn.read_until("�Ы����N���~��")
#tn.write("\r\n")
tn.read_until("�i�O�e��")
article_id = raw_input("Enter article id: ")
while True:
    tn.write(article_id + "\r\n")
    tn.write("r")
    fw = open(article_id , 'w')
    while True:
        line = tn.read_some()
        print line
        fw.write(line)
        fw.flush()
        print p.search(line)
        if p.search(line) != None:
            page = p.search(line).group()
            print "page:" , page
            member = page.split("/")[0]
            dominator = page.split("/")[1]
            print member , dominator
            if member != dominator:
                tn.write("\006")
            else:
                fw.close()
                tn.write("q")
                break
    tn.read_until("�i�O�e��")
    article_id = raw_input("Enter article id: ")

    


