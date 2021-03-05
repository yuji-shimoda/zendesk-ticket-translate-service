# Name
 
zendesk-ticket-translate-service
 
# Features
 
様々な言語での問い合わせ内容を、Amazon Translate で指定言語に機械翻訳を行いメモとして追記するサービス
Zendesk の新規チケット発行イベントを Amazon EventBridge 経由で Lambda 関数を呼び出し、処理しています。
PoC もしくは検証用途にてご利用ください。

# Requirement
 
* [Python 3.8](https://github.com/python/cpython)
* [boto3](https://github.com/boto/boto3)
* [zenpy](https://github.com/facetoe/zenpy)
* [pipenv](https://github.com/pypa/pipenv)
* [Serverless Framework](https://github.com/serverless/serverless)
* [serverless-python-requirements](https://github.com/UnitedIncome/serverless-python-requirements)
 
# Installation
 
```bash
pipenv --python 3.8
pipenv install zenpy boto3
sls plugin install -n serverless-python-requirements
```
 
# Documentation
 
See also

* https://dev.classmethod.jp/articles/try-to-automatically-translate-the-inquiry-contents-by-linking-zendesk-and-amazon-translate/
 
 
# License
 
zendesk-ticket-translate-service is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).