import sqlite3
import datetime
import calendar
import sys

# UPDATE THIS BEFORE USING
dbLoc = "C:\\Users\\tom\\Documents\\Publii\\sites\\tom-flanders-stuff\\input\\db.sqlite"

try:
    back = sys.argv[1]
except:
    back = 0

#get date
today = datetime.date.today()
backDate = today - datetime.timedelta(days=int(back))
compTime = calendar.timegm(backDate.timetuple()) * 1000

#connect to database
con = sqlite3.connect(dbLoc)
cur = con.cursor()

#list pages updated within range
sql_query = 'select id,title from posts where modified_at > ' + str(compTime) + ';'

result = cur.execute(sql_query)

records = cur.fetchall() 
rowCount = len(records) 
if rowCount == 0: 
    print("\nThere are no updates in specified time period\n")
    exit() 

sql_query = 'select title from posts where modified_at > ' + str(compTime) + ';'
result = cur.execute(sql_query)

print("\nUpload these files")
for row in result:
    print(row[0])

sql_query = 'select id from posts where modified_at > ' + str(compTime) + ';'
result = cur.execute(sql_query)

print("\nUpload these media folders")
for row in result:
    print(row[0])

#list tag folders updated within range
print("\nUpload these tag folders")
sql_query = 'select name from tags where tags.id in (select tag_id from posts_tags where post_id in (select id from posts where modified_at > ' + str(compTime) + '));'
for row in cur.execute(sql_query):
    print(row[0])

#list files that always need uploading
print("\nAlways upload these files\nindex.html\nfiles.publii.json\n")
