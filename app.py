from flask import Flask, flash, jsonify, render_template, request
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from sqlalchemy import false

app = Flask(__name__)

sentry_sdk.init(
    dsn="https://3e370496ad9a4efba52d5637fe3aada1@o1141471.ingest.sentry.io/6201702",
    integrations=[FlaskIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/post', methods=["POST"])
def testpost():
     input_json = request.get_json(force=True) 
     dictToReturn = {'text':input_json['text']}
     return jsonify(dictToReturn)



if __name__ == '__main__':
    app.run(debug=false,host='0.0.0.0')