#import intertools

def main():
    f = open("input.txt", 'r')

    x = []

    for i in f:
        x.append(i)

    part1(x)
    part2(x)

def part1(x):
    c=0
    for i in x:
        c+=int(i)
    print(c)

def part2(x):
    c=0
    y={0:True}
    a=False
    while True:
        for i in x:
            c+=int(i)
            if c in y:
                a=True
                print(c)
                break
            else:
                y[c] = True
        if a:
            break

if __name__ == "__main__":
    main()

