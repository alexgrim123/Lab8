def main():
    input_code = '000000000000000'
    Cn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Ck = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Mist_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(1, 32768):
        b = bin(i)
        b = b[2:]
        b = '0'*(15-len(b)) + b

        mistakes_count = 0
        list_with_mistakes = input_code + ''

        for bit in range(15):
            if b[bit] == '1':
                list_with_mistakes = list_with_mistakes[0:bit] + str((int(
                    list_with_mistakes[bit]) + 1) % 2) + list_with_mistakes[bit+1:]
                mistakes_count += 1

        Mist_count[mistakes_count] += 1
        if ((int(list_with_mistakes[0]) + int(list_with_mistakes[1]) + int(list_with_mistakes[2]) + int(
                list_with_mistakes[3]) + int(list_with_mistakes[4]) + int(list_with_mistakes[5]) + int(
                list_with_mistakes[6])) % 2 == int(list_with_mistakes[7])):
            mistake_sindrom = '0'
        else:
            mistake_sindrom = '1'

        if ((int(list_with_mistakes[0]) + int(list_with_mistakes[1]) + int(list_with_mistakes[2]) + int(
                list_with_mistakes[3]) + int(list_with_mistakes[8]) + int(list_with_mistakes[9]) + int(
            list_with_mistakes[10]))% 2==int(list_with_mistakes[11])):
            mistake_sindrom += '0'
        else:
            mistake_sindrom += '1'

        if ((int(list_with_mistakes[0]) + int(list_with_mistakes[1]) + int(list_with_mistakes[4]) + int(
                list_with_mistakes[5]) + int(list_with_mistakes[8]) + int(list_with_mistakes[9]) + int(
            list_with_mistakes[12])) % 2 == int(list_with_mistakes[13])):
            mistake_sindrom += '0'
        else:
            mistake_sindrom += '1'

        if ((int(list_with_mistakes[2]) + int(list_with_mistakes[4]) + int(list_with_mistakes[6]) + int(
                list_with_mistakes[8])+ int(list_with_mistakes[10])+ int(list_with_mistakes[12])+ int(
                list_with_mistakes[0] ))% 2==int(list_with_mistakes[14])):
            mistake_sindrom += '0'
        else:
            mistake_sindrom += '1'








        mistakes_bit =15- int(mistake_sindrom, 2)



        if mistakes_bit == 15:
            list_without_mistakes = list_with_mistakes
            Cn[mistakes_count] -= 1

        else:
            list_without_mistakes = list_with_mistakes[0:mistakes_bit] + str((int(
                list_with_mistakes[mistakes_bit]) + 1) % 2) + list_with_mistakes[mistakes_bit+1:]

        if list_without_mistakes == input_code:

            Ck[mistakes_count] += 1
            Cn[mistakes_count] += 1
        else:

            if ((int(list_without_mistakes[0]) + int(list_without_mistakes[1]) + int(list_without_mistakes[2]) == int(
                    list_without_mistakes[3])) and int(list_without_mistakes[0]) + int(list_without_mistakes[1]) + int(
                    list_without_mistakes[4]) == int(list_without_mistakes[5])) and (int(list_without_mistakes[0]) + int(
                    list_without_mistakes[2]) + int(list_without_mistakes[4]) == int(list_without_mistakes[6])):


                Cn[mistakes_count] += 1
            else:

                Cn[mistakes_count] += 1

    print("_________________________________________")
    print('i  |РљРѕР»-РІРѕ   | РСЃРїСЂ. |  РСЃРїСЂ.%')
    print("_________________________________________")

    for n in range(1, 15):
        print('{0:1d}   {1:4d}       {2:4d}    {3:4d}   %'.format(n, Mist_count[n], Ck[n], int((Ck[n])/Mist_count[n])*100))

    print("__________________________________________")


main()
