import queue
from urllib import response
import requests
from pythonds.basic import Queue

def get_page_links(wikitext):
    """
    Get a list of all Wikipedia pages linked to from some wikitext
    
    Paremeters:
        wikitext: a string with some wikitext
        
    Returns:
        a list of the titles of all Wikipedia pages that are linked to
        from the provided wikitext
    """
    list_of_linked_pages = []
    i = 0
    while i < len(wikitext):
        #is this the start of a wiki link?
        if wikitext[i:i+2] == "[[":
            
            i = i+2
            linked_page_name = "" #accumulator string
            
            #keep adding on to the accumulator string until we see a
            # | or ] which will indicate we've reached the end of the
            # linked page's name
            while wikitext[i] != '|' and wikitext[i] != ']':
                linked_page_name += wikitext[i]
                i += 1
            
            list_of_linked_pages.append(linked_page_name)
                
        #move on to the next character
        else:
            i += 1
    return list_of_linked_pages

def get_wiki_page_results(wiki_title):
    url = "https://en.wikipedia.org/w/rest.php/v1/page/" + wiki_title
    response = requests.get(url)
    return response.json()

#Define your explore_wiki function here
def explore_wiki(wiki_title, num_pages):
    q_to_explore = Queue()
    explored = set()
    #test 
    print(get_wiki_page_results(wiki_title)["source"][:num_pages])

mars_related = explore_wiki("Mars",1000)
print( mars_related )
# print( len(mars_related) )

cpu_related = explore_wiki("Central Processing Unit",10000)
print( cpu_related )
# print( len(cpu_related) )
