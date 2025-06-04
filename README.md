
# 🛒 Customer Behavior Predictor

A **Flask-based web application** that predicts whether a customer will make a purchase based on various behavioral and demographic features. This project uses a **Logistic Regression** model trained with customer purchase data.

---

## 📌 Overview

This web app allows users to input customer details like age, income, and time spent on a website and receive a prediction on whether the customer is likely to make a purchase.
It integrates **Flask** for the backend, **Pandas** and **Scikit-learn** for data processing and modeling, and a **simple HTML** interface for user input.

---

## 🚀 Features

* 🔢 **Input Features**:

  * Age
  * Gender
  * Annual Income
  * Number of Purchases
  * Product Category
  * Time Spent on Website
  * Loyalty Program Status
  * Discounts Availed

* 📈 **Prediction Output**:

  * Displays whether the customer **WILL** or **WILL NOT** make a purchase.

* ⚙️ **Model Details**:

  * Logistic Regression with:

    * `StandardScaler` for numerical feature scaling.
    * `LabelEncoder` for categorical feature encoding.

* 🌐 **Web Interface**:

  * Simple form-based input.
  * Instant results displayed after submission.

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/customer-purchase-prediction.git
cd customer-purchase-prediction
```

### 2. Set Up Virtual Environment (Recommended)

```bash
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install flask pandas scikit-learn
```

### 4. Prepare Dataset

Ensure `customer_purchase_data.csv` is in the project root directory (same location as `app.py`).

---

## 🧪 Usage

### 1. Run the Application

```bash
python app.py
```

The app will start at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### 2. Use the Web Interface

Fill out the form fields:

* **Age:** e.g., `40`
* **Gender:** `0` for Female, `1` for Male
* **Annual Income:** e.g., `66120.26`
* **Number of Purchases:** e.g., `8`
* **Product Category:** e.g., `0`
* **Time Spent on Website:** e.g., `30.56`
* **Loyalty Program:** `0` (No), `1` (Yes)
* **Discounts Availed:** e.g., `5`

Click **Predict** to see the result.

---

## 📁 Project Structure

```
customer-purchase-prediction/
├── app.py                      # Flask application
├── index.html                  # HTML form for input
├── customer_purchase_data.csv  # Dataset
├── README.md                   # Project documentation                       
```

---

## 📊 Dataset Description

| Column             | Description                    |
| ------------------ | ------------------------------ |
| Age                | Customer's age                 |
| Gender             | 0 = Female, 1 = Male           |
| AnnualIncome       | Annual income in dollars       |
| NumberOfPurchases  | Number of past purchases       |
| ProductCategory    | Product category ID            |
| TimeSpentOnWebsite | Time spent in minutes          |
| LoyaltyProgram     | 0 = Not enrolled, 1 = Enrolled |
| DiscountsAvailed   | Count of discounts used        |
| **PurchaseStatus** | Target: 0 = No, 1 = Yes        |

---

## 🧠 Model Details

* **Algorithm**: Logistic Regression
* **Preprocessing**:

  * `LabelEncoder` for categorical features
  * `StandardScaler` for numerical features
* **Split**: 80% train / 20% test (`random_state=42`)
* **Parameters**: `max_iter=1000`

---

## ⚠️ Limitations

* No input validation for incorrect types (e.g., text in numeric fields).
* Basic frontend — could be improved with CSS or frameworks like **Bootstrap**.
* Model trained on a static dataset — not optimized for real-time or changing trends.

---

## 📈 Future Improvements

* ✅ Add input validation and user feedback for errors
* 💅 Improve frontend design and UX
* 💾 Save and load model using `pickle` to avoid retraining
* 📉 Display model evaluation metrics (accuracy, precision, recall)
* 🤖 Add support for multiple models and comparisons



---

## 📄 License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for more details.

---

## 📬 Contact

Have questions or suggestions?
Open an issue on GitHub or email: **[your-email@example.com](mailto:your-email@example.com)**

---
