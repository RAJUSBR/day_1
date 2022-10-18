
import os
import pandas as pd
file1=os.path.join (os.getcwd(),'processing','diabetes_1.csv')
file2=os.path.join (os.getcwd(),'processing','diabetes_2.csv')

class DiabeticsData:
    
    def __init__(self,file1,file2) :
        self.file1=file1
        self.file2=file2
        
    #Reading the files    
    #def reading_files(self):
        df1=pd.read_csv(self.file1)
        df2=pd.read_csv(self.file2)
        print("reading completed")
        return df1,df2
        # print(df1)
        # print(df2)
    # Merging the data
    def merging_data(self):
        #self.reading_files()
        # df1=pd.read_csv(self.file1)
        #  df2=pd.read_csv(self.file2)
        df=df1.merge(df2,how='outer')
        #print(df)
        print('Merge Completed')   
    #SApplying statistics
    def statistics(self):
        df1=pd.read_csv(self.file1)
        df2=pd.read_csv(self.file2)
        df=df1.merge(df2,how='outer')
        total_pregnancies=df['Pregnancies'].sum()
        total_DiabetesPedigreeFunction= df['DiabetesPedigreeFunction'].count()
        mean=df['Pregnancies'].mean()
        median=df['Pregnancies'].median()
        minimum=df['Age'].min()
        maximum=df['Age'].max()
        print("total pregnancies are " +str(total_pregnancies ))
        print("mean of pragnancies are " + str(mean))
        print("median of pragnancies are " + str(median))
        print("minimum age of patients are " +str(minimum))
        print("maximum age of patients are " +str(maximum))
        
D=DiabeticsData(file1,file2)  
#D.reading_files()
D.merging_data() 
D.statistics()


# git config --global user.email "bhargav.s0696@gmail.com"
# git config --global user.name "rajusbr"
