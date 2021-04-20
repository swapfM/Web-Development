import bitly_api

# GENERATE YOUR TOKEN BEFORE PROCEEDING

BITLY_ACCESS_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


print("Enter your URL : ", end='')

long = input()

b = bitly_api.Connection(access_token=BITLY_ACCESS_TOKEN)


response = b.shorten(long)

print("The Generated Short URL is : ", end='')
print(response['url'])
