
import pandas as pd
import xml.etree.ElementTree as ET

def getMetrics(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    result = []
    for measure in root.iter('IMIXML'):     #Get all 'measure' tag
        #node = measure.attrib["measure"].split("-")[0].strip()    #获取节点属性
        for measurement in measure:                              #Get Metrics Information
            if "ReminderDate" in measurement.attrib:
                #result.append(dict(node=node, timestamp=measurement.attrib.get("timestamp"), max=measurement.attrib["max"], count=measurement.attrib["count"]))
                result.append(dict(ReminderDate=measurement.attrib.get("ReminderDate"), ReminderEvent=measurement.attrib["ReminderEvent"]
                                   , ReminderType=measurement.attrib["ReminderType"], ReminderObjectName=measurement.attrib["ReminderObjectName"]
                                   , ReminderObjectID=measurement.attrib["ReminderObjectID"], ReminderObjectShrtName=measurement.attrib["ReminderObjectShrtName"]
                                   , OptionType=measurement.attrib["OptionType"]))
    return result

filename = "C:/Users/xiaoming/Desktop/下30个自然日交易提示_20190410.xml"

df = pd.DataFrame(getMetrics(filename), columns=["ReminderDate", "ReminderEvent", "ReminderType",
                                                 "ReminderObjectName", "ReminderObjectID", "ReminderObjectShrtName", "OptionType"])          #Form Dataframe
print(df)

df.to_csv("C:/Users/xiaoming/Desktop/Your_Output.csv")     #Write to CSV.