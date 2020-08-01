import argparse
import dadjokes


def egg():
    print(
        """
        ████
      ██░░░░██
    ██░░░░░░░░██
    ██░░░░░░░░██
  ██░░░░░░░░░░░░██  Congratulations!
  ██░░░░░░░░░░░░██  You are one of the few people who read my code.
  ██░░░░░░░░░░░░██  Here is an egg.
    ██░░░░░░░░██
      ████████
    """
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--egg", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()

    if args.egg:
        egg()
        return

    print(dadjokes.joke())


if __name__ == "__main__":
    main()
