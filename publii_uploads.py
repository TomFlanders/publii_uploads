import sqlite3
import datetime
import calendar
import sys

# UPDATE THIS BEFORE USING
dbLoc = "C:\\Users\\tom\\Documents\\Publii\\sites\\tom-flanders-stuff\\input\\db.sqlite"

#get number of days back
back = sys.argv[1]

#get date
today = datetime.date.today()
compTime = calendar.timegm(today.timetuple()) * 1000

#connect to database
con = sqlite3.connect(dbLoc)
cur = con.cursor()

#list pages updated within range
sql_query = 'select id,title from posts where modified_at > ' + str(compTime) + ';'
print("\nUpload these files")
for row in cur.execute(sql_query):
    print(row[1])

print("\nUpload these media folders")
for row in cur.execute(sql_query):
    print(row[0])

#list tag folders updated within range
print("\nUpload these tag folders")
sql_query = 'select name from tags where tags.id in (select tag_id from posts_tags where post_id in (select id from posts where modified_at > ' + str(compTime) + '));'
for row in cur.execute(sql_query):
    print(row[0])

#list files that always need uploading
print("\nAlways upload these files\nindex.html\nfiles.publii.json\n")