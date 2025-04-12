# Lambda Layer用のDockerfile
FROM amazonlinux:2

# 必要なツールをインストール
RUN yum update -y && \
    yum install -y python3 python3-pip zip && \
    yum clean all

# 作業ディレクトリの設定
WORKDIR /app

# ライブラリのインストール先をLambdaの規約に合わせる
RUN mkdir -p /build/python/lib/python3.9/site-packages

# 元々入っているパッケージリストを取得するためのスクリプトをコピー
COPY get_base_packages.py ./get_base_packages.py

# ベースのパッケージリストを取得
RUN python3 ./get_base_packages.py > /tmp/base_packages.txt

COPY . .

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
