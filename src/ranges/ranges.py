def sort_even_odd(array):
    even_numbers = []
    odd_numbers = []
    for number in array:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    return even_numbers, odd_numbers
numbers = list(range(300))
even_numbers, odd_numbers = sort_even_odd(numbers)
print("Четные числа:", even_numbers)
print("Нечетные числа:", odd_numbers)