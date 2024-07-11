from flask import Flask, Response
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')  # Changed from '/get_xml' to '/'
def get_xml():
    # Make a request to the API
    response = requests.get("https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400")
    data = response.json()

    # Create a root XML element
    root = ET.Element("SunriseSunset")

    # Add API data as XML elements
    for key, value in data['results'].items():
        child = ET.SubElement(root, key)
        child.text = value

    # Convert the XML tree to a string
    xml_str = ET.tostring(root, encoding='utf8', method='xml')
    return Response(xml_str, mimetype='text/xml')

if __name__ == '__main__':
    app.run(debug=True)
