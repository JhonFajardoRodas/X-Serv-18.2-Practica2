from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from models import urlDB 

# Create your views here.

lista = urlDB.objects.all()
if len(lista) == 0:
	num = 0
else: 
	num = len(lista)
count = num

@csrf_exempt


def mostrar(solicitud):
	if solicitud.method == 'GET':
		tabla  = urlDB.objects.all()
		salida = ""
		formHtml = "<html><body><h1> <u>ACORTADOR DE URLs</u>" 
		formHtml += '<form action="" method="POST">'
		formHtml += '<h4>Introduce URL : <input type= "text" name="valor"</h4>'
		formHtml += '<input type="submit">'
		formHtml += '</form>' 
		formHtml +=  "</h1></body></html>"

		for linea in tabla:
			salida+= "<p><h3><li>" + linea.url + " =====> " + "<b>Url acortada: [" + str(linea.urlCut)  + "]</b></li></h3></p>"
		return HttpResponse(formHtml + salida)

	elif solicitud.method == 'POST':
		global count
		urlNew = solicitud.body
		urlNew = urlNew.split("valor=")[1]
		if len(urlNew.split("http"))!= 1:
			urlNew = urlNew.replace("%3A%2F%2F", "://")
		else:
			urlNew = "http://" +  urlNew

		try:
			exist = urlDB.objects.get(url=urlNew)
			form = ("<h1><a href='" + exist.url + "'> " + str(exist.url) + "</a><h1>"
        			+ "<h1><a href='" + str(exist.urlCut) + "'> " + str(exist.urlCut) + "</a><h1>" #Esto se abre cuando implemente el otro metodo
        	        + "<a href='" + "http://localhost:1234/" + "'>VOLVER</a>")
			return HttpResponse(form)
		except urlDB.DoesNotExist:
			
			entryNew = urlDB(url=urlNew, urlCut=count)
			urlStr = "http://localhost:1234/" + str(count)
	        entryNew.save()
	        count = count + 1

	        return HttpResponseNotFound("<h1><a href='" + urlNew + "'> " + str(urlNew) + "</a><h1>"
        					            + "<h1><a href='" + urlStr + "'> " + str(urlStr) + "</a><h1>" #Esto se abre cuando implemente el otro metodo
        	                            + "<a href='" + "http://localhost:1234/" + "'>VOLVER</a>")
        


def acortar(solicitud, recurso):
	if solicitud.method == 'GET':
		try:
			shortedURL = urlDB.objects.get(urlCut=recurso)
			url = shortedURL.url
			return HttpResponse(("<html><h1>"
								+"<head>"
                                +"<meta http-equiv=Refresh content= 2;url="+url+">"
							    +"<head>"
							    +"</body></html>"))
		except urlDB.DoesNotExist:
			return HttpResponseNotFound("<p><h1>No se encuentra el recurso solicitado !!</h1></p>" 
				                        + "<p><h1><a href='" + "http://localhost:1234/" + "'>VOLVER</a></h1></p>")

