def hands_of_blue(my_list) -> bool:
    """Determine if a list contains pairs.

    This function determines whether the elements of a list are in pairs - the
    first two elements are the same, the next two elements are the same, etc.
    The function should return True if that's the case, and False otherwise.

    NOTE: Your solution *must* use a loop.

    Arguments:
        my_list (list): A list of strings. Assume the list is not empty.

    Returns:
        bool: True if the list only contains pairs, False otherwise.

    Examples:

        >>> print(hands_of_blue(["partridge", "partridge", "dove", "dove"]))
        True

        >>> print(hands_of_blue(["hen", "songbird", "goose", "swan", "swan"]))
        False

        >>> print(hands_of_blue(["cow", "bull", "doe", "stag", "ewe", "ram"]))
        False

    """
    if len(my_list) % 2 == 1:
        print(len(my_list))
        return False
    i = 0
    k = 0
    for string in my_list:
        if my_list[i] == my_list[i+1]:
            i += 2
            k += 1
        else:
            return False
        if len(my_list) / 2 == k:
            return True
    return True

def delete_range(my_str, ranges) -> str:
    """Delete specified ranges from a string.

    This function takes a string and lists of indices, and returns a new string
    with the characters between those indices deleted. You may not use the del
    statement.

    NOTE: Although this question shows up on the autograder, there are NO test
    cases for it. You are responsible for creating your own test cases to make
    sure it works. You do not need to submit your testcases.

    Arguments:
        my_str (str): The string to be modified.
        ranges (list): A list of [start, end] indices. You may assume that both
            start and end are valid indices (ie. between 0 and len(my_str),
            inclusive), and that start <= end. You may further assume that the
            ranges are sorted from earliest to latest (ie. [0, 10] will come
            before [15, 20]), and that the ranges will not overlap.

    Returns:
        str: The string with the specified indices deleted.

    Examples:

       >>> s = "computer science"
        >>> indices = [[4, 8], [12, 16]]
        >>> print(delete_range(s, indices))
        comp sci

        >>> s = "Aren't you a little short for a stormtrooper?"
        >>> indices = [[20, 37]]
        >>> print(delete_range(s, indices))
        Aren't you a little trooper?

    """
    answer = ''
    for start, end in reversed(ranges):
        answer = my_str[:start] + my_str[end:]
    return answer

def peer_evals(ratings: list):
    """Calculate scores from a peer evaluation.

    Imagine a class where every student has rated every other student. A table
    that shows the peer evaluation ratings might look something like this:

             Alice  Bob  Charlie  Daryl
    Alice       -1    7       -1      0
    Bob          4   -1        7      5
    Charlie      5    7       -1     10
    Daryl        6    7        9     -1

    In this table, the rows are the ratings (out of 10) given to the columns.
    For example, Bob gave Alice a 4, and Charlie gave Daryl a 10. Since ratings
    go from 0 to 10, missing or inapplicable ratings are noted with a -1. This
    is the case for every student's rating for themselves, and in this case,
    Alice also did not give Charlie a rating.

    The overall peer evaluation score for each student is determined by two
    factors:

    * The maximum possible peer evaluation score is determined by whether the
    student has completed a rating for everyone. In this class of four students,
    each student should have rated three other student. Because Alice only rated
    two other students, her maximum possible score is 2/3 * 10 = 6.666.

    * The average rating from their peers, equivalent to the average of the
    numbers in a column (ignoring the -1's). For Alice, her peers have given her
    a 4, a 5, and a 6, to get an average of 5.

    The final peer evaluation score is the product of these two numbers, so for
    Alice, her final score is 6.666 * 5 = 33.33.

    This functional takes the ratings as a nested list of integers, and returns
    a list of the overall score for each student. The final score should be
    rounded to two decimal places; you can do this with the round() function,
    eg. round(n, 2) will return the decimal number n rounded to two decimal
    places. This final result should be the only place you do any rounding.

    NOTE: Because this question is fairly complex, I recommend defining
    additional functions that can help with parts of the problem. Any functions
    you write MUST contain a docstring comment (like this one) that explains
    what it does and how to use it, with examples. You will not be graded on
    these other functions, but they will be checked for style issues.

    Arguments:
        ratings (list): A nested list of peer evaluation ratings. You may assume
            that everyone has received at least one rating, and that their
            rating from themselves will always be -1. This nested list will
            always have as many rows as it does columns.

    Returns:
        list: A list of the final score for each student.

    Examples:

       >>> print(peer_evals([ \
                [ -1,  7, -1,  0 ], \
                [  4, -1,  7,  5 ], \
                [  5,  7, -1, 10 ], \
                [  6,  7,  9, -1 ], \
            ]))
        [33.33, 70.0, 80.0, 50.0]

    """
    max_value_list = []
    for row in ratings:
        max_value = determine_max_value(row)
        max_value_list.append(max_value)

    average_grade_list = []
    num_of_rows = len(ratings)
    for i in range(num_of_rows):
        column_list = []
        for row in ratings:
            column_list.append(row[i])
        average_grade = determine_average_grades(column_list)
        average_grade_list.append(average_grade)

    import operator
    final_score_list = []
    final_score_list = list(map(operator.mul, max_value_list, average_grade_list))
    final_score = []
    num3 = len(final_score_list)
    for i in range(num3):
        final_score.append(round(final_score_list[i], 2))
    return final_score

def determine_max_value(user_ratings: list):
    """
    This function takes a row from peer_evals list and determines the maximum possible peer
    evaluation score the student can get. It determines if there is more than one "-1" rating,
    and divides it by 3.

    Args:
        user_ratings: A list of rating given by the student.

    Returns:
        The maximum possible peer evaluation score.

    """
    j = len(user_ratings)
    for rating in user_ratings:
        if rating == -1:
            j -= 1
    max_value = j/(len(user_ratings)-1) * 10

    return max_value

def determine_average_grades(user_grades: list):
    """
    This function take a column from the peer_evals list and averages the grades.

    Args:
        user_grades: A list of grades for each student.

    Returns: The mean of the grades.

    """
    grades = []
    count = len(user_grades)
    for i in range(count):
        if user_grades[i] != -1:
            grades.append(user_grades[i])
    num = len(grades)
    average_grade = sum(grades) / num
    return average_grade
