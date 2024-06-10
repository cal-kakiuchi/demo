# 仕様技術
 -- Nuxt3.0(TypeScript)  
 -- FastAPI(python)  
 -- MYSQL  

# init  
 -- `docker compose build --no-cache`  
 -- `docker compose up -d`  
 (ドッカーが起動します）
   

 # Nuxt起動  
  フロントエンドフォルダに移動  
    -- `cd frontend`  
  フォルダ内で実行  
    -- `docker compose exec frontend bash`  
  #ドッカー内で起動  
    -- `npm run dev`  

# ブラウザからアクセス
 *フロントエンド*  
  https://localhost:3000  
 *バックエンド*  
  https://localhost:8000  
