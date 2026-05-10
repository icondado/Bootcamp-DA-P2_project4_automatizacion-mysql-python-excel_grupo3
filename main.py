import sys
import os

src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
sys.path.append(src_path)

from sakila_ETL import conection_bd
from sakila_ETL import test_connection
from sakila_ETL import get_data_list_from_join

if __name__ == "__main__":
    test_connection()
    get_data_list_from_join()