from browser import document

i=0

def click(event):
    print(document["formControlInput"].value)
    document["you-text"] <= document["formControlInput"].value
    document["formControlInput"].value = ""

document["enter"].bind("click", click)