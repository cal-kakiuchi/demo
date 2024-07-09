# 使用技術
 フロントエンド  
 -- Next 14(TypeScript 5.4)  
  参考: https://nuxt.com/  
 バックエンド  
 -- FastAPI 0.75(python 3.12.4)  
  参考: https://fastapi.tiangolo.com/ja/  
 データベース  
 -- MariaDB 11.4  
 仮想環境  
 -- Docker Compose version v2  
  *事前にRancher Desktopをインストールして起動しておくこと  
  　https://rancherdesktop.io/  
  
# init
 ``` bash
  #python環境ビルド(初回起動時のみ)
    docker compose run --entrypoint "poetry install --no-root" backend
  #ドッカー起動
    docker compose up --build -d
 ```
  
# ブラウザからアクセス
 *フロントエンド*  
  http://localhost/  
 *バックエンド*  
  http://localhost:8000/  
 *対話型APIドキュメント*  
  http://localhost:8000/docs  
