from flask import Flask

app = Flask(__name__,
           template_folder='templates', 
           static_folder='static'
           )


@app.route('/')
def base_page():
  return render_template('base.html')

# def index():
#     return '<h1>Jello from Flask!</h1>'


app.run(host='0.0.0.0', port=81)
