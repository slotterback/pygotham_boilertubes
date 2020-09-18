from marshmallow import post_load
from marshmallow_sqlalchemy import field_for
from app import ma
from models import Boiler, BoilerTube, TubePlugEvent

class TubePlugEventSchema(ma.Schema):
    class Meta:
        fields = ('timestamp','is_plug_event')


class BoilerTubeSchema(ma.Schema):
    id = field_for(BoilerTube, 'id', dump_only=True)

    class Meta:
        fields = ('is_plugged', 'radius','x_coord','y_coord')
        load_instance = True

    @post_load
    def make_boiler_tube(self, data, **kwargs):
        return BoilerTube(**data)

class BoilerTubeWithEventsSchema(ma.Schema):
    class Meta:
        fields = ('is_plugged', 'radius', 'x_coord', 'y_coord', 'events')
        dump_only = ('id')

    events = ma.Nested(TubePlugEventSchema, many=True)


class BoilerSchema(ma.Schema):
    id = field_for(Boiler, 'id', dump_only=True)

    class Meta:
        fields = ('shell_radius','tubes')
        load_instance = True

    tubes = ma.Nested(BoilerTubeSchema, many=True)

    @post_load
    def create_boiler(self, data, **kwargs):
        print(data["tubes"][0].boiler)
        boiler = Boiler(shell_radius=data["shell_radius"])
        for tube in data["tubes"]:
            tube.boiler=boiler            
        return boiler


class BoilerWithEventsSchema(ma.Schema):
    class Meta:
        fields = ('shell_radius', 'tubes')
        dump_only = ('id')

    tubes = ma.Nested(BoilerTubeWithEventsSchema, many=True)
    

boiler_schema = BoilerSchema()
boilers_schema = BoilerSchema(many=True)
boiler_with_events_schema = BoilerWithEventsSchema()
