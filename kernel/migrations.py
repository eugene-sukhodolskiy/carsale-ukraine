def migrate(db, cursor):
	cursor.execute('''CREATE TABLE IF NOT EXISTS `posts`(
		`id` INTEGER PRIMARY KEY AUTOINCREMENT,
		`uid` TEXT,
		-- Index of current step of posting. You can find map of exists steps in `config.py`
		`step` INTEGER,
		`phone_number` TEXT,
		-- draft | published | canceling
		`state` TEXT,
		`carlabel` TEXT,
		`model` TEXT,
		`photos` TEXT,
		`year` INTEGER,
		`region` TEXT,
		`fuel_type` TEXT,
		-- You can find map of gearboxes in `config.py`
		`gearbox_type` INTEGER,
		-- You can find map of exists drivetrains in `config.py`
		`drivetrain` INTEGER,
		`motorway` INTEGER,
		`engine_capacity` REAL,
		`price` INTEGER,
		`price_currency` TEXT,
		`description` TEXT,
		`create_at` TEXT,
		`published_at` TEXT
	)''')

	db.commit()
	pass