def break_words(stuff):
    """This function will break up words for us."""
# split 分割字符串：使用方式——————字符名称.split（‘分割依据’）  |||下文 分割依据为空格
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words."""
# sorted排序函数
    return sorted(words)  # 此处打错了返回名称导致发生递归超过递归速度导致报错


def print_first_word(words):
    """Prints the first word after popping it off. """
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """Print the last word after popping it off."""
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Print the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
