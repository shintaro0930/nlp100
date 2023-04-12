# NLP100本ノック 第7章
＊Google Colab上で.gzを解凍できなかったので、ローカルで行う。\
(colabが.gzを認識しなかった)

### 1. コンテナの起動
```zsh
docker build -t IMAGE .
```
適宜`IMAGE`を名付ける

```zsh
docker run --rm -it --gpus all -v $(pwd):/work IMAGE
```
機械学習を行うのでGPUを使用するように設定

