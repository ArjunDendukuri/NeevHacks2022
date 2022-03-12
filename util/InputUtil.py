def get_num(prompt, error):
    while True:
        try:
            num = int(input(prompt))
            return num
        except:
            print(error)