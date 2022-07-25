import re 
import pandas as pd

def checknamesyntax(name):
    output = re.sub(r"[^a-zA-Z ]", "", name)

    return output

def checkmailsyntax(email):
    output = re.sub(r"[^a-zA-Z0-9@\.]+", "", email)

    return output

def checkphonesyntax(phone):
    output = re.sub(r"[^0-9\-]+", "", phone)

    return output

def checklicenseseq(i):
    l = list(i)
    if l[0].isalpha() == False:
        e = l.pop(0)
        l.append(e)
    output = ''.join(l)
    return output


def checklicensesyntax(l):
    output = re.sub(r"[^A-Z0-9\-]+", "", l)

    output = checklicenseseq(output)
    return output

loyalty = pd.read_csv("test_dataset/loyalty.csv")
transaction = pd.read_csv("test_dataset/transactions.csv")

for i in loyalty.index:
    loyalty.loc[i, 'name'] = checknamesyntax(loyalty.loc[i, 'name'])
    loyalty.loc[i, 'city'] = checknamesyntax(loyalty.loc[i, 'city'])
    loyalty.loc[i, 'phone-number'] = checkphonesyntax(loyalty.loc[i, 'phone-number'])
    loyalty.loc[i, 'license-plate'] = checklicensesyntax(loyalty.loc[i, 'license-plate'])
    loyalty.loc[i, 'email'] = checkmailsyntax(loyalty.loc[i, 'email'])
merged = pd.merge(loyalty, transaction, on='id')
#merged2 = pd.concat([merged, transaction['Amount']])
print(merged)

