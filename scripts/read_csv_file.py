import os
import pandas as pd

def readingStudentData(): 

    file_path = os.path.join (os.getcwd(),'processing','StudentData.csv')
    # print(paath)
    #df= pd.read_csv("C:\sample_csv_ files\processing\StudentData.csv")
    df=pd.read_csv(file_path)
    print(df)
    #print(paath)
