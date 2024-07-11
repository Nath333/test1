from flask import Flask, Response
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/get_xml')
def get_xml():
    # Faire une requête à l'API
    response = requests.get("https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400")
    data = response.json()

    # Créer un élément racine pour le XML
    root = ET.Element("SunriseSunset")

    # Ajouter les données de l'API sous forme d'éléments XML
    for key, value in data['results'].items():
        child = ET.SubElement(root, key)
        child.text = value

    # Convertir l'arbre XML en une chaîne
    xml_str = ET.tostring(root, encoding='utf8', method='xml')
    return Response(xml_str, mimetype='text/xml')

if __name__ == '__main__':
    app.run(debug=True)