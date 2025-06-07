from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        news_text = request.form['news_text']
        # For demonstration, let's do a dummy prediction
        # Replace this with your actual model prediction logic
        if "fake" in news_text.lower():
            prediction = "Fake News"
        else:
            prediction = "Real News"
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
