from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL (/)
@app.route('/')
def Kumudini():
    return 'Kumudini!'

# Run the app if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
