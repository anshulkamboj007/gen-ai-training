import pandas as pd

def load_data(file_path):
    df1=pd.read_csv(file_path)
    df1=df1.drop(columns=['Unnamed: 0'])
    print('data loaded successfully')
    return df1

load_data(r'C:\Users\NODRS12290\Desktop\ai ml training\week_1\day_1\Salary_dataset.csv')