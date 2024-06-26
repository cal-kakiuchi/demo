# 使用技術
 -- Nuxt3.0(TypeScript)  
  参考: https://nuxt.com/  
 -- FastAPI(python3.8.19)  
  参考: https://fastapi.tiangolo.com/ja/  
 -- MYSQL8.4LTS  
 -- DOCKER　*事前にDOCKERまたはRANCHERをインストールして起動しておくこと

# init
 ``` bash
  #python環境ビルド(初回起動時のみ)
    docker compose run --entrypoint "poetry install --no-root" backend
  #ドッカー起動
    docker compose up -d
 ```
  
# ブラウザからアクセス
 *フロントエンド*  
  http://localhost/  
 *バックエンド*  
  http://localhost:8000/  
 *対話型APIドキュメント*  
  http://localhost:8000/docs  
