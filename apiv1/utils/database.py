from typing import Self
import pymysql
import django_redis


class mysqlBase():
  
  def __new__(cls) -> Self:
    if hasattr(cls,'__instance'):
      return getattr(cls, '__instanc')

    obj = super().__new__(cls)
    setattr(cls, '__instance', obj)
    return obj
