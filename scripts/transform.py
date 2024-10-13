# scripts/transform.py
import pandas as pd


def transform_data(fb_data):
    posts = fb_data['data']
    df = pd.DataFrame(posts)

    # Example transformation: Convert the created time to datetime
    df['created_time'] = pd.to_datetime(df['created_time'])

    return df
