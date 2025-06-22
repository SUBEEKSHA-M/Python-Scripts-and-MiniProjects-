#phrase

def main():
    yell("This is CS50")

def yell(phrase):
    print(phrase.upper())

if __name__=="__main__":
    main()

#words

def main():
    yell("This is CS50")

def yell(words):
    for word in words:
        print(word, end="")

if __name__=="__main__":
    main()