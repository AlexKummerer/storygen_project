from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.config import Base

class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    plan_type = Column(String, nullable=False)  # e.g., Free, Premium, Pro
