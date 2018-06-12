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
* https://github.com/Y-Suzaki/python-alchemy/blob/master/design/sample-er.wsd
* ![ER図](https://github.com/Y-Suzaki/python-alchemy/blob/master/design/out/sample-er/ER.png)
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
##### Session Open/Closeの実装
* https://github.com/Y-Suzaki/python-alchemy/blob/master/src/session_context.py
* サンプルでは自動Open/Closeさせるため、withブロックで使えるような実装にしている
##### 更新系
* https://github.com/Y-Suzaki/python-alchemy/blob/master/src/sqlalchemy_writer.py
* 追加
    * モデルにデータを設定し、addメソッドで追加するだけで良い
    ``` java
    @staticmethod
    def add_skill(skill):
        with SessionContext() as session:
            session.add(skill)
        return skill
    ```
* 更新
    * Session上に管理されている必要があるため、一度データを取得する必要がある
    ``` java
    @staticmethod
    def update_skill(id, name):
        with SessionContext() as session:
            target = session.query(Skill).get(id)
            target.name = name
    ```
* 削除
    * Session上に管理されている必要があるため、一度データを取得する必要がある
    ``` java
    @staticmethod
    def remove_skill(id):
        with SessionContext() as session:
            target = session.query(Skill).get(id)
            if target is not None:
                session.delete(target)
    ```
##### 参照系
* https://github.com/Y-Suzaki/python-alchemy/blob/master/src/sqlalchemy_reader.py
* デフォルト状態（明示的に指定しない）だと、以下の設定になっている
    * 結合方法は、Outer Join
    * 結合先のデータ取得は、Lazy Fetch
* クエリのパターン例
    * ID指定で1件取得する場合
    ``` java
    @staticmethod
    def get_skill_by_id(id):
        with SessionContext() as session:
            return session.query(Skill).get(id)
    ```
    * 全件取得する場合（order byやlimitは任意）
    ``` java
    @staticmethod
    def get_skill_all_order_by_name(limit=10):
        with SessionContext() as session:
            return session.query(Skill)\
                .order_by(asc(Skill.name))\
                .limit(limit).all()
    ```
    * 特定条件で絞り込み（where）する場合
    ``` java
    @staticmethod
    def get_skill_by_name(name):
        with SessionContext() as session:
            return session.query(Skill)\
                .filter(Skill.name == name).all()
    ```
    * Inner Join
    ``` java
    @staticmethod
    def get_engineer_with_skill_all():
        with SessionContext() as session:
            return session.query(Engineer)\
                .join(EngineerSkill)\
                .join(Skill) \
                .options(joinedload(Engineer.engineer_skill).joinedload(EngineerSkill.skill)).all()
    ```
    * Outer Join
    ``` java
    @staticmethod
    def get_engineer_with_skill_all_outer_join():
        with SessionContext() as session:
            return session.query(Engineer)\
                .outerjoin(EngineerSkill) \
                .outerjoin(Skill) \
                .options(joinedload(Engineer.engineer_skill).joinedload(EngineerSkill.skill)).all()
    ```
### Tips
* Session破棄後、Lazy Fetchでデータ取得するとエラーになる
    * 本サンプルでは、Eager Fetchを指定している
    * 本来であれば、Sessionスコープを広く取り、Lazy Fetchも活用した方が良い
