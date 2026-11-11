[✓]PLAN整合性チェック

完了

- ID: I-01 TITLE: ゲーム実行基盤
  - PLAN <
    - [完了] SPEC詳細
    - [完了] DESIGN詳細
  - IMPLEMENT <
    - [完了] コード作成
    - [完了] 簡易テスト

実装中

- ID: I-02 TITLE: オブジェクトと操作
  - PLAN < I-01
    - [完了] SPEC詳細
    - [完了] DESIGN詳細
  - IMPLEMENT < I-01
    - [未着手] コード作成
    - [未着手] 簡易テスト
- ID: I-03 TITLE: 戦闘処理
  - PLAN < I-02
    - [完了] SPEC詳細
    - [完了] DESIGN詳細
  - IMPLEMENT < (I-02)
    - [未着手] コード作成
    - [未着手] 簡易テスト
- ID: I-04 TITLE: ステージ進行
  - PLAN < I-03
    - [完了] SPEC詳細
    - [完了] DESIGN詳細
  - IMPLEMENT < (I-03)
    - [未着手] コード作成
    - [未着手] 簡易テスト

-- PC・HTMLの両方で1ステージのプレイサイクルを遊べる --
  - [未着手] 全体テスト

将来対応


- ID: I-05 TITLE: 敵02の追加
  - PLAN < I-02, I-03, I-04
    - [未着手] SPEC詳細
    - [未着手] DESIGN詳細
  - IMPLEMENT < (I-02,I-03,I-04)
    - [未着手] コード作成
    - [未着手] 簡易テスト
- ID: I-06 TITLE: ステージ2・3の進行
  - PLAN < I-04, (I-05)
    - [未着手] SPEC詳細
    - [未着手] DESIGN詳細
  - IMPLEMENT < (I-04,I-05)
    - [未着手] コード作成
    - [未着手] 簡易テスト

-- PC・HTMLで全3ステージを完走できる --
  - [未着手] 全体テスト
