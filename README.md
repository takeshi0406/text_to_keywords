# text_to_keywords

Python3 Library to convert Japanese text to word list はてなキーワード自動リンクAPI.

はてなキーワード自動リンクAPIを使って、日本語のテキストをキーワードに変換するライブラリです。

Mecab等の形態素解析器を利用するより、（対象となる単語がはてなキーワードに存在すれば）簡単に扱うことができます。
http://developer.hatena.ne.jp/ja/documents/keyword/apis/autolink

## Description

```python
from text_to_keywords.client
client = text_to_keywords.client()
text = 'スピッツが主催する夏季恒例ライブ「ロックのほそ道」と「新木場サンセット」の開催が決定した。'
res = client.parse_text(text=text, cname=['music'])
print(res)
```

result
```
[{'cname': 'music', 'refcount': 5, 'score': 10, 'word': 'サンセット'}, {'cname': 'music', 'refcount': 6, 'score': 55, 'word': 'スピッツ'}, {'cname': '', 'refcount': 89, 'score': 18, 'word': 'ロック'}, {'cname': '', 'refcount': 316, 'score': 17, 'word': 'ライブ'}, {'cname': '', 'refcount': 330, 'score': 17, 'word': 'ライブ'}, {'cname': '', 'refcount': 88, 'score': 15, 'word': '主催'}, {'cname': '', 'refcount': 9, 'score': 8, 'word': '夏季'}]
```


## Installation
```
pip install git+https://github.com/takeshi0406/text_to_keywords
```


