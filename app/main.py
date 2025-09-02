from database.db import Base, engine
from User.models import User
from Todo.models import Todo

# Cria as tabelas porém mas ficará comentado até ser necessário de novo
# Base.metadata.create_all(bind=engine)