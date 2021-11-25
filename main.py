from GoogleSpider import GoogleSpider

if __name__ == "__main__":
    gs = GoogleSpider()
    keywords = ["china","USA"]
    for keyword in  keywords:
        data = gs.search(keyword=keyword)
        with open('demo.json','a') as f:
            f.write(str(data)+"\n")

