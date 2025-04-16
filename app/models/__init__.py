# app/models/__init__.py
from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class UserBase(SQLModel):
    user_id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    password: str
    email: str = Field(index=True, unique=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

class User(UserBase, table=True):
    conversations: list["Conversation"] = Relationship(back_populates="user")
    feedbacks: list["Feedback"] = Relationship(back_populates="user")

class ConversationBase(SQLModel):
    started_at: datetime = Field(default_factory=datetime.utcnow)
    ended_at: Optional[datetime] = None

class Conversation(ConversationBase, table=True):
    conversation_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.user_id")
    
    user: User = Relationship(back_populates="conversations")
    messages: list["Message"] = Relationship(back_populates="conversation")

class MessageBase(SQLModel):
    content: str
    sent_at: datetime = Field(default_factory=datetime.utcnow)

class Message(MessageBase, table=True):
    message_id: Optional[int] = Field(default=None, primary_key=True)
    conversation_id: int = Field(foreign_key="conversation.conversation_id")
    
    conversation: Conversation = Relationship(back_populates="messages")
    bol_response: Optional["BolResponse"] = Relationship(back_populates="message")

class BolResponseBase(SQLModel):
    response_content: str
    generated_at: datetime = Field(default_factory=datetime.utcnow)

class BolResponse(BolResponseBase, table=True):
    response_id: Optional[int] = Field(default=None, primary_key=True)
    message_id: int = Field(foreign_key="message.message_id")
    
    message: Message = Relationship(back_populates="bol_response")
    feedback: Optional["Feedback"] = Relationship(back_populates="bol_response")

class FeedbackBase(SQLModel):
    rating: int = Field(ge=0, le=1)  # 0 or 1

class Feedback(FeedbackBase, table=True):
    feedback_id: Optional[int] = Field(default=None, primary_key=True)
    response_id: int = Field(foreign_key="bolresponse.response_id")
    user_id: int = Field(foreign_key="user.user_id")
    
    bol_response: BolResponse = Relationship(back_populates="feedback")
    user: User = Relationship(back_populates="feedbacks")

# Response models (without table=True)
class UserRead(UserBase):
    user_id: int

class ConversationRead(ConversationBase):
    conversation_id: int
    user_id: int

class MessageRead(MessageBase):
    message_id: int
    conversation_id: int

class BolResponseRead(BolResponseBase):
    response_id: int
    message_id: int

class FeedbackRead(FeedbackBase):
    feedback_id: int
    response_id: int
    user_id: int
