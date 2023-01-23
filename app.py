import openai
from googletrans import Translator
from os import system, name

translator = Translator()

oqdisse = input('Digite o que a pessoa te disse: ')

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
def clear():
   # for windows
   if name == 'nt':
      _ = system('cls')

   # for mac and linux
   else:
      _ = system('clear')

clear()

print(translated)
