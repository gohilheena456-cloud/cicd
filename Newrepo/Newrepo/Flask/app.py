from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'welcome to 1st page'

@app.route('/third')
def third():
    return 'welcome to 2nd page'


@app.route('/api/<name>')
def name(name):

    length = len(name)

    if length > 5:
        return 'name is too long'
    
    else:
        return 'Nice name'
    return 'welcome to 3rd page'

@app.route('/fyi/<other>')

def other(other):
    result = "hello " + other + "!"

    return result


if __name__=='__main__':
    app.run(debug=True)