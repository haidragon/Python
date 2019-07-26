
import pandas as pd
import xml.etree.ElementTree as ET

def getMetrics(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    result = []
    for measure in root.iter('SecDef'):     #Get all 'measure' tag
        #node = measure.attrib["measure"].split("-")[0].strip()    #获取节点属性
        for measurement in measure:                              #Get Metrics Information
            if "NoCredtRateAgencyInfo" in measurement.attrib:
                #result.append(dict(node=node, timestamp=measurement.attrib.get("timestamp"), max=measurement.attrib["max"], count=measurement.attrib["count"]))
                result.append(dict(NoCredtRateAgencyInfo=measurement.attrib.get("NoCredtRateAgencyInfo")
                                   , CreditRatingAgency=measurement.attrib["CreditRatingAgency"]
                                   , CrdRtg=measurement.attrib["CrdRtg"]
                                   , CreditRatingType=measurement.attrib["CreditRatingType"]
                                   , RatedObjectName=measurement.attrib["RatedObjectName"]
                                   , RatedExpect=measurement.attrib["RatedExpect"]
                                   , CreditValidityFrom=measurement.attrib["CreditValidityFrom"]
                                   , RatingChgDirection=measurement.attrib["RatingChgDirection"]
                                   , CreditValidityTo=measurement.attrib["CreditValidityTo"]
                                   , RatingChgRsnType=measurement.attrib["RatingChgRsnType"]
                                   , RatingChgRsn=measurement.attrib["RatingChgRsn"]))
    return result

filename = "C:/Users/xiaoming/Desktop/主体评级信息_全量_20190410.xml"

df = pd.DataFrame(getMetrics(filename), columns=["NoCredtRateAgencyInfo", "CreditRatingAgency", "CrdRtg",
                                                 "CreditRatingType", "RatedObjectName", "RatedExpect",
                                                 "CreditValidityFrom","RatingChgDirection", "CreditValidityTo",
                                                 "RatingChgRsnType", "RatingChgRsn"])          #Form Dataframe
print(df)

df.to_csv("C:/Users/xiaoming/Desktop/Your_Output_主体评级信息_全量_20190410.csv")     #Write to CSV.