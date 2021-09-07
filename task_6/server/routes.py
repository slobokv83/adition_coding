from server import app, db
from server.models import Advertisement
from flask import abort
from sqlalchemy import exc

@app.route('/user/<user_id>', methods=['GET'])
def advert_seen(user_id):
  try:
    advert = db.session.query(Advertisement).filter(
    Advertisement.userid == user_id).all()
  except exc.DataError:
    abort(400, 'Invalid user')
  except exc.SQLAlchemyError:
    abort(500, 'Internal server error')

  return {"advertisements": len(advert)}
    

  