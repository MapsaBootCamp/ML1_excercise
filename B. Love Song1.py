import string


def calculate_the_number_of_the_letters(poem: str, beginning_number, end_number) -> int:
    alphabets = list(string.ascii_lowercase)
    result_string = []

    subsegment = poem[beginning_number: end_number]

    for letter in subsegment:
        index_of_letter = alphabets.index(letter)
        result_string.append((letter * (index_of_letter + 1)))

    str1 = ''.join(result_string)
    return len(str1)


def do():
    first_line_input = input(
        "Please enter the length of your poem string as first number and then\n"
        "the number of your question as Second number: ")

    input1 = first_line_input.split()

    valid_length_of_string = int(input1[0])
    number_of_question = int(input1[1])

    poem_string = input("please insert your poem: ")

    if len(poem_string) == valid_length_of_string:

        list_of_question_ranges = []

        for i in range(number_of_question):
            length_of_subsegment = input("Please insert the range of your subsegment: ")
            input2 = length_of_subsegment.split()

            list_of_question_ranges.append(int(input2[0]))
            list_of_question_ranges.append(int(input2[1]))

        for i in range(number_of_question):
            beginning_of_range = int(list_of_question_ranges.pop(0)) - 1
            end_of_range = int(list_of_question_ranges.pop(0))

            print(calculate_the_number_of_the_letters(poem_string, beginning_of_range, end_of_range))

    else:
        raise Exception("The length of the poem must be equal with value of the valid_length_of_string")


do()
