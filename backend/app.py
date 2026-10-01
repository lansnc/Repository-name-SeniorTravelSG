from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Senior Travel SG</title>
    </head>
    <body>
        <h1>🇸🇬 Senior Travel SG</h1>
        <p>Your senior-friendly Singapore travel assistant.</p>

        <h2>Where would you like to go?</h2>

        <input type="text" placeholder="Enter destination">

        <br><br>

        <button>🚶 Walk</button>
        <button>🚌 Public Transport</button>
        <button>🚲 Cycle</button>

        <br><br>

        <button>🔍 Find Route</button>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)