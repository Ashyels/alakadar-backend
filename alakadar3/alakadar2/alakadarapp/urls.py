from django.conf.urls import url, include
from rest_framework import routers
from alakadar2.alakadarapp import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
"""Makanan"""
router.register(r'^makanan', views.MakananViewSet)
router.register(r'^bento', views.BentoViewSet)
router.register(r'^makanan-siap-makan', views.MakananSiapMakanViewSet)
router.register(r'^makanan-siap-catering', views.MakananSiapCateringViewSet)
router.register(r'^bento', views.BentoViewSet)
router.register(r'^siap-saji', views.SiapSajiViewSet)
router.register(r'^pembayaran', views.PembayaranViewSet)
router.register(r'^bahan', views.BahanViewSet)
router.register(r'^komposisi', views.KomposisiViewSet)
router.register(r'^siap-saji', views.SiapSajiViewSet)
"""Pemesanan"""
router.register(r'^pemesanan', views.PemesananViewSet)
router.register(r'^siap-makan', views.SiapMakanViewSet)
router.register(r'^siap-masak', views.SiapMasakViewSet)
router.register(r'^siap-catering', views.SiapCateringViewSet)
# router.register(r'^history-pemesanan', views.HistoryPemesananViewSet)
"""pelanggan"""
router.register(r'^pelanggan', views.PelangganViewSet)
"""Tracking"""
router.register(r'^tracking', views.TrackingViewSet)
"""Poin"""
router.register(r'^poin', views.PoinViewSet)
router.register(r'^pembelian-poin', views.PembelianPoinViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)