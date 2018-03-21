import requests

def generate_response(meaning="No meaning found for this word",fulfillmenState="Failed"):
    return {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": fulfillmenState,
            "message": {
                "contentType": "PlainText",
                "content": meaning
            }
        }
    }

def lambda_handler(event, context):
    word = event['currentIntent']['slots']['word']
    CONTENT_TYPE = "application/json"
    APP_ID = "ed932b14"
    APP_KEY = "b780c3a3498cac814d3dff096efbf3fd"
    head = {"Content-Type":CONTENT_TYPE,"app_id":APP_ID,"app_key":APP_KEY}
    r = requests.get("https://od-api.oxforddictionaries.com:443/api/v1/entries/en/"+word, headers = head)
    if r.status_code == 404 :
        return generate_response()
    else:
        data = r.json()
        meaning = data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
        return generate_response(word+" : "+meaning,"Fulfilled")