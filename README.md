# JaaneKhabar_kiSachae: Real-time News Detection System

## Project Overview
JaaneKhabar_kiSachae is a machine learning-based web application designed to detect fake and real news articles in real-time. It uses natural language processing (NLP) techniques along with multiple machine learning algorithms to classify news content accurately.

The system leverages datasets of labeled fake and real news, applies TF-IDF vectorization, and trains models such as Logistic Regression, Decision Tree, Random Forest, SVM, and XGBoost to achieve the best classification performance.

## Features
- Upload news text and instantly classify it as Fake or Real.
- Multiple ML models for comparison of accuracy.
- Interactive and user-friendly web interface built with Flask.
- Real-time prediction with fast response.
- Easily extensible to include more models or datasets.

## Technologies Used
- Python 3.x
- Flask (Web framework)
- Scikit-learn (Machine Learning)
- Pandas, NumPy (Data processing)
- NLTK (Text preprocessing)
- XGBoost
- HTML, CSS, Bootstrap (Frontend UI)

## Project Structure
![image](https://github.com/user-attachments/assets/460ccee0-143a-40b4-b674-3347c74a026b)


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Rishabh30062003/janneKhabbar_kiSachae.git
   cd janneKhabbar_kiSachae
2. Create and activate a virtual environment
python -m venv env
source env/bin/activate
3. Install dependencies:
   pip install -r requirements.txt

## Usage

1. Run the Flask application:
python app.py
2. Open your web browser and go to:
http://127.0.0.1:5000
3. Input any news text in the form and get the prediction whether the news is Fake or Real.

## Dataset
The datasets used (Fake.csv and True.csv) are large and not included in the repository due to GitHub file size limits.
You can download them from https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset
Place the datasets in the dataset/ folder if you want to retrain models.

## Model Training
The models were trained on the combined dataset using TF-IDF vectorization.
Trained models are saved as .pkl files in the model/ directory.
You can retrain the models by running the training script.

## Screenshot of visual results and home page
![Screenshot 2025-06-07 163009](https://github.com/user-attachments/assets/8c13ad27-a783-4eee-aab4-e2f1d1c50aef)
![Screenshot 2025-06-07 162938](https://github.com/user-attachments/assets/f6958463-be9c-4fbb-8194-935a61457be1)
![Screenshot 2025-06-07 162849](https://github.com/user-attachments/assets/41a25536-945f-4111-9499-0479e7806086)

## Notes
Large files like datasets and environment folders are excluded from the repo using .gitignore.
If you face any issues with package versions, check the requirements.txt file.
For deploying on a live server, additional configurations may be needed.

## Contact
If you have any questions or suggestions, feel free to reach out:
GitHub: Rishabh30062003
Email: rishavkumarjajauli@gmail.com

