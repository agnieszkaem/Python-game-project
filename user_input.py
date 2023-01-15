
def get_positive_int(txt):
    """
    gets input and returns a positive integer number from a player
    """
    while True:
        while True:
            num = input(txt)
            if num.lstrip("-").isdigit():
                break
        n=int(num)
        if n>0:
            break
    return n

def get_key(txt):
    """
    gets an input and returns a key indicated by the player to open the next stage
    """
    print("I suppose you posses a key to another place. Then, select the key to the place you want to visit!")
    while True:
        x = get_positive_int(txt)
        if x in range(0,4):
            break
    return x


def give_non_empty_str(txt):
    """
    gets input as non-empty string and returns it if valid
    """
    
    while True:
        data=input(txt)
        if len(data)!=0:
            break
    return data


#.