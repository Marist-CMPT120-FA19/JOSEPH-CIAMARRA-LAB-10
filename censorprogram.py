def censor(word):
    for i in range(len(word)):
        if word[i].isalpha():
            word=word[:i] + '*' + word [i+1:]
    return word

def main():
    file= input ("Enter the file name to censor: ")
    text= open(file, 'r')
    words_file= input ("Enter the file name with the censord words: ")
    censored= open(words_file, 'r')
    censorwords= censored.read().split()

    censoredtext= ""
    for line in text:
        words=line.split()

        for i in range(len(words)):
            word= ""
            for letter in words [i]:
                if letter.isalpha():
                    word+= letter
            if word in censorwords:
                words[i]= censor(words[i])
        censoredtext += " ".join(words) + '\n'

        newfile = open("censored:" + f, 'w')
        newfile.write(censored_text)
        text.close()
        censored.close()
        
        newfile=open("censored:" + file, 'w')
        newfile.write(censoredtext)
        newfile.close()

main()
        
