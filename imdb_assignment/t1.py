# 3. Print out the top ten movies, according to imdb score.

import json
with open("imdb_assignment\imdb_movies.json") as f:
    data = json.load(f)
    print(data)
# print(sorted(data, key = lambda x:x['imdb_score'], reverse = True)[:10])

