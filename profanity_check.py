# # This program demonstrates how to check profanity of a word or sentence.

import urllib.request

val = "My life is shit."
value = urllib.parse.quote(val)


def prof_check():
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=" + value)
    response = connection.read()
    result = response.decode('utf-8')

    if result:
        print("There is a slang word.")
    else:
        print("There is no slang word.")

    connection.close()

prof_check()
