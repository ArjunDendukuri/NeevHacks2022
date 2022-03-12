from json import load
import item.JsonParser

def main():
    #make the rendering in this file or another one if you want
    # also pls replace the print text with like on screen stuff
    print("Press enter to start!") # you can replace enter with a butto
    input("")
    start()


if __name__ == "__main__":
    main()

def start():
    item.JsonParser.load()
    pass
