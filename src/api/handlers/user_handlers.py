def handle_get_id(request_json, id):
	try:
		user_id = request_json['user_id']
		user = Users.query.filter_by(_id=user_id).first()
		return ResponseTemplate(error=False, message=f"User with id {user._id} found", 
			data=str(user))
	except psycopg2.OperationalError as oe:
		db.session.rollback()
		log.exception(oe)
		return ResponseTemplate(error=True, message=f"User with id {user._id} NOT found", 
			data=str(oe))
