import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot
from pymongo import MongoClient

mogo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

# Connect to database
client = MongoClient(mogo_uri)

# Get database
db = client.get_default_database()

# Create collection
customers = db["customers"]

events = db.customers.count({"ref": "events"})
wom = db.customers.count({"ref": "wom"})
ads = db.customers.count({"ref": "ads"})

#print(events)

# Prepare data
labels = ["events", "wom", "ads"]
values = [events, wom, ads]
colors = ["green", "red", "yellow"]
explode = [0, 0.1, 0.1]
# plot 
pyplot.pie( values, 
            labels= labels, 
            colors= colors, 
            explode= explode)
pyplot.axis("equal")
pyplot.title(" Marketing data ")
# show
pyplot.show()

