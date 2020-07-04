class Listing:
	
	title
	price
	imagesrc
	description

	def __init__(self, title, price, imagesrc):
		self.title = title
		self.price = price
		self.imagesrc = imagesrc
		self.description 

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


