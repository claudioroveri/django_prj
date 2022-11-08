from rest_framework.routers import DefaultRouter
from app.views import CarrosViewSet, MarcaViewSet, UsuarioViewSet

app_name = 'api'

# Esse 3 comandos fazem o conjunto de URL
# com padrão REST, utilizando a raiz carros
# prefixo r ==> raw para interpretar barra como barra
router = DefaultRouter(trailing_slash=False)
router.register(r'carros', CarrosViewSet)
router.register(r'marca', MarcaViewSet)
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = router.urls