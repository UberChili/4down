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


    url = prep_url(args.b, args.n)
    # print(url)
    get_response(url)


def get_response(url):
    r = requests.get(url)
    if r.ok:
        response_dict = r.json()
    else:
        sys.exit("Bad response.")
    print(response_dict)


def prep_url(board: str, n: str) -> str:
    url = "https://a.4cdn.org/board/thread/thread_num.json"
    return url.replace("board", board).replace("thread_num", n) # Do the replacement and return in one line


if __name__ == "__main__":
    main()
