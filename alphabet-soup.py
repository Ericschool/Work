# Load a character grid with scrambled words embedded within it and a words list of the words to find.  The following conditions apply:
# * Within the grid of characters, the words may appear vertical, horizontal or diagonal.
# * Within the grid of characters, the words may appear forwards or backwards.
# * Words that have spaces in them will not include spaces when hidden in the grid of characters.

def search_horizontaly(words_to_find, search_text):
    """
    This function searchs the search_text horizontally
    :param words_to_find: the multi dimentional list
    :param search_text:  the string to be searched
    """
    found_index = -1
    for idx, i in enumerate(words_to_find):       
        horizontal = ''.join(i)
        if search_text in horizontal:
            found_index = horizontal.index(search_text)
            return [(idx, found_index), (idx, found_index + len(search_text))]
    return -1


def search_verticaly(words_to_find, search_text):
    """
    This funciton searches the string vertically
    :param words_to_find: the multi dimentional list
    :param search_text:  the string to be searched
    """
    for row in range(len(words_to_find)):
        vertical_word = ''
        for col in range(len(words_to_find[0])):
            vertical_word += words_to_find[col][row]
        if search_text in vertical_word:
            found_index = vertical_word.index(search_text)
            return [(found_index, row), (found_index + len(search_text) -1, row)]
    return -1


def search_horizontaly_backword(words_to_find, search_text):
    """
    This funciton searches the string horizontally backword
    :param words_to_find: the multi dimentional list
    :param search_text:  the string to be searched
    """    
    found_index = -1
    for idx, i in enumerate(words_to_find):       
        horizontal = ''.join(i)
        if search_text[::-1] in horizontal:
            found_index = horizontal.index(search_text[::-1])
            return [(idx, found_index + len(search_text) -1), (idx, found_index)]
    return -1


def search_verticaly_backword(words_to_find, search_text):
    """
    This funciton searches the string vertically backword
    :param words_to_find: the multi dimentional list
    :param search_text:  the string to be searched
    """
    for row in range(len(words_to_find)):
        vertical_word = ''
        for col in range(len(words_to_find[0])):
            vertical_word += words_to_find[col][row]
        if search_text[::-1] in vertical_word:
            found_index = vertical_word.index(search_text[::-1])
            return [(found_index + len(search_text) -1, row), (found_index, row)]
    return -1


def search_diagonaly(words_to_find, search_text):
    """
    This funciton searches the string diagonally
    :param words_to_find: the multi dimentional list
    :param search_text:  the string to be searched
    """
    diagonal_word = ''
    for i in range(len(words_to_find[0])):
        diagonal_word += words_to_find[i][i]
    if search_text in diagonal_word:
        found_index = diagonal_word.index(search_text)
        return [(found_index, found_index), (found_index + len(search_text) -1, found_index + len(search_text) -1)]
    return -1


def print_helper(coordinates):
    """
    This funciton returned a formated coordinate 
    :param coordinates: list of coordinate tuples
    """    
    coordinates_str = ''
    for i in coordinates:
        coordinates_str += '{}:{} '.format(i[0], i[1])
    return coordinates_str

        
def main():
    crossword = []
    words_to_find = []
    grid_size = []

    with open('input.txt') as fp:
        for line in fp:
            if ' ' in line:
                crossword.append(line.strip().split(' '))
            elif 'x'.lower() in line:
                grid_size.append(line.strip().split('x'))
            else:
                words_to_find.append(line.strip())

    for query in words_to_find:
        # -- search string horizontaly
        horizontal = search_horizontaly(crossword, query)
        if horizontal != -1:
            print(query, print_helper(horizontal))

        # -- search vertically
        vertical = search_verticaly(crossword, query)
        if vertical != -1:
            print(query, print_helper(vertical))

        # -- search diagonal
        diagonal = search_diagonaly(crossword, query)
        if diagonal !=  -1:
            print(query, print_helper(diagonal))

        # -- search horizontal backword
        horizontal_backword = search_horizontaly_backword(crossword, query)
        if horizontal_backword != -1:
            print(query, print_helper(horizontal_backword))

        # -- search vertical backword
        vertical_backword = search_verticaly_backword(crossword, query)
        if vertical_backword != -1:
            print(query, print_helper(vertical_backword))

if __name__ == "__main__":
    main()