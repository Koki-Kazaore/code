# Flickrで写真を検索して、ダウンロードする
from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

# APIキーとシークレットの指定
key = "{{ APIキーを入力 }}"
secret = "{{ シークレットの入力 }}"
# 待機秒数
wait_time = 1

# キーワードとディレクトリ名を指定してダウンロード
def main():
    go_download("マグロ寿司", "sushi")
    go_download("サラダ", "salad")
    go_download("麻婆豆腐", "tofu")

# Flickr APIで写真を検索
def go_download(keyword, dir):
    # 画像の保存パスを決定
    savedir = "./image/" + dir
    if not os.path.exists(savedir):
        os.mkdir(savedir)
    # APIを使ってダウンロード
    flickr = FlickrAPI(key, secret, format="parsed-json")
    res = flickr.photos.search(
        text = keyword,         # 検索語
        per_page = 10,          # 取得件数
        media = "photos",       # 写真を検索
        sort = "relevance",     # 検索語の関連順に並べる
        safe_search = 1,        # セーフサーチ
        extras = "url_q, license"
    )
    # 検索結果を確認
    photos = res["photos"]
    pprint(photos)
    try:
        # 1枚ずつ画像をダウンロード
        for i, photo in enumerate(photos["photo"]):
            url_q = photo["url_q"]
            filepath = savedir + "/" + photo["id"] + ".jpg"
            if os.path.exists(filepath): continue
            print(str(i + 1) + ":download=", url_q)
            urlretrieve(url_q, filepath)
            time.sleep(wait_time)
    except:
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
