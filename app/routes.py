from flask import current_app as app, render_template, url_for, request

@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('index.php')

@app.route('/process/process-index.php', methods=['POST', 'GET'])
def process():
    return render_template('process/process-index.php')