def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count_days(current):
        if current > days:
            return
        print("Day", current)
        count_days(current + 1)

    count_days(1)
    print("Harvest time!")
