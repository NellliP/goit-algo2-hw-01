def find_min_max(arr):
    if not arr:
        raise ValueError("Масив не повинен бути порожнім")

    def divide_and_conquer(start, end):
        # Один елемент
        if start == end:
            return arr[start], arr[start]

        # Два елементи
        if end == start + 1:
            if arr[start] < arr[end]:
                return arr[start], arr[end]
            else:
                return arr[end], arr[start]

        # Рекурсивно обробляємо дві половини
        mid = (start + end) // 2
        min1, max1 = divide_and_conquer(start, mid)
        min2, max2 = divide_and_conquer(mid + 1, end)

        return min(min1, min2), max(max1, max2)

    return divide_and_conquer(0, len(arr) - 1)


# ✅ Приклад запуску
if __name__ == "__main__":
    numbers = [4, 7, 1, 9, -3, 10, 2]
    minimum, maximum = find_min_max(numbers)
    print(f"Мінімум: {minimum}, Максимум: {maximum}")
