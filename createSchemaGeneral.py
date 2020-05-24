from createJson import createJson
from datetime import datetime

root = {
	"type":"vendor",
}

def createSchemaGeneral(cvsinput, vendor, url):

    timestamp = datetime.now().timestamp()
    date_time = datetime.fromtimestamp(timestamp).strftime("%d %B, %Y")
    type(date_time)
    root["source"]= vendor
    cves=[]
    for df_1 in cvsinput:
        if type(df_1[5]) != str:
            continue
        cve ={
            "timestamp": date_time,
			"published_date": df_1[0],
			"last_modified_date":df_1[0],
			"id":df_1[5],
			"url":url,
			"name":df_1[1],
			"description":df_1[2],
        }

        cpes={
            "operator":"OR",
        }
        
        cpe_list= []
        versions = df_1[4].split(",")

        for ver in versions:
            lis={
                "vendor":vendor,
                "product":vendor,
                "category":"a",
                "versionStartIncluding":ver,
                "versionEndIncluding":ver,
            }

            cpe_list.append(lis)
        # print("cpe_list type {} cpe_list {}".format(type(cpe_list), cpe_list))
        
        cpes["cpe_list"]= cpe_list
        cve["cpes"] = cpes 
        cves.append(cve)
    
    root["cves"] = cves

        


    # print("root: {}".format(root))
    # createJson(root)
    return root