# FileDelete ファイルとフォルダを削除するスクリプト

![License-MIT](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)
![Python](https://custom-icon-badges.herokuapp.com/badge/Python-3572A5.svg?logo=Python&logoColor=white)

このPythonスクリプトは、指定されたディレクトリ内のファイルとフォルダを削除するためのものです。  
削除対象は、指定されたテキストファイル`DeleteList.txt`から読み取ります。  
大量のファイルから複数のファイルを削除する際に使用ください。  

## 注意事項

ゴミ箱を経由せずファイルを削除します。使用には細心の注意を払ってください。  
本スクリプトにより不利益が生じた場合、使用したユーザー自身に責任があるものとし、一切の責任を負いません。  

## 使用方法(概要)

1. `DeleteList.txt`ファイル一行目に削除したいファイルが含まれるディレクトリを記述
2. `DeleteList.txt`ファイルに削除したいファイルに含まれる名称(検索ワード)を記述
3. `file_delete.py`もしくは`file_delete.exe`を実行すると、検索ワードに部分一致したファイルを削除
4. フォルダが入れ子状になっている場合、フォルダ内が空の場合はフォルダも削除

## 使用方法 DeleteList.txt

以下の書式で`DeleteList.txt`を編集

### 削除したいファイルが含まれるフォルダパスの記述

削除したいファイルが含まれるフォルダ`sample_dir`が`file_delete.py`もしくは`file_delete.exe`と同一階層に存在する場合、`DeleteList.txt`の一行目に下記のように相対パスでフォルダのパスを記述。

```txt
root=./sample_dir
```

### 削除したいファイルの条件を記述

削除したいファイルに含まれる名称(検索ワード)を下記の書式で2行目以降に記述

```txt
root=./sample_dir
sample_word01
sample_word02
```

### 使用方法 file_deleteの実行

`file_delete.py`の場合  

Windows  

```shell
python -m file_delete.py
```

Linux(Ubuntu)

```shell
python3 file_delete.py
```

`file_delete.exe`の場合はそのまま実行

## デバッグモード

`file_delete.py`を使用する場合のみソースコード中の10,11行目のコメントアウト部を変更することで、削除処理を回避することが可能です。
実行結果はスクリプト実行時に生成される`file_processing.log`を確認。

```python
import os
import logging

# ログの設定
logging.basicConfig(filename='file_processing.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# デバッグモードの有無
#   True : 有効
#   False : 無効
# DEBUG = True
DEBUG = False

def delete_files_with_name(directory, target_name):

def delete_empty_folder(directory):

def main():

if __name__=='__main__':
    main()
```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細については、[LICENSE][LICENSE]ファイルを参照してください。

[LICENSE]: https://github.com/mizu-99/FindItNow/blob/master/LICENSE

## 作者

file_deleteは、GitHubで[Mizu-99][Mizu-99]によって開発されました。

[Mizu-99]: https://github.com/mizu-99
