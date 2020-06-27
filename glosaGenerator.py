import requests

with open('text.txt', 'r') as s:
    with open('glosas.txt', 'a') as g:
        for i,line_without in enumerate(s, 1):
            line = line_without.strip().replace('"', '')
            
            r = requests.post('insert the URL of your glossing API', data={'text':line})
            print(f'Line: {i} | Response time: {r.elapsed.total_seconds()}')
            g.write(f'{r.text}\n')
