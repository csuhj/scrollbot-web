from flask import Flask, render_template, request
import scrollphathd as sphd
import time
import threading

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

scrollName= ['Hello']

def startScroll():
    sphd.rotate(180)
    scrollThread = threading.Thread(target = scroll, args = (scrollName, ))
    scrollThread.start()

def scroll(scrollTextArray):
    
    while True:
        scrollText = scrollTextArray[0] + '   '
        sphd.clear()
        sphd.write_string(scrollText, brightness=0.3)
        
        for xPos in range(len(scrollText) * 6):
            sphd.show()
            sphd.scroll(1)
            time.sleep(0.02)

def reverseLettersInWords(text):
    reversedText = ''
    words = text.split()
    for word in words:
        reversedWord = word[::-1]
        reversedText += reversedWord + ' '
    
    return reversedText

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<name>')

def hello(name):
    scrollName[0] = 'Hello '+name
    return render_template('hello.html', name=name)

@app.route('/hello')
def helloFromForm():
    name = request.args.get('name')
    return hello(name)

@app.route('/secret')
def secret():
    text = request.args.get('text')
    secretText = reverseLettersInWords(text)
    return render_template('secret.html', text=text, secretText=secretText)

@app.route('/recipe')
def recipe():
    return render_template('recipe.html')

@app.route('/more-activities')
def moreActivities():
    return render_template('more-activities.html')

@app.route('/more-recipes')
def moreRecipes():
    return render_template('more-recipes.html')

@app.route('/useful-links')
def usefulLinks():
    return render_template('useful-links.html')

@app.route('/dinosaurs')
def dinosaurs():
    return render_template('dinosaurs.html')

if __name__ == '__main__':
    startScroll()
    app.run(debug=False, host='0.0.0.0', port=int('80'))
