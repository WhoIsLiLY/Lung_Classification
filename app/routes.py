from flask import current_app as app, render_template, jsonify, request

@app.route('/', methods=['GET'])
def input():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    import time
    time.sleep(5)
    # Code to classify the image and get the result
    result = "Normal"  # Replace with your actual classification result
    return jsonify({'result': result})

@app.route('/output', methods=['POST', 'GET'])
def output():
    result = {
            'lung_type' : 'COVID',
            'model_accuracy' : 90,
            'pre_process_accuracy' : 30,
            'process_method' : 'CNN'
    }
    return render_template('output.html', result=result)

@app.route('/process/process-index.php', methods=['POST', 'GET'])
def process():
    return render_template('process/process-index.php')

@app.route('/classify', methods=['POST'])
def classify_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Dummy response for now, replace with your model prediction
    prediction = "cat"

    return jsonify({'message': f'Image classified as {prediction}'}), 200

# Optional: Handle GET requests with a simple form (useful for testing)
@app.route('/classify', methods=['GET'])
def classify_form():
    return '''
    <!doctype html>
    <title>Upload an Image</title>
    <h1>Upload an Image for Classification</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''
