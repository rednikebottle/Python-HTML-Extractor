from bs4 import BeautifulSoup

with open("(Html file)", "r") as file:
    html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")

    element_with_class = soup.find_all(class_="(Class id)")
    
    # if there are multiple items in the same class
    for element in element_with_class:    
        print(element.string)
