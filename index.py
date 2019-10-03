import json
import datetime
import anagrams

alpha = anagrams.build_dict(r"Dictionary/Dictionary.txt")
userinput = "sort"
results = anagrams.anagram(alpha, userinput.upper())


def handler(event, context):
    data = {
        'output': results,
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
