import statistics

class Recommender:
    def __init__(self, sp):
        self.sp = sp

    def generate_recommendations(self, features, limit=20):
        avg_bpm = statistics.mean([f['tempo'] for f in features])
        avg_danceability = statistics.mean([f['danceability'] for f in features])
        avg_energy = statistics.mean([f['energy'] for f in features])

        seed_genres = ['pop', 'electronic', 'hip-hop']  # В будущем можно получить из треков

        recommendations = self.sp.recommendations(
            seed_genres=seed_genres,
            limit=limit,
            target_tempo=avg_bpm,
            target_danceability=avg_danceability,
            target_energy=avg_energy
        )
        return recommendations['tracks']
