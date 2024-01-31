# GeoguessrConverter

グーグルマップの情報をジオゲッサーに入力するために作成したプログラムです。
分からないことがあったら、[Qiita 記事](https://qiita.com/takenakadx/items/dc7c61510ee5d53746e1)を読んでいただけるといいかも知れません。

## 事前に用意するもの

- Google Street View Static API が利用できる API Key
- python3 とライブラリ
  - csv
  - requests
- google map からダウンロードした自分のピン情報 csv

## 使い方

設定ファイル(setting.json)に API の情報を書き込みます。

```
python3 convert.py <設定ファイルのパス>
```

初期では、次のようなコマンドで動きます。

```
python3 convert.py setting.json
```
