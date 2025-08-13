import timeit
import random
from algorithms.bubble_sort import bubble_sort
from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort
from utils.plotter import plot_results


def generate_random_list(size):
    return [random.randint(0, 10000) for _ in range(size)]


def measure_time(sort_func, arr):
    start_time = timeit.default_timer()
    sort_func(arr.copy())
    return timeit.default_timer() - start_time


def run_performance_test():
    sizes = [100, 500, 1000, 2000, 5000]
    algorithms = {
        'Bubble Sort': bubble_sort,
        'Selection Sort': selection_sort,
        'Insertion Sort': insertion_sort
    }

    results = {name: [] for name in algorithms}

    for size in sizes:
        test_list = generate_random_list(size)
        for name, func in algorithms.items():
            time_taken = measure_time(func, test_list)
            results[name].append(time_taken)
            print(f"{name} with size {size}: {time_taken:.5f} seconds")

    plot_results(sizes, results)


if __name__ == '__main__':
    run_performance_test()