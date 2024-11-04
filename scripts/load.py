# scripts/load.py
from sqlalchemy import create_engine

def load_data_to_sql(df, db_uri):
    engine = create_engine(db_uri)
    df.to_sql('facebook_posts', con=engine, if_exists='replace', index=False)
    print(f"Data loaded to table 'facebook_posts'")
