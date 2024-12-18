from belial_db.models import MapModel
from belial_db.repos import MapRepo

from belial_db import create_connection

DATABASE_URL = "sqlite:///file.db"
engine = create_connection(DATABASE_URL, echo=True)

map = MapModel()
map.Name = "test"
map.Id = 11120

mapRepo = MapRepo(engine)
# mapRepo.create_map(map)


asdasd = mapRepo.get_map(11120)
print(asdasd)
