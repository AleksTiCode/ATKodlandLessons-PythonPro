#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_modrinth = request.form.get('button_modrinth')
    button_youtube = request.form.get('button_youtube')
    button_godot = request.form.get('button_godot')
    return render_template('index.html', button_python=button_python,
                           button_modrinth=button_modrinth,
                           button_youtube=button_youtube,
                           button_godot=button_godot)

#Форма фидбэка
@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

#Обработка формы фидбэка
@app.route('/feedback', methods=['POST'])
def process_feedback():
    email = request.form.get('email')
    message = request.form.get('text')
    
    # Здесь можно добавить код для сохранения данных или отправки их по почте
    
    return render_template('feedback.html', 
                          feedback_submitted=True,
                          email=email,
                          message=message)


if __name__ == "__main__":
    app.run(debug=True)
