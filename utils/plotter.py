import matplotlib.pyplot as plt


def plot_results(sizes, results):
    plt.figure(figsize=(10, 6))

    for name, times in results.items():
        plt.plot(sizes, times, label=name, marker='o')

    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithms Performance Comparison')
    plt.legend()
    plt.grid(True)
    plt.savefig('sorting_performance.png')
    plt.show()