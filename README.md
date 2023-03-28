# google_history_format

Pythonを使ってGoogleの検索履歴を取得するには、Google Takeoutからダウンロードした検索履歴のJSONファイルを解析するスクリプトを書くことができます。

まず、Google Takeoutから検索履歴のデータをダウンロードしてください:

Google Takeoutにアクセスし、Googleアカウントにサインインします。
'データの選択'で、'検索履歴'を選択します。
'次へ'をクリックし、エクスポート方法やファイル形式を選択します。JSON形式を選択してください。
'エクスポートを作成'をクリックし、ダウンロードが完了するのを待ちます。
ダウンロードが完了したら、以下のPythonスクリプトを使って検索履歴を取得できます。この例では、検索履歴のJSONファイルの名前を search_history.json としています。

```python
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
```
