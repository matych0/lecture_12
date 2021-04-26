import csv
import os
import random

cwd_path = os.getcwd()

def read_row(file_name):
    """
    Reads one row for a CSV file and returns numeric data.
    :param file_name: (str), name of CSV file
    :return: (list, int),
    """
    file_path = os.path.join(cwd_path, file_name)
    numbers_list = []
    with open(file_path, "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            for number in row:
                numbers_list.append(int(number))
    return numbers_list

def read_rows(file_name, row_number):
    """
    Reads selected row for a CSV file and returns selected numeric data.
    :param file_name: (str), name of CSV file
    :param row_number: (int), number of selected row
    :return: (list, int),
    """
    file_path = os.path.join(cwd_path, file_name)
    numbers_list = []
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        for row_idx, row in enumerate(reader):
            if row_idx + 1 == row_number:
                for number in row:
                    numbers_list.append(int(number))
    return numbers_list

def selection_sort(number_array, direction="ascending"):
    """
        Sorts and returns selected numeric data with Selection Sort.
        :param number_array: (list,int), list with numeric array
        :return: (list, int), sorted numeric array
    """
    n = len(number_array)
    for i in range(n - 1):
        min_idx = i
        for num_idx in range(i + 1, n):
            if direction == "ascending":
                if number_array[min_idx] > number_array[num_idx]:
                    min_idx = num_idx
            elif direction == "descending":
                if number_array[min_idx] < number_array[num_idx]:
                    min_idx = num_idx
        number_array[i], number_array[min_idx] = number_array[min_idx], number_array[i]
    return number_array


def bubble_sort(number_array):
    """
       Sorts and returns selected numeric data with Bubble Sort.
       :param number_array: (list,int), list with numeric array
       :return: (list, int), sorted numeric array
    """
    n = len(number_array)
    for i in range(n - 1):
        for idx in range(n - i - 1):
            if number_array[idx] > number_array[idx + 1]:
                number_array[idx], number_array[idx + 1] = number_array[idx + 1], number_array[idx]
    return number_array



def main():
    data = read_row("numbers_one.csv")
    print(data)
    # Ukol: Selection Sort
    sorted_num = selection_sort(data)

    # Ukol: Selection Sort - se smerem razeni
    sorted_num = selection_sort(data, "descending")
    print(sorted_num)

    data_2 = read_rows("numbers_two.csv", 1)
    print(data_2)
    # Ukol: Bubble Sort
    print(bubble_sort(data_2))

    # příklad výpisu hodnot seřazené řady
    # print ("Seřazená řada čísel je:")
    # for i in range(len(number_array)):
    #	print ("%d" %number_array[i]),


if __name__ == '__main__':
    main()

