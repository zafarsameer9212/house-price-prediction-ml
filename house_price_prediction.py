# House Price Prediction using Machine Learning
# Author: Muhammad Zafar Sameer

# 1. Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 2. Create Dataset
# You can later replace this with CSV data
data = {
    'Area': [800, 1200, 1500, 2000, 2500],
    'Bedrooms': [2, 3, 3, 4, 4],
    'Price': [50000, 75000, 95000, 130000, 150000]
}

df = pd.DataFrame(data)

# 3. Split Features and Target
X = df[['Area', 'Bedrooms']]  # Inputs
y = df['Price']               # Output

# 4. Split into Train and Test Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Create Linear Regression Model
model = LinearRegression()

# 6. Train the Model
model.fit(X_train, y_train)

# 7. Make Predictions
y_pred = model.predict(X_test)

# 8. Evaluate the Model
score = r2_score(y_test, y_pred)
print("R² Score:", score)

# 9. Test Prediction
new_house = [[1800, 3]]  # Area = 1800, Bedrooms = 3
predicted_price = model.predict(new_house)
print("Predicted Price for house:", predicted_price[0])
