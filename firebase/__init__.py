
#   Copyright (c) 2022 Asif Arman Rahman
#   Licensed under MIT (https://github.com/AsifArmanRahman/firebase/blob/main/LICENSE)

# --------------------------------------------------------------------------------------


"""A simple python wrapper for Google's `Firebase`_ REST APIs.

.. _Firebase: https://firebase.google.com/
"""

from .auth import Auth
from .storage import Storage
from .database import Database
from .firestore import Firestore
from ._custom_requests import _custom_request
from ._service_account_credentials import _service_account_creds_from_secret


def initialize_app(config, oauth_config):
	"""Initializes and returns a new Firebase instance.

	:type config: dict
	:param config: Firebase configuration

	:type oauth_config: dict
	:param oauth_config: OAuth configuration

	:return: A newly initialized instance of Firebase.
	:rtype: Firebase
	"""

	return Firebase(config, oauth_config)


class Firebase:
	""" Firebase Interface

	:type config: dict
	:param config: Firebase configuration
	"""

	def __init__(self, config, oauth_config):
		""" Constructor """

		self.api_key = config["apiKey"]
		self.auth_domain = config["authDomain"]
		self.database_url = config["databaseURL"]
		self.project_id = config["projectId"]
		self.storage_bucket = config["storageBucket"]
		self.oauth_config = oauth_config

		self.credentials = None
		self.requests = _custom_request()

		if config.get("serviceAccount"):
			self.credentials = _service_account_creds_from_secret(config['serviceAccount'])

	def auth(self):
		"""Initializes and returns a new Firebase Authentication
		instance.

		:param client_id: OAuth 2.0 client ID
		:type client_id: str

		:param client_secret: OAuth 2.0 client secret
		:type client_secret: str

		:return: A newly initialized instance of Auth.
		:rtype: Auth
		"""

		return Auth(self.api_key, self.credentials, self.requests, self.oauth_config)

	def database(self):
		"""Initializes and returns a new Firebase Realtime Database
		instance.

		:return: A newly initialized instance of Database.
		:rtype: Database
		"""

		return Database(self.credentials, self.database_url, self.requests)

	def firestore(self):
		"""Initializes and returns a new Firebase Cloud Firestore
		instance.

		:return: A newly initialized instance of Firestore.
		:rtype: Firestore
		"""

		return Firestore(self.api_key, self.credentials, self.project_id, self.requests)

	def storage(self):
		"""Initializes and returns a new Firebase Storage instance.

		:return: A newly initialized instance of Storage.
		:rtype: Storage
		"""

		return Storage(self.credentials, self.requests, self.storage_bucket)
