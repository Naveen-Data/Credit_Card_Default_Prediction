from flask import Flask
from pipeline.train_pipeline import TrainPipeline
app = Flask(__name__)

print('Model Training')
pipeline = TrainPipeline()
pipeline.run_train_pipeline()
print('model trained')

if __name__ == "__main__":
    app.run(debug= True)
