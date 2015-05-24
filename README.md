# doco

###はじめに
docoは、IPアドレスを返す簡単なエコーサーバーです。doco.pyとcoco.pyの組み合わせで使います。

　まず、coco.pyをサーバー側でを立ち上げておきます。こいつは、自信のIPアドレスを教えるデーモンとなります。<br />
　そして、クライアント側で doco.py を実行すると、ブロードキャストでネットワーク内に問い合わせ、coco.pyからIPアドレスを聞いて、サーバーのIPを確認するプログラムとなります。
　
###動作環境
python 2.7.6 or 3.4.0

####インストール
```
git clone git@github.com:sigwin/doco.git
pip install netifaces python-daemon
```

###使い方
####サーバー側
1. 設定の変更<br />
  サーバー側から返すIPアドレスのインターフェースをconfig.jsonの[interface]に設定して下さい。<br />

2. 実行<br />
./coco.py -s

3. 実行確認<br />
ls /tmp/srvApp_*.pid が存在していたら起動OKです。

4. その他<br />
./coco.py -k で停止、-rでサービス再起動です

####クライアント側
./doco.py を起動するだけです。<br />
[サーバーのホスト名]    [IPアドレス]<br />
が表示されればOKです

###その他
python3.4の場合runner.pyの修正が少し必要でした。（何かエラーでる）。

```python
/usr/local/lib/python3.4/dist-packages/daemon/runner.py
try:
	self.daemon_context.stdout = open(app.stdout_path, 'w+t')
except ValueError:
	self.daemon_context.stdout = open(app.stdout_path, 'w+b', buffering=0)

try:
	self.daemon_context.stderr = open(
                app.stderr_path, 'w+t', buffering=0)
except ValueError:
	self.daemon_context.stderr = open(
                app.stderr_path, 'w+b', buffering=0)
```
