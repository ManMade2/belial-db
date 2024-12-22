from pathlib import Path
from belial_db.models import MapModel, AssetModel  # type: ignore
from belial_db.repos import MapRepo, AssetRepo, AssetFileRepo

from belial_db import create_connection

output_path = Path("C:/Users/MadsKris/Desktop/Converted Data")
DATABASE_URL = f"sqlite:///{output_path}/data.db"
engine = create_connection(DATABASE_URL, echo=False)


mapRepo = MapRepo(engine)
assetRepo = AssetRepo(engine)
assetFileRepo = AssetFileRepo(engine)
