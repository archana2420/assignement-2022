import sqlalchemy  as sql
import sqlalchemy.orm as orm
import database


class Students(database.Base):
    __tablename__ = "Students"
    id = sql.Column(sql.Integer,primary_key=True)
    name = sql.Column(sql.String)
    department = sql.Column(sql.String)
    email = sql.Column(sql.String)
    mobile = sql.Column(sql.BIGINT)
    address = sql.Column(sql.String)
    