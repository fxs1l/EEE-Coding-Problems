def str_asterisk(text):
    x = text.split()
    for i in range(len(x)):
        asterisk = ''
        for j in range(len(x[i])):
            if i==j:
                asterisk += '*'
            else:
                asterisk += x[i][j]
        x[i] = asterisk
    print(x)

if __name__ == "__main__":
    text = input()
    str_asterisk(text)
    
