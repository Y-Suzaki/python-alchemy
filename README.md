# python-alchemy

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
    
### 実装手順
##### 共通設定
* データベース設定の実装
##### モデルの定義
* 実装方法
* 各モデルの説明
    * Engineer
        * URL
    * Skill
        * URL
    * EngineerSkill
        * URL
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
