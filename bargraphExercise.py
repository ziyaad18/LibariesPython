import matplotlib.pyplot as plt



test_scores= [12,99,65,85,42]

names= ["Andy","Martin","Zahara","Vuyo","Ziyaad"]
x_pos = [i for i, _ in enumerate (names)]
plt.bar(x_pos, test_scores, color="blue")
plt.xticks(x_pos, names)
plt.title("Python marks for 5 students")
plt.show()
