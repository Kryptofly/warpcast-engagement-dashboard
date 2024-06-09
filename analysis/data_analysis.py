import pandas as pd
from collections import defaultdict

def analyze_engagement(interactions):
    engagement_summary = defaultdict(int)
    engagement_timeline = defaultdict(list)
    
    for interaction in interactions:
        engagement_summary[interaction['type']] += 1
        engagement_timeline['date'].append(interaction['timestamp'])
        engagement_timeline[interaction['type']].append(1)
    
    # Convert lists to pandas DataFrame for better handling
    df = pd.DataFrame(engagement_timeline)
    df['date'] = pd.to_datetime(df['date'])
    df = df.groupby(df['date'].dt.date).sum().reset_index()
    
    return engagement_summary, df
