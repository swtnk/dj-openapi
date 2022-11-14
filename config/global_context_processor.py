from django.conf import settings


def get_social_tag_context(*args, **kwargs):
    discription = """OpenAPI Tool"""
    social_tags = {
        "static_version": settings.STATIC_VERSION,
        "application_name": settings.APP_NAME,
        "title": settings.APP_NAME,
        "seo_keywords": "OpenAPI, API, Open, Opensource, source, v3, v2, v1, swagger, swagger-ui, redoc, redoc-ui",
        "seo_description": discription,
        "seo_author": "VetPracto",
        "st_type": "website",
        "st_url": "https://vetpracto.com",
        "st_title": "VetPracto",
        "st_description": discription,
        "st_image": "http://0.0.0.0:8000/static/logo/vet-practo-white-transparent.png",
        "st_site_name": "VetPracto",
        "st_locale": "en_US",  # en_US, en_GB, en_CA, en_AU, en_IN, en_IE, en_NZ, en_ZA, en_HK, en_DE, en_JP, en_CN, en_TW, en_FR, en_ES, en_RU, en_IT, en_BR, en_AR, en_KR, en_MX, en_CL, en_CO, en_CR, en_HR, en_HU, en_ID, en_IL, en_IN, en_MY, en_NG, en_PH, en_PK, en_PL, en_PT, en_RO, en_SG, en_TH, en_TR, en_UA, en_VN, en_CY, en_CZ, en_DK, en_EE, en_FI, en_GR, en_HN, en_IS, en_LT, en_LV, en_MT, en_NO, en_NL, en_PE, en_SV, en_SI, en_SK, en_US, en_UY, en_VE, en_BE, en_BG, en_CH, en_CY, en_CZ, en_DE, en_DK, en_EE, en_ES, en_FI, en_FR, en_GR, en_HU, en_IE, en_IT, en_LT, en_LU, en_LV, en_MT, en_NL, en_PL, en_PT, en_RO, en_SE, en_SI, en_SK, en_US, en_AT, en_BE, en_CH, en_DE, en_DK, en_ES, en_FI, en_FR, en_GB, en_IE, en_IT, en_LU, en_NL, en_PT, en_SE, en_US, en_AD, en_AL, en_AR, en_AS, en_AT, en_BA, en_BE, en_BG, en_BY, en_CH, en_CY, en_CZ, en_DE, en_DK, en_EE, en_EL, en_ES, en_FI
        "st_img_alt": "VetPracto",
        "st_card": "summary_large_image",  # summary, summary_large_image, photo, gallery, product, app, player
    }
    return social_tags
