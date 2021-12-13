import numpy as np
import pandas as pd

from helpers.file_handling import raw_input_from_file


def get_paper_instructions(file_name):
    raw = raw_input_from_file(file_name)
    lines = raw.splitlines()
    coords = [(int(line.split(",")[0]), int(line.split(",")[1])) for line in lines]
    return coords


def make_paper(instructions: [(int, int)]):
    xs = [ins[0] for ins in instructions]
    ys = [ins[1] for ins in instructions]
    max_x = max(xs)
    max_y = max(ys)

    paper = np.zeros((1311, 1311), dtype=int)

    for ins in instructions:
        paper[ins[0], ins[1]] = 1

    return paper


def init_test_paper():
    paper = np.zeros((7, 11), dtype=int)
    paper[0, 0] = 1
    paper[0, 2] = 1
    paper[0, 3] = 1
    paper[0, 6] = 1
    paper[0, 9] = 1
    paper[1, 0] = 1
    paper[1, 4] = 1
    paper[2, 6] = 1
    paper[2, 10] = 1
    paper[3, 0] = 1
    paper[3, 4] = 1
    paper[4, 1] = 1
    paper[4, 3] = 1
    paper[4, 6] = 1
    paper[4, 8] = 1
    paper[4, 9] = 1
    paper[4, 10] = 1

    return paper


def fold(paper, along, where):
    df = pd.DataFrame(paper)
    if along == "y":
        df1 = df.iloc[:, :where]
        df2 = df.iloc[:, where + 1:]
        df2 = df2[df2.columns[::-1]]

        a1 = df1.to_numpy()
        a2 = df2.to_numpy()
        for i in range(len(a1[:, 0])):
            for j in range(len(a1[0])):
                if a2[i, j] == 1:
                    a1[i, j] = 1
        return a1

    if along == "x":
        df1 = df.iloc[:where, :]
        df2 = df.iloc[where + 1:, :]
        df2 = df2.iloc[::-1]

        a1 = df1.to_numpy()
        a2 = df2.to_numpy()
        for i in range(len(a1[:, 0])):
            for j in range(len(a1[0])):
                if a2[i, j] == 1:
                    a1[i, j] = 1
        return a1
