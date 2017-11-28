from protobuf3.message import Message
from protobuf3.fields import MessageField, Int32Field, StringField


class BaseReply(Message):

    class SpareParameterEntry(Message):
        pass

BaseReply.SpareParameterEntry.add_field('key', StringField(field_number=1, optional=True))
BaseReply.SpareParameterEntry.add_field('value', StringField(field_number=2, optional=True))
BaseReply.add_field('Code', Int32Field(field_number=1, optional=True))
BaseReply.add_field('Message', StringField(field_number=2, optional=True))
BaseReply.add_field('spareParameter', MessageField(field_number=3, repeated=True, message_cls=BaseReply.SpareParameterEntry))
