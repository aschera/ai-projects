import matplotlib.pyplot as plt

class Proposition:
    def __init__(self, name):
        self.name = name
        self.value = None

    def __str__(self):
        return self.name

    def set_value(self, value):
        self.value = value


class Expression:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def evaluate(self):
        left_val = self.left.value if isinstance(self.left, Proposition) else self.left.evaluate()
        right_val = self.right.value if isinstance(self.right, Proposition) else self.right.evaluate()

        if self.op == '^':
            return left_val and right_val
        elif self.op == '=>':
            return not left_val or right_val


def generate_combinations(prop_list):
    if not prop_list:
        return [[]]

    rest_combinations = generate_combinations(prop_list[1:])
    return [[False] + item for item in rest_combinations] + [[True] + item for item in rest_combinations]


def print_header(props):
    max_column_width = max(len(prop.name) for prop in props)
    max_column_width = max(max_column_width, len("(P ^ Q) => R"), len("KB"), len("KB => R"))

    header = "\t".join(prop.name.center(max_column_width) for prop in props)
    print(header + "\t" + "(P ^ Q) => R".center(max_column_width) + "\t" + "KB".center(max_column_width) + "\t" + "KB => R".center(max_column_width))

def print_truth_table(props, kb, kb_implies_r):
   # print_header(props)
    combinations = generate_combinations(props)

    max_column_width = max(len(prop.name) for prop in props)
    max_column_width = max(max_column_width, len("(P ^ Q) => R"), len("KB"), len("KB => R"))

    # Generate truth table data
    table_data = []
    for item in combinations:
        for i, prop in enumerate(props):
            prop.set_value(item[i])

        kb_value = int(kb.evaluate())
        kb_implies_r_value = int(kb_implies_r.evaluate())
        expr_value = int(Expression(Expression(props[0], '^', props[1]), '=>', props[2]).evaluate())

        row_values = [str(int(prop.value)) for prop in props]
        table_data.append(row_values + [str(expr_value), str(kb_value), str(kb_implies_r_value)])

    # Create the table
    columns = [prop.name for prop in props] + ["(P ^ Q) => R", "KB", "KB => R"]
    cell_text = table_data

    plt.figure(figsize=(8, 6))
    the_table = plt.table(cellText=cell_text, colLabels=columns, loc='center', cellLoc='center')

    # Set header text in bold for each column
    for (i, name) in enumerate(columns):
        cell = the_table[(0, i)]
        cell.get_text().set_fontweight('bold')

    the_table.auto_set_font_size(False)
    the_table.set_fontsize(10)

    plt.axis('off')  # Hide the axis

    plt.show()

def main():
    P = Proposition("P")
    Q = Proposition("Q")
    R = Proposition("R")

    kb = Expression(Expression(P, '^', Q), '=>', R)
    kb_implies_r = Expression(kb, '=>', R)

    print_truth_table([P, Q, R], kb, kb_implies_r)

if __name__ == "__main__":
    main()
