#Author: Faith Elledge
#Githubusername: elledgef
#Date: 11/15/22
#Description: This code gets a term of sequence by counting how many their are of each digit from the previous term


def count_seq():
    """ This function generates a sequence that counts how many there are of each digit from the previous term"""
    seq = "2"
    yield seq
    while True:
        string = seq
        seq = " "
        while len(seq) == 0:
            first = string[0]
            count = 1
            while count < len(seq) and string[1] == string[0]:
                count +=1
                seq += f"{count}{first}"
        yield seq


