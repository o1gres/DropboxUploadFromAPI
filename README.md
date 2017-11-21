# DropboxUploadFromAPI

This script allow to upload file to DropBox using API Oauth2.

------------------------------------------------------------------------------------------------------------------------------

HOW TO USE

1) Create a Dropbox account https://www.dropbox.com
2) Go to https://www.dropbox.com/developers and "Create your app"
3) Select Dropbox API > Full dropbox and choose a name for yuor applicaion > "Create App"
4) Create a token into "Generated access token" section.

IMPORTANT!!! the token generaten into the step 4 give access to your dropbox, DON'T SHARE IT

5) Download the file dropboxUploadAPI.py from this repository
6) Change the string 'token' with the token generated at the step 4th "dbx = dropbox.Dropbox('token')"
7) Run the script: python /path/dropboxUploadAPI.py /path/fileToUpload.ext

N.B. It's necessary install the last version of dropbox SDK using pip 

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Licenza Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/80x15.png" /></a><br />Quest'opera è distribuita con Licenza <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribuzione - Non commerciale - Condividi allo stesso modo 4.0 Internazionale</a>.
