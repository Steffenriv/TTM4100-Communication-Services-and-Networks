def inverter(number1, number2):
    newNum = len(number1) * '0'
    for i in range(len(number1)):
        if(number1[i] == '0' and number2[i] == '0'):
            newNum = newNum[:i] + '1' + newNum[i + 1:]
        else:
            newNum = newNum[:i] + '0' + newNum[i + 1:]
    return newNum
    
def checksum(word1,word2,word3):
    answer1 = inverter(word1, word2)
    answer2 = inverter(answer1, word3)

    return answer2

print('Task 1:')
print(checksum('01010011', '01100110', '01110100'))
print('Task 2:')
print(checksum('0101001101100110', '0111010010110100', '0000110111000001'))
print('Task 3:')
print(checksum('1010011000111010', '1110100100001011', '0111100000111110'))
print('Task 4:')
print(checksum('1000100010001000', '0000111100001111', '1111111111111111'))
