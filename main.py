# loading dataset
import pandas as pd
data=pd.read_csv("Salary_Data.csv")
print("Dataset has been loaded ...")
# Creating features and target.
feature=data[["YearsExperience"]]
target=data["Salary"]
# loading LinearRegression
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(feature,target)
print("Model has been created ...")
# Now, our model has been trained
# Saving model
import joblib
joblib.dump(model,'Salary__model.pkl')
print("MODEL SAVED SUCCESSFULLY IN WORKSPACE ...")
