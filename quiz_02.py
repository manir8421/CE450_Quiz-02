def decode(message_file):
    from_file = []   # Initializes from_file, a list to store each line read from the file
    number_corresponding_word = {}  # a dictionary to map each number as an integer to its corresponding word


    with open(message_file, 'r') as file:  # Opens message_file for reading ('r') and assigns its contents to the variable file. The with statement ensures the file is properly closed
        for line in file:
            line_info = line.strip()   # Strips leading and trailing whitespace from the current line and appends it to the from_file list
            from_file.append(line_info)
            number, word = line_info.split(' ', 1)
            number_corresponding_word[int(number)] = word  # It converts the number part to an integer and then adds an entry to the number_corresponding_word dictionary with the number as the key and the word as the value
    for line in from_file:
        print(line)


    sort_numbers = sorted(number_corresponding_word.keys())  # Creates a sorted list of the keys from number_corresponding_word, ensuring the numbers are in ascending order for pyramid construction
    
    pyr_height = 1  # Initializes pyr_height, which will represent the height of the pyramid, starting at 1
    while len(sort_numbers) > pyr_height * (pyr_height - 1) // 2:
        pyr_height += 1
    '''Increments pyr_height to find the maximum height of the pyramid that can be formed with the given numbers.
    It checks if the total number of sorted numbers is greater than the sum of numbers that can fit in a pyramid
    of one less than the current height, ensuring all numbers can be placed in the pyramid structure.'''
    pyr_height -= 1  # Adjusts pyr_height down by one since the while loop exits when pyr_height exceeds the possible height by 1.
    ''' # calculates the total number of elements that can fit in a complete pyramid of height pyr_height - 1
        # By comparing len(sort_numbers), the total number of numbers available, with the total capacity of a pyramid of height pyr_height - 1, we can determine if adding another level to the pyramid is possible or not.
        # If len(sort_numbers) is greater than the capacity of the current pyramid height, it indicates that the pyramid can be taller, and thus, pyr_height is incremented
        # repeats until the condition is true,the current pyr_height is the maximum height that can accommodate all numbers without exceeding the total count.
        # the condition len(sort_numbers) > pyr_height * (pyr_height - 1) // 2 becomes false,indicates the pyramid has height where adding another levelrequire more numbers than available.
        # Thus, the current pyr_height is the maximum height the pyramid can given the number of elements'''

    get_numbers = []   # Initializes get_numbers to store the numbers at the right edge of the pyramid. mk_pyr is set to control the initial the first level of the pyramid.
    mk_pyr = pyr_height - 1
    number_index = 0  # Initializes number_index to keep track of the current index in sort_numbers while building the pyramid
    for level in range(1, pyr_height + 1):
        print(' ' * mk_pyr, end='')  # Iterates over each level of the pyramid, printing leading spaces (' ' * mk_pyr) to align the numbers aesthetically, without moving to a new line after the spaces (end='')
        for i in range(level):
            if number_index < len(sort_numbers):
                print(sort_numbers[number_index], end=' ') # Checks if there are still numbers to be placed in the pyramid. If so, prints the current number followed by a space, without moving to a new line (end=' ')
                if i == level - 1: # If the current element is the last one in its level (i == level - 1), it adds the number to get_numbers, which stores numbers at the right edge of each level.
                    get_numbers.append(sort_numbers[number_index])
                number_index += 1
        print()
        mk_pyr -= 1  


    decode_corrsp_word = ' '.join([number_corresponding_word[number] for number in get_numbers])  # Constructs the decoded message by joining words corresponding to the numbers
    print("\nDecoding the words from corresponding numbers for right edge line of pyramid:")
    for number in get_numbers:
        print(f"{number}: {number_corresponding_word[number]}")
    print(f"\nFunction return the string:\n \"{decode_corrsp_word}\".")

    return decode_corrsp_word

message_file = 'coding_qual_input.txt'
decode_corrsp_word = decode(message_file) 
