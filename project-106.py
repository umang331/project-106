import csv 
import plotly.express as px
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x = "Marks In Percentage",y = "Days Present")
        fig.show()
    
def getDataSource(data_path):
    marks_in_percentage = []
    days_Present = []
    with open(data_path) as csvFile:
        csv_reader = csv.DictReader(csvFile)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_Present.append(float(row["Days Present"]))
    return {"x":marks_in_percentage,"y":days_Present}
def findCorrelation(data_soruce):
    Correlation = np.corrcoef(data_soruce["x"],data_soruce["y"])
    print(Correlation[0,1])
def setup():
    data_Path = "E:\whitehatjr\PYTHON\Student Marks vs Days Present.csv"
    DataSource = getDataSource(data_Path)
    findCorrelation(DataSource)
    plotFigure(data_Path)
setup()
