mkdir bin
wget "https://modelscope.cn/api/v1/models/issaccv/OllamaDeploy/repo?Revision=master&FilePath=ollama-linux-amd64" -O bin/ollama
chmod +x bin/ollama
OLLAMA_FLASH_ATTENTION=1 bin/ollama serve &

wget "https://www.modelscope.cn/api/v1/models/qwen/Qwen2-7B-Instruct-GGUF/repo?Revision=master&FilePath=qwen2-7b-instruct-q8_0.gguf" -O qwen-2-7b-instruct.gguf

bin/ollama create qwen -f modelfile