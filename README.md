### NOTE:
Publii has changed how it monitors files. This program may now have now real purpose. I will update if another sync failure happens. (Add 12/2/2023)

# publii_uploads
List files to be uploaded if Publii sync fails

## author
Tom Flanders

## requirements
python3

## installation
cd to the directory where you want the program to live

type:

git clone https://github.com/TomFlanders/publii_uploads

Edit the file publii_uploads.py to specify the full path to your Publii database. This is in a site's input folder by default.

## usage
cd to the publii_uploads folder

py publii_oploads.py 0

note: The zero can be any integer. This is the number of days of recent updates.

## output
Will look somethin like this

Upload these files

Tom Week

100 Words

Upload these media folders

484

485

Upload these tag folders

Tom

Writing

escape

Always upload these files

index.html

files.publii.json

## Issues
This method does not update the left navigation for older posts. Those will be corrected during the next successful sync.