#!/usr/bin/python3
include sqlite3
#
#load cosmetics from a configuration file***********************
#
#get working directory********************************
#
#eventually a list will be used... so here.
somelist=[]
connection = sqlite3.connect("test.db")
argline = connection.cursor()
#
#
#i assume execute only takes string info to run sql things on... so we use string (:
#args should eventually be variable taking input as the user wishes to use or to be taken from********
#some configuration file defining common tasks to do
args = ''
#
#
#sqlite data types for py will be
#string = text
#int = integer
#float = real
#binary = blob
#
argline.execute("create table testTable(year integer, titles int)")
# ^^^^^ start passing commands
#
#dont sql inject pls. do a batch insert (for speed, zoom!)
#each "?" is a placeholder for eventual list data to be put into the tables.
#the table only has 2 columns in it so 2 ? should be used to place the things that should pop
#those columns
argline.executemany("insert into testTable values(?,?)",someList)
#
#check working directory for any db file, if no file then create file**********************
#
#if file do not create db and simply open connection on present db file*******************
#
#start doing sql things**********************************
#
#dont be a fool<<<<<<<
connection.close()
#dont be a fool<<<<<<<
