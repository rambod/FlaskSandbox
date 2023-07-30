from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Rambod Ghashghai',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'July 30, 2023'
    },
    {
        'author': 'James Smith',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'April 27, 2023'
    }
]

@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', posts=posts, title='Home')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)