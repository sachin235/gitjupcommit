from gitjupcommit.handlers import setup_handlers
# Jupyter Extension points
def _jupyter_server_extension_paths():
    return [{
        'module': 'gitjupcommit',
    }]

def _jupyter_nbextension_paths():
    return [{
        "section": "notebook",
        "dest": "gitjupcommit",
        "src": "static",
        "require": "gitjupcommit/main"
    }]

def load_jupyter_server_extension(nbapp):
    setup_handlers(nbapp.web_app)
