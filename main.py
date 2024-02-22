import pandas as pd

data = pd.read_csv('podaci.csv')

data['time_seconds'] = data['time_fps'] / 24 

data['time_interval'] = (data['time_seconds'] // 15) * 15

interval_counts = data.groupby('time_interval').size().reset_index(name='interaction_count')

interval_counts['time_interval_formatted'] = interval_counts['time_interval'].apply(
    lambda x: f"{int(x // 60)}m {int(x % 60)}s" if x >= 60 else f"{int(x)}s"
)

interval_counts[['time_interval_formatted', 'interaction_count']].to_csv('rezultat.csv', index=False)

print("Rezultati su spremljeni u rezultat.csv datoteku.")

