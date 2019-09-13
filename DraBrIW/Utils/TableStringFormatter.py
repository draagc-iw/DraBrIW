class TableStringFormatter:
    def __init__(self):
        self._table_str = ""
        self._num_columns = 0
        self._header_items = []
        self._rows = []

    def header(self, header_items: list):
        self._header_items = list(self._stringify(header_items))
        self._num_columns = len(header_items)

    def row(self, row_items):
        self._check_len(row_items)
        self._rows.append(list(self._stringify(row_items)))

    def get(self):
        cell_widths = self._calc_cell_widths()
        sep_thick = separator_thick(cell_widths, self._num_columns)
        sep_thin = separator_thin(cell_widths, self._num_columns)

        output = sep_thick
        output += self._generate_str_row(cell_widths, self._header_items)
        output += sep_thick

        for row in self._rows:
            output += self._generate_str_row(cell_widths, row)
            output += sep_thin

        return f"\n{output}\n"

    def _generate_header(self):
        output = separator_thick(self._calc_cell_widths(), self._num_columns)
        return output

    def _generate_str_row(self, cell_widths: iter, row_items: iter):
        output = str()
        for item, cell_width in zip(row_items, cell_widths):
            output += f"|{item}{' ' * (cell_width - len(item))}"
        output += "|\n"
        return output

    def _calc_cell_widths(self):
        cell_widths = list()
        for index in range(self._num_columns):
            column = [self._header_items[index]] + list(map(lambda row: row[index], self._rows))
            max_cell_len = max(map(lambda item: len(item), column))
            cell_widths.append(max_cell_len + 1)

        return cell_widths

    def _check_len(self, lst: list):
        if len(lst) != self._num_columns:
            raise ValueError("The number of items in argument must be equal to the number of columns")

    def _stringify(self, items: iter):
        return map(lambda item: str(item), items)


def separator_thick(cell_widths: list, num_cells: int):
    output = "+"
    for index in range(num_cells):
        output += f"{'=' * cell_widths[index]}+"
    return output + "\n"


def separator_thin(cell_widths: list, num_cells: int):
    output = "+"
    for index in range(num_cells):
        output += f"{'-' * cell_widths[index]}+"
    return output + "\n"
