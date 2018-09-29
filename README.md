# Plant-Search-Engine

This plant engine uses a flask based web interface to host a website which acts as a search engine for searching plants.

The underlying algorithm uses inverted index with term frequency - inverse document frequency.

To execute this run 
FLASK_APP=webapp.py flask run

To run the script as a development server which is suitable for debugging
FLASK_APP=webapp.py FLASK_ENV=development flask run

After executing the above lines go to http://127.0.0.1:5000 and enjoy!
