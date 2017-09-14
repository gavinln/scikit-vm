plt.figure(figsize=(10, 7))
colors = ["darkblue", "darkgreen", "gray"]

for n, color in enumerate(colors):
    idx = np.where(test_y == n)[0]
    plt.scatter(test_X[idx, 1], test_X[idx, 2], color=color, label="Class %s" % str(n))

markers = ['o', 'v', 's']
for idx, marker in zip(incorrect_idx, markers):
    label = 'a:{}, p:{}'.format(test_y[idx], pred_y[idx])
    plt.scatter(test_X[idx, 1], test_X[idx, 2],
                color="darkred", marker=marker, label=label)

plt.xlabel('sepal width [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc=3)
plt.title("Iris Classification results")
plt.show()
