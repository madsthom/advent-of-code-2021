import unittest

import numpy as np

from day13.folding import get_paper_instructions, make_paper, init_test_paper, fold


class FoldingTestCase(unittest.TestCase):
    def test_dot_input(self):
        self.assertEqual((95, 196), get_paper_instructions("dot_input")[0])
        self.assertEqual((500, 420), get_paper_instructions("dot_input")[1])
        self.assertEqual((774, 285),
                         get_paper_instructions("dot_input")[len(get_paper_instructions("dot_input")) - 1])

    def test_init_paper(self):
        instructions = get_paper_instructions("dot_input")
        paper = make_paper(instructions)

        self.assertEqual(1, paper[95, 196])
        self.assertEqual(1, paper[774, 285])
        self.assertEqual(1311, len(paper))

    def test_fold_operation(self):
        paper = init_test_paper()

        new_paper = fold(paper, along="y", where=5)

        self.assertEqual([1, 1, 1, 1, 1], list(new_paper[0]))
        self.assertEqual([1, 0, 0, 0, 1], list(new_paper[1]))
        self.assertEqual([1, 0, 0, 0, 1], list(new_paper[2]))
        self.assertEqual([1, 0, 0, 0, 1], list(new_paper[3]))
        self.assertEqual([1, 1, 1, 1, 1], list(new_paper[4]))

    def test_fold_operation2(self):
        paper = make_paper(get_paper_instructions("dot_input"))

        new_paper = fold(paper, along="x", where=655)
        new_paper = fold(new_paper, along="y", where=447)
        new_paper = fold(new_paper, along="x", where=327)
        new_paper = fold(new_paper, along="y", where=223)
        new_paper = fold(new_paper, along="x", where=163)
        new_paper = fold(new_paper, along="y", where=111)
        new_paper = fold(new_paper, along="x", where=81)
        new_paper = fold(new_paper, along="y", where=55)
        new_paper = fold(new_paper, along="x", where=40)
        new_paper = fold(new_paper, along="y", where=27)
        new_paper = fold(new_paper, along="y", where=13)
        new_paper = fold(new_paper, along="y", where=6)
        row_string = ""
        for row in np.transpose(new_paper):
            for value in row:
                if value == 1:
                    row_string += "#"
                else:
                    row_string += " "
            row_string += "\n"
        print(row_string)
        count = np.sum(new_paper)

        print(count)


if __name__ == '__main__':
    unittest.main()
