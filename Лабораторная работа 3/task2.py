# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, razd = ','):
    command1 = set(group1.split(razd))
    command2 = set(group2.split(razd))

    common_commands = sorted(command1.intersection(command2))

    return common_commands

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_commands = find_common_participants(participants_first_group, participants_second_group, razd='|')

print(common_commands)


# TODO Провеьте работу функции с разделителем отличным от запятой
