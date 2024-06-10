# 仕様技術
 -- Nuxt3.0(TypeScript)
 -- FastAPI(python)
 -- MYSQL

# init
 ``` bash
  #ビルド
    docker compose build --no-cache

  #ドッカー起動
    docker compose up -d
 ```

 # Nuxt起動
  ``` bash
  #フロントエンドフォルダに移動
    cd ../demo/frontend
  #フロントエンドフォルダ内で実行
    docker compose run frontend npm run dev
  ```

# ブラウザからアクセス
 *フロントエンド*
  https://localhost:3000
 *バックエンド*
  https://localhost:8000
