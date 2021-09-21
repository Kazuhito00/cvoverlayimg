# cvoverlayimg
 cvoverlayimgはOpenCVで透過PNGを画像の上に重ね合わせるクラスです。
 
 ![2020-02-18 (1)](https://user-images.githubusercontent.com/37477845/74670515-b04a1c00-51ec-11ea-90bc-f09e9d1ae96d.png)

# Requirements
 
* OpenCV 3.4.15.55
* Pillow 8.3.2
 
# Installation
 
利用したいPythonプログラムと同階層に`cvoverlayimg/`ディレクトリと`requirements.txt`をコピーしてください。

使用方法はsample.pyを参考にしてください。
 
# Usage

仮想環境に依存ライブラリをインストールします。

※表記について: `(venv)`は仮想環境が有効であることを示しています。

```bash
python -m venv venv
source venv/bin/activate
# win の場合は .\venv\Scripts\activate.bat

(venv) pip install -r requirements.txt
```
 
サンプルの実行方法は以下です。
 
```bash
(venv) python sample.py
```

# Note
サンプルの画像はいらすとや様を使用しています。
https://www.irasutoya.com/

# Author
高橋かずひと
 
# License 
cvoverlayimg is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).

