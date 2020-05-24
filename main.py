from parsetheURL import parsetheURLPage
from createJson import createJson

inputUrlMapping = {
  "1": "https://www.mongodb.com/alerts",
  "2": "https://helpx.adobe.com/security/products/acrobat/apsb20-13.html",
  "3": "Enter your Url"
}

def readUserInput():
    val = input("Enter your value to parse: \n 1. {} \n 2. {} \n 3. {}\n".format(inputUrlMapping.get("1"), inputUrlMapping.get("2"), inputUrlMapping.get("3"))) 
    # print(type(val))
    if val == "3":
        urlInput = input("Please enter URL to parse:")
    elif inputUrlMapping.get(val) == None:
        print("Invalid input")
        urlInput = input("Please enter URL to parse:")
    else:
        urlInput = inputUrlMapping.get(val)

    print("input url: {}".format(urlInput))

    # url= "https://helpx.adobe.com/security/products/acrobat/apsb20-13.html"
    # url= "https://www.mongodb.com/alerts"
    # url= "https://www.google.com/"
    # parse the URL web Page
    
    # parsetheURLPage(urlInput)
    return urlInput


if __name__ == "__main__":
    inputUrl = readUserInput()
    parsedObj = parsetheURLPage(inputUrl)
    createJson(parsedObj)
