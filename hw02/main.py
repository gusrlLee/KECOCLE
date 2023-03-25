from Dice import DiceProbability

def main(n):
    dice_probability = DiceProbability(n)
    dice_probability.calcProbability()
    dice_probability.printProbability()


if __name__ == "__main__":
    N = input()
    main(N)