from tethys_sdk.base import TethysAppBase, url_map_maker


class Flashfloodnp(TethysAppBase):
    """
    Tethys app class for flashfloodnp.
    """

    name = 'Flash Flood Prediction Tool - Nepal'
    description = ''
    package = 'flashfloodnp'  # WARNING: Do not change this value
    index = 'home'
    icon = 'flashfloodnp/images/icon.png'
    root_url = 'flashfloodnp'
    color = '#192a56'
    tags = 'Flash Flood Prediction'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)
        url_maps = (
            UrlMap(
                name='home',
                url='flashfloodnp',
                controller='flashfloodnp.controllers.home'),
            UrlMap(
                name='chartHiwat',
                url='flashfloodnp/chartHiwat',
                controller='flashfloodnp.controllers.chartHiwat'),
            UrlMap(
                name='getGeoJson1',
                url='flashfloodnp/getGeoJson1',
                controller='flashfloodnp.controllers.getGeoJson1'),
            UrlMap(
                name='getForecastCSV',
                url='flashfloodnp/getForecastCSV',
                controller='flashfloodnp.controllers.getForecastCSV'),
            UrlMap(
                name='getHistoricCSV',
                url='flashfloodnp/getHistoricCSV',
                controller='flashfloodnp.controllers.getHistoricCSV'),
        )
        return url_maps
