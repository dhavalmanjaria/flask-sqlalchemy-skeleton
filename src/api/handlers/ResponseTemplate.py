class ResponseTemplate:
	"""DTO containing a standard response that we want to send

	"""

	def __init__(self, message, data, error=False):
		self.message = message
		self.data = data
		self.error = error


	def to_dict(self):
		return self.__dict__