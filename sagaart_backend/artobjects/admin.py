from django.contrib import admin
from .models import (
    Category, Color, Genre, MaterialArtObject, BaseArtObject, Style,
    Artist, ArtistSocialMedia, TeachingActivities, Education, EducationalInstitution,
    ArtistAward, Award, Collection, ArtObject, Gallery, Show, Price
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(MaterialArtObject)
class MaterialArtObjectAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(BaseArtObject)
class BaseArtObjectAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['first_name',
                    'last_name',
                    'sex',
                    'date_of_birth',
                    'date_of_death']

    list_filter = ['sex',
                   'personal_style']

    search_fields = ['first_name',
                     'last_name',
                     'description']

    raw_id_fields = ['city_of_birth',
                     'city_of_living',
                     'photo',]
    filter_horizontal=('favorited_by',)



@admin.register(ArtistSocialMedia)
class ArtistSocialMediaAdmin(admin.ModelAdmin):
    list_display = ['artist',
                    'link',
                    'social_media']

    search_fields = ['artist__first_name',
                     'artist__last_name',
                     'link']


@admin.register(TeachingActivities)
class TeachingActivitiesAdmin(admin.ModelAdmin):
    list_display = ['artist',
                    'educational_institutions',
                    'started_at',
                    'ended_at']
    
    search_fields = ['artist__first_name',
                     'artist__last_name',
                     'educational_institutions__name']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['artist',
                    'educational_institutions',
                    'degree',
                    'started_at',
                    'ended_at']

    search_fields = ['artist__first_name',
                     'artist__last_name',
                     'educational_institutions__name']


@admin.register(EducationalInstitution)
class EducationalInstitutionAdmin(admin.ModelAdmin):
    list_display = ['name', 
                    'type_ei',
                    'city']

    list_filter = ['type_ei']
    search_fields = ['name', 'city__name']


@admin.register(ArtistAward)
class ArtistAwardAdmin(admin.ModelAdmin):
    list_display = ['artist',
                    'award',
                    'year',
                    'city']

    search_fields = ['artist__first_name',
                     'artist__last_name',
                     'award__name']


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'created_at',
                    'private']

    search_fields = ['name']
    list_filter = ['private']


@admin.register(ArtObject)
class ArtObjectAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'artist',
                    'owner',
                    'vendor',
                    'status',
                    'date_of_creation',
                    'category',
                    'material_art_object']

    list_filter = ['status',
                   'category',
                   'material_art_object']

    search_fields = ['name',
                     'owner__username',
                     'vendor']
    
    raw_id_fields = ['owner',
                     'city_sold',
                     'category',
                     'genre',
                     'material_art_object',
                     'base_art_object',
                     'style',
                     'collection',
                     'main_image']

    filter_horizontal = ('favourited_by', 'colors',  'images',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']
    search_fields = ['name', 'city__name']


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'started_at',
                    'ended_at',
                    'place',
                    'personal']

    list_filter = ['place', 'personal']
    search_fields = ['name', 'place__name']


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['artobject',
                    'price',
                    'created_at']

    search_fields = ['artobject__name']
