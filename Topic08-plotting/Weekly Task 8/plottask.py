import numpy as np
import matplotlib.pyplot as plt
# import mpld3
# mpld3.enable_notebook()

def h(x):
    x**3
    return x
    
# Generate x values from 0 to 10
x = np.linspace(0, 10, 400)
y = h(x)


data = np.random.normal(loc=5, scale = 2, size=1000)

plt.hist(data, bins=20, color='C9', edgecolor='k', linewidth=0.5, alpha=0.6, label="Histogram")
plt.plot(x,y, label="Plot", color="blue", marker='X', alpha=0.3)
plt.title("Normal Distribution").set_fontweight('bold')
plt.xlabel('Value').set_fontstyle('italic')
plt.xlabel('Value').set_fontsize('x-large')
plt.ylabel('Value').set_fontstyle('italic')
plt.ylabel('Value').set_fontsize('x-large')
plt.legend()
plt.ylabel('Frequency')
plt.grid(True)
plt.grid( alpha=0.2)
plt.show()
plt.figure(figsize=(8,6))
plt.savefig("hist.png")