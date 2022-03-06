import queue
from re import I
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

def request_wiki_page_results(wiki_title_req):
    url = "https://en.wikipedia.org/w/rest.php/v1/page/" + wiki_title_req
    response = requests.get(url)
    return response.json()


#Define your explore_wiki function here
def explore_wiki(wiki_title, num_pages_requested):
    cur_wiki_page_results = request_wiki_page_results(wiki_title)
    q_to_explore = Queue() #1. initialize an empty _queue_ for keeping track of page titles that you haven't yet explored
    set_explored = set() #2. initialize an empty _set_ <a href="#footnote2">[Note 2]</a> for keeping track of page titles that you have already explored
    
    # if "source" in cur_wiki_page_results:
    # q_to_explore.enqueue("Sucker")
    q_to_explore.enqueue(wiki_title) #3. Enqueue the starting page
    
    while len(set_explored) < num_pages_requested: #4. While you haven't yet explored enough pages
        # x = q_to_explore.dequeue()
        # y = request_wiki_page_results(x)

        cur_wiki_page_results = request_wiki_page_results(q_to_explore.dequeue()) #Dequeue the next page to explore
         #Explore it by requesting the page from the Wikipedia API
    
        if "source" in cur_wiki_page_results:    #Check if the request worked <a href="#footnote3">[Note 3]</a>. If it did and you haven't already explored this page, then...
            # print(True)
            set_explored.add(cur_wiki_page_results["title"])    #add the current page to your set of explored pages
            all_links = get_page_links(cur_wiki_page_results["source"])
            
            #test
            print(cur_wiki_page_results["key"])
            print(len(all_links),"explored: ",len(set_explored))
            
            for i in range(10):
                if i < len(all_links):
                    
                    q_to_explore.enqueue(all_links[i]) #retrieve the first 10 outgoing links from the current page <a href="#footnote4">[Note 4]</a> and enqueue them so you can open and explore it on some future iteration of the loop
        else: 
            print("no source in link")
    return set_explored


# explore_wiki("Mars",10)
# for x in request_wiki_page_results("File:Mars symbol (bold).svg"):
#     print(x)



mars_related = explore_wiki("Mars",150)
print( mars_related )
print( len(mars_related) )

"""
cpu_related = explore_wiki("Central Processing Unit",10000)
print( cpu_related )
# print( len(cpu_related) )
"""