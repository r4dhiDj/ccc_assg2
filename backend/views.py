import couchdb
import connectDB
from couchdb import design

def create_income_view(db):
    view = design.ViewDefinition('views', 'data', """
        function (doc) {
            if (doc.city) {
                emit(doc.city, {city :doc.city,year:doc.year,mean:doc.mean_income_yr});
            }
        }
        """)
    if not view.get_doc(db):
        view.sync(db)

def create_unemployment_view(db):
    view = design.ViewDefinition('views', 'data', """
        function (doc) {
            if (doc.city) {
                emit(doc.city, {city :doc.city,year:doc.year,rate:doc.avg_unemp_rate});
            }
        }
        """)
    if not view.get_doc(db):
        view.sync(db)

def create_sentiment_view(db):
    view = design.ViewDefinition('data', 'alldata', """
        function (doc) {
            emit([doc.location,doc.time.slice(doc.time.length-4)], {compound:doc.sentiment.compound,negative:doc.sentiment.neg,
                neutral:doc.sentiment.neu,positive:doc.sentiment.pos
            },true);
        }
        """, '''\
        _sum''')
    # if not view.get_doc(db):
    view.sync(db)

def create_sentiment_satisfaction_view(db):
    view = design.ViewDefinition('data', 'rekap', """
        function (doc) {
            emit(doc.location, {compound:doc.sentiment.compound,negative:doc.sentiment.neg,
                neutral:doc.sentiment.neu,positive:doc.sentiment.pos
            },true);
        }
        """, '''\
        _sum''')
    # if not view.get_doc(db):
    view.sync(db)
    
create_income_view(connectDB.dbIncome)
create_sentiment_view(connectDB.dbSentiment)
create_unemployment_view(connectDB.dbUnemployment)
create_sentiment_satisfaction_view(connectDB.dbSentiment)