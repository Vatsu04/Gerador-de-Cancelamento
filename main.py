from flask import Flask, request
import random 

app = Flask(__name__)

cancelamento = ['ser gostoso(a) demais', 'ser homofóbico', 'ser otaco fedido', 'ser Paulista', 'ser debochado', 'ser fanatico por politico', 'ser fanatico religioso', 'falar muita merda no twitter', 'ser tik toker', 'usar Reddit não ironicamente', 'ser antivacina', 'tomar banho de chinelo','ser bolsominion']

@app.route('/')
def index():  
  name = request.args.get('nome')
  message = ''
  if name:
    cancelar = random.choice(cancelamento)
    message = f'{name} foi cancelado por {cancelar}'

  return f'''
  <h1>Gerador de cancelamento</h1>
  <hr>
  <div align ="center">
   <form>
     Nome:
     <input type="text"
     name="nome"/>
     <input type="submit"
     value="Enviar" />
  </form>
  <p>{message}</p>

<div/>
'''
app.run(debug=True, host='0.0.0.0', port='8888')



idx = random.randint(0, len(cancelamento)-1)

print(cancelamento[idx])
