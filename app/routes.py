from flask import current_app as app, render_template, url_for

@app.route('/')
def home():
    return render_template('index.html')
