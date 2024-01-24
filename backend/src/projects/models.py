from django.db import models
from djmoney.models.fields import MoneyField
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField
from django.utils.timezone import now


# Create your models here.

INDUSTRIES = (
    ('ecommerse_and_retail', 'Ecommerse andretail tech'),
    ('delivery_services', 'Delivery Services'),
    ('healthcare_tech', 'Healthcare Tech'),
    ('artificial_intelligence', 'Aritificial Intelligence'),
    ('vr', 'Virtual Reality'),
    ('ed_tech', 'Educational Tech'),
    ('fin_tech', 'Financial Tech'),
    ('big_data', 'Big Data'),
    ('supply_chain_management_logistic', 'Supply Chain Management Logistic'),
    ('media_entertainment','Media and Entertainment'),
    ('real_estate', 'Real Estate'),
    ('b2b_software', 'B2B software'),
    ('shared_mobility', 'Shared Mobility'),
    ('transportation', 'Transportation'),
    ('hr_tech', 'HR Tech'),
    ('comp_hardware', 'Computer Hardware'),
    ('services', 'Professional, scientific and technical services'),
    ('networking', 'Networking'),
    ('ads_marketing', 'Advertising and Marketing'),
    ('streaming_services', 'Streaming Services'),
    ('manufacturing', 'Manufacturing'),
    ('eco_waste_management', 'Ecology and Waste Management')
)

def upload_path(instance, filname):
    return '/'.join(['pictures', str(instance.project_name), filname])
class Project(models.Model):

    class StageType(models.TextChoices):
        PRE_SEED = 'Pre Seed'
        SEED ='seed'
        SERIES_A_B = 'Series A B'
        SERIES_C ='Series C'
    
    founder =models.EmailField(max_length =255, default ='Email')
    project_name = models.CharField(max_length = 30)
    slug = models.SlugField(unique=True)
    investment =models.IntegerField()
    description = models.TextField()
    website=models.URLField(max_length=200)
    stage = models.CharField(max_length=15, choices=StageType.choices, default= StageType.PRE_SEED)
    industry = MultiSelectField(choices = INDUSTRIES, max_choices =3, max_length =50, null = True)
    country = CountryField(null = True)
    end_date = models.DateField(default=now, blank=True)
    project_image = models.ImageField( null = True, upload_to = upload_path)
    presentation=models.URLField(max_length=200, null = True)
    video = models.URLField(max_length=200, null = True)
    papers =models.URLField(max_length=200, null =True)

    def __str__(self):
        return self.project_name
    def creator(self):
        return self.founder
    # def create(self, project_name, founder, slug, investment, description, website, stage, industry, country,
    #             end_date, project_image, presentation, video, papers):
    #     project = self.model(
    #         project_name = project_name, founder=founder, slug=slug, investment=investment,
    #         description = description, website=website, stage=stage, industry=industry, country= country,
    #         end_date=end_date, project_image=project_image, presentation=presentation, video=video, papers=papers
    #     )
    #     project.save(using= self._db)
    #     return project













