import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics as stat

def cleanAndMean(filename):
    """
        This function takes in a .csv file that contains train performace data and turns it into a data frame containing average 
        train delays for the month. 
        The following columns are removed: stop_sequence, data, train_id, type, from, from_id, to, to_id, scheduled_time, actual_time and status.
        The following lines are removed: Atl. City Line and Princeton Shuttle
        Note that each file contains one month worth of data. 
    
    Args:
        filename(str): A .csv file
    Returns:
        dfNew(DataFrame): A pandas DataFrame containing only the line name and average delay in minutes for the month.
    """
    
    #Clean the columns up
    dfOriginal = pd.read_csv(filename) #open the .csv file
    dfOriginal.drop(columns=['stop_sequence', 'date', 'train_id', 'type', 'from', 'from_id', 'to', 'to_id', 'scheduled_time', 
                     'actual_time', 'status'], inplace=True) #drop unwanted columns
    dfOriginal.dropna(inplace=True) #drop anything that is NA

    #Find the mean for each line
    dfNew = dfOriginal.groupby(['line']).mean() #group by the each line's mean late time
    filename = filename[-11:-4] #find the year and month
    dfNew = dfNew.rename(columns={"delay_minutes": f"avg_delay_{filename}"}) #add year and month to column name
    
    #Remove unwanted Lines
    for index, rows in dfNew.iterrows(): #iterate through rows
        
        if index == "Atl. City Line" or index == "Princeton Shuttle": #find Atl. City Line and Princeton Shuttle lines...
            dfNew.drop(index, inplace=True) #...remove the row

    return dfNew #return the data frame

def main(filenames):
    """
    The function sorts through files, finds averages using the cleanAndMean functions and uses matplotlib to display two graphs,
    witch each containing monthly average values.
    The first graph will show average data for the following NJ Transit Lines:
        Bergen County Line
        Gladstone Branch
        Main Line
        Montclair-Boonton Line
        Morristown Line
        North Jersey Coast Line
        Northeast Corridor Line
        Pascack Valley Line
        Raritan Valley Line
    The second graph will contain a monthly average for all the above lines and the following two, targeted lines that are of interest:
        North Jersey Coast Line
        Pascack Valley Line
    
    Args:
        filenames(str): A list of .csv files
    """
    
    #create empty list for x and y values
    dates = []
    yBergenValues = []
    yGladstoneValues = []
    yMainValues = []
    yMontclairValues = []
    yMorristownValues = []
    yNoValues = []
    yNortheastValues = []
    yPascackValues = []
    yRaritanValues = []
    yAvgValues = []
    
    
    for file in filenames: #for each file...
        
        avgList = [] #create empty avg pist
        
        df = cleanAndMean(file) #create the dataframe
        columnName = df.columns[0]
        date = columnName[10:] #pull the date from the columns
        dates.append(date) #add to the dates list
        
        #Pull and append data for Bergen Co. Line
        avgDelay = df.iloc[0][columnName]
        yBergenValues.append(avgDelay)
        avgList.append(avgDelay) #append to avg list
        
        #Pull and append data for Gladstone Branch
        avgDelay = df.iloc[1][columnName]
        yGladstoneValues.append(avgDelay)
        avgList.append(avgDelay) #append to avg list
        
        #Pull and append data for Main Line
        avgDelay = df.iloc[2][columnName]
        yMainValues.append(avgDelay)
        avgList.append(avgDelay) #append to avg list
        
        #Pull and append data for Montclair-Boonton
        avgDelay = df.iloc[3][columnName]
        yMontclairValues.append(avgDelay)
        avgList.append(avgDelay) #append to avg list
        
        #Pull and append data for Morristown Line
        avgDelay = df.iloc[4][columnName]
        yMorristownValues.append(avgDelay)
        avgList.append(avgDelay) #append to avg list
        
        #Pull and append data for No Jersey Coast
        avgDelay = df.iloc[5][columnName]
        yNoValues.append(avgDelay)
        avgList.append(avgDelay) #append to avg list
        
        #Pull and append data for Northeast Corrdr
        avgDelay = df.iloc[6][columnName]
        yNortheastValues.append(avgDelay)
        avgList.append(avgDelay) #append to avg list
        
        #Pull and append data for Pascack Valley
        avgDelay = df.iloc[7][columnName]
        yPascackValues.append(avgDelay)
        avgList.append(avgDelay) #append to avg list
        
        #Pull and append data for Raritan Valley
        avgDelay = df.iloc[8][columnName]
        yRaritanValues.append(avgDelay)
        avgList.append(avgDelay) #append to avg list
        
        #Find the average for the month and append it to the list
        yAvgValues.append(stat.mean(avgList))
        
        #print(f"{df.iloc[1]} with avg delay of {avgDelay}")
    
    #print(dates)
    
        
    xDates = np.array(dates) #create array from dates
    yBergenPoints = np.array(yBergenValues) #Create array from Bergen Values. Will be blue
    yMainPoints = np.array(yMainValues) #Create array from Main values. Will be orange
    yMontclairPoints = np.array(yMontclairValues) #Create array from Montclair values. Will be green
    yMorristownPoints = np.array(yMorristownValues) #Create array from Morristown values. Will be red
    yNoPoints = np.array(yNoValues) #Create array from No values. Will be purple. Will be orange on focused graph.
    yPascackPoints = np.array(yPascackValues) #Create array from Pascack values. Will be brown. Will be green on focused graph. 
    yRaritanPoints = np.array(yRaritanValues) #Create array from Raritan values. Will be pink
    yAvgPoints = np.array(yAvgValues) #Create array from the average values. Will be blue on focused graph.
    
    #Create Full Graph
    plt.plot(xDates, yBergenPoints, xDates, yMainPoints, xDates, yMontclairPoints, xDates, yMorristownPoints, xDates, yNoPoints,
             xDates, yPascackPoints, xDates, yRaritanPoints) #create full graph
    plt.show() #show the targeted graph
    
    plt.plot(xDates, yAvgPoints, xDates, yNoPoints, xDates, yPascackPoints) #create focused graph
    plt.show() #show the graph
    
def oneMonthDF(filename):
    df = cleanAndMean(filename) #create the dataframe
    print(df) #print the Dataframe

if __name__ == "__main__":
    filenames = ("performancearchive/2019_01.csv", "performancearchive/2019_02.csv", "performancearchive/2019_03.csv", "performancearchive/2019_03.csv", 
                 "performancearchive/2019_04.csv", "performancearchive/2019_05.csv", "performancearchive/2019_06.csv", "performancearchive/2019_07.csv",
                 "performancearchive/2019_08.csv", "performancearchive/2019_09.csv", "performancearchive/2019_10.csv", "performancearchive/2019_11.csv",
                 "performancearchive/2019_12.csv",)
    main(filenames)
    #oneMonthDF("performancearchive/2019_06.csv")