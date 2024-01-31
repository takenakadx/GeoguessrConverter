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

1. 設定ファイル(setting.json)に API の情報と、ダウンロードしたピン情報のパスを書き込みます。

2. その後、programs にある convertcsv.py を次のようなオプションで実行します。

```
python3 convertcsv.py <設定ファイルのパス>
```

初期では、次のようなコマンドで動きます。

```
python3 convertcsv.py setting.json
```
