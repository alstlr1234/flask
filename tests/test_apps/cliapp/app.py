from flask import Flask, request
import openai

app = Flask(__name__)

openai.api_key = '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'

def code_review(content):
    messages = [{"role":"user","content":content}]
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    chat_response = completion.choices[0].message.content
    return chat_response

@app.route("/", methods=['GET', 'POST'])
def review():
    if request.method == 'POST':
        content = request.form['content']
        response = code_review(content)
        return response
    else:
        return '''
            <form onsubmit="submitForm(event)">
                <input type="text" id="content" name="content">
                <input type="submit" value="Submit">
            </form>
            <div id="response"></div>
            <script>
                async function submitForm(event) {
                    event.preventDefault();
                    const content = document.querySelector('#content').value;
                    const response = await fetch('/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded'
                        },
                        body: `content=${encodeURIComponent(content)}`
                    });
                    const text = await response.text();
                    document.querySelector('#response').textContent = text;
                }
            </script>
        '''
