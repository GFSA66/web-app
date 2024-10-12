# from random import randint
# from flask import Flask, session, redirect, url_for, request, render_template
# from main_db_controll import db
# def index():
#    return render_template('main.html')
# # f'''<a href="/test">Тест №{session['quiz']}</a>'''



# def test():
#    if request.method == 'POST':
#       # print(request.form.get('first_name'))
#       obj = request.form.to_dict()
#       print(obj)
#       db.add_data(obj)
#       info = db.get_data()
#       print(info)
#       return render_template('answer.html', obj=info)
#    # obj['first_name'][0]
#    # request.form.get('first_name')
#    return 'Получил не POST запрос'

# def result():
#    return "that's all folks!"



# # Створюємо об'єкт веб-програми:
# app = Flask(__name__)  
# app.add_url_rule('/', 'index', index)   # створює правило для URL '/'
# app.add_url_rule('/test', 'test', test, methods=['POST']) # створює правило для URL '/test'
# app.add_url_rule('/result', 'result', result) # створює правило для URL '/test'
# app.config['SECRET_KEY'] = 'secret_key'

# if __name__ == '__main__':
#    # Запускаємо веб-сервер:
#    app.run(debug=True)

# obj = {'key': [1, 2, 3]}
# obj['key'][0]

from flask import Flask, session, redirect, request, url_for, render_template
from main_db_controll import db

def index():
   return render_template('main.html')

def test():
   req = request.form.to_dict(flat=True)
   db.add_data(req)
   return redirect(url_for('result'))

def result():
   info = db.get_data() 
   return render_template('answer.html', obj=info)

def delete():
   db.delete_data()
   return redirect(url_for('result'),)

def back_to_index():
   return redirect(url_for(''))

app = Flask(__name__)

app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
app.add_url_rule('/index', 'index', index, methods=['GET', 'POST'])
app.add_url_rule('/test', 'test', test, methods=['POST'])
app.add_url_rule('/result', 'result', result, methods=['GET'])
app.add_url_rule('/delete','delete',delete,methods=['POST'])

if __name__ == '__main__':
   app.run(debug=True)