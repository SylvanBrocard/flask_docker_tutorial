from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    # handle the POST request
    if request.method == 'POST':
        texte = request.form.get('texte')
        return '''<h1>Your text was: {}</h1>'''.format(texte)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Your text is: <input type="text" name="texte"></label></div>
               <input type="submit" value="Submit">
           </form>'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
