Create a file called hello.py

    from flask import Flask
    app = Flask(__name__)
 
    @app.route("/")
    def hello():
        return "Hello World!"
 
    if __name__ == "__main__":
        app.run()
        
Finally run the web app using this command:
     
     $ python hello.py
        
        * Running on http://localhost:5000/