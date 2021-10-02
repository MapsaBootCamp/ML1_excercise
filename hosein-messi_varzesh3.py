import requests
import csv


r = requests.get('https://api.varzesh3.com/v2.0/news/tag/1028/1775955/1')
if r:
    txts = txt = r.json()
    with open('messi_varzesh3.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Id','Title','Lead','ViewCount','Date','PlainText']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        data_dict = {'Id':txt[0]['Id'],'Title':txt[0]['Title'],'Lead':txt[0]['Lead'],'ViewCount':txt[0]['ViewCount']
                        ,'Date':txt[0]['Date'],'PlainText':txt[0]['PlainText']}
        writer.writerow(data_dict)
        while r:
            r = requests.get(f"https://api.varzesh3.com/v2.0/news/tag/1028/{txts[-1]['Id']}/100")
            if r:
                txts = r.json()
                for txt in txts:
                    data_dict = {'Id':txt['Id'],'Title':txt['Title'],'Lead':txt['Lead'],'ViewCount':txt['ViewCount']
                        ,'Date':txt['Date'],'PlainText':txt['PlainText']}
                    writer.writerow(data_dict)
                    if int(txt['Date'].split('/')[0]) < 1397:
                        break
