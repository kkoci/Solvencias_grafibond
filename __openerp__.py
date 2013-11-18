{
    "name" : "Solvencia Grafibond",
    "version" : "6.0.1",
    "author" : "Koci",
	"website" : "http://www.tuespacioweb.com.ve",
    "category" : "General",
    "depends" : ["base","compra_grafibond"],
    'data': [
        'security/purchase_tender.xml',
        'security/ir.model.access.csv',
        'solven_reporte.xml',
    ],
	"description" : "Modulo para llevar las solvencias de la Empresa con respecto a el Seguro Social",
    "init_xml" : [],
	"demo xml" : [],
    "update_xml" : [ "solvencia_view.xml"],
    "installable": True,
    "active": False,
	"certificate" : ""
}