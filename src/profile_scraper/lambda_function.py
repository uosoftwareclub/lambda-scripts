import json
from scraper import scrape

def lambda_handler(event, context):
  res = scrape()
  return {
    'statusCode': 200,
    'body': json.dumps(res)
  }
