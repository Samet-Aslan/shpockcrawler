class Listing:
	
	def __init__(self, title, price, imagesrc, description):
		self.title = title
		self.price = price
		self.imagesrc = imagesrc
		self.description = description

	def getTitle(self):
		return self.title

	def getPrice(self):
		return self.price

	def getImgsrc(self):
		return self.imagesrc

	def getDescription(self):
		return self.description

	def setTitle(self, title):
		self.title = title

	def setPrice(self, price):
		self.price = price

	def setImagesrc(self, imagesrc):
		self.imagesrc = imagesrc

	def setDescription(self, description):
		self.desription = description


