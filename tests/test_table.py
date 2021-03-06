import random

import numpy as np
from nose import with_setup

from pypair.contingency import BinaryTable, CategoricalTable, ConfusionMatrix


def setup():
    """
    Setup.
    :return: None.
    """
    np.random.seed(37)
    random.seed(37)


def teardown():
    """
    Teardown.
    :return: None.
    """
    pass


@with_setup(setup, teardown)
def test_confusion_matrix_creation():
    """
    Tests creating ConfusionMatrix.

    :return: None.
    """
    a = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    b = [0, 0, 0, 1, 1, 0, 0, 1, 1, 1]

    table = ConfusionMatrix(a, b)
    for measure in ConfusionMatrix.measures():
        stats = table.get(measure)
        if isinstance(stats, tuple):
            print(f'{stats[0]:.8f}, {stats[1]:.8f}: {measure}')
        else:
            print(f'{stats:.8f}: {measure}')


@with_setup(setup, teardown)
def test_binary_table_creation():
    """
    Tests creating BinaryTable. The data is simulated from this `site <https://www.mathsisfun.com/data/chi-square-test.html>`_.

    :return: None.
    """
    get_data = lambda x, y, n: [(x, y) for _ in range(n)]
    data = get_data(1, 1, 207) + get_data(1, 0, 282) + get_data(0, 1, 231) + get_data(0, 0, 242)
    a = [a for a, _ in data]
    b = [b for _, b in data]

    table = BinaryTable(a, b)
    for measure in BinaryTable.measures():
        stats = table.get(measure)
        if isinstance(stats, tuple):
            print(f'{stats[0]:.8f}, {stats[1]:.8f}: {measure}')
        else:
            print(f'{stats:.8f}: {measure}')


@with_setup(setup, teardown)
def test_categorical_table_creation():
    """
    Tests creating CategoricalTable.

    :return: None.
    """
    a = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    b = [0, 0, 0, 1, 1, 0, 0, 1, 1, 1]

    table = CategoricalTable(a, b)
    chisq = table.get('chisq')
    phi = table.get('phi')
    print(chisq, phi)
