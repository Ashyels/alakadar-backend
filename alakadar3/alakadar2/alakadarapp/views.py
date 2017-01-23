from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from alakadar2.alakadarapp.serializers import *
from alakadar2.alakadarapp.models import *

""" Makanan """
class MakananViewSet(viewsets.ModelViewSet):
	queryset = Makanan.objects.all()
	serializer_class = MakananSerializer

class MakananSiapMakanViewSet(viewsets.ModelViewSet):
	queryset = MakananSiapMakan.objects.all()
	serializer_class = MakananSiapMakanSerializer

class MakananSiapCateringViewSet(viewsets.ModelViewSet):
	queryset = MakananSiapCatering.objects.all()
	serializer_class = MakananSiapCateringSerializer

class BentoViewSet(viewsets.ModelViewSet):
	queryset = Bento.objects.all()
	serializer_class = BentoSerializer

class SiapSajiViewSet(viewsets.ModelViewSet):
	queryset = SiapSaji.objects.all()
	serializer_class = SiapSajiSerializer

class BahanViewSet(viewsets.ModelViewSet):
	queryset = Bahan.objects.all()
	serializer_class = BahanSerializer

class KomposisiViewSet(viewsets.ModelViewSet):
	queryset = Komposisi.objects.all()
	serializer_class = KomposisiSerializer

"""Pemesanan"""
class PemesananViewSet(viewsets.ModelViewSet):
	queryset = Pemesanan.objects.all()
	serializer_class = PemesananSerializer
"""
class HistoryPemesananViewSet(viewsets.ModelViewSet):
	queryset = HistoryPemesanan.objects.all()
	serializer_class = HistoryPemesananSerializer
"""
class SiapMakanViewSet(viewsets.ModelViewSet):
	queryset = SiapMakan.objects.all()
	serializer_class = SiapMakanSerializer

class SiapMasakViewSet(viewsets.ModelViewSet):
	queryset = SiapMasak.objects.all()
	serializer_class = SiapMasakSerializer

class SiapCateringViewSet(viewsets.ModelViewSet):
	queryset = SiapCatering.objects.all()
	serializer_class = SiapCateringSerializer

"""Pelanggan"""
class PelangganViewSet(viewsets.ModelViewSet):
	queryset = Pelanggan.objects.all()
	serializer_class = PelangganSerializer

"""Pembayaran"""
class PembayaranViewSet(viewsets.ModelViewSet):
	queryset = Pembayaran.objects.all()
	serializer_class = PembayaranSerializer

"""Tracking"""
class TrackingViewSet(viewsets.ModelViewSet):
	queryset = Tracking.objects.all()
	serializer_class = TrackingSerializer

"""Poin"""
class PembelianPoinViewSet(viewsets.ModelViewSet):
	queryset = PembelianPoin.objects.all()
	serializer_class = PembelianPoinSerializer

class PoinViewSet(viewsets.ModelViewSet):
	queryset = Poin.objects.all()
	serializer_class = PoinSerializer




"""
def update(request, id):
   emp = Makanan.objects.get(pk = id)
   emp.name = request.POST.get('name')
   emp.save()
   return HttpResponse('updated')
"""

"""
def delete(request, id):
   obj = Makanan.objects.get(pk = id)
   obj.delete()
   return HttpResponse('deleted')
"""
