import matplotlib.pyplot as plt
data_students=[5,15,25,15,45,55]
plt.hist(data_students,bins=[0,10,20,30,40,50,60],weights=[10,1,0,2,20,2],edgecolor="red")
plt.show