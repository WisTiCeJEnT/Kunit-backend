import kunit
from flask import Flask
from flask_cors import CORS
import major

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    return "I'm WORKING"

#inp = [[5,3,0,2,0,0],['01999012'],[],['01999111'],[],[]]a01999021
@app.route('/add/<inp>')
def add_to_table(inp):
    try:
        table = inp[:inp.index('a')]
        subject = inp[inp.index('a')+1:]
        listOfTable = eval(table)
        #print(lt,subject)
        return "{\"data\" : "+str(kunit.add(listOfTable,subject)).replace(" ","")+"}"
    except:
        return "invalid syntax (API Doc in -> https://github.com/WisTiCeJEnT/Kunit-backend)"
    #return "still alive"

@app.route('/remove/<inp>')
def del_from_table(inp):
    try:
        table = inp[:inp.index('d')]
        subject = inp[inp.index('d')+1:]
        listOfTable = eval(table)
        return "{\"data\" : "+str(kunit.remove(listOfTable,subject)).replace(" ","")+"}"
    except:
        return "invalid syntax (API Doc in -> https://github.com/WisTiCeJEnT/Kunit-backend)"

@app.route('/unitOf/<inp>')
def unit_of_major(inp):
    try:
        return "{\"data\" : "+str(major.unitOf(inp.lower())).replace(" ","")+"}"
    except:
        return "invalid syntax (API Doc in -> https://github.com/WisTiCeJEnT/Kunit-backend)"

@app.route('/new')
def new_data_struture(): #New KUDS
    return "[[0,0,0,0,0,0],[],[],[],[],[]]"

if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0")
