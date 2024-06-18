import csv

csv_content = """
track_name,artist(s)_name,artist_count,released_year,released_month,released_day,in_spotify_playlists,in_spotify_charts,streams,in_apple_playlists
"When I Was Your Man","Bruno Mars",1,2012,4,16,1,4,1661187319,1
"I Wanna Be Yours","Arctic Monkeys",1,2013,9,6,1,1,1297026226,1
"As It Was","Harry Styles",1,2022,6,22,1,1,2513188493,1
"""

try:
    reader = csv.reader(csv_content.strip().splitlines())
    next(reader)

    popular_songs = {}

    for line in reader:
        if len(line) >= 10:
            track_name = line[0].strip()
            artist_name = line[1].strip()
            artist_count = int(line[2].strip())
            released_year = int(line[3].strip())
            streams = int(line[8].strip())

            if 2012 <= released_year <= 2022 and '"' not in artist_name and '"' not in track_name:
                if released_year not in popular_songs:
                    popular_songs[released_year] = [track_name, artist_name, released_year, streams]
                else:
                    if streams > popular_songs[released_year][3]:
                        popular_songs[released_year] = [track_name, artist_name, released_year, streams]

    popular_songs_list = sorted(popular_songs.values(), key=lambda x: x[2])

    for song in popular_songs_list:
        print(song)

except ValueError as e:
    print(f'Erro de valor: {e}')
except Exception as e:
    print(f'Erro inesperado: {e}')
