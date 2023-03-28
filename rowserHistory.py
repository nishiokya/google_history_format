import json
from datetime import datetime

def parse_search_history(file_path):
 with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

    search_history = []

    for item in data:
        if "query" in item:
            query = item["query"]["query_text"]
            timestamp = int(item["query"]["id"][0]["timestamp_usec"]) // 1000000
            datetime_obj = datetime.fromtimestamp(timestamp)
            search_history.append((query, datetime_obj))

    return search_history

def main():
    file_path = "search_history.json"  # JSONファイルのパスを指定してください
    search_history = parse_search_history(file_path)

    for query, timestamp in search_history:
        print(f"{timestamp} - {query}")

if __name__ == "__main__":
    main()