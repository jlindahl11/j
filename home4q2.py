# Jonathan Lindahl
# 2/9/2024
# Youtube Link: https://youtu.be/1KWcwSNYONo
# I have not given or received any unauthorized assistance on this assignment.


def humanPyramid(row, column):
    """Calculate the weight on a person's back in a human pyramid.

    Each person weighs 128 pounds. The weight on each person is the sum of half the weight
    of the person above and the full weight of the person.
    
    Args:
    row: An integer, the row number of the person, 0 indexed.
    column: An integer, the column number of the person, 0 indexed.
    
    Returns:
    The total weight on that person's back.
    """
    person_weight = 128  # weight of each person
    # Base case: If it's the top of the pyramid, no weight is above them.
    if row == 0:
        return 0
    # If the person is at the edge, only one person is above them.
    elif column == 0 or column == row:
        return 0.5 * humanPyramid(row - 1, column if column == row else column - 1) + person_weight
    # General case: Split the weight from the person above and add the person's weight.
    else:
        return 0.5 * (humanPyramid(row - 1, column - 1) + humanPyramid(row - 1, column)) + person_weight


