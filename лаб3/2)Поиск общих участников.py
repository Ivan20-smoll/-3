# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, separator=","):
  """
  Находит общих участников в двух группах.

  Args:
    group1: Строка с фамилиями участников первой группы, разделенными разделителем.
    group2: Строка с фамилиями участников второй группы, разделенными разделителем.
    separator: Разделитель между фамилиями участников (по умолчанию - запятая).

  Returns:
    Список общих участников, отсортированный в алфавитном порядке.
  """
  first_group = set(group1.split(separator))
  second_group = set(group2.split(separator))
  common_participants = list(first_group.intersection(second_group))
  common_participants.sort()
  return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group, separator="|")
print(common_participants)  # Вывод: ['Петров', 'Сидоров']