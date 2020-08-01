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
    parser = argparse.ArgumentParser(
        prog="dadjokes", description=f"dadjokes CLI v{dadjokes.__version__}"
    )
    parser.add_argument(
        "-l",
        "--load",
        dest="lpath",
        metavar="PATH",
        nargs="?",
        type=str,
        const="jokes.txt",
        default=None,
        help="load all jokes from a file (faster and offline)",
    )
    parser.add_argument(
        "-d",
        "--download",
        dest="dpath",
        metavar="PATH",
        nargs="?",
        type=str,
        const="jokes.txt",
        default=None,
        help="download all jokes to a file (faster and offline)",
    )
    parser.add_argument("--egg", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()

    if args.egg:
        egg()
    elif args.dpath is not None:
        dadjokes.save_jokes(args.dpath)
        return
    elif args.lpath is not None:
        print(dadjokes.joke(file=args.lpath), end="")
    else:
        print(dadjokes.joke())


if __name__ == "__main__":
    main()
