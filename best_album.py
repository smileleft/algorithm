
def solution(genres, plays):
    answer = []
    genres_dict = {}
    plays_dict = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in genres_dict:
            genres_dict[genre] = []
            plays_dict[genre] = 0
        genres_dict[genre].append((i, play))
        plays_dict[genre] += play

    sorted_genres = sorted(plays_dict.items(), key=lambda x:x[1], reverse=True)

    for genre, _ in sorted_genres:
        sorted_songs = sorted(genres_dict[genre], key=lambda x:(-x[1], x[0]))
        answer.extend([idx for idx, _ in sorted_songs[:2]])

    return answer


genres = ["classic","pop","classic","classic","pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))