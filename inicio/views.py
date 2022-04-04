from django.shortcuts import render
from django.http import HttpResponse
from propuestas.models import Propuesta
from usuarios.models import Organizacion
from django.views.generic import TemplateView
from django.db.models import Count

from .forms import GlosarioForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings


class LandingView(TemplateView):
    template_name = 'inicio/presentacion.html'

class EsperaView(TemplateView):
    template_name = 'inicio/en_construccion.html'

class ReimaginalaView(TemplateView):
    template_name = 'inicio/reimaginala.html'

class HomeView(TemplateView):
    template_name = 'inicio/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['organizaciones'] = Organizacion.objects.all()

        # este context fue cambiado para una org
        context['propuestas'] = Propuesta.objects.order_by('-id')[:3]
        # este context fue cambiado para una org

        # context['propuestas'] = Propuesta.objects.annotate(apoyos_count=Count('apoyos')).order_by('-autor__organizacion','-apoyos_count')[:3]
        return context


class QueesView(TemplateView):
    template_name = 'inicio/que_es.html'


class PreguntasView(TemplateView):
    template_name = 'inicio/preguntas-frecuentes.html'


class EnsayosView(TemplateView):
    template_name = 'inicio/ensayos.html'


class EnsayotomounoView(TemplateView):
    template_name = "inicio/ensayo-tomouno.html"


class EnsayotomodosView(TemplateView):
    template_name = "inicio/ensayo-tomodos.html"


class EnsayotomotresView(TemplateView):
    template_name = "inicio/ensayo-tomotres.html"


class EnsayotomocuatroView(TemplateView):
    template_name = "inicio/ensayo-tomocuatro.html"


class EnsayotomocincoView(TemplateView):
    template_name = "inicio/ensayo-tomocinco.html"


class TerminosView(TemplateView):
    template_name = 'inicio/terminos.html'


class Feminista1View(TemplateView):
    template_name = 'inicio/constitucion-feminista.html'

# class Feminista2View(TemplateView):
#     template_name = 'inicio/mujeres-y-desc.html'

# class Feminista3View(TemplateView):
#     template_name = 'inicio/mas-que-juanitas-del-mar.html'


class Feminista4View(TemplateView):
    template_name = 'inicio/las-duenas-de-casa-sin-casa.html'


class Feminista5View(TemplateView):
    template_name = 'inicio/el-rol-de-las-mujeres-indigenas-en-el-desarrollo-social-politico-y-cultural-de-sus-pueblos.html'


class Feminista6View(TemplateView):
    template_name = 'inicio/la-vision-de-las-mujeres-afrodescencientes.html'

# class Feminista7View(TemplateView):
#     template_name = 'inicio/ensayos.html'


class Feminista8View(TemplateView):
    template_name = 'inicio/derechos-sexuales-y-reproductivos-descentralizados-en-la-nueva-constitucion.html'

# class Feminista9View(TemplateView):
#     template_name = 'inicio/ensayos.html'


class Feminista10View(TemplateView):
    template_name = 'inicio/constitucion-con-enfoque-de-desarrollo-territorial.html'


class Feminista11View(TemplateView):
    template_name = 'inicio/derecho-al-trabajo-remunerado.html'


class Feminista12View(TemplateView):
    template_name = 'inicio/derechos-sexuales-y-reproductivos-descentralizados-en-la-nueva-constitucion.html'


class Feminista13View(TemplateView):
    template_name = 'inicio/salud-y-autonomia-sexual-y-reproductiva.html'


class Feminista14View(TemplateView):
    template_name = 'inicio/educacion-integral-en-sexualidad-en-la-nueva-constitucion.html'


class Feminista15View(TemplateView):
    template_name = 'inicio/educacion-no-sexista.html'


class Feminista16View(TemplateView):
    template_name = 'inicio/el-rol-de-las-mujeres-y-ninas-en-la-gestion-hidrica.html'


class Feminista17View(TemplateView):
    template_name = 'inicio/juntas-abortamos.html'


class Feminista18View(TemplateView):
    template_name = 'inicio/la-importancia-de-los-derechos-sexuales-y-reproductivos-y-su-inclusion-en-la-nueva-constitucion.html'


class Feminista19View(TemplateView):
    template_name = 'inicio/el-rol-de-las-mujeres-indigenas-en-el-desarrollo-social-politico-y-cultural-de-sus-pueblos.html'


class Feminista20View(TemplateView):
    template_name = 'iniciolas-duenas-de-casa-sin-casa.html'


class Feminista21View(TemplateView):
    template_name = 'inicio/los-desafios-del-proceso-constituyente-para-abordar-la-crisis-de-los-ciudadanos.html'


class Feminista22View(TemplateView):
    template_name = 'inicio/la-vision-de-las-mujeres-afrodescendientes.html'


class Feminista23View(TemplateView):
    template_name = 'inicio/mujeres-de-maya-sawuri-unicas-tejedoras-un-oficio-multigeneracional.html'


class Feminista24View(TemplateView):
    template_name = 'inicio/mujeres-de-zonas-de-sacrificio-en-resistencia-de-quintero-y-puchuncavi-reflexiones-y-propuestas.html'


class Feminista25View(TemplateView):
    template_name = 'inicio/las-mujeres-en-chile.html'


class Feminista26View(TemplateView):
    template_name = 'inicio/mujeres-salud-y-patologizacion-del-ciclo-vital.html'


class Feminista27View(TemplateView):
    template_name = 'inicio/mujeres-y-desc.html'


class Feminista28View(TemplateView):
    template_name = 'inicio/mujeres-y-migracion.html'


class Feminista29View(TemplateView):
    template_name = 'inicio/mas-que-juanitas-del-mar.html'


