def get_num(prompt:str, error:str)-> int:
    while True:
        try:
            num = int(input(prompt))
            return num
        except:
            print(error)