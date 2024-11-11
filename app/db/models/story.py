from sqlalchemy import JSON, Boolean, Column, DateTime, Integer, String, ForeignKey, Text, func
from app.core.config import Base

class Story(Base):
    __tablename__ = "stories"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    summary = Column(String)
    content = Column(Text, nullable=False)
    
    # Customization fields based on inputs
    language = Column(String, default="en")  # Language: "en" or "de"
    target_audience = Column(String)  # Target audience: "children", "teenagers", "adults", "60+"
    theme = Column(String)  # Theme of the story
    main_characters = Column(JSON)  # JSON with character names and descriptions
    moral = Column(String)  # Moral or message of the story
    setting = Column(String)  # Setting of the story
    story_length = Column(String)  # Story length: "short", "medium", "long"
    genre = Column(String)  # Genre: "Adventure", "Fairy Tale", etc.
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Links to the user who created the story
    is_public = Column(Boolean, default=False) 