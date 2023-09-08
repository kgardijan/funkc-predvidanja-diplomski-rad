import pandas as pd
import os

file_path= 'nba_data_processed.csv'
if os.path.exists(file_path):
    data= pd.read_csv(file_path)
    print("File found")
else: 
    print(f"File not found.")

try:
    data = pd.read_csv('nba_data_processed.csv')
    data.fillna(value=0, inplace=True)
    print("Rows without values modified")

    data.drop_duplicates(inplace=True)
    print("Duplicates droped")

    data=pd.get_dummies(data, columns=['Pos'])
    data=pd.get_dummies(data, columns=['Tm'])
    print("Categorical data modified")

    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    data[data.columns] = scaler.fit_transform(data[data.columns])

    data.to_csv('processed_nba_data.csv', index=False)
    print("Data modified and saved")

except Exception as e:
    print(f"An error occurred: {str(e)}")




