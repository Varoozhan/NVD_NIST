import json
from cpe import CPE


def listOfCpes(userInput, NvdNistDBJson):
    # list_of_cpes = NvdNistDBJson[30]['configurations']['nodes'][2]['cpe_match']
    # print(list_of_cpes[0]['cpe23Uri'])
    # Extracting cpes only and returning them as a list
    cpe_s = []
    count = 1
    for nvdobject in NvdNistDBJson:
        if not nvdobject['configurations']['nodes']:
            print('list empty')
        else:
            # print(type(nvdobject['configurations']['nodes']))
            for cpe in nvdobject['configurations']['nodes']:
                # print(cpe)
                if cpe['operator'] == 'OR':
                    for cpe23Uri in cpe['cpe_match']:
                        print(cpe23Uri['cpe23Uri'])
                            # print(pos['cpe_match'])
                else:
                    if not cpe.get('children'):
                        print('and without children')
                        print(cpe['cpe_match'])
                    else:
                        print('and with children')
                        for child in cpe['children']:
                            for cpe23Uri in child['cpe_match']:
                                print(cpe23Uri['cpe23Uri'])
                                    # print(type(child['cpe_match']))
        # print(cpe)
    print("************" + userInput)
        # for pos in cpe:
            # if not pos['cpe_match']:
            #     print('no matches')
            # else:
            # print(pos['operator'])
        # cpe_s.append(cpe)
    # return cpe_s


def nvdNistJson():
    result = []
    with open("nvdcve-1.1-modified.json", encoding="utf8") as file:
        contents = json.load(file)
    # print(contents["CVE_Items"][2])
    for cve in contents["CVE_Items"]:
        result.append(cve)
    return result

def main():
    # str23_wfn = 'wfn:[part="a", vendor="hp", product="?insight_diagnostics?", version="8\.*", target_sw=ANY, target_hw="x32"]'
    # c23_wfn = CPE(str23_wfn)
    # c23_fs = c23_wfn.as_fs()
    # print(c23_fs)

    userInputWFN = 'wfn:[part="a", vendor="hp"]'
    userInputCpeFormat = CPE(userInputWFN)
    userInputFormattedString = userInputCpeFormat.as_fs()

    # print(userInputFormattedString)
    # print(nvdNistJson()[0])
    NvdNistJsonObject = nvdNistJson()
    # print(listOfCpes(userInputFormattedString, NvdNistJsonObject))
    listOfCpes(userInputFormattedString, NvdNistJsonObject)

main()