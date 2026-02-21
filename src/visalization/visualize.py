import matplotlib.pyplot as plt

def plot_results(x, y1, y2):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    ax1.plot(x, y1, color='blue')
    ax1.set_title('Linear Growth')
    ax2.scatter(x, y2, color='red')
    ax2.set_title('Stochastic Noise')
    plt.tight_layout()
    plt.show()
