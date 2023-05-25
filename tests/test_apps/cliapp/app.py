from flask import Flask, request
import openai

app = Flask(__name__)
openai.api_key = 'YOUR_API_KEY'

def process_code(code):
    response = openai.Completion.create(
        engine="davinci",
        prompt=code,
        max_tokens=150
    )
    return response['choices'][0]['text']

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        code = request.form['code']
        result = process_code(code)
    return f'''
        <form method="POST">
            <textarea name="code"></textarea>
            <input type="submit" value="Submit">
        </form>
        <div>{result}</div>
    '''

if __name__ == '__main__':
    app.run()
