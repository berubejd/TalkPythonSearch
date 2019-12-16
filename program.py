#!/usr/bin/env python3.8

import api
import os
import webbrowser


def main():
    try:
        keyword = input("What search KEYWORD would you like to look for? ")

    except KeyboardInterrupt:
        print()
        os.sys.exit()

    results = api.search_by_keyword(keyword)

    count = len(results)

    print()
    print(f"Your search for {keyword} resulted in {count} matches!")
    print()

    if count == 0:
        os.sys.exit()

    for i, episode in enumerate(results, 1):
        print(f"{i}.  {episode.category} - {episode.title}")

    print()

    choice = ""
    while not choice in range(1, count + 1):
        try:
            choice = input("Which item would you like to view? (Enter QUIT to exit) ")

        except KeyboardInterrupt:
            print()
            os.sys.exit()

        if choice.lower() == "quit":
            os.sys.exit()

        try:
            choice = int(choice)
        except ValueError:
            continue

    webbrowser.open(f"https://talkpython.fm{results[choice - 1].url}", new=2)


if __name__ == "__main__":
    main()
