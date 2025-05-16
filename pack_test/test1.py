# %%
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from pack_test.kadai_E_1 import kadai_E_1


def main():
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter,
        description="Test script for kadaiE1.",
    )

    parser.add_argument(
        "-i",
        "--input1",
        help="argument for input1",
        type=str,
    )
    parser.add_argument(
        "-l",
        "--input2",
        help="argument for input2",
        type=int,
    )

    args = parser.parse_args()
    kadai_E_1(args.input1, args.input2)


if __name__ == "__main__":
    main()
# %%
