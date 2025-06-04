from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pickle

app = Flask(__name__)

# Load and preprocess your dataset (only once)
file_path = r"customer_purchase_data.csv"
df = pd.read_csv(file_path) 

target_column = 'PurchaseStatus' 
X = df.drop(columns=[target_column])
y = df[target_column]

label_encoders = {}
for col in X.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

if y.dtype == 'object':
    y = LabelEncoder().fit_transform(y)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = LogisticRegression(random_state=42, max_iter=1000) 
model.fit(X_train, y_train)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    try: 
        user_input = {
            'Age': float(request.form['Age']), 
            'Gender': int(request.form['Gender']),
            'AnnualIncome': float(request.form['AnnualIncome']),
            'NumberOfPurchases': int(request.form['NumberOfPurchases']),
            'ProductCategory': int(request.form['ProductCategory']),
            'TimeSpentOnWebsite': float(request.form['TimeSpentOnWebsite']),
            'LoyaltyProgram': int(request.form['LoyaltyProgram']), 
            'DiscountsAvailed': int(request.form['DiscountsAvailed']), 
        }  

        user_df = pd.DataFrame([user_input]) 
        user_scaled = scaler.transform(user_df)

        prediction = model.predict(user_scaled)

        result = "Customer <strong style='color: green;'>WILL</strong> make a purchase." if prediction[0] == 1 else "Customer <strong style='color: red;'>WILL NOT</strong> make a purchase."

        styled_html = f"""
        <html> 
        <head>
            <title>Prediction Result</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f9f9f9;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center; 
                    height: 100vh;
                }}
                .result-box {{
                    background-color: #fff;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                    text-align: center;
                }}
                h2 {{
                    color: #333;
                }}
                a {{ 
                    margin-top: 20px;
                    display: inline-block;
                    padding: 10px 20px;
                    background-color: #007bff;
                    color: white;
                    text-decoration: none;
                    border-radius: 6px;
                }}
                a:hover {{
                    background-color: #0056b3;
                }}
            </style>
        </head>
        <body>
            <div class="result-box">
                <h2>Prediction Result:</h2> 
                <p>{result}</p>
                <a href="/">Try Again</a>
            </div>
        </body>
        </html>
        """
        return styled_html

    except Exception as e:
        return f"<h3 style='color:red;'>Error occurred: {str(e)}</h3><br><a href='/'>Back</a>"
if __name__ == '__main__':
    app.run(debug=True) 