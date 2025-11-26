# Meu Controle Financeiro

Estrutura organizada do projeto e instruções básicas (explicação simples para leigos).

Raiz do projeto (descrição simples):

- `manage.py` — utilitário do Django para rodar o servidor, migrações e comandos.
- `db.sqlite3` — banco de dados SQLite (arquivo de dados). Recomendado NÃO versionar em repositórios.
- `requirements.txt` — dependências do projeto (usar para criar o ambiente virtual).
- `scripts/` — scripts CLI auxiliares (aqui está o `main.py` original). Está separado do app web.
- `core/` — app Django principal (models, views, admin, templates, lógica de negócio).
- `financeiro/` — configuração do projeto Django (`settings.py`, `urls.py`, `wsgi.py`).

Notas rápidas para uso

1. Preparar ambiente (Windows, bash):

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

2. Rodar o servidor Django:

```bash
# na raiz do projeto
python manage.py migrate
python manage.py runserver
```

3. Acessar admin: http://127.0.0.1:8000/admin/ (crie superuser com `python manage.py createsuperuser`)

4. Usar o CLI antigo (opcional):

```bash
python scripts/main.py
```

Por que separei `scripts/`?

O `main.py` original é um utilitário de terminal que escreve/ler CSVs. Para evitar confusão com o Django (que usa ORM e admin), movi ele para `scripts/` — assim fica claro que é uma ferramenta separada.

Se quiser integrar a funcionalidade CLI ao Django (ex.: usar ORM), eu posso converter o código para um comando `manage.py`.