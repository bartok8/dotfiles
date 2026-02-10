#! /bin/bash -x

#./bs.py > lsturl.py
#./bs.py | grep -v --after-context=1 '楽天ブログラッキーくじ'
./bs.py | \
grep -v 'https://kuji.rakuten.co.jp/c8437c01c5' | \
grep -v 'https://kuji.rakuten.co.jp/7e14010b80' \
> lsturl.py
#./bs.py

# ends here.
