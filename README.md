# aws-sam-examples
AWS SAM Sandbox with some usage examples


sam init
sam build --user-container                      #Build lambda
sam local start-lambda				#Start lambda locally. Does not require restart upon code change
sam local generate-event s3 put --bucket nazariene-s3 --key fileKey > s3_event.json	#generate event that simulates s3 put event
aws lambda invoke --function-name "HelloWorldFunction" --endpoint-url "http://127.0.0.1:3001" --no-verify-ssl --payload file://s3_event.json out.txt  	#trigger lambda locally

To Deploy:
sam deploy --guided

To delete:
aws cloudformation delete-stack --stack-name sam-app

