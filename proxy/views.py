from django.http import HttpResponse
from django.http import Http404
from designateclient.v1 import Client
from designateclient.v1.domains import Domain
from designateclient.v1.servers import Server
from designateclient.v1.records import Record
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict

def change_response (in_data):
  out_data = json.dumps({"data": in_data, "success": True})
  return out_data

@csrf_exempt
def server(request, server_id=''):
  client = Client(
    auth_url="http://keystone:5000/v2.0/",
    username="designate",
    password="designate",
    tenant_name="service",
    endpoint="http://designate:9001/v1"
  )
  if request.method == "GET":
    if server_id:
      try:
        return HttpResponse(change_response(client.servers.get(server_id)))
      except:
        return HttpResponse("Not found", status=404)
    else:
      return HttpResponse(change_response(client.servers.list()))
  elif request.method == "POST":
    server = Server(name=request.POST['name'])
    return HttpResponse(change_response(client.servers.create(server)))
  elif request.method == "PUT":
    params = QueryDict(request.body, encoding=request._encoding)
    server = client.servers.get(server_id)
    server.name = params['name'] 
    return HttpResponse(change_response(client.servers.update(server)))
  elif request.method == "DELETE":
    client.servers.delete(server_id)
    return HttpResponse("OK", status=200)

@csrf_exempt
def domain(request, domain_id=''):
  client = Client(
    auth_url="http://keystone:5000/v2.0/",
    username="designate",
    password="designate",
    tenant_name="service",
    endpoint="http://designate:9001/v1"
  )
  if request.method == "GET":
    if domain_id:
      try:
        return HttpResponse(change_response(client.domains.get(domain_id)))
      except:
        return HttpResponse("Not found", status=404)
    else:
      return HttpResponse(change_response(client.domains.list()))
  elif request.method == "POST":
    if 'ttl' not in request.POST:
      defined_ttl = 3600
    else:
      defined_ttl = int(request.POST['ttl'])
    if 'description' not in request.POST:
      defined_description = None
    else:
      defined_description = request.POST['description']
    domain = Domain(name=request.POST['name'], email=request.POST['email'], ttl=defined_ttl, description=defined_description)
    return HttpResponse(change_response(client.domains.create(domain)))
  elif request.method == "PUT":
    params = QueryDict(request.body, encoding=request._encoding)
    domain = client.domains.get(domain_id)
    if 'name' in params:
      domain.name = params['name']
    if 'email' in params:
      domain.email = params['email']
    if 'ttl' in params:
      domain.ttl = int(params['ttl'])
    if 'description' in params:
      domain.description = params['description']
    return HttpResponse(change_response(client.domains.update(domain)))
  elif request.method == "DELETE":
    client.domains.delete(domain_id)
    return HttpResponse("OK", status=200)

@csrf_exempt
def record(request, domain_id='', record_id=''):
  client = Client(
    auth_url="http://keystone:5000/v2.0/",
    username="designate",
    password="designate",
    tenant_name="service",
    endpoint="http://designate:9001/v1"
  )
  if request.method == "GET":
    print(domain_id)
    print(record_id)
    if record_id:
      try:
        return HttpResponse(change_response(client.records.get(domain_id, record_id)))
      except:
        return HttpResponse("Not found", status=404)
    else:
      return HttpResponse(change_response(client.records.list(domain_id)))
  elif request.method == "POST":
    if 'priority' not in request.POST:
      defined_priority = None
    else:
      defined_priority = int(request.POST['priority'])
    if 'ttl' not in request.POST:
      defined_ttl = 3600
    else:
      defined_ttl = int(request.POST['ttl'])
    if 'description' not in request.POST:
      defined_description = None
    else:
      defined_description = request.POST['description']
    record = Record(name=request.POST['name'], type=request.POST['type'], data=request.POST['data'], priority=defined_priority, ttl=defined_ttl, description=defined_description)
    return HttpResponse(change_response(client.records.create(domain_id, record)))
  elif request.method == "PUT":
    params = QueryDict(request.body, encoding=request._encoding)
    record = client.records.get(domain_id, record_id)    
    if 'name' in params:
      record.name = params['name']
    if 'type' in params:
      record.type = params['type']
    if 'data' in params:
      record.data = params['data']
    if 'priority' in params:
      record.priority = int(params['priority'])
    if 'ttl' in params:
      record.ttl = int(params['ttl'])
    if 'description' in params:
      domain.description = params['description']
    return HttpResponse(change_response(client.records.update(domain_id, record)))
  elif request.method == "DELETE":
    client.records.delete(domain_id, record_id)
    return HttpResponse("OK", status=200)

