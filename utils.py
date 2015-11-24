from os import urandom
import google, urllib2, bs4, re

secret_key = urandom(32)

pattern = "[A-Z][a-z]+(?: [A-Z](?:[a-z]+|\.))? [A-Z][a-z]+"

def look_up(query_string):
    results = google.search(query_string, num=10, start=0, stop=10)
    result_list = []
    for result in results:
        print result, "\n"
        try:
            url = urllib2.urlopen(result)
            page = url.read()
            soup = bs4.BeautifulSoup(page, 'html.parser')
            raw = soup.get_text()
            clean = re.sub("[ \t\n]+", " ", raw)
            findings = re.findall(pattern, clean)
            result_list += findings
        except:
            print "error"
    return most_common(result_list)

def most_common(lst):
    return max(set(lst), key=lst.count)
