
import psycopg2
from facebook_scraper import get_posts

def scrape_page(url, db_name,db_user,db_password,db_host):
    # Connect to the database
    conn = psycopg2.connect(
        database=db_name,
        user=db_user,
        password=db_password,
        host=db_host
    )
    cur = conn.cursor()

    # Create the table to hold the scraping data
    cur.execute("""
        CREATE TABLE IF NOT EXISTS scraping_data (
            id SERIAL PRIMARY KEY,
            post_title TEXT,
            post_content TEXT,
            post_date TIMESTAMP,
            post_likes INTEGER,
            post_comments INTEGER
        );
    """)
    conn.commit()

    # Scrape the Facebook page and insert the data into the database
    for post in get_posts(url, pages=5):
        post_title = post['text'] if 'text' in post else ''
        post_content = post['post_text'] if 'post_text' in post else ''
        post_date = post['time']
        post_likes = post['likes']
        post_comments = post['comments']
        print(post_content)
        print(post_date)

        print(post_title)

        print(post_likes)

        cur.execute("""
            INSERT INTO scraping_data (
                post_title,
                post_content,
                post_date,
                post_likes,
                post_comments
            ) VALUES (%s, %s, %s, %s, %s);
        """, (post_title, post_content, post_date, post_likes, post_comments))
        conn.commit()

    # Close the database connection
    cur.close()
    conn.close()

