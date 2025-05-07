import requests  # Importing requests library to handle HTTP requests


class FlowerNames:
    def __init__(self, url):
        self.url = url

    def GetFlowerNames(self):
        response = requests.get(self.url)
        data = response.text
        flower_names = self.ExtractFlowerNames(data)
        return flower_names

    def ExtractFlowerNames(self, data):
        lines = data.split('\n')  # .split is use to split data into lines
        flower_names = set()  # set is used to avoid duplicates
        for line in lines:
            if line.strip():  # .strip used to remove trailing and leading whitespace
                parts = line.split(',')
                if len(parts) > 4:
                    flower_name = parts[4].strip()
                    flower_names.add(flower_name)
        return list(flower_names)


def main():
    # URL of the Iris dataset
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    fetch = FlowerNames(url)
    flower_names = fetch.GetFlowerNames()
    print("Flower names in the dataset:")
    for name in flower_names:
        print(name)


if __name__ == "__main__":
    main()
