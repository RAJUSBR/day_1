
import os
import pandas as pd
file1=os.path.join (os.getcwd(),'processing','diabetes_1.csv')
file2=os.path.join (os.getcwd(),'processing','diabetes_2.csv')

class DiabeticsData:
    """This is basic class to merge two dataframes and get some basic\
        statics when combine the two files
    Parameters:
    arg1 (str): path of the first file
    arg2 (str):path of second file   
  
    Returns:
    int: Returns mean, meadian, max ans minimum values    
    """          
    def __init__(self,file1,file2) :
        self.file1=file1
        self.file2=file2
        
    #Reading the files    
    def reading_files(self):
        global df2
        global df1
        df1=pd.read_csv(self.file1)
        df2=pd.read_csv(self.file2) 
        print("reading completed")
        return df1,df2
        
    def merging_data(self):
        self.reading_files()
        global df
        df=df1.merge(df2,how='outer')
        return df
        print('Merge Completed')
    def statistics(self):
        self.merging_data()
        total_pregnancies=df['Pregnancies'].sum()
        total_DiabetesPedigreeFunction= df['DiabetesPedigreeFunction'].count()
        mean=df['Pregnancies'].mean()
        median=df['Pregnancies'].median()
        minimum=df['Age'].min()
        maximum=df['Age'].max()
        
        print(f"{total_pregnancies} are the total pregnancies")
        print(f"{mean} are the mean of pregnancies")
        print(f"{median} are the median of pregnancies")
        print( f"the maximum age of patient {maximum}" )
        print(f"{minimum} are the minimum age of patients")
        
D=DiabeticsData(file1,file2)  
#D.reading_files()
# D.merging_data() 
D.statistics()
