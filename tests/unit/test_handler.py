import json

import pytest

from hello_world import app


@pytest.fixture()
def s3_event():
    """ Generates S3 Event """

    return {
          "Records": [
            {
              "eventVersion": "2.0",
              "eventSource": "aws:s3",
              "awsRegion": "us-east-1",
              "eventTime": "1970-01-01T00:00:00.000Z",
              "eventName": "ObjectCreated:Put",
              "userIdentity": {
                "principalId": "EXAMPLE"
              },
              "requestParameters": {
                "sourceIPAddress": "127.0.0.1"
              },
              "responseElements": {
                "x-amz-request-id": "EXAMPLE123456789",
                "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH"
              },
              "s3": {
                "s3SchemaVersion": "1.0",
                "configurationId": "testConfigRule",
                "bucket": {
                  "name": "test-s3",
                  "ownerIdentity": {
                    "principalId": "EXAMPLE"
                  },
                  "arn": "arn:aws:s3:::test-s3"
                },
                "object": {
                  "key": "fileKey",
                  "size": 1024,
                  "eTag": "0123456789abcdef0123456789abcdef",
                  "sequencer": "0A1B2C3D4E5F678901"
                }
              }
            }
          ]
        }            

def test_lambda_handler(s3_event, mocker):

    ret = app.lambda_handler(s3_event, "")
    #TODO assert
