from json_utils.http import JSONResponse

def response_json(request, content):
	if "application/json" in request.META['HTTP_ACCEPT_ENCODING']:
		mimetype = 'application/json'
	else:
		mimetype = 'text/plain'
	return JSONResponse(content, mimetype=mimetype)