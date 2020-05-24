import json

def createJson(inputString):
    # print("root: {}".format(root))

    jsonObj = json.dumps(inputString, indent=2)

    # name the output file to write to local disk
    out_filename = "output.json"

    # opens file
    f = open(out_filename, "w")


    f.write(jsonObj)

    f.close()  # Close the file