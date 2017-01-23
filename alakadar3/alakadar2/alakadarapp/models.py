# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Bahan(models.Model):
    id_bahan = models.CharField(db_column='ID_BAHAN', primary_key=True, max_length=10)  # Field name made lowercase.
    harga_bahan = models.IntegerField(db_column='HARGA_BAHAN')  # Field name made lowercase.
    jumlah_bahan = models.IntegerField(db_column='JUMLAH_BAHAN')  # Field name made lowercase.
    nama_bahan = models.CharField(db_column='NAMA_BAHAN', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bahan'


class HistoryPemesanan(models.Model):
    tanggal_pemesanan = models.DateTimeField(db_column='TANGGAL_PEMESANAN', primary_key=True)  # Field name made lowercase.
    id_pesanan = models.ForeignKey('Pemesanan', models.DO_NOTHING, db_column='ID_PESANAN')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'history_pemesanan'


class Komposisi(models.Model):
    id_bahan = models.ForeignKey(Bahan, models.DO_NOTHING, db_column='ID_BAHAN', primary_key=True)  # Field name made lowercase.
    id_makanan = models.ForeignKey('SiapSaji', models.DO_NOTHING, db_column='ID_MAKANAN')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'komposisi'


class Makanan(models.Model):
	id_makanan = models.CharField(db_column='ID_MAKANAN', primary_key=True, max_length=10)  # Field name made lowercase.
	nama_makanan = models.CharField(db_column='NAMA_MAKANAN', max_length=15)  # Field name made lowercase.
	rating = models.IntegerField(db_column='RATING')  # Field name made lowercase.
	energi = models.CharField(db_column='ENERGI', max_length=10)  # Field name made lowercase.
	protein = models.CharField(db_column='PROTEIN', max_length=10)  # Field name made lowercase.
	deskripsi = models.CharField(db_column='DESKRIPSI', max_length=100)  # Field name made lowercase.
	stok_makanan = models.IntegerField(db_column='STOK_MAKANAN')  # Field name made lowercase.
	lemak = models.CharField(db_column='LEMAK', max_length=10)  # Field name made lowercase.
	gambar = models.ImageField(upload_to="image/produk")
	
	class Meta:
		managed = False
		db_table = 'makanan'
		
class MakananSiapCatering(Makanan):
    makanan = models.OneToOneField(Makanan, models.DO_NOTHING, db_column='ID_MAKANAN', parent_link=True)  # Field name made lowercase.
	# makanan = models.OneToOneField(Makanan, models.DO_NOTHING, db_column='ID_MAKANAN', primary_key=True)  # Field name made lowercase.
    # nama_makanan = models.CharField(db_column='NAMA_MAKANAN', max_length=15)  # Field name made lowercase.
    # rating = models.IntegerField(db_column='RATING')  # Field name made lowercase.
    # energi = models.CharField(db_column='ENERGI', max_length=10)  # Field name made lowercase.
    # protein = models.CharField(db_column='PROTEIN', max_length=10)  # Field name made lowercase.
    # deskripsi = models.CharField(db_column='DESKRIPSI', max_length=100)  # Field name made lowercase.
    # stok_makanan = models.IntegerField(db_column='STOK_MAKANAN')  # Field name made lowercase.
    # lemak = models.CharField(db_column='LEMAK', max_length=10)  # Field name made lowercase.
    poin = models.IntegerField(db_column='POIN')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'makanan_siap_catering'


class MakananSiapMakan(Makanan):
    makanan = models.OneToOneField(Makanan, models.DO_NOTHING, db_column='ID_MAKANAN', parent_link=True)# id_makanan = models.ForeignKey(Makanan, models.DO_NOTHING, db_column='ID_MAKANAN', primary_key=True)  # Field name made lowercase.
    # nama_makanan = models.CharField(db_column='NAMA_MAKANAN', max_length=15)  # Field name made lowercase.
    # rating = models.IntegerField(db_column='RATING')  # Field name made lowercase.
    # energi = models.CharField(db_column='ENERGI', max_length=10)  # Field name made lowercase.
    # protein = models.CharField(db_column='PROTEIN', max_length=10)  # Field name made lowercase.
    # deskripsi = models.CharField(db_column='DESKRIPSI', max_length=100)  # Field name made lowercase.
    # stok_makanan = models.IntegerField(db_column='STOK_MAKANAN')  # Field name made lowercase.
    # lemak = models.CharField(db_column='LEMAK', max_length=10)  # Field name made lowercase.
    harga = models.IntegerField(db_column='HARGA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'makanan_siap_makan'


		
class Bento(MakananSiapMakan):
    msm = models.OneToOneField(MakananSiapMakan, models.DO_NOTHING, db_column='ID_MAKANAN', parent_link=True)
	# id_makanan = models.ForeignKey(Makanan, 
    # id_makanan = models.ForeignKey('MakananSiapMakan', models.DO_NOTHING, db_column='ID_MAKANAN', primary_key=True, unique=True)  # Field name made lowercase.
    # nama_makanan = models.CharField(db_column='NAMA_MAKANAN', max_length=15)  # Field name made lowercase.
    # rating = models.IntegerField(db_column='RATING')  # Field name made lowercase.
    # energi = models.CharField(db_column='ENERGI', max_length=10)  # Field name made lowercase.
    # protein = models.CharField(db_column='PROTEIN', max_length=10)  # Field name made lowercase.
    # deskripsi = models.CharField(db_column='DESKRIPSI', max_length=100)  # Field name made lowercase.
    # stok_makanan = models.IntegerField(db_column='STOK_MAKANAN')  # Field name made lowercase.
    # lemak = models.CharField(db_column='LEMAK', max_length=10)  # Field name made lowercase.
    # harga = models.IntegerField(db_column='HARGA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bento'

		
class Pelanggan(models.Model):
    id_pelanggan = models.CharField(db_column='ID_PELANGGAN', primary_key=True, max_length=10)  # Field name made lowercase.
    nama = models.CharField(db_column='NAMA', max_length=25)  # Field name made lowercase.
    alamat = models.CharField(db_column='ALAMAT', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=30)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=25)  # Field name made lowercase.
    no_hp = models.IntegerField(db_column='NO_HP', blank=True, null=True)  # Field name made lowercase.
    total_poin = models.IntegerField(db_column='TOTAL_POIN')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pelanggan'


class Pembayaran(models.Model):
    id_pembayaran = models.CharField(db_column='ID_PEMBAYARAN', primary_key=True, max_length=10)  # Field name made lowercase.
    id_pelanggan = models.ForeignKey(Pelanggan, models.DO_NOTHING, db_column='ID_PELANGGAN')  # Field name made lowercase.
    id_pesanan = models.ForeignKey('Pemesanan', models.DO_NOTHING, db_column='ID_PESANAN')  # Field name made lowercase.
    status_pembayaran = models.IntegerField(db_column='STATUS_PEMBAYARAN')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pembayaran'


class PembelianPoin(models.Model):
    jumlah_pembelian_poin = models.IntegerField(db_column='JUMLAH_PEMBELIAN_POIN')  # Field name made lowercase.
    tanggal_pembelian = models.DateTimeField(db_column='TANGGAL_PEMBELIAN', primary_key=True)  # Field name made lowercase.
    id_poin = models.ForeignKey('Poin', models.DO_NOTHING, db_column='ID_POIN')  # Field name made lowercase.
    id_pelanggan = models.ForeignKey(Pelanggan, models.DO_NOTHING, db_column='ID_PELANGGAN')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pembelian_poin'


class Pemesanan(models.Model):
    id_pesanan = models.CharField(db_column='ID_PESANAN', primary_key=True, max_length=10)  # Field name made lowercase.
    id_pelanggan = models.ForeignKey(Pelanggan, models.DO_NOTHING, db_column='ID_PELANGGAN')  # Field name made lowercase.
    id_makanan = models.ForeignKey(Makanan, models.DO_NOTHING, db_column='ID_MAKANAN')  # Field name made lowercase.
    jumlah_pesanan = models.IntegerField(db_column='JUMLAH_PESANAN')  # Field name made lowercase.
    tanggal_pengiriman = models.DateTimeField(db_column='TANGGAL_PENGIRIMAN')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pemesanan'


class Poin(models.Model):
    id_poin = models.CharField(db_column='ID_POIN', primary_key=True, max_length=10)  # Field name made lowercase.
    harga_poin = models.IntegerField(db_column='HARGA_POIN')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'poin'


class SiapCatering(models.Model):
    pesanan = models.OneToOneField(Pemesanan, models.DO_NOTHING, db_column='ID_PESANAN', parent_link=True)# id_makanan = models.ForeignKey(Makanan, 
    # id_pesanan = models.ForeignKey(Pemesanan, models.DO_NOTHING, db_column='ID_PESANAN', primary_key=True)  # Field name made lowercase.
    # id_pelanggan = models.CharField(db_column='ID_PELANGGAN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    # id_makanan = models.CharField(db_column='ID_MAKANAN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    # jumlah_pesanan = models.IntegerField(db_column='JUMLAH_PESANAN')  # Field name made lowercase.
    # tanggal_pengiriman = models.DateTimeField(db_column='TANGGAL_PENGIRIMAN')  # Field name made lowercase.
    total_poin = models.IntegerField(db_column='TOTAL_POIN')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'siap_catering'


class SiapMakan(models.Model):
    pesanan = models.OneToOneField(Pemesanan, models.DO_NOTHING, db_column='ID_PESANAN', parent_link=True)# id_makanan = models.ForeignKey(Makanan, 
    # id_pesanan = models.ForeignKey(Pemesanan, models.DO_NOTHING, db_column='ID_PESANAN', primary_key=True)  # Field name made lowercase.
    # id_pelanggan = models.CharField(db_column='ID_PELANGGAN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    # id_makanan = models.CharField(db_column='ID_MAKANAN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    # jumlah_pesanan = models.IntegerField(db_column='JUMLAH_PESANAN')  # Field name made lowercase.
    # tanggal_pengiriman = models.DateTimeField(db_column='TANGGAL_PENGIRIMAN')  # Field name made lowercase.
    total_harga = models.IntegerField(db_column='TOTAL_HARGA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'siap_makan'


class SiapMasak(models.Model):
    pesanan = models.OneToOneField(Pemesanan, models.DO_NOTHING, db_column='ID_PESANAN', parent_link=True)# id_makanan = models.ForeignKey(Makanan, 
    # id_pesanan = models.ForeignKey(Pemesanan, models.DO_NOTHING, db_column='ID_PESANAN', primary_key=True)  # Field name made lowercase.
    # id_pelanggan = models.CharField(db_column='ID_PELANGGAN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    # id_makanan = models.CharField(db_column='ID_MAKANAN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    # jumlah_pesanan = models.IntegerField(db_column='JUMLAH_PESANAN')  # Field name made lowercase.
    # tanggal_pengiriman = models.DateTimeField(db_column='TANGGAL_PENGIRIMAN')  # Field name made lowercase.
    total_harga = models.IntegerField(db_column='TOTAL_HARGA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'siap_masak'


class SiapSaji(MakananSiapMakan):
    msm = models.OneToOneField(MakananSiapMakan, models.DO_NOTHING, db_column='ID_MAKANAN', parent_link=True)# id_makanan = models.ForeignKey(Makanan, 
    # id_makanan = models.ForeignKey(MakananSiapMakan, models.DO_NOTHING, db_column='ID_MAKANAN', primary_key=True)  # Field name made lowercase.
    # nama_makanan = models.CharField(db_column='NAMA_MAKANAN', max_length=15)  # Field name made lowercase.
    # rating = models.IntegerField(db_column='RATING')  # Field name made lowercase.
    # energi = models.CharField(db_column='ENERGI', max_length=10)  # Field name made lowercase.
    # protein = models.CharField(db_column='PROTEIN', max_length=10)  # Field name made lowercase.
    # deskripsi = models.CharField(db_column='DESKRIPSI', max_length=100)  # Field name made lowercase.
    # stok_makanan = models.IntegerField(db_column='STOK_MAKANAN')  # Field name made lowercase.
    # lemak = models.CharField(db_column='LEMAK', max_length=10)  # Field name made lowercase.
    # harga = models.IntegerField(db_column='HARGA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'siap_saji'


class Tracking(models.Model):
    id_tracking = models.CharField(db_column='ID_TRACKING', primary_key=True, max_length=10)  # Field name made lowercase.
    id_pembayaran = models.ForeignKey(Pembayaran, models.DO_NOTHING, db_column='ID_PEMBAYARAN')  # Field name made lowercase.
    status_tracking = models.IntegerField(db_column='STATUS_TRACKING')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tracking'
