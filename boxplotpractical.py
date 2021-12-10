import matplotlib.pyplot as plt
a1=[72,76,24,40,57,62,75,78,31,32]
a2=[62,5,92,25,36,32,96,95,30,90]
a3=[23,89,12,78,72,89,25,69,68,86]
a4=[99,73,70,16,82,61,88,98,10,87]
box_plot_data=[a1,a2,a3,a4]
box=plt.boxplot(box_plot_data,vert=1,patch_artist=True,labels=['course1','course2','course3','course4'],)
colors=['cyan','lightblue','lightgreen','tan']
for patch,color in zip(box['boxes'],colors):patch.set_facecolor(color)
plt.show()
