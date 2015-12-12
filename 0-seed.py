import dataset
import base36 as b36
import settings as s

# access the database with table `images`
db = dataset.connect('sqlite:///%s' % s.db_fname)

# Conduct as SQL Transaction to reduce commits
with db as tx:
	i = 1679616
	base36_id = "010000"
	img_url = ""
	
	# insert into table
	tx['images'].insert(dict(id=i, img_id=base36_id, img_url=img_url))