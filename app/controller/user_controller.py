from app.model.mysql import db
from app.model.mysql.user import User
from app.model.mysql.role import Role

def checkUserExists(username):
    user = User.query.filter_by(username=username).first()
    print "user: %s %s" % (str(user), type(user))
    if user:
        return True
    else:
        return False

def addUser(username, role='developer'):
    role = Role.query.filter_by(name=role).first()
    if role:
        user = User(username=username, role=role)
        db.session.add(user)
        db.session.commit()
        return True
    else:
        return False