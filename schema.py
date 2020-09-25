from app import ma
from models import Boiler, BoilerTube, TubePlugEvent

class TubePlugEventSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TubePlugEvent
        include_fk = True
        load_instance = True

    id = ma.auto_field(dump_only=True)


class BoilerTubeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BoilerTube
        include_fk = True
        load_instance = True

    id = ma.auto_field(dump_only=True)


class BoilerTubeWithEventsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BoilerTube
        include_fk = True
        load_instance = True
    
    id = ma.auto_field(dump_only=True)
    events = ma.Nested(TubePlugEventSchema, many=True)


class BoilerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Boiler
        load_instance = True
        
    id = ma.auto_field(dump_only=True)
    tubes = ma.Nested(BoilerTubeSchema,many=True)


class BoilerWithEventsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Boiler
        load_instance = True

    id = ma.auto_field(dump_only=True)
    tubes = ma.Nested(BoilerTubeWithEventsSchema, many=True)
    

boiler_schema = BoilerSchema()
boilers_schema = BoilerSchema(many=True)
boiler_with_events_schema = BoilerWithEventsSchema()
