from dremio_client import init
from dremio_client.conf.config_parser import build_config
from dremio_client.dremio_simple_client import SimpleClient


client = init(config_dict={"auth.username": "welly", "hostname": "10.100.0.109"}) # initialise connectivity to Dremio via config file

catalog = client.data # fetch catalog

vds = catalog.space.vds.get() # fetch a specific dataset
# df = vds.query() # query the first 1000 rows of the dataset and return as a DataFrame
# pds = catalog.source.pds.get() # fetch a physical dataset
# pds.metadata_refresh() # refresh metadata on that dataset