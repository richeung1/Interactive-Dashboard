mkdir -p ~/.streamlit/

echo "[theme]
primaryColor='#FF6347'
backgroundColor='#00172B'
secondaryBackgroundColor='#00172B'
textColor='#FFF'
font='sans serif'
[server]
headless = true
enableCORS=false
port = $PORT
" > ~/.streamlit/config.toml