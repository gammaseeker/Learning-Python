from flask import Flask, render_template, redirect, url_for
from flask import *
from forms import MyForm
import re
import operator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somekey'
#output=0
def countChar(text):
    return len(list(text))

def countWords(text, delim):
    delim = delim + '| '
    text_list= re.split(delim, text)
    return len(text_list)

def freq(text, delim):
    delim = delim + '| '
    text_list= re.split(delim, text)
    table={}
    for item in text_list:
        if(item in table):
            table[item] = table[item]+1
        else:
            table[item] = 1
    sorted_output = sorted(table.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_output[0:5]

@app.route('/', methods=['GET', 'POST'])
def index():
    output = 0
    form = MyForm()
    if form.validate_on_submit():
        text = form.text_input.data
        delim = form.delimiter.data
        operation = form.the_choices.data
        if (not text or not operation):
            return redirect(url_for('result', operationname='error'))
        #print(text, delim, operation)
        if(operation == 'countChar'):
            output=countChar(text)
        else:
            if(operation == 'countWord'):
                output=countWords(text, delim)
            else:
                if(operation == 'freq'):
                    output = freq(text, delim)
                else:
                    return redirect(url_for('result', operationname='error'))

        session['value'] = output
        return redirect(url_for('result', operationname=operation))
    return render_template('index.html', form=form) 

@app.route("/result/<operationname>", methods=['GET', 'POST'])
def result(operationname):
   if(operationname=='error'):
       return render_template('result.html', output = 'Error') 
   return render_template('result.html', output = session.get('value', None)) 

@app.errorhandler(403)
def forbidden(error):
    return render_template('403.html'), 403

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    #db.session.rollback()
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()
    #app.run(debug=True)
