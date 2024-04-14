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
    # directory内のすべてのファイルに対してループを実行
    for root, dirs, files in os.walk(directory):
        # 検索上に適合するファイルを削除
        for file in files:
            # ファイルのパスを生成
            file_path = os.path.join(root, file)

            # ターゲット名がファイル名に含まれているかチェック
            if target_name in file:
                # ターゲット名がファイル名に含まれている場合の処理
                # デバッグモードが有効でない場合、ファイルを削除
                if not DEBUG:
                    try:
                        os.remove(file_path)
                        logging.info('{:6} - {:6} : "{}" found in {}/"{}"'.format('File', 'Dell', target_name, root, file))
                    except OSError as e:
                        # ファイルが削除されなかった場合のメッセージを出力
                        logging.info('{:6} - {:6} : "{}" connot be deleted : {}'.format('File', 'Error', file_pathl, str(e)))
            else:
                # ターゲット名がファイル名に含まれていない場合の処理
                logging.info('{:6} - {:6} : "{}" not found in {}/"{}"'.format('File', 'Pass', target_name, root, file))


def delete_empty_folder(directory):
    # directory内のすべてのフォルダに対してループを実行
    # 空のフォルダを削除
    for root, dirs, files in os.walk(directory):
        for folder in dirs:
            # フォルダのパスを生成
            folder_path = os.path.join(root, folder)
            # フォルダがからの場合削除
            try:
                if not DEBUG:
                    os.rmdir(folder_path)
                # フォルダが削除された場合のメッセージを出力
                logging.info('{:6} - {:6} : "{}" is empty'.format('Folder', 'Dell', folder_path))
            except OSError as e:
                # フォルダが削除されなかった場合のメッセージを出力
                logging.info('{:6} - {:6} : "{}" is not empty'.format('Folder', 'Pass', folder_path))


def main():
    # DeleteList.txtから削除対象のディレクトリとファイル名を取得
    delete_list_path = "DeleteList.txt"  # ファイルのパス

    # ファイルを開いて空の行を取り除きながら全ての行を読み込む
    with open(delete_list_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    # ディレクトリと削除したいファイル名を定義
    root_directory = lines[0].split('=')[1]

    # ファイルとを削除
    for file_name_to_delete in lines[1:]:
        delete_files_with_name(root_directory, file_name_to_delete)

    # 空のディレクトリを削除
    delete_empty_folder(root_directory)


if __name__=='__main__':
    main()
