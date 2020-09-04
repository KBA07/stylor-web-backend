from sqlalchemy import Column, UniqueConstraint, Index

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.sqlite import CHAR, INTEGER

Base = declarative_base()


class Inventory(Base):
    __tablename__ = 'inventory'
    productId = Column(CHAR(50), primary_key=True)
    groupProductId = Column(CHAR(50))
    color = Column(CHAR(20))
    category = Column(CHAR(50))
    sizeType = Column(CHAR(50))
    sizeInventory = Column(CHAR(100))
    price = Column(INTEGER)
    images = Column(CHAR(2048))
    merchantId = Column(CHAR(50))

    __table_args__ = (
        UniqueConstraint('productId'),
        Index('productId_index', 'productId'),
        Index('category_index', 'category')
    )

    def __init__(self, productId, groupProductId, color, category, sizeType, sizeInventory,
                 price, images, merchantId):
        self.productId = productId
        self.groupProductId = groupProductId
        self.color = color
        self.category = category
        self.sizeType = sizeType
        self.sizeInventory = sizeInventory
        self.price = price
        self.images = images
        self.merchantId = merchantId

    def __repr__(self):
        return "productId={} groupProductId={} color={} category={} sizeType={}" \
               "sizeInventory={} price={} images={} merchantId={}".format(
            self.productId, self.groupProductId, self.color, self.category, self.sizeType,
            self.sizeInventory, self.price, self.images, self.merchantId)
