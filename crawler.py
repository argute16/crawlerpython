from crawler import ArticleFetcher
import csv

fetcher = ArticleFetcher()
# this part prints the first 8 articles
count = 0
for article in fetcher.fetch():
    if count == 8:  # stops the scraping when we have reached 8 articles (this is only possible when we use generator)
        break
    count = count + 1
    print(article.emoji + ": " + article.title)
# this part stores all articles
with open('crawler_output.csv', 'w', newline='', encoding='utf-8') as csvfile:  # without encoding an error occurred
    articlewriter = csv.writer(csvfile, delimiter=';', quotechar='"',
                               quoting=csv.QUOTE_MINIMAL)  # ; and " are necessary for excel
    for article in fetcher.fetch():
        articlewriter.writerow([article.emoji, article.title, article.image, article.content])
print("All Articles are stored")
