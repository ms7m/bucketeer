
# 🪣 Bucketeer

#### Still in developement.


Bucketeer allows you to automatically use the lowest keys for your external API requests..

```python

from bucketeer.objects.service import Service
from bucketeer.objects.key import Key
from bucketeer.bucketeer import Bucketeer, BucketeerContext
from bucketeer.connections.local import DictReference
from bucketeer.connections.redis_connection import RedisReference

# First define the service. 
# Let's assume I'm rotating multiple API keys from this service.

current_service = [
    Key("UniqueKey"),
    Key("UniqueKey2", weight=5) # add a weight. This 'duplicates' 
    # the amount of times you want this key to appear.
]



# Create the referencer object. This "remembers" how 
# much each key is being utilized..


connection = DictReference(current_service)

# create bucketeer

bucket = Bucketeer(connection)


# now you can use it in a context manager..


with BucketeerContext(bucket, "service" ) as api_key:
    print(api_key.key)

```

#### This only accepts pure string formats only.