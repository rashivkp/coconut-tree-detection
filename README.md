# COCONUT WEB

provide a web interface to trained model to count and localize coconut trees from google satellite imagery.

## Setup

Download  [tensorflw/models](https://github.com/tensorflow/models/tree/master/research).

And Follow [installation instructions](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md)

And install flask using  `pip install -r requirements.txt`

## Configuration

`cp setting.py.example settings.py`

modify settings.py accordingly.


## Run

`python app.py runserver`

## Sample Output

![Sample Output](static/images/output.png "Found 17 coconut trees")

## Team Members

- [Hijas Ajmal](https://github.com/HijasAjmal)
- [Shabeer Salman](https://github.com/shabeersalman)
- [Mohammed Afal](https://github.com/afalmuhammad)
- [Mohamed Rashid](https://github.com/rashivkp)
