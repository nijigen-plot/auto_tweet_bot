# python_repository_template
python主体のリポジトリを立てる際のテンプレートとなるリポジトリ

## Linter/Formatter
- [isort](https://github.com/PyCQA/isort)
- [black](https://github.com/psf/black)
- [pflake8](https://github.com/csachs/pyproject-flake8)

## CI
- Github Actionsにて以下の条件時にチェック
  - mainブランチへのプッシュ時
  - プルリクエスト発行時
  - クローズされたプルリクエストの再度オープン時
  - プルリクエストを発行したプルされる側のブランチに対するプッシュをした時
