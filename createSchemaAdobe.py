from datetime import datetime
from createJson import createJson

root = {
    
	"type":"vendor",
}

def createSchemaAdobe(cvsinput, vendor, url):

    timestamp = datetime.now().timestamp()
    date_time = datetime.fromtimestamp(timestamp).strftime("%d %B, %Y")
    type(date_time)
    root["source"]= vendor
    cves=[]
    for df_1 in cvsinput:
        if type(df_1[3]) != str:
            continue
        cve ={
            "timestamp": date_time,
			"published_date": "",
			"id":df_1[3],
			"url":url,
			"name":df_1[1],
			"description":df_1[0],
        }

        cpes={
            "operator":"OR",
        }
        
        cpe_list= []
        versions = [1.0, 2.1]

        for ver in versions:
            lis={
                "vendor":vendor,
                "product":"vendor",
                "category":"a",
                "versionStartIncluding":ver,
                "versionEndIncluding":ver,
            }

            cpe_list.append(lis)
        # print("cpe_list type {} cpe_list {}".format(type(cpe_list), cpe_list))
        cvssv2={
            "severity": df_1[2]
        }
        cvssv3={
            "severity": "HIGH"
        }
        cpes["cpe_list"]= cpe_list
        cve["cpes"] = cpes
        cve["cvssv2"] = cvssv2
        cve["cvssv3"] = cvssv3
        cves.append(cve)
    
    root["cves"] = cves

        


    # print("root: {}".format(root))
    # createJson(root)
    return root

