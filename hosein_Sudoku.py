import time
from typing import Optional, Tuple, List, Set, Dict, Union


class Sudoku:
    def __init__(self, table: Optional[Tuple[Tuple[int, ...], ...]] = None):
        self.row_allow: List[Set[int], ...] = []
        self.column_allow: List[Set[int], ...] = []
        self.box_allow: List[List[Set[int], ...], ...] = []
        if table:
            self.raw_table = table
            self.table = [list(row) for row in table]
        else:
            self._get_table()
        self.full_possibility_analyse()
        self.decision_list: List[Dict[str, Union[Tuple[int, int], set]]] = []
        self.guess_trace: List[List[Tuple[int, int]]] = []

    def __str__(self):
        if self.table:
            rows = [' '.join(map(str, row)) for row in self.table]
            return '\n'.join(rows)
        else:
            return ''

    def __getitem__(self, item):
        assert isinstance(item, tuple) and len(item) == 2
        return self.table[item[0]][item[1]]

    def _get_table(self):
        table = []
        for _ in range(9):
            while True:
                try:
                    line = input().replace(' ', '')
                    if line.isalnum() and len(line) == 9:
                        table.append(list(map(int, line)))
                    else:
                        raise UserWarning
                except UserWarning:
                    print('Please enter the numbers correctly:\nEnter 0 for empty cell')
                else:
                    break
        self.table = table
        self.raw_table = tuple(table)

    def node_possibility(self, node_row, node_column):
        if self[node_row, node_column]:
            return 0
        else:
            return self.row_allow[node_row] \
                   & self.column_allow[node_column] \
                   & self.box_allow[node_row // 3][node_column // 3]

    def full_possibility_analyse(self):
        num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.row_allow = [num_set.copy() for _ in range(9)]
        self.column_allow = [num_set.copy() for _ in range(9)]
        self.box_allow = [[num_set.copy() for _ in range(3)] for _ in range(3)]
        for n, row in enumerate(self.table):
            self.row_allow[n] -= set(row)
            for k in range(3):
                self.box_allow[n // 3][k] -= set(row[3 * k:3 * (k + 1)])
            for m, clm in enumerate(row):
                self.column_allow[m] -= {clm}

    def solve(self) -> bool:
        some_done = True
        while some_done:
            some_done = self.num_from_cell_possibility() or self.single_num_extract_from_constrains()
        if not any(0 in row for row in self.table):
            return True
        else:
            self.decision()

    def num_from_cell_possibility(self):
        do_any = False
        for n_cell in range(9):
            for m_cell in range(9):
                data_set = self.node_possibility(n_cell, m_cell)
                if data_set:
                    if len(data_set) == 1:
                        do_any = True
                        cell = n_cell, m_cell, data_set.pop()
                        self.write_cell(*cell)
                    elif len(data_set) == 0:
                        raise UserWarning(1, "This Sudoku does not have solution")
        return do_any

    def choose_cell_for_level(self, lvl: int) -> Tuple[Tuple[int, int], set]:
        for n_cell in range(9):
            for m_cell in range(9):
                data_set = self.node_possibility(n_cell, m_cell)
                if data_set:
                    if len(data_set) == lvl:
                        return (n_cell, m_cell), data_set
        raise UserWarning(lvl, f"there isn't {lvl} possibility at this level")

    def write_cell(self, n_cell, m_cell, num):
        self.row_allow[n_cell] -= {num}
        self.column_allow[m_cell] -= {num}
        self.box_allow[n_cell // 3][m_cell // 3] -= {num}
        self.table[n_cell][m_cell] = num
        if self.guess_trace:
            self.guess_trace[-1].append((n_cell, m_cell))

    def write_back(self, cell):
        n_cell, m_cell = cell
        num = self[cell]
        self.row_allow[n_cell] |= {num}
        self.column_allow[m_cell] |= {num}
        self.box_allow[n_cell // 3][m_cell // 3] |= {num}
        self.table[n_cell][m_cell] = 0

    def single_num_extract_from_constrains(self):
        do_any = False
        for n_cell in range(9):
            for m_cell in range(9):
                data_set = self.node_possibility(n_cell, m_cell)
                if data_set:
                    m_data_set = data_set.copy()
                    n_data_set = data_set.copy()
                    b_data_set = data_set.copy()
                    for mm in range(9):
                        m_node = self.node_possibility(n_cell, mm)
                        if mm != m_cell and m_node:
                            m_data_set -= m_node
                    for nn in range(9):
                        n_node = self.node_possibility(nn, m_cell)
                        if nn != n_cell and n_node:
                            n_data_set -= n_node
                    for nn in range(9):
                        for mm in range(9):
                            if (mm != m_cell or nn != n_cell) and mm // 3 == m_cell // 3 and nn // 3 == n_cell // 3:
                                b_node = self.node_possibility(nn, mm)
                                if b_node:
                                    b_data_set -= b_node
                    all_data_set = m_data_set | n_data_set | b_data_set
                    if len(all_data_set) == 1:
                        cell = n_cell, m_cell, all_data_set.pop()
                        self.write_cell(*cell)
                        do_any = True
        return do_any

    def decision(self) -> bool:
        level = 2
        while level < 10:
            try:
                guess_cell, guess_cell_set = self.choose_cell_for_level(level)
                self.decision_list.append({'guess_cell': guess_cell, 'guess_cell_set': guess_cell_set})
                self.guess_trace.append([])
                break
            except UserWarning as err:
                if err.args[0] < 9:
                    level += 1
                else:
                    raise UserWarning(1, 'Previous decision is incorrect')

        while self.decision_list[-1]['guess_cell_set']:
            try:
                self.write_cell(*self.decision_list[-1]['guess_cell'], self.decision_list[-1]['guess_cell_set'].pop())
                return self.solve()
            except UserWarning as err:
                if err.args[0] == 1:
                    self.decision_rollback()
        else:
            self.decision_list.pop()
            self.guess_trace.pop()
            raise UserWarning(1, "previous decision is incorrect")

    def decision_rollback(self):
        while self.guess_trace[-1]:
            self.write_back(self.guess_trace[-1].pop())


if __name__ == '__main__':
    base_all_zero = (
        (0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0)
    )

    base_easy = (
        (0, 0, 0, 0, 0, 0, 5, 0, 1),
        (5, 6, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 7, 2, 0, 4, 0, 0, 0),
        (0, 0, 5, 0, 7, 9, 2, 1, 3),
        (0, 0, 4, 1, 0, 2, 0, 5, 9),
        (2, 0, 0, 0, 0, 8, 4, 0, 0),
        (0, 0, 0, 3, 0, 5, 0, 0, 7),
        (8, 0, 1, 0, 2, 6, 9, 3, 4),
        (0, 7, 3, 8, 9, 1, 0, 2, 5)
    )

    base_hard = (
        (0, 0, 4, 0, 0, 3, 5, 6, 8),
        (5, 0, 0, 8, 0, 7, 0, 4, 2),
        (0, 0, 0, 0, 0, 4, 0, 0, 0),
        (8, 0, 5, 0, 1, 2, 0, 0, 0),
        (0, 0, 0, 0, 5, 0, 2, 0, 9),
        (0, 0, 0, 0, 0, 0, 6, 0, 0),
        (0, 7, 8, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 5, 0),
        (6, 0, 0, 9, 0, 0, 0, 7, 0)
    )
    base_expert = (
        (3, 0, 0, 9, 0, 0, 0, 0, 0),
        (0, 0, 7, 0, 0, 0, 2, 5, 0),
        (5, 0, 0, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 1, 0, 2, 0, 7, 9),
        (0, 0, 0, 0, 0, 8, 1, 0, 0),
        (0, 0, 0, 0, 0, 4, 0, 0, 0),
        (0, 7, 0, 0, 0, 0, 0, 0, 0),
        (0, 2, 0, 0, 7, 0, 0, 4, 5),
        (0, 0, 1, 3, 0, 0, 0, 0, 6)
    )
    base_pdf_1 = (
        (5, 3, 0, 0, 7, 0, 0, 0, 0),
        (6, 0, 0, 1, 9, 5, 0, 0, 0),
        (0, 9, 8, 0, 0, 0, 0, 6, 0),
        (8, 0, 0, 0, 6, 0, 0, 0, 3),
        (4, 0, 0, 8, 0, 3, 0, 0, 1),
        (7, 0, 0, 0, 2, 0, 0, 0, 6),
        (0, 6, 0, 0, 0, 0, 2, 8, 0),
        (0, 0, 0, 4, 1, 9, 0, 0, 5),
        (0, 0, 0, 0, 8, 0, 0, 7, 9)
    )
    base_pdf_2 = (
        (3, 0, 6, 5, 0, 8, 4, 0, 0),
        (5, 2, 0, 0, 0, 0, 0, 0, 0),
        (0, 8, 7, 0, 0, 0, 0, 3, 1),
        (0, 0, 3, 0, 1, 0, 0, 8, 0),
        (9, 0, 0, 8, 6, 3, 0, 0, 5),
        (0, 5, 0, 0, 9, 0, 6, 0, 0),
        (1, 3, 0, 0, 0, 0, 2, 5, 0),
        (0, 0, 0, 0, 0, 0, 0, 7, 4),
        (0, 0, 5, 2, 0, 6, 3, 0, 0)
    )
    base_al_escargot = (
        (8, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 3, 6, 0, 0, 0, 0, 0),
        (0, 7, 0, 0, 9, 0, 2, 0, 0),
        (0, 5, 0, 0, 0, 7, 0, 0, 0),
        (0, 0, 0, 0, 4, 5, 7, 0, 0),
        (0, 0, 0, 1, 0, 0, 0, 3, 0),
        (0, 0, 1, 0, 0, 0, 0, 6, 8),
        (0, 0, 8, 5, 0, 0, 0, 1, 0),
        (0, 9, 0, 0, 0, 0, 4, 0, 0)
    )
    star_time = time.time()
    sudoku = Sudoku(base_al_escargot)
    sudoku.solve()
    print(sudoku)
    print(time.time() - star_time)
