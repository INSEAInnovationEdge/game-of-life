def is_valid_universe(universe):
    """
    this function checks if the board is a valid universe
    a valid universe is a 2d list where all the lines contain
    0 or 1 and they all have the same size.

    >>> a = [[1, 0], [0, 1], [1, 0], [0, 1]]
    >>> is_valid_universe(a)
    True

    Args:
        universe (list): 2d list 

    Returns:
        boolean : True if the universe is a valid universe, False if not.
    """
    pass

def universe_to_str(universe):
    """
    this function translate the game from binary to charchters

    >>> universe1 = universe_to_str ([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0]])
    >>> print(universe1)
    +----+
    |*   |
    | *  |
    |  * |
    |*   |
    +----+

    Args:
        universe (list): a valid universe 
    """
    pass

def count_live_neighbors(universe, x, y):
    """
    this function returns the number of neighboors to the (x,y) coordination

    >>> universe1 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
    >>> count_live_neighbors(universe1,1,1)
    2

    Args:
        universe (list): a valid 2d list 
        x (int): the line number
        y (int): the row number

    Returns:
        int: the number of neighboors
    """
    pass

def get_next_gen_cell(universe, x, y):
    """
    this function gives the status of the (x,y) coords in the next universe

    >>> universe1 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
    >>> get_next_gen_cell(universe1,1,1)
    1

    Args:
        universe (list): a valid 2d universe 
        x (int): the line number
        y (int): the row number

    Returns:
        int: the status of the element
    """
    pass

def get_next_gen_universe(universe):
    """
    generates the next universe

    >>> universe1 = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
    >>> get_next_gen_universe(universe1)
    [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]

    Args:
        universe (list): a valid 2 universe

    Returns:
        list: the next universe
    """
    pass

def get_n_generations(universe, n):
    """
    generates n generations or the repeated geenrations

    >>> universe1  = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
    >>> universes1 = get_n_generations(universe1, 5)
    >>> len(universes1)
    3
    >>> print(universes1[2])
    +----+
    |    |
    |    |
    |    |
    |    |
    +----+

    Args:
        universe (list): a valid 2 universe
        n (int): number of repitions

    Returns:
        list: a list of the str of the univereses generations 
    """
    pass