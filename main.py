from flask import *
import json
import xml.dom.minidom

app = Flask(__name__)

def remove_new_line(data):
    # return data.replace('\n','')
    return "".join(data.splitlines())

####################################
#改行を削除
####################################
@app.route('/', methods=['GET', 'POST'])
def linedata():
    if request.method == 'GET':
        indata = ''
        outdata = ''
    else:
        indata = request.form['input']
        outdata = remove_new_line(indata)

    html = render_template('lineindex.html', indata = indata, outdata = outdata)
    return html

####################################
#jsonを整形
####################################
@app.route('/json', methods=['GET', 'POST'])
def jsondata():
    if request.method == 'GET':
        indata = ''
        outdata = ''
    else:
        indata = request.form['input']
        if indata != "":
            data = json.loads(indata)
            outdata = json.dumps(data, indent=2)
        else:
            outdata = ""

    html = render_template('jsonindex.html', indata = indata, outdata = outdata)
    return html

####################################
#xmlを整形
####################################
@app.route('/xml', methods=['GET', 'POST'])
def xmldata():
    if request.method == 'GET':
        indata = ''
        outdata = ''
    else:
        indata = request.form['input']
        if indata != "":
            indata = indata.replace(' ', '')
            print("-----------------------")
            print(indata)
            data = xml.dom.minidom.parseString(indata)
            outdata = data.toprettyxml(indent="  ")
            print("-----------------------")
            print(outdata)
        else:
            outdata = ""

    html = render_template('xmlindex.html', indata = indata, outdata = outdata)
    return html

if __name__ == '__main__':
    app.run(debug=True)
