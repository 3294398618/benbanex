# 不知道是调用的什么但是和之前学的不一样不需要在程序开始的时候提交参数
import sys
script, encodings, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()
# 该if语句内嵌在main里面要缩进
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()                               # 拼写错误strip
    raw_bytes = next_lang.encode(encoding, errors=errors)  # 拼写错误encode
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, encodings, error)