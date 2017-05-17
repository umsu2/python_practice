# algorithm to determine if string has all unique characters


def is_unique(value : str) ->bool: #this will be O(n^2)
    #simple implementation, go through each char, and see if it's in the whole string
    for char in value:
        counter = 0
        for test_char in value:
            if test_char == char:
                counter += 1
        if counter > 1:
            return False
    return True

def is_unique3(value):
    #with datastruct, this will be O(n),
    hash_table = {}
    for char in value:
        if char in hash_table:
            return False
        hash_table[char] = char
    return True

def is_unique2(value: str) -> bool:
    #do a sort, each sort compare with previous, if same, not unique
    #this will be o(log(n))
    sorted_str = sorted(value)
    for index in range(len(sorted_str)-1):

        if sorted_str[index] == sorted_str[index+1]:
            return False

    return True

def main():
    input_string = 'abcdefga'
    print(is_unique(input_string))
    print(is_unique2(input_string))
    print(is_unique3(input_string))


if __name__ == '__main__':
    main()