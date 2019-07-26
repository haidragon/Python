
import pandas as pd
import xml.etree.ElementTree as ET

def getMetrics(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    result = []
    for measure in root.iter('SecDef'):  # Get all 'measure' tag
        # node = measure.attrib["measure"].split("-")[0].strip()    #获取节点属性
        u_dict_instrmt = {}
        for instrmt in measure.iter("Instrmt"):
            if "ID" in instrmt.attrib:
                u_dict_instrmt = dict(ID=getValue(instrmt,"ID")
                                      , Sym=getValue(instrmt,"Sym")
                                      , SecTyp=getValue(instrmt,"SecTyp")
                                      , Status=getValue(instrmt,"Status")
                                      , Issued=getValue(instrmt,"Issued")
                                      , CirculationSize=getValue(instrmt,"CirculationSize")
                                      , DelistDate=getValue(instrmt,"DelistDate")
                                      , ListDate=getValue(instrmt,"ListDate")
                                      , IssuePx=getValue(instrmt,"IssuePx")
                                      , IssueSize=getValue(instrmt,"IssueSize")
                                      , CouponPaymentFrequency=getValue(instrmt,"CouponPaymentFrequency")
                                      , Principal=getValue(instrmt,"Principal")
                                      , CouponRateType=getValue(instrmt,"CouponRateType"))
                print(u_dict_instrmt)

        u_dict_SprdBnchmkCurve = {}
        for SprdBnchmkCurve in measure.iter("SprdBnchmkCurve"):

            if "Name" in SprdBnchmkCurve.attrib:
                u_dict_SprdBnchmkCurve = dict(Name=SprdBnchmkCurve.attrib.get("Name")
                                              , Px=SprdBnchmkCurve.attrib["Px"]
                                              , Spread=SprdBnchmkCurve.attrib["Spread"])
            #print(u_dict_SprdBnchmkCurve)
        u_dict_SecurityRelatedParties = {}
        i = 0
        for SecurityRelatedParties in measure.iter("SecurityRelatedParties"):
            u_dict_PartySubGrp = {}
            i += 1
            for PartySubGrp in SecurityRelatedParties.iter("PartySubGrp"):
                #print("=======start=======")
                if "NoPartySubIDs" in PartySubGrp.attrib:

                    ID_PartySubGrp = "ID_PartySubGrp" + str(i)
                    NoPartySubIDs = "NoPartySubIDs" + str(i)
                    Typ = "Typ" + str(i)
                    u_dict_PartySubGrp[NoPartySubIDs] = PartySubGrp.attrib.get("NoPartySubIDs")
                    u_dict_PartySubGrp[Typ] = PartySubGrp.attrib.get("Typ")
                    u_dict_PartySubGrp[ID_PartySubGrp] = PartySubGrp.attrib.get("ID")

                    #u_dict_PartySubGrp = dict(NoPartySubIDs=PartySubGrp.attrib.get("NoPartySubIDs")
                    #                         , Typ=PartySubGrp.attrib["Typ"]
                    #                          , ID_PartySubGrp=PartySubGrp.attrib["ID"])
            u_dict_SecurityRelatedParties = dict(u_dict_SecurityRelatedParties, **u_dict_PartySubGrp)
            #print(u_dict_SecurityRelatedParties)

        u_dict = dict(u_dict_instrmt, **u_dict_SprdBnchmkCurve)
        u_dict = dict(u_dict, **u_dict_SecurityRelatedParties)
        result.append(u_dict)
    print("========end========")
    return result

def getValue(node, key):
    result_v = ""
    try:
        result_v = node.attrib[key]
    except Exception as e:
        print("不存在的key值%s"%key)
    return result_v


filename = "C:/Users/xiaoming/Desktop/资产支持证券信息_20190108.xml"

df = pd.DataFrame(getMetrics(filename), columns=["ID", "Sym", "SecTyp",
                                                 "Status", "Issued", "CirculationSize",
                                                 "DelistDate","ListDate", "IssuePx",
                                                 "IssueSize", "IssueSize", "CouponPaymentFrequency",
                                                 "Principal", "CouponRateType", "Name",
                                                 "Px","Spread","NoPartySubIDs1","Typ1",
                                                 "ID_PartySubGrp1","NoPartySubIDs2","Typ2",
                                                 "ID_PartySubGrp2","NoPartySubIDs3","Typ3",
                                                 "ID_PartySubGrp3"])          #Form Dataframe
#print(df)

df.to_csv("C:/Users/xiaoming/Desktop/Your_Output_资产支持证券信息_20190108.csv")     #Write to CSV.