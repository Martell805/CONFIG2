import requests
from bs4 import BeautifulSoup


class DepParser:
    @staticmethod
    def __parse(package_name: str, tab_level: int = 1) -> None:
        request = requests.get(f"https://www.npmjs.com/package/{package_name}/?activeTab=dependencies").content.decode()
        soup = BeautifulSoup(request, features="lxml")

        deps = soup.find("ul", {"aria-label": "Dependencies"})

        if deps is None:
            return

        for dep in deps.find_all("a"):
            dep = dep.text
            print("\t" * tab_level, package_name, " -> ", dep, sep="")
            DepParser.__parse(dep, tab_level + 1)

    @staticmethod
    def parse(package_name: str) -> None:
        print("Digraph {")
        DepParser.__parse(package_name)
        print("}")
