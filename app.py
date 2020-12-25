from flask import Flask, render_template

app = Flask(__name__)

@app.route('/welcome')
@app.route('/')
def hello_world():
    return render_template("welcome.html")


if __name__ == '__main__':
    app.run('0.0.0.0', 8085,debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)
    # Use $ export FLASK_DEBUG=1   for not rerunning it again and again.
    #flask run --port 8085     to run in debug mode.