class Feminista30View(TemplateView):
    template_name = 'inicio/ninas-adolescentes-y-la-constitucion.html'


class Feminista31View(TemplateView):
    template_name = 'inicio/participar-en-la-vida-cultural-o-participar-para-cambiar-la-cultura.html'


class Feminista32View(TemplateView):
    template_name = 'inicio/red-de-defensoras-de-los-ddhh-y-el-programa-feminista-por-una-nueva-constitución-en-busqueda-de-la-articulacion-y-vocacion-de-poder-del-movimiento-feminista.html'


class Feminista33View(TemplateView):
    template_name = 'inicio/reflexiones-a-partir-de-las-experiencias-de-cinco-mujeres-en-la-defensa-de-sus-territorios.html'


class Feminista34View(TemplateView):
    template_name = 'inicio/teletrabajo-e-inequidades-de-genero.html'


class Feminista35View(TemplateView):
    template_name = 'inicio/vida-y-aborto-en-torno-a-la-violencia-de-la-penalizacion.html'


class Feminista36View(TemplateView):
    template_name = 'inicio/nueva-constitucion-ninas-y-adolescentes.html'


class Feminista37View(TemplateView):
    template_name = 'inicio/mujeres-y-sistema-judicial.html'


class Feminista38View(TemplateView):
    template_name = 'inicio/mujeres-y-campamentos-en-pandemia.html'


class MapaconstitucionalView(TemplateView):
    template_name = "inicio/mapa-constitucional.html"


class MapaconstitucionalterminosView(TemplateView):
    template_name = "inicio/mapa-constitucional-terminos.html"


class RoldeestadoView(TemplateView):
    template_name = "inicio/rol-de-estado.html"


class PoliticafiscalView(TemplateView):
    template_name = "inicio/politica-fiscal.html"


class RepublicademocraticaView(TemplateView):
    template_name = "inicio/republica-democratica.html"


class SistemadegobiernoView(TemplateView):
    template_name = "inicio/sistema-de-gobierno.html"


class PlurinacionalidadView(TemplateView):
    template_name = "inicio/plurinacionalidad.html"


class FormadeestadoView(TemplateView):
    template_name = "inicio/forma-de-estado.html"


class ControlconstitucionalView(TemplateView):
    template_name = "inicio/control-constitucional.html"


class OrganosautonomosView(TemplateView):
    template_name = "inicio/organos-autonomos.html"


class FuerzasarmadasypoliciasView(TemplateView):
    template_name = "inicio/fuerzas-armadas-y-policias.html"


class ParticipacionpopularView(TemplateView):
    template_name = "inicio/participacion-popular.html"


class TrabajodignoView(TemplateView):
    template_name = "inicio/trabajo-digno.html"


class PensionesyseguridadsocialView(TemplateView):
    template_name = "inicio/pensiones-y-seguridad-social.html"


class NiveldevidaadecuadoView(TemplateView):
    template_name = "inicio/nivel-de-vida-adecuado.html"


class AlimentacionView(TemplateView):
    template_name = "inicio/alimentacion.html"


class AguaView(TemplateView):
    template_name = "inicio/agua.html"


class ViviendaadecuadaView(TemplateView):
    template_name = "inicio/vivienda-adecuada.html"


class SaludView(TemplateView):
    template_name = "inicio/salud.html"


class EducacionView(TemplateView):
    template_name = "inicio/educacion.html"


class CulturaView(TemplateView):
    template_name = "inicio/cultura.html"


class CienciayarteView(TemplateView):
    template_name = "inicio/ciencia-y-arte.html"


class MedioambientesanoView(TemplateView):
    template_name = "inicio/medio-ambiente-sano.html"


class ExigibilidaddelosderechosView(TemplateView):
    template_name = "inicio/exigibilidad-de-los-derechos.html"


class MujeresView(TemplateView):
    template_name = "inicio/mujeres.html"


class LgbtiView(TemplateView):
    template_name = "inicio/lgbti+.html"


class InfanciasView(TemplateView):
    template_name = "inicio/infancias.html"


class PueblosindigenasView(TemplateView):
    template_name = "inicio/pueblos-indigenas.html"


class PersonascondiscapacidadView(TemplateView):
    template_name = "inicio/personas-con-discapacidad.html"


class PersonasmayoresView(TemplateView):
    template_name = "inicio/personas-mayores.html"


class PersonasmigrantesView(TemplateView):
    template_name = "inicio/personas-migrantes.html"


class IniciativapopularView(TemplateView):
    template_name = "inicio/iniciativa-popular.html"


class DebateconstituyenteView(TemplateView):
    template_name = "inicio/debate-constituyente.html"


class CronogramaconstitucionalView(TemplateView):
    template_name = "inicio/cronograma-constitucional.html"


class GlosarioconstitucionalView(TemplateView):
    template_name = "inicio/glosario-constitucional.html"

    def getpalabra(request):
        form = GlosarioForm()
        if request.method == 'POST':
            form = GlosarioForm(request.POST)
            if form.is_valid():
                subject = 'Enviado'
                palabra = form.GET['palabra']
                send_mail(subject,
                          palabra, settings.EMAIL_HOST_USER, ['felipe.perry@gmail.com'], fail_silently=False)

        return render(request, 'inicio/home.html', {'form': form})


def error404(request, exception, template_name='inicio/error.html'):
    return render(request, template_name)


def error500(request, template_name='inicio/error.html'):
    return render(request, template_name)


def error403(request, exception, template_name='inicio/error.html'):
    return render(request, template_name)


def error400(request, exception, template_name='inicio/error.html'):
    return render(request, template_name)
