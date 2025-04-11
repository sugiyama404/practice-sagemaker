#!/bin/bash
set -e

cd /app

echo "ベースパッケージを除外して、指定されたパッケージのみをインストールします..."

# 差分を取得してインストールするパッケージリストを作成
python3 install_diff_packages.py >/tmp/diff_requirements.txt

echo "インストールするパッケージ:"
cat /tmp/diff_requirements.txt

# 差分のパッケージをインストール
if [ -s /tmp/diff_requirements.txt ]; then
  pip3 install -r /tmp/diff_requirements.txt -t /build/python/lib/python3.9/site-packages
else
  echo "インストールするパッケージはありません"
fi

# パッケージをzipに圧縮
echo "Lambda Layer用のzipファイルを作成します..."
zip -r /app/output/my_deployment_package.zip /build/python/lib/python3.9/site-packages

echo "Lambda Layer用のzipファイルが作成されました: /app/output/my_deployment_package.zip"
