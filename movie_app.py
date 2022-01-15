from flask import Flask,jsonify,request
import csv
from content_filtering import getRecommendation
from demographic_filtering import output
from storage import all_movies,liked_movies,disliked_movies,did_not_watch
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get-movie')
def get_movie():
    movie_data = {
        'title': all_movies[0][19],
        'poster_link': all_movies[0][27],
        'release_date': all_movies[0][13] or 'N/A',
        'duration': all_movies[0][15],
        'rating': all_movies[0][20],
        'overview': all_movies[0][9]
        }
    return jsonify({
        'data': movie_data,
        'status':'Success'
    })

@app.route('/liked-movie',methods=['POST'])
def liked_movies():
    movie = all_movies[0]
    liked_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        'status':'Success'
    }), 201

@app.route('/disliked-movie',methods=['POST'])
def disliked_movies():
    movie = all_movies[0]
    disliked_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        'status':'Success'
    }),201

@app.route('/did-not-watch',methods=['POST'])
def did_not_watch():
    movie = all_movies[0]
    did_not_watch.append(movie)
    all_movies.pop(0)
    return jsonify({
        'status':'Success'
    }),201

@app.route('/popular-movie')
def popular_movies():
    movie_data=[]
    for movie in output:
        _d = {
        'title': movie[0],
        'poster_link': movie[1],
        'release_date': movie[2] or 'N/A',
        'duration': movie[3],
        'rating': movie[4],
        'overview': movie[5]
        }
        movie_data.append(_d)
    return jsonify({
        'data':movie_data,
        'status':'Success'
    }),200


@app.route("/recommended-movie")
def recommended_movies(): 
    all_recommended = [] 
    for liked_movie in liked_movies: 
        output = getRecommendation(liked_movie[19]) 
        for data in output: 
            all_recommended.append(data) 
            import itertools 
            all_recommended.sort() 
            all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended)) 
            movie_data = [] 
            for recommended in all_recommended: 
                _d = { 
                    "title": recommended[0],
                    "poster_link": recommended[1], 
                    "release_date": recommended[2] or "N/A", 
                    "duration": recommended[3], 
                    "rating": recommended[4], 
                    "overview": recommended[5] 
                    } 
                movie_data.append(_d) 
    return jsonify({ 
        "data": movie_data, 
        "status": "success" 
        }), 200

if __name__ == '__main__':
    app.run(debug=True,port=8080)

