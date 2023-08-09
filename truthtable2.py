class PropositionalLogic:
    def __init__(self):
        self.truth_values = [True, False]
        self.expressions = {
            "P": "It is hot",
            "Q": "It is humid",
            "R": "It is raining",
        }
        self.knowledge_base = {
            "((P ^ Q) => R)": [],
            "(Q => P)": [],
            "Q": [],
            "KB": [],
            "R": [],
            "(KB => R)": []
        }

    def conjunction(self, p, q):
        return p and q

    def implication(self, p, q):
        return not p or q

    def evaluate_expression(self, expr, p, q, r):
        if expr == "P":
            return p
        elif expr == "Q":
            return q
        elif expr == "R":
            return r
        elif expr == "(P ^ Q) => R":
            return self.implication(self.conjunction(p, q), r)
        elif expr == "(Q => P)":
            return self.implication(q, p)
        elif expr == "KB":
            return all(self.knowledge_base[expr])
        elif expr == "(KB => R)":
            return self.implication(all(self.knowledge_base["KB"]), r)

    def generate_truth_table(self):
        print("{:^6} {:^6} {:^6} {:^20} {:^10} {:^5} {:^5}".format(
            "P", "Q", "R", "(P ^ Q) => R", "(Q => P)", "KB", "KB=>R"
        ))
        print("="*60)

        for p in self.truth_values:
            for q in self.truth_values:
                for r in self.truth_values:
                    self.knowledge_base["P"] = [p]
                    self.knowledge_base["Q"] = [q]
                    self.knowledge_base["R"] = [r]

                    self.knowledge_base["((P ^ Q) => R)"] = [self.evaluate_expression("(P ^ Q) => R", p, q, r)]
                    self.knowledge_base["(Q => P)"] = [self.evaluate_expression("(Q => P)", p, q, r)]
                    self.knowledge_base["KB"] = [self.evaluate_expression("KB", p, q, r)]
                    self.knowledge_base["(KB => R)"] = [self.evaluate_expression("(KB => R)", p, q, r)]

                    print("{:^6} {:^6} {:^6} {:^20} {:^10} {:^5} {:^5}".format(
                        str(p), str(q), str(r),
                        str(self.knowledge_base["((P ^ Q) => R)"][0]),
                        str(self.knowledge_base["(Q => P)"][0]),
                        str(self.knowledge_base["KB"][0]),
                        str(self.knowledge_base["(KB => R)"][0])
                    ))


if __name__ == "__main__":
    pl = PropositionalLogic()
    pl.generate_truth_table()
