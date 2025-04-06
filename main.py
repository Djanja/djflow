from config import get_spotify_client
from playlist_analyzer import PlaylistAnalyzer
from recommender import Recommender


def main():
    sp = get_spotify_client()

    playlist_url = input("Вставьте ссылку на ваш плейлист: ")

    analyzer = PlaylistAnalyzer(sp)
    data = analyzer.analyze(playlist_url)

    recommender = Recommender(sp)
    recommended_tracks = recommender.generate_recommendations(data['features'])

    print("\n🎧 Новый плейлист:")
    for track in recommended_tracks:
        print(f"{track['name']} — {track['artists'][0]['name']}")


if __name__ == "__main__":
    main()
