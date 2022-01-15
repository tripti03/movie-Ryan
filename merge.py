import csv


with open('movies.csv',encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]
headers.append('poster_link')

with open('final.csv','a+', encoding='utf-8-sig') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)

with open('movie_links.csv', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    data2 = list(reader)
    all_links = data2[1:]

for movieitem in all_movies:
    poster_found=any(movieitem[8] in movielinkitems for movielinkitems in all_links)
    if poster_found:
        for movielinkitems in all_links:
            if movieitem[8] == movielinkitems[0]:
                movieitem.append(movielinkitems[1])
                if len(movieitem) == 28:
                    with open('final.csv','a+',encoding='utf-8-sig') as f:
                        writer = csv.writer(f)
                        writer.writerow(movieitem)


