def total_salary(path):
    try:    
        with open(f"{path}", 'r') as fi:
            lines = [el.strip() for el in fi.readlines()]
            all_sums = list()
            midle_sum = 0
            final_sum = 0
            count_repeats = 0
            for el in lines:
                new_element = el.split(',')
                new_element.pop(0)
                final_sum += int(''.join(new_element))
                count_repeats += 1

            midle_sum = final_sum // count_repeats
            all_sums.append(final_sum)
            all_sums.append(midle_sum)

            return tuple(all_sums)
        
    except Exception as e:
        print(e)

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


def get_cats_info(path):
    try:
        with open(f"{path}", 'r') as fi:
            current_list = list()
            lines = [el.strip() for el in fi.readlines()]
            for el in lines:
                new_element = el.split(',')
                new_dict = {'id': new_element[0], 'name': new_element[1], 'age': new_element[2]}
                current_list.append(new_dict)
        return current_list
    except Exception as e:
        print(e)

cats_info = get_cats_info("cats_file.txt")
print(cats_info)