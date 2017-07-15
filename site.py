from flask import Flask, request, render_template

try:
	from db import get_programs_list
except:
	pass

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():

    try:
    	edu_programs_list = get_programs_list(30)
    except:
    	edu_programs_list = [{'name':'Первая обучающая программа', 'description':'Описание программы 1. Много букв...', 'city':'Москва', 'link':'https://www.rambler.ru/'}, {'name':'Вторая обучающая программа', 'description':'Описание программы 2. Много букв...', 'city':'Тамбов', 'link':'https://www.yandex.ru/'}]
    
    return render_template('index.html', edu_programs_list=edu_programs_list)


if __name__ == "__main__":
    app.run(debug=True)
