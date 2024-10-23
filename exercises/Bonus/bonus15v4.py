import webbrowser

user_term = input("Search something: ")
SEARCH_BAR = f"https://www.google.com/search?q={user_term}"

webbrowser.open(SEARCH_BAR)
