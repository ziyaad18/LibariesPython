import matplotlib.pyplot as plt



girls_ages = [12,99,65,85,42]

girls_names= ["Andy","Martin","Zahara","Vuyo","Ziyaad"]
x_pos = [i for i, _ in enumerate (girls_names)]
plt.bar(x_pos, girls_ages, color="red")
plt.xticks(x_pos, girls_names)
plt.title("bar graph")
plt.show()






