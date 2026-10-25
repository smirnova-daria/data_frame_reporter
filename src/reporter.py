class DataFrameReporter:
    def __init__(self, float_format="0.05f", percent_format="0.02%", include_all=False):
        self.float_format = float_format
        self.percent_format = percent_format
        self.include_all = include_all

    def show_report(self, df, title=None):
        if title:
            print(title)

        n_rows, n_cols = df.shape
        dups_count = df.duplicated().sum()
        dups_percent = dups_count / n_rows if n_rows else 0 * 100

        print(f'Количество столбцов: {n_cols}')
        print(f'Количество строк: {n_rows}')
        print(f'Количество дубликатов: {dups_count}')
        print(f'Доля дубликатов: {dups_percent:{self.percent_format}}')
