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
        

FLASK Function vs View
    
    With Flask, a function is marked as a view when it is decorated by app.route.
    
method keyword argument 

    The methods keyword argument will take a list of strings as a value,
    with each string a type of possible HTTP method
    
Trailing Slash
    
    @app.route('/api/v1', methods=["GET"])
    @app.route('/api/v1/', methods=["GET"])
    def info_view():
    # blah blah blah more code