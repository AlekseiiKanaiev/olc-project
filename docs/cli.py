import os
from app import app
import click

@app.cli.group()
def translate():
    pass

@translate.command()
def update():
    """Upadate all languages"""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system('pybabel update -i message.pot -d app/translations'):
        raise RuntimeError('update command failed')
    os.remove('message.pot')

@translate.command()
def compile():
    """Compile all languages"""
    if os.system('pybabel compile -d app/translation'):
        raise RuntimeError('ccompile command failed')

@translate.command()
@click.argument('lang')
def init(lang):
    """Initialize a new language"""
    if os.system('pybabel extract -F babel.cfg -k _l -o message.pot .'):
        raise RuntimeError('extract command failed')
    if os.system('pybabel init -i message.pot -d app/translations -l'+lang):
        raise RuntimeError('init command failed')
    os.remove('message.pot')