from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField


class LandmarkPage(Page):
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    coordinate_latitude = models.DecimalField(null=True, decimal_places=6, max_digits=10)
    coordinate_longitude = models.DecimalField(null=True, decimal_places=6, max_digits=10)
    isFeatured = models.BooleanField(default=False)
    isFavorite = models.BooleanField(default=False)
    park = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('category'),
        FieldPanel('city'),
        FieldPanel('state'),
        MultiFieldPanel([
                FieldPanel("coordinate_latitude"),
                FieldPanel("coordinate_longitude"),
            ],
            heading="Coordinates"
        ),
        FieldPanel('isFeatured'),
        FieldPanel('isFavorite'),
        FieldPanel('park'),
        FieldPanel('description'),
        FieldPanel('image')
    ]

    api_fields = [
        APIField('name'),
        APIField('category'),
        APIField('city'),
        APIField('state'),
        APIField('isFeatured'),
        APIField('isFavorite'),
        APIField('park'),
        APIField('description'),
        APIField('coordinate_latitude'),
        APIField('coordinate_longitude'),
        APIField('image', serializer=ImageRenditionField('fill-640x640'))
    ]
