import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("E:/zje/ibmi/ibi1/IBI1_2023-24/Practical7")
#read the csv file
dalys_data = pd.read_csv("dalys-rate-from-all-causes(1).csv")
# showing the fourth column (the DALYs) from every 10th row,
print(dalys_data.iloc[0:101:10,3])
#show DALYs for all rows corresponding to Afghanistan.
value=dalys_data["Entity"] == "Afghanistan"
data = dalys_data.loc[value, "DALYs"]
print(data)
#computed the mean DALYs in China
china_data=dalys_data["Entity"] == "China"
print(np.mean(dalys_data.loc[china_data, "DALYs"]))
#Compare this value to the DALYs measured for 2019 
print("Dalys for 2019 in China is 22270.51<30667.647 so it is less then the mean.")
china_data_Year=dalys_data.loc[china_data, "Year"]
china_data_DALYs=dalys_data.loc[china_data, "DALYs"]
plt.plot(china_data_Year, china_data_DALYs, 'bo')
plt.xticks(china_data_Year,rotation=-90)
plt.title("show how has the DALYs changed in the China over time")
plt.show()
plt.close
# question is how to plot a boxplot of DALYs in England
dalys_data["Entity"] == "England"
plt.boxplot(dalys_data.loc[dalys_data["Entity"] == "England", "DALYs"])
plt.xlabel("DALYs in England over years")
plt.show()
plt.close
