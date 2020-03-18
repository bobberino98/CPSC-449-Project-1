import sqlite3
from flask import jsonify
class Schema:
    def __init__(self):
        # connecting to the database
        self.conn = sqlite3.connect('posts.db')
        # table 
        self.create_posts_table()

    def create_posts_table(self):

        query = """
        CREATE TABLE "Post" (
          title TEXT,
          "text" TEXT,
          community TEXT,
          URL TEXT,
          username TEXT,
          postDate Date
        );
        """

        self.conn.execute(query)


class PostModel:
    def __init__(self):
        self.conn = sqlite3.connect('posts.db')
        self.table_name = 'Post'

    def create_post(self, title, text, community, URL, username, postDate):
        
        query = f'insert into {self.table_name} ' \
                f'(title, text, community, URL, username, postDate) ' \
                f'values ("{title}","{text}", "{community}", "{URL}", "{username}", "{postDate}")'
        try:
            self.conn.execute(query)
            return {'message': f'Post with the title:{title} is created!'}
        except:
            return {'message': 'Could not create the post'}
    
    def delete_post(self, title):

        query = f'DELETE FROM {self.table_name} WHERE title = "{title}"'
        try:
            self.conn.execute(query)
            return {'message': f'Post with the title:{title} is deleted!'}
        except:
            return {'message': 'Could not delete the post'}
    
    def retrieve_post(self, title):
        query = f'SELECT * FROM {self.table_name} WHERE title = "{title}"'
        result = self.conn.execute(query).fetchall()
        return jsonify(list(result))
    
    def list_particular(self, community, n):
        query = f'SELECT * FROM {self.table_name} WHERE community = "{community}"' \
                f'ORDER BY postDate DESC LIMIT {n}'
        result = self.conn.execute(query).fetchall()
        return jsonify(list(result))
    
    def list_recent(self, n):
        query = f'SELECT * FROM {self.table_name} ' \
                f'ORDER BY postDate'
        result = self.conn.execute(query).fetchall()
        return jsonify(list(result))
