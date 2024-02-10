from flask import Flask, render_template

app = Flask(__name__, template_folder='templates' )


@app.route('/')
def base_page():
  return render_template('base.html')

def scripts_page():
  return render_template('script')

# def index():
#     return '<h1>Jello from Flask!</h1>'

# @app.route('/templates')
# def index():
#   return render_template('templates/base.html')


app.run(host='0.0.0.0', port=81)
