# -*- coding: utf-8 -*-
import time
from datetime import datetime
from osv import osv, fields

class solvencia_solvencia(osv.osv):

    _name = 'solvencia.solvencia'
    _description = "Modulo para llevar las solvencias"
    
	
    _columns = {
        'Fecha_de_Emision': fields.date('Fecha de Emision', required=True, select=True),
        'Fecha_de_Vence': fields.date('Fecha de Vencimiento', required=True, select=True),
        'user_id': fields.many2one('res.users', 'Responsible'),
        'company_id': fields.many2one('res.company', 'Compañia', required=True, select=1, help="Compañia relacionada con ésta solvencia"),
        'ins_em' : fields.char('Institucion emisora', size=30),
        'nsol' : fields.char('Numero de solvencia'),
        'cadidate' : fields.date('Fecha de entrega CADIVI', required=True, select=True),
        'observa' : fields.text('Observaciones'),
    }

    _defaults = {
    'user_id': lambda self, cr, uid, c: self.pool.get('res.users').browse(cr, uid, uid, c).id ,
    }
solvencia_solvencia()