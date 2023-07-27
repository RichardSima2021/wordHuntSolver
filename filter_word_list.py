def modifyWords():
    try:
        with open("words.txt", "r") as fr:
            lines = fr.readlines()

            with open("filtered_words.txt", "w") as fw:
                for line in lines:
                    if len(line.strip()) > 2 or len(line.strip()) <= 16:
                        fw.write(line)
                    else:
                        print("Removed " + line)
    except:
        print("Shits fucked up")


if __name__ == "__main__":
    modifyWords()