class literal:
    def __init__(self, var_name, is_negated):
        self.var_name = var_name
        self.is_negated = is_negated

# s - це множина диз'юнктів, яка представлена у вингляді списку списків літералів.


s = [
    [literal("p", True), literal("r", True)],
    [literal("q", True), literal("r", True)],
    [literal("r", True), literal("q", False)],
    [literal("p", True), literal("r", False)]
]

def merge_disjunkts(dis_1: list, dis_2: list) -> list:
    result = dis_1 + dis_2

    indexes_to_remove = set()
    for i in range(len(result)):
        for j in range(len(result)):
            if result[i].var_name == result[j].var_name and result[i].is_negated != result[j].is_negated:
                indexes_to_remove.add(i)
                indexes_to_remove.add(j)

    for i in sorted(list(indexes_to_remove))[::-1]:
        del result[i]

    return result

def has_contrary(dis_1: list, dis_2: list) -> bool:
    for i in range(len(dis_1)):
        for j in range(len(dis_2)):
            if dis_1[i].var_name == dis_2[j].var_name and dis_1[i].is_negated != dis_2[j].is_negated:
                return True

    return False

# Застосовує метод резолюції і повертає ранг резольвенти.
def apply_resolution_method(s) -> int:
    contrary_pair_found = True
    already_merged = set()
    while (contrary_pair_found):
        contrary_pair_found = False

        for i in range(len(s)):
            if contrary_pair_found:
                break
            if i in already_merged:
                continue

            for j in range(len(s)):
                if j in already_merged:
                    continue

                if i != j and has_contrary(s[i], s[j]):
                    s.append(merge_disjunkts(s[i], s[j]))
                    contrary_pair_found = True
                    already_merged.add(i)
                    already_merged.add(j)
                    break

    # Шукємо диз'юнкт з найменшим рангом.
    min_rank = len(s[0])
    for el in s:
        if len(el) < min_rank:
            min_rank = len(el)

    return min_rank

if apply_resolution_method(s) == 0:
    print("Множина невиконанна")
else:
    print("Множина виконанна")
