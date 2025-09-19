class Spreadsheet(object):
    def __init__(self, rows):
        self.rows = rows
        self.data = {}

    def setCell(self, cell, value):
        self.data[cell] = value

    def resetCell(self, cell):
        if cell in self.data:
            del self.data[cell]

    def getValue(self, formula):
        if formula.startswith("="):
            formula = formula[1:]
        tokens = []
        i = 0
        while i < len(formula):
            if formula[i].isalpha():
                j = i
                while j < len(formula) and (formula[j].isalpha() or formula[j].isdigit()):
                    j += 1
                cell_ref = formula[i:j]
                tokens.append(str(self.data.get(cell_ref, 0)))
                i = j
            else:
                tokens.append(formula[i])
                i += 1
        eval_formula = "".join(tokens)
        return eval(eval_formula)
