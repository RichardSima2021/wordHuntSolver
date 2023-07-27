consonant_blends = {
    'b':{'bl','br'},
    'c':{'cl','cr','ch'},
    'd':{'dr'},
    'f':{'fr','fl'},
    't':{'tr','th'},
    'g':{'gl','gr'},
    'p':{'pr','pl'},
    's':{'sl','sm','sp','st','sh','sn','sc','sk','sw'},
    'w':{'wh','wr'}}

vowels = {'a','e','i','o','u','y'}

letter_indices = {
    'A':0, 'B':16202, 'C':31437, 'D':56479, 'E':73099, 'F':84433, 'G':95067, 'H':104420,'I':114944,
    'J':124548, 'K':126859, 'L':130254, 'M':138312, 'N':154138, 'O':160706, 'P':169601, 'Q':193947,
    'R':195358, 'S':210379, 'T':242373, 'U':256942, 'V':266466, 'W':271056, 'X':276979, 'Y':277288, 'Z':278324}


def take_input():
    board = []
    for i in range(4):
        line = input()
        while len(line) != 4:
            line = input("A line can only have 4 chars")

        line = line.upper()
        board.append(list(line))

    return board

def print_board(board):
    for line in board:
        print(line)

def load_words():
    try:
        with open("filtered_words.txt", "r") as word_list:
            lines = list(word_list.readlines())
            return lines
    except:
        print("Shits fucked up")


def find_words(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            board_status = [
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]
            ]
            board_status[r][c] = 1
            start_char = board[r][c]

            list_start_index = letter_indices[start_char]
            list_end_index = -1
            if start_char != 'Z':
                list_end_index =  letter_indices[list(letter_indices.keys())[list(letter_indices.keys()).index(start_char) + 1]]
            # what this abomination does: take the keys of letter_indices as a list
            # find the index of start_char in that list
            # add one to it
            # that's now the start index of the next char in the list aka where our word search will end
            # use that index and get the character from the letter_indices keys
            # then use that character to find the letter_index
            dfs(start_char, r, c, board_status)

def dfs(cur_str, row, col, board_status):
    pass

if __name__ == '__main__':

    board = take_input()
    print_board(board)


    words = load_words()

    # get word indices
    # for i in range(1,len(words)):
    #     if words[i][0] != words[i-1][0]:
    #         print(words[i][0], i)
    #     else:
    #         if words[i][0] == 'Z':
    #             break

    find_words(board)
