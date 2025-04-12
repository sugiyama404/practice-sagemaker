import pkg_resources

# 現在インストールされているパッケージとそのバージョンを取得
installed_packages = [(d.project_name, d.version) for d in pkg_resources.working_set]

# パッケージ名とバージョンを出力
for package_name, version in sorted(installed_packages):
    print(f"{package_name}=={version}")
