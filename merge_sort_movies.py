import json
from pprint import pprint #for displaying the data in an easier-to-read way

with open("HighestGrossingMovies.json") as moviefile:
    movies = json.load(moviefile)
    
    
def mergeSort(alist,bloop):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf,bloop)
        mergeSort(righthalf,bloop)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            # if lefthalf[i]["World Sales"] <= righthalf[j]["World Sales"]:
            if lefthalf[i][bloop] >= righthalf[j][bloop]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
x = "Title"
mergeSort(movies,x)
pprint(movies[:10][])