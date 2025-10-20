class TDDExample():
    def __init__(self):
        pass

    def reverse_string(self, input_str: str) -> str:
        """
        Reverses order of characters in string input_str.
        """
        return input_str[::-1]

    def find_longest_word(self, sentence: str) -> str:
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        words = sentence.split(" ")
        longest_word = max(words, key=len)
        return longest_word

    def reverse_list(self, input_list: list) -> list:
        """
        Reverses order of elements in list input_list.
        """
        res =[]
        for i in range(len(input_list)-1, -1, -1):
            res.append(input_list[i])
        return res

    def count_digits(self, input_list: list, number_to_be_counted: int) -> int:
        """
        Return count of digits
        """

        return len(set(input_list))
    