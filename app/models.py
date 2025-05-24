from .database import Base
from sqlalchemy.orm import Mapped, mapped_column, Relationship
from datetime import datetime
from sqlalchemy import TIMESTAMP, text, ForeignKey


class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key = True, nullable = False) 
    title: Mapped[str] = mapped_column(nullable = False)
    content: Mapped[str] = mapped_column(nullable = False)
    published: Mapped[bool] = mapped_column(server_default='TRUE') 
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False, server_default=text('now()'))
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    owner = Relationship("User")
    
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key = True, nullable = False) 
    email: Mapped[str] = mapped_column(nullable = False, unique=True)
    password: Mapped[str] = mapped_column(nullable = False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False, server_default=text('now()'))
    
    phone_number : Mapped[str] = mapped_column(nullable = True)

    
class Vote(Base):
    __tablename__ = "votes"
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), primary_key = True, nullable = False) 
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id", ondelete="CASCADE"), primary_key = True, nullable = False) 