from os import urandom
import google, urllib2, bs4, re

secret_key = urandom(32)

pattern = "[A-Z][a-z]+(?: [A-Z](?:[a-z]+|\.))? [A-Z][a-z\-]+[A-Z]*[a-z]*"

common_list = ["yes", "no", "the",
               "and", "or", "a",
               "amazing", "man", "wonder",
               "spectacular", "action", "comics",
               "arrow", "green", "blue",
               "black", "super", "hero",
               "justice", "league", "america",
               "hall", "team", "friends",
               "canary", "cat", "dog",
               "woman", "girl", "boy",
               "permalink", "hide", "warner",
               "bros", "dc", "marvel",
               "dark", "knight", "white",
               "retrieved"]


def look_up(query_string):
    results = google.search(query_string, num=10, start=0, stop=10)
    result_list = []
    link_list = []
    for result in results:
        print result
        try:
            url = urllib2.urlopen(result)
            page = url.read()
            soup = bs4.BeautifulSoup(page)
            raw = soup.get_text()
            spacer = re.sub("[ \t\n]+", " ", raw)
            
            uncommon = clean_common(spacer)
            findings = re.findall(pattern, uncommon)
            result_list += findings
        except:
            print "Error Bad Link: ", result
    return most_common(result_list)


def most_common(lst):
    """Returns the most common word(s) in a given text                                                               
 
    Arguments:                                                                                                        
    lst: a list of words found in a text                                                                             
    
    Returns:                                                                                                              
    >>> most_common([])
    None

    >>> most_common(["test"])                                                                                    
    "test"
    
    >>> most_common(["Wow","What Is Sleep","Wow","Queue Queue","Wow"])                                           
    "Wow"                                                                                                       
    """ 
    return max(set(lst), key=lst.count)


def clean_common(string):
    """Returns a new string with all the common words (in the list above) removed

    Arguments:
    string: the string of text

    Returns:
    
    >>> clean_common("the the the the pizza"):
    "pizza"

    >>> clean_common("the the the the a the the"):
    ""

    """
    lst = string.split(" ")
    i = 0
    while i < len(lst):
        if lst[i].lower() in common_list:
            lst.remove(lst[i])
        else:
            i += 1
    return " ".join(lst)

def test_one():
    string = "hello hello hello hi hi hi hi the the the the the the"
    lst = string.split(" ")
    print "Given " + string
    print "clean_common returns " + clean_common(string)
    print "most_common returns " + most_common(lst)
