import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data = {
  "question": "How can I request a refill for my prescription at Lamna Healthcare?",
  "chat_history": []
}


body = str.encode(json.dumps(data))

url = 'https://rag-11111-endpoint.eastus2.inference.ml.azure.com/score'
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCIsImtpZCI6Inp4ZWcyV09OcFRrd041R21lWWN1VGR0QzZKMCJ9.eyJhdWQiOiJodHRwczovL21sLmF6dXJlLmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzZkZjdmY2VhLTUzZDEtNGQ2Zi1hNmU3LWQ4Mjk2OTRiY2M5Ny8iLCJpYXQiOjE3MzQwNTgxNzIsIm5iZiI6MTczNDA1ODE3MiwiZXhwIjoxNzM0MDYzNTAzLCJhY3IiOiIxIiwiYWlvIjoiQVhRQmkvNFlBQUFBVVdxa2g3dzI1Q04rd08yYnhqZ2o5cFZHbXI4dGVoMUhHZnVkUThVYlZMZFNQbUlPMVVkRldVQzlBeU92MVZIcjBVRXh2NkdHdVVmWTlzcThzQk5SaEJWa3htZXN3bXZMQkhobkJwOFR5VkRjOUUyZjNUS0NoazR0d1p3UGpMeXpNZlozc05qU0d4UG8zN3dvQUZ6elNYc3psUk94a0ZHUjVCQ2VWaW53MzVzVlRPWkJLRWljcU9xUDBRL2xQcGIwQmMyMVkyYXp5NFZJei92VmdNcm45TGRiWHA4bGtTVkEyMnFFb3BIY3JuYm16QkJ0T2FDTzRQd2FJKy9EUnBPd3JwamtGYVA2WjFWSXFkdmx4dXg1dHRFZE41ejk1OXV0QjREOFVJMzZVLzNRTGY2U1lNYisxSmlDdElCTXdXNG9sN1NQS0xMaXdGYWVwanZMU0QzTDFRRUlPbHVxQU0vZHRiK1Q5QkFaQVg1bTRnQmh3R3JDVmswQmRrY0NEUUovMk4wT2UzR0ZCc2J1em5FOFJCVm45VWdOVEJ1eFFaMmF2b3AzSzZCSUZ1Z00xd2VUcmJFVDgvTGlncHN1Y3FhUGhtdytNZTdOZTZZU21nSTJpS3hmcFdNMVNiOG5nMXd3UXZwL01ONzl5MlU9IiwiYWx0c2VjaWQiOiI1OjoxMDAzMjAwM0FGMkU3QjY1IiwiYW1yIjpbInB3ZCIsInJzYSIsIm1mYSJdLCJhcHBpZCI6ImNiMmZmODYzLTdmMzAtNGNlZC1hYjg5LWEwMDE5NGJjZjZkOSIsImFwcGlkYWNyIjoiMCIsImVtYWlsIjoiaGFyaXRoYXRAbWljcm9zb2Z0LmNvbSIsImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzcyZjk4OGJmLTg2ZjEtNDFhZi05MWFiLTJkN2NkMDExZGI0Ny8iLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIxNjMuNDcuNjguNjMiLCJuYW1lIjoiSGFyaXRoYSBUaGlsYWthcmF0aG5lIiwib2lkIjoiNDY1MDRlOTUtYjA4NC00MGM5LWI5ODItNWU4Y2RhN2FkYmFkIiwicHVpZCI6IjEwMDMyMDAzQjhCMTI0MjAiLCJyaCI6IjEuQVc4QjZ2ejNiZEZUYjAybTU5Z3BhVXZNbDE5dnBoamYyeGRNbmRjV05IRXFuTDV2QVhKdkFRLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInN1YiI6Ino0eExlaWw1RWltejZ1dzc3Snk0SE9xYmNwNjFxeTBuREZXcDBCcmlVc2MiLCJ0aWQiOiI2ZGY3ZmNlYS01M2QxLTRkNmYtYTZlNy1kODI5Njk0YmNjOTciLCJ1bmlxdWVfbmFtZSI6Imhhcml0aGF0QG1pY3Jvc29mdC5jb20iLCJ1dGkiOiJxMHNnTHJZTFJVR0FNNWhiTmFBUkFBIiwidmVyIjoiMS4wIiwieG1zX2lkcmVsIjoiMSAxNCJ9.K4-bBOwE8_M8JngiBz-EggstH1iTbv5KayVKqzb-p_E99rA0V45sPkt_bqDHHfIsw2v_LVbiA9g49MKBbV7Gj88UB5Pn7S5sULwxCRW8W30wNTVxcWeDZroMdPmEHy3OnFkkqxcFrqaqcWhSIoybLNVIDVlsmeuU79b0SWKoMcg_4ppkC3cfQbDVvMBUOYdq3hqJHBTHvOgJe6FaGc7aE8Ll3jKNDxvgWlLKkXhktd9LHeFZ_YZFODp3JH4V3ZNXV86_f-1M0Y7922SC24uWMRFCzIvUBmvklW9NKNzpO_iYUFkQkpbdnKGzuFpKvHMQDGFq-Ezt3b1CVp7hmTRPfA'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))