'''

@generated at 21/11/2017
@author Sergio Cordedda
@version 1.0

Quest'opera è distribuita con Licenza Creative Commons Attribuzione - Non commerciale - Condividi allo stesso modo 4.0 Internazionale.

'''


#Import Dropbox SDK
import dropbox
from dropbox.files import WriteMode
from sys import argv


argument = argv # upload file that is passed as argument to the script


dbx = dropbox.Dropbox('token')

f = open(argument[1])
response = dbx.files_upload(f.read(), '/'+argument[1], mode=dropbox.files.WriteMode.overwrite)
f.close()
print 'uploaded: ', response