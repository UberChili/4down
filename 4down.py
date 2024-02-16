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
    thread = get_response(url)

    process(args.b, thread)
    # for post in thread['posts']:
    #     # if 'filename' in post:
    #         print(post['filename'], post['ext'])


def process(board: str, thread: str):
    url = "https://a.4cdn.org/"
    for post in thread['posts']:
        if 'filename' in post:
            # print(post)
            tim = str(post['tim'])
            filename = post['filename']
            ext = post['ext']
            download_file(board, tim, filename, ext)


def download_file(board: str, tim: str, filename: str, ext: str):
    url = "https://i.4cdn.org/" + board + '/' + tim + ext
    # print(url)
    dest_filename = filename + ext
    print(dest_filename)
    response = requests.get(url)
    if response.ok == True:
        with open(dest_filename, 'wb') as fp:
            fp.write(response.content)



def get_response(url) -> dict:
    r = requests.get(url)
    if r.ok:
        response_dict = r.json()
    else:
        sys.exit("Bad response.")
    return response_dict


def prep_url(board: str, n: str) -> str:
    url = "https://a.4cdn.org/board/thread/thread_num.json"
    return url.replace("board", board).replace("thread_num", n) # Do the replacement and return in one line


if __name__ == "__main__":
    main()
