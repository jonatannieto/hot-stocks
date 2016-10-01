# hot-stocks
MONGO_URL=mongodb://crawler:3ny3H94A@ds035006.mlab.com:35006/hot_stocks 

# Run app in android device (Localhost)
  meteor run android-device
or
  MONGO_URL=mongodb://crawler:3ny3H94A@ds035006.mlab.com:35006/hot_stocks meteor run android-device

# Run app (With Server)
meteor run android-device --mobile-server http://46.101.144.90:3000/
