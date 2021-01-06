# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route("/")
def home():
  return "Hello World"

# Add uniform route (json)
@app.route('/api/uniform')
def uniform():
  return {"value": np.random.uniform()}

# Add normal route (json)
@app.route('/api/normal')
def normal():
  return {"value": np.random.normal()}