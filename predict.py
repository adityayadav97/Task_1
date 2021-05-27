import joblib
model = joblib.load("Salary__model.pkl")
#predict
exp=int(input("Enter years of experience: "))
pred=model.predict([[exp]])
print("Expected Salary is ",round(pred[0],2)," INR.")
