# File Manipulator Program
## 概要
ファイルの操作を行うコマンドを提供するプログラムです。</br>
ターミナルで実行すると、コマンドの入力を求められるので、以下のコマンドから選んで入力してください。
</br>
</br>
## コマンド一覧
### reverse
*python3 file_manipulator.py reverse inputpath outputpath*</br>
inputpathの内容を受け取り、その内容を逆にしたものをoutputpathに保存します。</br>
### copy
*python3 file_manipulator.py copy inputpath outputpath*</br>
inputpathのファイルのコピーを作成し、outputpathに保存します。</br>
### duplicate-contents
*python3 file_manipulator.py duplicate-contents inputpath n*</br>
inputpathの内容を読み込んで複製し、その内容をn回だけinputpathに複製します。</br>
### replace-string
*python3 file_manipulator.py replace-string inputpath needle newstring*</br>
inputpathの内容から文字列'needle'を検索し、すべての該当文字列を'newstring'に置き換えます。置換する文字列の内容は変更可能です。</br>
### reset
*python3 file_manipulator.py reset inputpath outputpath*</br>
input/outputに使用したファイルの入力内容を初期値にリセットすることができます。テスト用に作成しました。
</br>
</br>
## 工夫した点
- 存在しないコマンドが入力された場合に「入力が間違っています。」と表示されるようにしました。</br>
- duplicate-contentsで整数以外の数字が入力された場合に再入力を求めるようにしました。</br>
- 動作テストの際に使用するためのresetコマンドを実装しました。
</br>
</br>
## 開発環境
Visual Studio Code
</br>
</br>
## 実行環境
Windows 11
