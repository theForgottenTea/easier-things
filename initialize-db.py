#!/usr/bin/python3
include sqlite3
#
#load cosmetics from a configuration file***********************
#
confile=open("config.txt", "r", encoding="utf-8")
readed =confile.read()
conflist=[]
conflist.append(readed)
#dont be a fool<<<<<<<<<<
confile.close()
#dont be a fool<<<<<<<<<<
somelist=[]
connection = sqlite3.connect("test.db")
sqlcursor = connection.cursor()
#
#
args = ''
#sqlite data types for py will be
#string = text
#int = integer
#float = real
#binary = blob
sqlcursor.execute("create table testTable(year integer, titles string)")
argline.executemany("insert into testTable values(?,?)",someList)
#dont be a fool<<<<<<<
connection.close()
#dont be a fool<<<<<<<
