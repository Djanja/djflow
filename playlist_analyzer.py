class PlaylistAnalyzer:
    def __init__(self, sp):
        self.sp = sp

    def get_playlist_tracks(self, playlist_url):
        playlist_id = playlist_url.split("/")[-1].split("?")[0]
        results = self.sp.playlist_tracks(playlist_id)
        tracks = []
        for item in results['items']:
            track = item['track']
            if track:
                tracks.append(track)
        return tracks

    def extract_audio_features(self, track_ids):
        features = self.sp.audio_features(tracks=track_ids)
        return [f for f in features if f is not None]

    def analyze(self, playlist_url):
        tracks = self.get_playlist_tracks(playlist_url)
        track_ids = [track['id'] for track in tracks if track and track['id']]
        audio_features = self.extract_audio_features(track_ids)
        return {
            'tracks': tracks,
            'features': audio_features
        }
