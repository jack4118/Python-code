import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

FileNo = 1
for ExportGraph in range(len(csv_file)):
    # File path with the File name
    filepath = file_path + 'File' + str(FileNo) + '.csv'

    logdata = pd.read_csv(filepath)

    plt.style.use('ggplot')
    plt.figure(figsize=(20,20))
    
    D_T = logdata.values[:,3]
    Y_V = logdata.values[:,2] # Y-Axis Value
    X_V = logdata.values[:,4] # X-Axis Value
    
    plt.scatter(X_V,Y_V)
    
    DateTime = str(D_T[(len(D_T))-1])
    
    plt.ylim(bottom = 0e-09, top = 8.5e-09)
    TitleName = 'Graph'+ str(FileNo) + '\nDate and Time:' + str(DateTime)
    plt.title(TitleName)
    plt.legend(['Y-Axis Value'])

    SaveName = 'Graph' + str(FileNo) + '.png'
    plt.savefig(SaveName)
    plt.show()
    
    FileNo += 1
