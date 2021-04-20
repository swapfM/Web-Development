import bitly_api

# GENERATE YOUR TOKEN BEFORE PROCEEDING

BITLY_ACCESS_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"



long = input

b = bitly_api.Connection(access_token=BITLY_ACCESS_TOKEN)


response = b.shorten(long)
return(response['url'])
