#  Install and setup Ollama

To setup Ollama for public access, edit as follows:

```
vi /etc/systemd/system/ollama.service
```

contents

```
[Unit]
Description=Ollama Service
After=network-online.target

[Service]
ExecStart=/usr/local/bin/ollama serve
User=ollama
Group=ollama
Restart=always
RestartSec=3
Environment="PATH=/root/.local/bin:/root/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin"
Environment="https_proxy=$PROXY"
Environment="http_proxy=$PROXY"
#Environment='OLLAMA_HOST="127.0.0.1:11434"'
Environment='OLLAMA_HOST="0.0.0.0:11434"'
Environment='OLLAMA_MODELS=/disk01/ollama/models/'
Environment='no_proxy="localhost,127.0.0.1,10.10.10.6 ,.org.com"'

[Install]
WantedBy=default.target


```