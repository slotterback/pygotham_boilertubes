from datetime import datetime
from app import db

class Boiler( db.Model ):
    id = db.Column( db.Integer, primary_key = True )
    tubes = db.relationship('BoilerTube', backref = 'boiler', lazy = True )
    shell_radius = db.Column( db.Float )


class BoilerTube( db.Model ):
    id = db.Column( db.Integer, primary_key = True )
    boiler_id = db.Column( db.Integer, db.ForeignKey( 'boiler.id' ) )
    x_coord = db.Column( db.Float )
    y_coord = db.Column( db.Float )
    radius = db.Column( db.Float )
    is_plugged = db.Column( db.Boolean, default = False )
    events = db.relationship( 'TubePlugEvent', backref = 'boiler_tube', 
                              lazy = True )


class TubePlugEvent( db.Model ):
    id = db.Column( db.Integer, primary_key = True )
    timestamp = db.Column( db.DateTime, index = True, 
                           default = datetime.utcnow() )
    tube_id = db.Column( db.Integer, db.ForeignKey( 'boiler_tube.id' ) )
    is_plug_event = db.Column( db.Boolean )


