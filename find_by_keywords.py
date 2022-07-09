from config import config
from send_email import send_email
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
from search import d1


keyword = d1["keywords"]
def get_result():
    list_of_items = []
    try:
        api = Finding(appid=config.api_key, config_file=None)
        response = api.execute("findItemsAdvanced",d1)
        print(f"Total items {response.reply.paginationOutput.totalEntries}\n")
        for i in response.reply.searchResult.item:
            item_description = [f"Title: {i.title}, ViewURL: {i.viewItemURL}, Price: {i.sellingStatus.currentPrice._currencyId} {i.sellingStatus.currentPrice.value}, Buy It Now: {i.listingInfo.buyItNowAvailable}"]
            list_of_items.append(item_description)
        return response.dict(), list_of_items
    except ConnectionError as e:
        print(e)
        print(e.response.dict())


def main():
    api_result, description = get_result()
    with open("result.csv","w+",encoding="UTF-8") as fopen:
        fopen.write(str(*description))    send_email()


if __name__ == "__main__":
    main()