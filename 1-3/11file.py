#file = open("11tool.py")

def main():

    #print(__doc__)

    file = open("readme",encoding="UTF-8")

    text = file.read()

    print(text)

    file.close()

if __name__ == "__main__":
    main()