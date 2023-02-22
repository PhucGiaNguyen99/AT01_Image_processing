import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Cast the input to string, int or float type
    parser.add_argument(dest='argument1', type=str, help="A string argument")
    parser.add_argument(dest='argument2', type=int, help="An integer argument")
    parser.add_argument(dest='argument3', type=float, help="A float argument")

    # Validate that the input is in specified list
    parser.add_argument(dest='argument4', choices=['red', 'green', 'blue'])

    args = parser.parse_args()

    print("arg 1: ", args.argument1)

    print("arg 2: ", args.argument2)

    print("arg 3: ", args.argument3)

    print("arg 4: ", args.argument4)
