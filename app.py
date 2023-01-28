from flask import Flask, render_template
import openai
from googletrans import Translator

translator = Translator()

app = Flask(__name__)

def buscar_usuarios(username, userid):
    usuarios = []
    users = open("users.txt", "r+", encoding='Utf-8', newline='')
    for user in users:
        user = user.strip(",")
        usuarios.append(user.split())
    for usuario in usuarios:
        user = usuario[0]
        id = usuario[1]
        if username == user and id == userid:
            return True

def gerar(received_oqdisse):
    oqdisse = received_oqdisse.replace('-', " ")
    
    openai.api_key = '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'
    test = oqdisse
    translate = translator.translate(test, dest = 'en')
    translated = translate.text
    def generate_prompt(oqdisse):
        return str('generate a rude sentence for a person who said to me ' + oqdisse)

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=generate_prompt(translated),
    temperature=1.2,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
        presence_penalty=0
    )
    translate = translator.translate(response.choices[0].text, dest = 'pt')
    translated = translate.text

    return str('<h3>' + translated + '</h3>')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/como_funciona')
def how_it_works():
    return render_template('comofunciona.html')

@app.route('/gerador/<username>/<userid>/<oqdisse>')
def gerador(username, userid, oqdisse):
    user = buscar_usuarios(username, userid)
    if user == True:
        return gerar(oqdisse)
    elif user == 'user_pass-id_notpass':
            return '<p>O Usuário está correto, porém o ID não! Tente novamente. Caso o erro persista, entre em contato com um administrador.</p>'
    elif user == 'user_notpass':
        return '<p>O Usuário está incorreto! Tente novamente. Caso o erro persista, entre em contato com um administrador.</p>'

@app.route('/new/adm/kg-MuskitoMan2401/<username>/<userid>')
def new_user(username, userid):
    user = buscar_usuarios(username, userid)
    if user == True:
        return '<p>Este usuário já existe!</p>'
    else:
        users = open("users.txt", "a+", encoding='Utf-8', newline='')
        users.writelines(f'{username} {userid}\n')
        return '<p>Cadastro aprovado!</p>'
        
if __name__ == "__main__":
    app.run(debug=True)
