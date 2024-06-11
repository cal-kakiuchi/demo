# 仕様技術
 -- Nuxt3.0(TypeScript)  
 -- FastAPI(python)  
 -- MYSQL  
 -- DOCKER　*事前にDOCKERまたはRANCHERをインストールしておいてください  

# init
 ``` bash
  #ビルド
  docker compose build --no-cache
  #poetry install(初回起動時のみ)
  docker compose run --entrypoint "poetry install --no-root" backend
  #ドッカー起動
  docker compose up -d
 ```
  
# ブラウザからアクセス
 *フロントエンド*  
  http://localhost/  
 *バックエンド*  
  http://localhost:8000/  
