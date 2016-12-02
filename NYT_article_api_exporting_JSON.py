



#Tried to write out file by creating an empty list and trying to write into it. No dice. Tells me the attributes don't have a text element can't figure out why it can't get the text from there.
import requests, json

all_ghosts = []

payload = {'fq': 'subject:("ghosts","haunted houses") OR headline:("A Ghost in Long Island City","Flatbush Has a Ghost","spectral lodgers")' ,'begin_date': '18510918' , 'end_date': '19351231'}
r = requests.get('INTERNAL API', params=payload)

data = json.loads(r.text)

total_hits=data['response']['meta']['hits']
counter = 0
#print(total_hits)
#would divide that by 10 + 1 and that is number of times to loop

while counter < (total_hits/10+1):
    r = requests.get('INTERNAL API', params={'fq': 'subject:("ghosts","haunted houses") OR headline:("A Ghost in Long Island City","Flatbush Has a Ghost","spectral lodgers")' , 'begin_date': '18510918' , 'end_date': '19501231', 'limit': 10, 'offset': 10 * counter})
    counter = counter + 1
    data = json.loads(r.text)
    for a_doc in data['response']['docs']:
        headline = a_doc['headline']['main']
        publication_date = a_doc['legacy']['dat']
        abstract = a_doc['abstract']
        glocations = ''
        for a_keyword in a_doc['keywords']:
            if a_keyword['name'] == 'glocations':
                glocations = a_keyword['value']
        url = a_doc['legacy']['web_url']

        a_ghost_dict = {"Headline": headline, "Publication Date" : publication_date, "Abstract" : abstract, "Location": glocations, "URL": url }
        all_ghosts.append(a_ghost_dict)

    with open('nyt_article_results.json', 'w') as f:
        f.write(json.dumps(all_ghosts,indent=4))
