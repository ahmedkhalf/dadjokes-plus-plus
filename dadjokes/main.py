import argparse
import dadjokes


def main():
    parser = argparse.ArgumentParser()
    parser.parse_args()

    print(dadjokes.joke())


if __name__ == "__main__":
    main()
