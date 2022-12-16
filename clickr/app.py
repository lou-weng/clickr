import os

from boto3 import resource
from dotenv import load_dotenv
from flask import Flask

app = Flask(__name__)

TABLE_NAME = 'clickr'
PROJECT_INSTANCE_ATTRIBUTE = 'project_instance'
PROJECT_COUNTER_ATTRIBUTE = 'project_counter'
PROJECT_INSTANCE = 'clickr_py'

load_dotenv()

resource = resource(
    'dynamodb',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
    region_name=os.environ.get('AWS_REGION')
)
table = resource.Table(TABLE_NAME)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/clickr')
def increment_click():
    table.update_item(
        Key={
            'project_instance': PROJECT_INSTANCE
        },
        UpdateExpression=f"""set {PROJECT_COUNTER_ATTRIBUTE} =
            {PROJECT_COUNTER_ATTRIBUTE} + :incr""",
        ExpressionAttributeValues={
            ':incr': 1
        },
        ReturnValues="UPDATED_NEW"
    )
    return table.get_item(
        Key={
            'project_instance': PROJECT_INSTANCE
        }
    )


if __name__ == "__main__":
    app.run(debug=False)
