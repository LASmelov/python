from flask import Flask, render_template, request

def search4letters(phrase: str, letters: str='aeiou') -> set:
    return set(letters).intersection(set(phrase))

app=Flask(__name__)
@app.route('/')
def hello() -> str:
    return 'Hello world from Flask'

@app.route('/test')
def test_page()->'html':
    return render_template('test.html', the_title="Welcom")

@app.route('/test-result', methods=['POST'])
def testPost()->'html':
    your_name=request.form['your_name']
    return render_template('test-result.html',
                           your_name=your_name)

@app.route('/search4', methods=['POST'])
def do_search()->'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                        the_phrase=phrase,
                        the_letters=letters,
                        the_title=title,
                        the_results=results)
@app.route('/entry')
def entry_page()->'html':
    return render_template('entry.html', the_title="Welcom")
app.run()