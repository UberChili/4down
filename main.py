import py8chan
import argparse
import sys
import requests


def main():
    if len(sys.argv) != 5:
        sys.exit("Usage: downloader.py -b <board> -n <thread_number>")

    parser = argparse.ArgumentParser()
    parser.add_argument('-b', help="Board for the thread.")
    parser.add_argument('--board', help="Board for the thread.")
    parser.add_argument('-n', help="Thread number.")
    parser.add_argument('--number', help="Thread number.")
    args = parser.parse_args()

    board = py8chan.Board(args.b)
    thread = py8chan.Board(args.n)

    # print(prep_url(args.b, args.n))


def prep_url(board: str, n: str) -> str:
    url = "https://a.4cdn.org/board/thread/thread_num.json"
    return url.replace("board", board).replace("thread_num", n) # Do the replacement and return in one line


if __name__ == "__main__":
    main()
