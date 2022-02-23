from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Imovel, Acionamento, Status, Sensor, Notificacao
from .serializers import ImovelSerializer, AcionamentoSerializer, StatusSerializer, SensorSerializer, NotificacaoSerializer
import requests

@api_view(['GET'])
def getImovel(request):
    imoveis = Imovel.objects.all()
    serializer_imoveis = ImovelSerializer(imoveis, many=True)
    return Response(serializer_imoveis.data)

@api_view(['POST'])
def addImovel(request):
    serializer_imovel = ImovelSerializer(data=request.data)
    if serializer_imovel.is_valid():
        serializer_imovel.save()
    return Response(serializer_imovel.data)

@api_view(['GET'])
def getAcionamento(request):
    acionamento = Acionamento.objects.all()
    serializer_acionamento = AcionamentoSerializer(acionamento, many=True)
    return Response(serializer_acionamento.data)

@api_view(['POST'])
def addAcionamento(request):
    serializer_acionamento = AcionamentoSerializer(data=request.data)
    if serializer_acionamento.is_valid():
        serializer_acionamento.save()
    return Response(serializer_acionamento.data)

@api_view(['GET'])
def getStatus(request):
    status = Status.objects.all()
    serializer_status = StatusSerializer(status, many=True)
    return Response(serializer_status.data)

@api_view(['POST'])
def addStatus(request):

    request_getAcionamento = requests.get('http://127.0.0.1:8000/getAcionamento?format=json')
    json_req_acioamento = request_getAcionamento.json()
    alarm_on = json_req_acioamento[-1]["switch_bool"]
    if alarm_on:
        request_data = request.data
        request_data["status_bool"] = True
        serializer_status = StatusSerializer(data=request_data)
        if serializer_status.is_valid():
            serializer_status.save()
        print("Alarme online. Mensagem automatica a cada 30 segundos.")
        return Response(serializer_status.data)
    else:
        print("Alarme automático desativado!")
        return Response({"Alarme automático desativado!": "Nada enviado"})

@api_view(['GET'])
def getSensor(request):
    sensor = Sensor.objects.all()
    serializer_sensor = SensorSerializer(sensor, many=True)
    return Response(serializer_sensor.data)

@api_view(['POST'])
def addSensor(request):
    serializer_sensor = SensorSerializer(data=request.data)
    if serializer_sensor.is_valid():
        serializer_sensor.save()

    payload = \
        {
            "imovel_id": f"{serializer_sensor.data['imovel_id']}"
        }
    request_addNotificacao = requests.post('http://127.0.0.1:8000/addNotificacao', payload)
    print(f'Sensor {serializer_sensor.data["imovel_sensor"]}')
    return Response(serializer_sensor.data)

@api_view(['GET'])
def getNotificacao(request):
    notificacao = Notificacao.objects.all()
    serializer_notificacao = NotificacaoSerializer(notificacao, many=True)
    return Response(serializer_notificacao.data)

@api_view(['POST'])
def addNotificacao(request):
    request_data = request.data
    request_getImovel = requests.get('http://127.0.0.1:8000/?format=json')
    found = False
    for imovel in request_getImovel.json():
        if int(imovel['id']) == int(request_data['imovel_id']):
            serializer_notificacao = NotificacaoSerializer(data=request_data)
            if serializer_notificacao.is_valid():
                serializer_notificacao.save()
            print("!!! ATENÇÃO !!! ACESSO SUSPEITO !!! ATENCÃO !!! SUSPEITO !!!")
            print(f"Acesso suspeito no imóvel do {imovel['nome_dono']}. Contato: {imovel['contato_dono']}. Endereço: {imovel['endereco']}")
            return Response(serializer_notificacao.data)
    if not found:
        print("addNotificacao INVÁLIDO: O id do imovel informado ao criar um alerta de sensor não foi encontrado pelo addNotificacao")
        return Response({"addNotificacao INVÁLIDO": "O id do imovel informado ao criar um alerta de sensor não foi encontrado pelo addNotificacao"})

