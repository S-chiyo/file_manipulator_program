import sys

inputpath = 'input_text.txt'
outputpath = 'output_text.txt'

commands = ['reverse', 'copy', 'duplicate-contents', 'replace-string', 'reset']

# command = input('コマンドを入力してください：')
command = sys.argv[1]


# duplicate-contentsで使用する整数判定用の関数
def checkInt(n):
    if n.isdigit():
        return n 
    else:
        n = input('複製したい回数を整数で入力してください：')
        return checkInt(n)


if command in commands:

    # reverse, 内容を逆にするコマンド
    # 練習のため、最初のコマンドのみ、withを使わずに実装
    if command == commands[0] and len(sys.argv) == 4:
        inputpath = sys.argv[2]
        outputpath = sys.argv[3]

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
    if command == commands[1] and len(sys.argv) == 4:
        inputpath = sys.argv[2]
        outputpath = sys.argv[3]
        with open(inputpath) as f:
            contents = f.read()
        with open(outputpath, 'w') as f:
            f.write(contents)

    # duplicate-contents, inputファイルの内容をn回複製するコマンド
    if command == commands[2] and len(sys.argv) == 4:
        inputpath = sys.argv[2]
        n = sys.argv[3]
        n = int(checkInt(n))

        with open(inputpath) as f:
            contents = f.read()
            result = contents
        for i in range(n):
            result += contents
        with open(inputpath, 'w') as f:
            f.write(result)
    
    # replace-string, ファイルに含まれる置換したい文字列を検索し、別の文字列に置き換えるコマンド
    if command == commands[3] and len(sys.argv) == 5:
        inputpath = sys.argv[2]
        before_s = sys.argv[3]
        after_s = sys.argv[4]
        with open(inputpath) as f:
            s = f.read()
        with open(inputpath, 'w') as f:
            f.write(s.replace(before_s, after_s))

    
    # reset, デバッグ用。input_txtとoutput_txtの中身をリセットするコマンド
    if command == commands[4] and len(sys.argv) == 4:
        inputpath = sys.argv[2]
        outputpath = sys.argv[3]
        with open(inputpath, 'w') as f:
            f.write('noodle needle noodle needle')
        with open(outputpath, 'w') as f:
            f.write('')
    
else:
    print('入力が間違っています。')

