import click
import os

root = os.path.abspath(os.path.dirname(__file__))+'/../'

@click.command(name='createBundle')
@click.option('--name', prompt=True, help='name of the bundle')
def newBundle(name):
    bundle = root+name
    if os.path.isdir(bundle):
        print('Name is already taken')
        return
    else:
        os.mkdir(bundle)
        createInitFile(bundle+'/__init__.py')
        createCommandFile(bundle+'/command.py')
        createModelFile(bundle+'/model.py')
        createControllerFile(bundle+'/controller.py')
        print('Bundle {} created succesfully'.format(name))

def createInitFile(root):
    with open(root, 'w') as file:
        pass

def createCommandFile(root):
    with open(root, 'w') as file:
        file.write('import click')

def createControllerFile(root):
    with open(root, 'w') as file:
        file.write('from flask import Blueprint ')

def createModelFile(root):
    with open(root, 'w') as file:
        file.write('from app.extensions import db')
