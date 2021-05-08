from pymongo import MongoClient
import ssl
import matplotlib.pyplot as plt
import numpy as np

# Set up normal Mongo Atlas connection + db + collection
# mongopass = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.mmhgn.mongodb.net/test"
client = MongoClient(uri, username='mongouser', password="mayfirst", connectTimeoutMS=200, retryWrites=True, ssl_cert_reqs=ssl.CERT_NONE)
db = client.sample

data = db.pi.find()
pis = []
factors = []
idxs = [i for  i in range(60)]
for d in data:
    print(d)
    pis.append(d["pi"])
    factors.append(d["factor"])

pis = np.array(pis)
factors = np.array(factors)
print(pis.argmax(), factors.argmax())
plt.subplot(1, 2, 1)
plt.plot(idxs, pis)
plt.subplot(1, 2, 2)
plt.plot(idxs, factors)
# plt.plot(pis, factors, "o")
plt.show()
