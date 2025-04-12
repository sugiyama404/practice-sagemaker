import sys

# ベースパッケージを読み込む
base_packages = {}
with open('/tmp/base_packages.txt', 'r') as f:
    for line in f:
        if '==' in line:
            name, version = line.strip().split('==', 1)
            base_packages[name.lower()] = version

# requirements.txtからインストールするパッケージを抽出
install_packages = []
with open('requirements.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#'):
            # パッケージ名を抽出（バージョン指定があればそのまま使用）
            if '==' in line:
                name = line.split('==', 1)[0].lower()
            elif '>=' in line:
                name = line.split('>=', 1)[0].lower()
            elif '<=' in line:
                name = line.split('<=', 1)[0].lower()
            else:
                name = line.lower()

            # ベースパッケージに含まれていなければインストール対象に追加
            if name not in base_packages:
                install_packages.append(line)

# 結果を出力
for package in install_packages:
    print(package)
