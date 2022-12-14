import pandas as pd
from sklearn import preprocessing
import joblib

df_test = pd.read_csv('datasets\\hospitalizaciones_test.csv', delimiter=',', encoding="utf-8")
df_test = df_test.drop(columns=['patientid','Visitors with Patient'])

E = preprocessing.LabelEncoder()

E.fit(df_test['Type of Admission'])
df_test['Type of Admission'] = E.transform(df_test['Type of Admission'])

E.fit(df_test['Severity of Illness'])
df_test['Severity of Illness'] = E.transform(df_test['Severity of Illness'])

E.fit(df_test.health_conditions)
df_test.health_conditions = E.transform(df_test.health_conditions)

E.fit(df_test.Insurance)
df_test.Insurance = E.transform(df_test.Insurance)

E.fit(df_test.Department)
df_test.Department = E.transform(df_test.Department)

E.fit(df_test.Ward_Facility_Code)
df_test.Ward_Facility_Code = E.transform(df_test.Ward_Facility_Code)

E.fit(df_test.doctor_name)
df_test.doctor_name = E.transform(df_test.doctor_name)

E.fit(df_test.Age)
df_test.Age = E.transform(df_test.Age)

E.fit(df_test.gender)
df_test.gender = E.transform(df_test.gender)

DecisionTree_model = joblib.load('Modelo.pkl')
X_test = df_test[['staff_available','Severity of Illness','Available Extra Rooms in Hospital','Department','Ward_Facility_Code','doctor_name','Age','gender','Admission_Deposit']]
pred = DecisionTree_model.predict(X_test)
df_test['pred'] = pred
df_test = df_test['pred']
df_test.to_csv('Nefuulus.csv', index=False)