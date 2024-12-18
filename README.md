# farmer-project-KNN
                                             𝐅𝐚𝐫𝐦𝐞𝐫-𝐏𝐫𝐨𝐣𝐞𝐜𝐭-𝐊𝐍𝐍

This repository contains a Flask web application that predicts farming outcomes using the K-Nearest Neighbors (KNN) algorithm. The project was developed during a 45-day training program and is a practical example of integrating machine learning with web development.

𝐓𝐚𝐛𝐥𝐞 𝐨𝐟 𝐂𝐨𝐧𝐭𝐞𝐧𝐭𝐬
Project Overview
Features
Installation
How to Run the Project
Project Structure
Usage
Technologies Used
Contributing
License

𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐎𝐯𝐞𝐫𝐯𝐢𝐞𝐰
Using a machine learning model (KNN), this project predicts farming outcomes based on various inputs. The application is built with Flask for the backend, and the model is trained using a dataset of farming features.

𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬
Predict farming outcomes based on user inputs.
Simple web interface using Flask.
Data preprocessing and KNN model training included.


𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐚𝐭𝐢𝐨𝐧
𝐏𝐫𝐞𝐫𝐞𝐪𝐮𝐢𝐬𝐢𝐭𝐞𝐬
Python 3. x
Git

𝑬𝒏𝒗𝒊𝒓𝒐𝒏𝒎𝒆𝒏𝒕 𝑺𝒆𝒕𝒖𝒑
𝑪𝒍𝒐𝒏𝒆 𝒕𝒉𝒆 𝒓𝒆𝒑𝒐𝒔𝒊𝒕𝒐𝒓𝒚:: git clone https://github.com/devankitkumar/farmer-project-KNN.git
cd farmer-project-KNN

𝐂𝐫𝐞𝐚𝐭𝐞 𝐚 𝐯𝐢𝐫𝐭𝐮𝐚𝐥 𝐞𝐧𝐯𝐢𝐫𝐨𝐧𝐦𝐞𝐧𝐭:: python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

𝐈𝐧𝐬𝐭𝐚𝐥𝐥 𝐝𝐞𝐩𝐞𝐧𝐝𝐞𝐧𝐜𝐢𝐞𝐬:: pip install -r requirements.txt


𝐇𝐨𝐰 𝐭𝐨 𝐑𝐮𝐧 𝐭𝐡𝐞 𝐏𝐫𝐨𝐣𝐞𝐜𝐭
𝐑𝐮𝐧 𝐭𝐡𝐞 𝐅𝐥𝐚𝐬𝐤 𝐚𝐩𝐩𝐥𝐢𝐜𝐚𝐭𝐢𝐨𝐧:
python app.py

𝐀𝐜𝐜𝐞𝐬𝐬 𝐭𝐡𝐞 𝐚𝐩𝐩𝐥𝐢𝐜𝐚𝐭𝐢𝐨𝐧: 𝐎𝐩𝐞𝐧 𝐲𝐨𝐮𝐫 𝐛𝐫𝐨𝐰𝐬𝐞𝐫 𝐚𝐧𝐝 𝐠𝐨 𝐭𝐨 𝐡𝐭𝐭𝐩://𝟏𝟐𝟕.𝟎.𝟎.𝟏:𝟓𝟎𝟎𝟎/

𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐒𝐭𝐫𝐮𝐜𝐭𝐮𝐫𝐞
app.py: The main Flask application file handles routes and integrates the KNN model.
fetch_data.py: Script for loading and preprocessing data from the CSV file.
newnotebook.ipynb: Jupyter notebook for data exploration, model training, and evaluation.
farmer.csv: Dataset containing features for model training.
home.html: HTML template for the homepage of the web app.
requirements.txt: List of Python libraries required to run the project.

𝐔𝐬𝐚𝐠𝐞
Enter farming-related input data in the web form on the home page.
Submit the form to receive predictions based on the KNN model.
View the result on the same page.


𝐓𝐞𝐜𝐡𝐧𝐨𝐥𝐨𝐠𝐢𝐞𝐬 𝐔𝐬𝐞𝐝
Flask: For the web framework.
Scikit-learn: For implementing the KNN algorithm.
Pandas, NumPy: For data handling.
HTML/CSS: For the front end.


Contributing
Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License - see the LICENSE file for details.

