from flask import current_app as app, render_template, jsonify, request, send_from_directory
import os, subprocess, logging

def delete_images():
    current_dir = os.path.dirname(os.path.abspath(__file__)) #redirect to /app
    target_dir = os.path.dirname(current_dir) #to /models

    files_pre = os.listdir(target_dir + "\\models\\predict_image\\")
    files_pra = os.listdir(target_dir + "\\models\\preprocessed_image\\")
    if(len(files_pre) > 0 and len(files_pra) > 0):
        image_path_name_pre = os.path.join(target_dir+"\\models\\predict_image\\", files_pre[0])
        image_path_name_pra = os.path.join(target_dir+ "\\models\\preprocessed_image\\", files_pra[0])
        # Ensure the image is removed after processing
        # print(image_path_name_pra)
        if os.path.exists(image_path_name_pra):
            #print(image_path_name_pra)
            os.remove(image_path_name_pra)
        if os.path.exists(image_path_name_pre):
            #print(image_path_name_pre)
            os.remove(image_path_name_pre)

@app.route('/', methods=['GET'])
def input():
    delete_images()
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    delete_images()
    # Save the uploaded image
    image = request.files['image']
    
    current_dir = os.path.dirname(os.path.abspath(__file__)) #redirect to /app
    target_dir = os.path.dirname(current_dir) #to /models
    #print(current_dir)
    image_path = target_dir+"\\models\\predict_image\\"+image.filename
    image.save(image_path) # save image
    model_path = target_dir+"\\models\\model-classify.py"

    try:
        result = subprocess.run(
            ['python', model_path],
            check=True,
            capture_output=True,
            text=True
        )
        output = result.stdout.strip()
        print(output)
         # Kembalikan output dalam format JSON
        return jsonify(output)
        
    except subprocess.CalledProcessError as e:
       print(f"Error: {e.stderr}")
       return jsonify({'error': str(e), 'output': e.stderr}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/output', methods=['POST', 'GET'])
def output():
    attrImage = request.args.get('result', default='Unknown')
    # Remove the surrounding brackets and double quotes
    cleaned_attrImage = attrImage.strip('"')

    # Remove the backslashes
    cleaned_attrImage = cleaned_attrImage.replace('\\n', '\n')

    # Now split the cleaned string by the newline character '\n'
    arrAttr = cleaned_attrImage.split('\n')

    lung_type = arrAttr[0].strip('[]')
    print(lung_type)
    print(type(lung_type))
    probability = arrAttr[1] 
    print(type(probability))
    cross_validation_method = arrAttr[2]

    current_dir = os.path.dirname(os.path.abspath(__file__))  # redirect to /app
    target_dir = os.path.join(current_dir, "..")  # to root directory

    try:
        files_pre = os.listdir(os.path.join(target_dir, "models", "predict_image"))
        image_name_pre = files_pre[0]

        files_pra = os.listdir(os.path.join(target_dir, "models", "preprocessed_image"))
        image_name_pra = files_pra[0]

        result = {
            'lung_type': lung_type[1:-1],
            'model_accuracy': round(float(probability),2),
            'process_method': 'SVM',
            'preprocess_method': 'Laplacian',
            'cross_validation_method': cross_validation_method,
            'image_before': image_name_pre,
            'image_after': image_name_pra
        }
        return render_template('output.html', result=result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/models/predict_image/<filename>')
def serve_predict_image(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = os.path.join(current_dir, "..")  # to root directory
    directory = os.path.join(target_dir, "models", "predict_image")
    return send_from_directory(directory, filename)

@app.route('/models/preprocessed_image/<filename>')
def serve_preprocessed_image(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = os.path.join(current_dir, "..")  # to root directory
    directory = os.path.join(target_dir, "models", "preprocessed_image")
    return send_from_directory(directory, filename)