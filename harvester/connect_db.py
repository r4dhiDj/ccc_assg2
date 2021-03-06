'''
COMP90024
Team 17
Jeanelle Abanto: 1133815
Kartika Waluyo: 1000555
Radhimas Djan: 1146240
Zi Jin: 987771  
'''

import couchdb

# CouchDB environment variables
host = "172.26.130.64"
port = "5984"
username = "admin"
password = "admin"
db_name = "tweets"


def connect_to_couchdb_server(username, password, host, port):
    """
    Establish connection ot couchdb server.
    """
    couchdb_server = couchdb.Server('http://' + username + ':' + password + '@' + host + ':' + port)
    return couchdb_server


def connect_to_db(server, db_name):
    """
    Connect to or create a database with db_name.
    """
    try:
        return server[db_name]
    except:
        return server.create(db_name)


# Establish connection to couchDB server and database
server = connect_to_couchdb_server(username, password, host, port)
database = connect_to_db(server, db_name)


def save_to_db(tweet, db=database):
    """
    Save tweets to db if tweet ID does not exist in database (to avoid duplicates).
    """
    # check for duplication first
    if str(tweet["id"]) not in db:
        # set tweet id as the document id for duplication removal
        tweet["_id"] = "%s" % tweet["id"]

        if not tweet is None:
            try:
                db.save(tweet)
            except:
                pass