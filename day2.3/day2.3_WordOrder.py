def main():
    num = int(input())
    word_dict = {}
    for i in range(num):
        word = input()
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    print(word_dict.items().__len__())
    for key, value in word_dict.items():
        print(value, end=' ')

if __name__ == '__main__':
    main()