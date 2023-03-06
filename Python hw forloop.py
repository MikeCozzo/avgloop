
def main(x):
    prints(x)


def prints(x):
    numbers = open(x, 'r')
    y = 1
    total = 0
    for line in numbers:
        amount = float(line)
        total = total + amount
        print ('I read in', y, 'number(s) Current number is', amount, 'total is:', total)
        y += 1
    avg = (int(total) / 3)
    print (format(avg, '.2f'))

    
if __name__ == '__main__':
    main('numbers.txt')
        
