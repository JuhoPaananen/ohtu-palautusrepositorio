from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        data = toml.loads(content)
        name = data["tool"]["poetry"]["name"]
        description = data["tool"]["poetry"]["description"]
        dependencies = []
        for key in data["tool"]["poetry"]["dependencies"]:
            dependencies.append(key)
        dev_dependencies = []
        for key in data["tool"]["poetry"]["group"]["dev"]["dependencies"]:
            dev_dependencies.append(key)

        return Project(name, description, dependencies, dev_dependencies)
