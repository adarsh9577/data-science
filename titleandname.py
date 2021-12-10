
import matplotlib.pyplot as plt
data_students=[1,11,21,31,41,51]
plt.hist(data_students,bins=[0,10,20,30,40,50,60],weights=[10,1,0,2,20,2],edgecolor="red",facecolor='pink')
plt.title("Histogram for students data")
plt.xlabel('value')
plt.ylabel('frequency')
plt.savefig("student.png")
plt.show()
