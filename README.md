# python-alchemy

### 所感
* やりたいことは一通り実現できるため、機能的には問題ない
* 同じSQLでも書き方が複数存在するため、最初に認識合わせしておいた方が良さそう

### 対象
* Python3.6
* MySQL
* MySQL Driver mysqlclient

### 環境準備
* MySQL Driverのインストール（他でも良いが、本説明ではmysqlclientを使用する）
    ```
    pip3 install mysqlclient
    ```
* alchemyのインストール
    ```
    pip3 install SQLAlchemy
    ```
### 本サンプルで扱うER図   

### 実装手順
##### 共通設定
* データベース設定の実装
    * https://github.com/Y-Suzaki/python-alchemy/blob/master/src/sqlalchemy_settings.py
    * DBの接続設定や、モデル共通で継承するBaseクラスを定義している
##### モデルの定義
* 実装方法
    * 上述したBaseクラスを必ず継承する必要がある
    * テーブル名やカラムの定義は規則に従って必ず実装する必要がある
    * リレーション設定は必須ではないが、Joinする際に楽になるため、定義しておいた方が良い
* 各モデルの説明
    * Engineer
        * https://github.com/Y-Suzaki/python-alchemy/blob/master/src/model/engineer.py
    * Skill
        * https://github.com/Y-Suzaki/python-alchemy/blob/master/src/model/skill.py
    * EngineerSkill
        * https://github.com/Y-Suzaki/python-alchemy/blob/master/src/model/engineer_skill.py
        * 複合Primary Keyを設定している
##### 更新系
* 追加
    * モデルにデータを設定し、addメソッドで追加するだけで良い
    ``` java
    ```
* 更新
    * Session上に管理されている必要があるため、一度データを取得する必要がある
    ``` java
    ```
* 削除
    * Session上に管理されている必要があるため、一度データを取得する必要がある
    ``` java
    ```
##### 参照系
* デフォルト状態（明示的に指定しない）だと、以下の設定になっている
    * 結合方法は、Outer Join
    * 結合先のデータ取得は、Lazy Fetch
* Inner Join
    * a
    ``` java
    ```
* Outer Join
    * a
    ``` java
    ```
### Tips
* Session破棄後、Lazy Fetchでデータ取得するとエラーになる
    * 本サンプルでは、Eager Fetchを指定している
    * 本来であれば、Sessionスコープを広く取り、Lazy Fetchも活用した方が良い
