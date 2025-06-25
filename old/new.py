import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
print("CODE RUNNING SUCCESSFULLY")
def cleanData(fileName):
    iaq = pd.read_excel(fileName)
    iaq['DateTime'] = iaq['Date'].astype(str) + ' ' + iaq['Time'].astype(str)
    iaq['DateTime'] = pd.to_datetime(iaq['DateTime'], errors='coerce')
    iaq = iaq.drop(['Date', 'Time'], axis=1)
    print(iaq.head())   
    print(iaq.describe())
    iaq.to_excel('iaq_sorted.xlsx', index=False)

def sort(fileName):
    iaq = pd.read_excel(fileName)
    iaq = iaq.sort_values(by='DateTime', ascending=True)
    iaq.to_excel('oaq_sorted1.xlsx', index=False)

def missing(fileName):
    iaq = pd.read_excel(fileName)
    iaq.replace('No CT', np.nan, inplace=True)
    iaq.replace('###', np.nan, inplace=True)
    print(iaq.isnull().sum())

def usableRange(fileName):
    iaq = pd.read_excel(fileName)
    iaq.replace('No CT', np.nan, inplace=True)
    iaq.replace('###', np.nan, inplace=True)
    
    iaq['DateTime'] = pd.to_datetime(iaq['DateTime'], errors='coerce')
    non_missing_rows = iaq[iaq.notnull().all(axis=1)]
    
   
    non_missing_rows = non_missing_rows.sort_values('DateTime')
    
    
    usable_ranges = []
    start_date = non_missing_rows['DateTime'].iloc[0]
    end_date = start_date

    for i in range(1, len(non_missing_rows)):
        current_date = non_missing_rows['DateTime'].iloc[i]
        if (current_date - end_date).seconds > 3600:  
            usable_ranges.append((start_date, end_date))
            start_date = current_date
        end_date = current_date

    
    usable_ranges.append((start_date, end_date))

    if usable_ranges:
        print("Usable ranges of datetime (no missing values):")
        print(len(usable_ranges))
        for start, end in usable_ranges:
            print(f"{start} to {end}")
    else:
        print("No rows with complete data found.")

    
def mergeExcel(file1, file2, file3):
    df1 = pd.read_excel('file1.xlsx')
    df2 = pd.read_excel('file2.xlsx')
    
    # Convert timestamp columns to datetime format
    df1['timestamp'] = pd.to_datetime(df1['timestamp'])
    df2['timestamp'] = pd.to_datetime(df2['timestamp'])
    

    # Merge based on exact timestamps
    merged_df = pd.merge(df1, df2, on='timestamp', how='inner')
    
def boxplot(filename, column):
    
    df = pd.read_excel(filename)
    df = df.iloc[:50]
    for co in df.columns:
        print(co)
    plt.figure(figsize=(8, 6))
    sns.boxplot( data=df, y=column, x = "testo 160 IAQ_51616135_outdoor [ppm]")
    plt.title('Boxplot of Temperature')
    plt.ylabel(column)
    plt.show()
   
def main():
    boxplot("Merged.xlsx", "testo 160 IAQ_51616135_outdoor [°C]")
    #cleanData("OAQ.xlsx")
    #cleanData("ENERGYDATA.xlsx")
    
    
    
if __name__ == "__main__":
    main()