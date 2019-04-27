from tagger import *


def main():
    readfile = open('joji1.txt', 'rU', encoding="ISO-8859-1").read()

    tag_test_class = Tagger(readfile)

    tag_test_class.pos_tagger()

    tag_test_class.most_common_tag()


    common_tag_val = tag_test_class.return_value('common_part_speech')
    print(common_tag_val)
    print(common_tag_val.most_common())

if __name__ == '__main__':
    main()
