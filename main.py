from flask import *
app = Flask(__name__)

def remove_new_line(data):
    # return data.replace('\n','')
    return "".join(data.splitlines())

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        indata = ''
        outdata = ''
    else:
        indata = request.form['input']
        outdata = remove_new_line(indata)

    html = render_template('index.html', indata = indata, outdata = outdata)
    return html

if __name__ == '__main__':
    app.run(debug=True)
