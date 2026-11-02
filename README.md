# First Shooting

Python標準ライブラリのTkinterで作った小さなシューティングゲームです。
敵を撃つと10点。敵にぶつかったり、敵が画面の下へ抜けたりするとライフが減り、
3回でゲームオーバーになります。スコアが増えると難しくなります。

## 起動

Python 3.13以降（Tkinter付き）で、プロジェクトのフォルダから実行します。

```powershell
$env:PYTHONPATH = "src"
python -m first_sht
```

uvを使う場合は `uv run first-sht` でも起動できます。

## 操作

- 左右キー / A・D：移動
- スペース：射撃（長押しで連射）
- R：ゲームオーバー後にリスタート
- ウィンドウを閉じる：終了

ゲーム本体は `src/first_sht/__init__.py` にあります。
