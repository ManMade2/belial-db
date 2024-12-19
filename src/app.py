from belial_db.models import MapModel, AssetModel  # type: ignore
from belial_db.repos import MapRepo, AssetRepo

from belial_db import create_connection

DATABASE_URL = "sqlite:///:memory:"
engine = create_connection(DATABASE_URL, echo=True)

map = MapModel()
map.Name = "test"
map.Id = 11120

mapRepo = MapRepo(engine)
# mapRepo.create_map(map)

assetRepo = AssetRepo(engine)

asset = assetRepo.get_asset(1)
if asset is not None:
    id: int = asset.Id

asdasd = mapRepo.get_map(11120)
print(asdasd)
