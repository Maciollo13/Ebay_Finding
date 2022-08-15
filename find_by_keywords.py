from config import config
from send_email import send_email
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
import csv



def get_result():
    list_of_items = []
    try:
        api = Finding(appid=config.api_key, config_file=None)
        response = api.execute("findItemsAdvanced",get_search())
        print(f"Total items {response.reply.paginationOutput.totalEntries}\n")
        for i in response.reply.searchResult.item:
            item_description = [f"Title: {i.title}, ViewURL: {i.viewItemURL}, Price: {i.sellingStatus.currentPrice._currencyId} {i.sellingStatus.currentPrice.value}, Buy It Now: {i.listingInfo.buyItNowAvailable}"]
            list_of_items.append(item_description)
        return response.dict(), list_of_items
    except ConnectionError as e:
        print(e)
        print(e.response.dict())


def get_search():
    print("You'll be asked to type in various variables to the program to tighten up searching result.")
    d1 = {}
    d1["keywords"] = input("Type in the keywords for product to search: ")
    try :
        d1["categoryId"] = int(input("Type in the category Id. If you dont know the Id type \"None\": "))
    except ValueError:
        pass
    while True:
        try:
            d1["paginationInput"] = {"entriesPerPage" : int(input("Type number of entries per page: ")), "pageNumber": int(input("Type page number: "))}
            break
        except ValueError:
            print("Number must be integer. Try again.")
    d1["itemFilter"] = {"name": "LocatedIn", "value" : input("Type country to search in: ")}
    d1["sortOrder"] = ["PricePlusShippingLowest", "StartTimeNewest"]
    return d1


def main():
    api_result, description = get_result()
    with open("result.csv","w+",encoding="UTF-8") as fopen:
        writer = csv.writer(fopen)
        for i in description:
            writer.writerow(i)
    send_email()


if __name__ == "__main__":
    main()