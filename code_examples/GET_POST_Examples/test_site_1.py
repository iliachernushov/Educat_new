from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', city="Kursk", page=5)


@app.route('/programs/', methods=['GET', 'POST'])
def programs():
    
    try:
        print('значение текстового поля формы = ', request.form.get('text_field'))
        if request.form.get('city')=='':
            print("значение города не указано")
        else:
            print('значение выпадающего списка формы = ', request.form.get('city'))
    except:
        pass

    try:
        print('значение параметров get запроса при клике по ссылке:')
        print(request.args.get('city'))
        print(request.args.get('page'))
        print(request.args.get('word'))
    except:
        pass

    return render_template('index.html', city="Kursk", page=5)

@app.route('/sucess')
def sucess():
    return render_template('page2.html')

@app.route('/programs')
def all_news():
    for item in request.args:
        print(item)

    print(request.args.get('city'))
    return 'News'


if __name__ == "__main__":
    app.run(debug=True)
