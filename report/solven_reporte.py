import time
from openerp.report import report_sxw
from openerp.osv import osv
from openerp import pooler

class solven_reporte(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(solven_reporte, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
        })
   
report_sxw.report_sxw('report.solven.reporte','solvencia.solvencia','solvencia2/report/solven_reporte.rml',parser=solven_reporte, header='internal')
