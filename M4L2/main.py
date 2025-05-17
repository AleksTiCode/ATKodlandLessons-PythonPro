#Импорт
from flask import Flask, render_template, request, redirect, session
#Подключение библиотеки баз данных
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#Подключение SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Создание db
db = SQLAlchemy(app)
# Secret key for session
app.secret_key = 'your_secret_key_here'

#Создание таблицы
class Card(db.Model):
    #Создание полей
    #id
    id = db.Column(db.Integer, primary_key=True)
    #Заголовок
    title = db.Column(db.String(100), nullable=False)
    #Описание
    subtitle = db.Column(db.String(300), nullable=False)
    #Текст
    text = db.Column(db.Text, nullable=False)
    #Автор
    author = db.Column(db.Integer, nullable=False)

    #Вывод объекта и id
    def __repr__(self):
        return f'<Card {self.id}>'
    

#Задание №1. Создать таблицу User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)


#Запуск страницы с контентом
@app.route('/', methods=['GET','POST'])
def login():
        error = ''
        if request.method == 'POST':
            form_login = request.form['email']
            form_password = request.form['password']
            
            users_db = User.query.all()
            for user in users_db:
                if form_login == user.login and form_password == user.password:
                    # Store user ID in session
                    session['user_id'] = user.id
                    return redirect('/index')
            
            # If we get here, no user matched
            error = 'Неправильно указан пользователь или пароль'
            return render_template('login.html', error=error)
        else:
            return render_template('login.html')



@app.route('/reg', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        login= request.form['email']
        password = request.form['password']
        
        #Задание №3. Реализовать запись пользователей
        user = User(login=login, password=password)
        db.session.add(user)
        db.session.commit()        

        
        return redirect('/')
    
    else:    
        return render_template('registration.html')


#Запуск страницы с контентом
@app.route('/index')
def index():
    # Check if user is logged in
    if 'user_id' not in session:
        return redirect('/')
    
    # Get only cards created by the current user
    user_id = session['user_id']
    cards = Card.query.filter_by(author=user_id).order_by(Card.id).all()
    return render_template('index.html', cards=cards)

#Запуск страницы c картой
@app.route('/card/<int:id>')
def card(id):
    # Check if user is logged in
    if 'user_id' not in session:
        return redirect('/')
    
    card = Card.query.get(id)
    
    # Check if the card belongs to the current user
    if card.author != session['user_id']:
        return redirect('/index')
        
    return render_template('card.html', card=card)

#Запуск страницы c созданием карты
@app.route('/create')
def create():
    # Check if user is logged in
    if 'user_id' not in session:
        return redirect('/')
    return render_template('create_card.html')

#Форма карты
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    # Check if user is logged in
    if 'user_id' not in session:
        return redirect('/')
        
    if request.method == 'POST':
        title = request.form['title']
        subtitle = request.form['subtitle']
        text = request.form['text']
        
        # Get the current user's ID from the session
        user_id = session['user_id']

        #Создание объкта для передачи в дб
        card = Card(title=title, subtitle=subtitle, text=text, author=user_id)

        db.session.add(card)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('create_card.html')

# Add logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)