import matplotlib.pyplot as plt

plt.figure()

# plt.subplot(2, 2, 1)
# plt.plot([0, 1], [0, 1])

# plt.subplot(2, 2, 2)
# plt.plot([0, 1], [0, 2])

# plt.subplot(2, 2, 3)
# plt.plot([0, 1], [0, 3])

# plt.subplot(2, 2, 4)
# plt.plot([0, 1], [0, 4])

plt.subplot(2, 1, 1)
plt.plot([0, 1], [0, 1])

plt.subplot(234)
plt.plot([0, 1], [0, 2])

plt.subplot(235)
plt.plot([0, 1], [0, 3])

plt.subplot(236)
plt.plot([0, 1], [0, 4])

plt.tight_layout()
plt.show()