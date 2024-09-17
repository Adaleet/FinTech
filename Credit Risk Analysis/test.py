from flask import Flask

# Create the Flask app instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return "Welcome to the Credit Risk API"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
