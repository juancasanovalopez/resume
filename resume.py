# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
# http://ondras.zarovi.cz/sql/demo/
# https://medium.com/@charlie.b.ohara/building-a-flask-rest-api-with-docker-94ca4219f460
# https://docs.docker.com/network/links/

from app import app, db
from app.models import Job

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Job': Job}
