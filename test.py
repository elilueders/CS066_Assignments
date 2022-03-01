            
import requests

endpoint = "https://en.wikipedia.org/w/rest.php/v1/page/Mars"
response = requests.get(endpoint)
page_results = response.json()
# sometext = page_results["source"][:10000] #use slicing to print only 10000 characters



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

results = get_page_links(page_results["source"])

def get_first_ten(page_source):
    first_ten = []
    for i in range(10):
        # print(i, page_source[i])
        first_ten.append(page_source[i])
    return first_ten

print(get_first_ten(results))