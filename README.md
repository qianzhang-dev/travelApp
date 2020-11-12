# travelApp
A cross-platform travel app for logging &amp; planning travels

# Server Side Development
1. Activate Python virtual environment `source ./Server/.venv37/bin/activate`
2. Launch flask app by `flask run`
3. Create a sqlite db by `flask db init`
4. Create a new db migration by `flask db migrate -m <message>`
5. Apply chanages to db by `flask db upgrade`