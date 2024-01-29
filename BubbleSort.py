class BubbleSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        n = len(self.data)

        for i in range(n):
            # Last i elements are already sorted, no need to check them
            for j in range(0, n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    # Swap if the element found is greater than the next element
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]

    def display(self):
        print("Sorted Data:", self.data)


# Example usage:
if __name__ == "__main__":
    # Create an instance of BubbleSort
    bubble_sort_instance = BubbleSort([64, 34, 25, 12, 22, 11, 90])

    # Display the original data
    print("Original Data:", bubble_sort_instance.data)

    # Perform Bubble Sort
    bubble_sort_instance.sort()

    # Display the sorted data
    bubble_sort_instance.display()
