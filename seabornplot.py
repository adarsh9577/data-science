import matplotlib.pyplot as plt
import seaborn as sn
df = sn.load_dataset('iris') 
sn.histplot(data=df,x="petal_length")
plt.show()
