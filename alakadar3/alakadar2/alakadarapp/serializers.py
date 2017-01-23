from django.contrib.auth.models import User, Group
from rest_framework import serializers
from alakadar2.alakadarapp.models import *


"""Makanan"""
class MakananSerializer(serializers.ModelSerializer):
	class Meta:
		model = Makanan
		fields = '__all__'

class MakananSiapMakanSerializer(serializers.ModelSerializer):
	class Meta:
		model = MakananSiapMakan
		fields = '__all__'

class MakananSiapCateringSerializer(serializers.ModelSerializer):
	class Meta:
		model = MakananSiapCatering
		fields = '__all__'

class BentoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bento
		fields = '__all__'

class KomposisiSerializer(serializers.ModelSerializer):
	class Meta:
		model = Komposisi
		fields = '__all__'

class SiapSajiSerializer(serializers.ModelSerializer):
	class Meta:
		model = SiapSaji
		fields = '__all__'

class BahanSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bahan
		fields = '__all__'

"""Pemesanan"""
class PemesananSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pemesanan
		fields = '__all__'
		depth = 2;

class SiapMakanSerializer(serializers.ModelSerializer):
	class Meta:
		model = SiapMakan
		fields = '__all__'

class SiapMasakSerializer(serializers.ModelSerializer):
	class Meta:
		model = SiapMasak
		fields = '__all__'

class SiapCateringSerializer(serializers.ModelSerializer):
	class Meta:
		model = SiapCatering
		fields = '__all__'
"""
class HistoryPemesananSerializer(serializers.ModelSerializer):
	class Meta:
		model = HistoryPemesanan
		fields = '__all__'
"""
"""Pelanggan"""
class PelangganSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pelanggan
		fields = '__all__'

class PembayaranSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pembayaran
		fields = '__all__'


class TrackingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tracking
		fields = '__all__'

"""Poin"""
class PembelianPoinSerializer(serializers.ModelSerializer):
	class Meta:
		model = PembelianPoin
		fields = '__all__'

class PoinSerializer(serializers.ModelSerializer):
	class Meta:
		model = Poin
		fields = '__all__'
