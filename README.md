# First Shooting

Pyxelで開発している、固定画面型の2Dシューティングゲームです。
画面は256×192ピクセルです。

## 現在の状態

ゲーム実行基盤を作成中です。現在起動できるのは黒い画面だけで、
自機・敵・攻撃・ステージ進行などのゲーム機能はまだ実装されていません。
実装項目と進捗は [`PLAN/IMPLEMENTATION.md`](PLAN/IMPLEMENTATION.md) を参照してください。

## 必要なもの

- Python 3.13以降
- [uv](https://docs.astral.sh/uv/)

## 準備

プロジェクトのルートフォルダーで依存関係を同期します。

```powershell
uv sync
```

## PCで起動

```powershell
uv run python main.py
```

現状は黒いゲーム画面が開きます。Pyxelの終了操作はEscキーです。

## HTMLを作成

Pyxelは、アプリのソースを`.pyxapp`にまとめてから、単独で動作するHTMLへ変換できます。
HTML出力ではアプリのソース一式が必要です。次の例では、`main.py`と`game/`を
`build/pyxel-app/`へコピーしてから変換します。

```powershell
New-Item -ItemType Directory -Force build/pyxel-app | Out-Null
Copy-Item main.py build/pyxel-app/
Copy-Item game build/pyxel-app/ -Recurse
uv run pyxel package build/pyxel-app main.py
```

`pyxel package`が出力した`.pyxapp`のパスを指定してHTMLに変換します。

```powershell
uv run pyxel app2html <生成された.pyxappのパス>
```

`<生成された.pyxappのパス>`は、実際に出力されたファイルのパスに置き換えてください。
生成されたHTMLはサーバーなしで実行できます。

詳しくは[Pyxel公式ガイド](https://github.com/kitao/pyxel/blob/main/docs/user-guide.md)と
[Pyxel Webガイド](https://github.com/kitao/pyxel/wiki/How-To-Use-Pyxel-Web/3c7ccc624e95584ecc1c9696628cafca91bff7df)を参照してください。
