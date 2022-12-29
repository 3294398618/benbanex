import ex25
sentence = "All good things come to those who wait."
words = ex25.break_words(sentence)     # 调用函数将字符串sentence打散变成列表赋值给words
words
sorted_words = ex25.sort_words(words)  # 调用函数将数组排序
sorted_words
ex25.print_first_word(words)           # 打印了words的第一个
ex25.print_last_word(words)            # 打印了words的最后一个
words
ex25.print_first_word(sorted_words)    # 打印了sorted——words的第一个
ex25.print_last_word(sorted_words)     # 打印了sorted——words的最后一个
sorted_words
sorted_words = ex25.sort_sentence(sentence)
sorted_words
ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)