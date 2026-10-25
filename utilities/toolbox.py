from pathlib import Path
import pandas as pd
import seaborn as sns
import warnings

from IPython.core.display_functions import display

# Пути к данным
BASE_DIR = Path('raw')
SALES_DICT = 'sales_data_dictionary.csv'
SALES_DICT_PATH = BASE_DIR / SALES_DICT
TRANSACTIONS = 'Sales_transactions_2022_2025.csv'
TRANSACTIONS_PATH = BASE_DIR / TRANSACTIONS

MAKE_STRING = '=' * 40

def make_settings():
    """Настраивает среду для удобного анализа данных в Jupyter Notebook."""

    pd.set_option('display.max_columns', None)
    pd.set_option('display.float_format', lambda x: '%.2f' % x)
    sns.set_theme(style='whitegrid')
    warnings.filterwarnings('ignore')
    print('Настройки отображения установлены.')


def dataset_audit(df, name):
    print(MAKE_STRING)
    print(f'Data Quality Check: {name}')
    print(MAKE_STRING)

    # 1. Общая информация о датасете
    print('\n1. Общая информация (.info()):')
    df.info(show_counts=True)

    # 2. Пропуски
    missing = df.isna().sum()
    if missing.sum() > 0:
        print('\n2. Пропуски (Missing Values):')
        print(missing[missing > 0])
    else:
        print('\n2. Пропуски: Не обнаружены.')

    # 3. Дубли
    dups = df.duplicated().sum()
    print(f'\n3. Дубликаты строк: {dups}')

    # 4. Первые 3 строки для визуального контроля
    print('\n4. Пример данных (.head(3)):')
    display(df.head(3))