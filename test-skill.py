from flask import Flask, render_template
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app. '/')

@ask.launch
def launch():
    welcome_text = render_template('welcome_text')
    return question(welcome_text)

@ask.intent('AMAZON.FallbackIntent')
def fallback():
    reprompt_text = render_template('ask_name_reprompt')
    return question(reprompt_text)

@ask.intent('TestIntent')
def test(givenfirstname):
    if givenfirstname is None:
        ask_name_text = render_template('ask_name')
        return question(ask_name_text)
        response_text = render_template('hello', firstname = givenfirstname)
        return statement(response_text).simple_card('Hello', response_text)

if __name__ == '__main__':
    app.run(debug=True)