inputpath = 'input_text.txt'
outputpath = 'output_text.txt'

commands = ['reverse', 'copy', 'duplicate-contents', 'replace-string', 'reset']

command = input('コマンドを入力してください：')

# duplicate-contentsで使用する整数判定用の関数
def checkInt(n):
    if n.isdigit():
        return n 
    else:
        n = input('整数を入力してください：')
        return checkInt(n)


# 練習のため、最初のコマンドのみ、withを使わずに実装
if command in commands:

    # reverse, 内容を逆にするコマンド
    if command == commands[0]:
        in_file = open(inputpath)
        in_file_contents = in_file.read()
        contents = ''
        for i in range(len(in_file_contents)):
            contents = in_file_contents[i] + contents
        in_file.close()

        out_file = open(outputpath, 'w')
        out_file.write(contents)
        out_file.close()

    # copy, コピーを作成して保存するコマンド
    if command == commands[1]:
        with open(inputpath) as f:
            contents = f.read()
        with open(outputpath, 'w') as f:
            f.write(contents)

    # duplicate-contents, inputファイルの内容をn回複製するコマンド
    if command == commands[2]:

        n = input('複製する回数を入力してください：')
        n = int(checkInt(n))

        with open(inputpath) as f:
            contents = f.read()
            result = contents
        for i in range(n):
            result += contents
        with open(inputpath, 'w') as f:
            f.write(result)
    
    # replace-string, inputファイルの中にある文字列'needle'を検索し、'newstring'に置き換えるコマンド
    if command == commands[3]:
        with open(inputpath) as f:
            s = f.read()
        with open(inputpath, 'w') as f:
            f.write(s.replace('needle', 'newstring'))

    
    # reset, デバッグ用。input_txtとoutput_txtの中身をリセットするコマンド
    if command == commands[4]:
        with open(inputpath, 'w') as f:
            f.write('noodle needle noodle needle')
        with open(outputpath, 'w') as f:
            f.write('')
    
else:
    print('このコマンドは存在しません。')

