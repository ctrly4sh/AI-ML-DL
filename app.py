from flask import Flask, render_template, request
import wikipedia

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    topic = request.form['search']
    number_of_lines = int(request.form['lines'])  
    result = wikipedia.summary(topic, sentences=number_of_lines)
    return render_template('result.html', topic=topic, result=result)

if __name__ == '__main__':
    app.run(debug=True)
