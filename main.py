from flask import Flask, render_template , request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def page():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def predict():
	imageFile = request.files['imagefile']
	image_path = "./images/" + imageFile.filename
	imageFile.save(image_path)

	return render_template('index.html')
    
	


if __name__ == '__main__':
    app.run(port=3000, debug=True)
