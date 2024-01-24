from rest_framework.views import APIView
from .models import Project
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProjectSerializer
from rest_framework import permissions
from django.contrib.postgres.search import SearchVector, SearchQuery
from django.utils.text import slugify




class ManageProjectView(APIView):
    def get(self, request, format = None):
        try:
            user = request.user
            if user.is_founder:
                # Get the project associated with the founder
                project = Project.objects.get(founder=user)
                serializer = ProjectSerializer(project)
                return Response(serializer.data)
            else:
                # Get all the projects
                projects = Project.objects.all()
                serializer = ProjectSerializer(projects, many=True)
                return Response(serializer.data)
        except Project.DoesNotExist:
            return Response(
                {'error': 'The founder does not have any project associated with their account'},
                status = status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': 'Something went wrong in retrieving the project(s)'},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    


    def post(self, request):
        try:
            user = request.user
            if not user.is_founder:
                return Response(
                    {'error': 'User does not have necessary permissions for creating a project'},
                    status = status.HTTP_403_FORBIDDEN
                )
            if Project.objects.filter(founder=user).exists():
                return Response(
                    {'error': 'Founder can only create one project'},
                    status = status.HTTP_400_BAD_REQUEST)
                
            
            data = request.data
            
               
            data["founder"] = user.email
            project_name = data['project_name']
    
            website = data['website']
            country = data['country']
            description = data['description']
            
            end_date = data['end_date']
            
         

            investment = data['investment']
            
           
        


            stage = data['stage']
            
            industry = data['industry']
            project_image = data['project_image']
            presentation = data['presentation']
            video = data['video']
            papers = data['papers']
            data["slug"]= slugify(data['project_name'])
            slug = data["slug"]
            
            

            data = {
                'project_name': project_name,
                'website': website,
                'country': country,
                'end_date':end_date,
                'description': description,
                'investment': investment,
                'stage': stage,
                'industry': industry,
                'project_image': project_image,
                'presentation': presentation,
                'video': video,
                'papers': papers,
                
            }
            

            Project.objects.create(project_name=project_name,
                                    founder = user.email,
                                    slug = slug,
                                    investment=investment,
                                    website= website,
                                    country=country,
                                    end_date=end_date,
                                    description=description,
                                    
                                    stage=stage,
                                    industry=industry,
                                    project_image=project_image,
                                    presentation=presentation,
                                    video=video,
                                    papers=papers)
          




            return Response(
                {'success': 'Project created successfully'},
                status = status.HTTP_201_CREATED
            )
        except:
            return Response(
               {'error': 'Something went wrong when creating the project'},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    def retrieve_values(self, data):
        project_name = data['project_name']
    
        website = data['website']
        country = data['country']
        description = data['description']

        investment = data['investment']
        try:
            investment = int(investment)
        except:
            return -1


        stage = data['stage']
        
        if stage == 'PRE_SEED':
            stage = 'Pre Seed'
        if stage == 'SEED':
            stage = 'Seed'
        if stage == 'SERIES_A_B':
            stage = 'Series A B'
        if stage == 'SERIES C':
            stage = 'Series C'

        industry = data.getlist('industry')
        if len(industry) > 3:
            return -2      
        project_image = data['project_image']
        presentation = data['presentation']
        video = data['video']
        papers = data['papers']

        data = {
            'project_name': project_name,
            'website': website,
            'country': country,
            'description': description,
            'investment': investment,
            'stage': stage,
            'industry': industry,
            'project_image': project_image,
            'presentation': presentation,
            'video': video,
            'papers': papers,
        }

        return data

   


    def put(self, request):
        try:
            user = request.user

            if not user.is_founder:
                return Response(
                    {'error': 'User does not have necessary permissions for updating this Project data'},
                    status=status.HTTP_403_FORBIDDEN
                )

            data = request.data

            data = self.retrieve_values(data)

            if data == -1:
                return Response(
                    {'error': 'investment must be an integer'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            if data == -2:
                return Response(
                    {'error': 'only 3 industries can be selected'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            project_name = data['project_name']
            website = data['website']
            country = data['country']
            description = data['description']
            investment = data['investment']
            stage = data['stage']
            industry = data['industry']
            project_image = data['project_image']
            video = data['video']
            papers = data['papers']
            presentation = data['presentation']

            # Get the project instance by founder and project_name
            project = Project.objects.get(founder=user.email, project_name=project_name)
            project.project_name = project_name
            project.website = website
            project.country = country
            project.description = description
            project.investment = investment
            project.stage = stage
            project.industry = industry
            project.project_image = project_image
            project.presentation = presentation
            project.video = video
            project.papers = papers
            project.save()

            return Response(
                {'success': 'Project updated successfully'},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when updating Project'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def patch(self, request):
        try:
            user = request.user

            if not user.is_founder:
                return Response(
                    {'error': 'User does not have necessary permissions for updating this Project data'},
                    status=status.HTTP_403_FORBIDDEN
                )

            data = request.data

            slug = data['slug']

            if not Project.objects.filter(founder=user.email, slug=slug).exists():
                return Response(
                    {'error': 'Project does not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )

            project = Project.objects.get(founder=user.email, slug=slug)

            if 'project_name' in data:
                project.project_name = data['project_name']
            if 'website' in data:
                project.website = data['website']
            if 'country' in data:
                project.country = data['country']
            if 'description' in data:
                project.description = data['description']
            if 'investment' in data:
                investment = data['investment']
                try:
                    investment = int(investment)
                except:
                    return Response(
                        {'error': 'Investment must be an integer'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                project.investment = investment
            if 'stage' in data:
                stage = data['stage']
                if stage == 'PRE_SEED':
                    stage = 'Pre Seed'
                if stage == 'SEED':
                    stage = 'Seed'
                if stage == 'SERIES_A_B':
                    stage = 'Series A B'
                if stage == 'SERIES C':
                    stage = 'Series C'
                project.stage = stage
            if 'industry' in data:
                industry = data['industry']
                project.industry.set(industry)
            if 'project_image' in data:
                project.project_image = data['project_image']
            if 'presentation' in data:
                project.presentation = data['presentation']
            if 'video' in data:
                project.video = data['video']
            if 'papers' in data:
                project.papers = data['papers']

            project.save()

            return Response(
                {'success': 'Project updated successfully'},
                status=status.HTTP_200_OK)
        except:
            return Response(
                {'error': 'Something went wrong when updating Project'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request):
        try:
            user = request.user

            if not user.is_founder:
                return Response(
                    {'error': 'User does not have necessary permissions for deleting this Project data'},
                    status=status.HTTP_403_FORBIDDEN
                )

            data = request.data

            try:
                slug = data['slug']
            except:
                return Response(
                    {'error': 'Slug was not provided'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if not Project.objects.filter(founder=user.email, slug=slug).exists():
                return Response(
                    {'error': 'Project you are trying to delete does not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )

            Project.objects.filter(founder=user.email, slug=slug).delete()

            if not Project.objects.filter(founder=user.email, slug=slug).exists():
                return Response(
                    status=status.HTTP_204_NO_CONTENT
                )
            else:
                return Response(
                    {'error': 'Failed to delete Project'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response(
                {'error': 'Something went wrong when deleting Project'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class ProjectDetailView(APIView):
    
    def get(self,request,slug, format=None):
        try:
            user = request.user
            slug = slug

            if not slug:
                return Response(
                    {'error': 'Must provide slug'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            if user.is_founder and not Project.objects.filter(founder=user.email, slug=slug).exists():
                return Response(
                    {'error': 'Founders can only view their own Projects'},
                    status=status.HTTP_404_NOT_FOUND
                )

            if not Project.objects.filter(slug=slug).exists():
                return Response(
                    {'error': 'Published Project with this slug does not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )

            project_detail = Project.objects.get(slug=slug)
            project_detail = ProjectSerializer(project_detail)

            return Response(
                {'Project': project_detail.data},
                status=status.HTTP_200_OK
            )
        except Project.DoesNotExist:
            return Response(
                 {'error': 'Published project with this slug does not exist'},
                     status=status.HTTP_404_NOT_FOUND
    )

class ProjectsView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, slug, format=None):
        try:
            slug = slug
            user = request.user
            
            if not Project.objects.filter(slug=slug).exists():
                return Response(
                    {'error': 'No published Projects in the database'},
                    status=status.HTTP_404_NOT_FOUND
                )
            if user.is_founder and not Project.objects.filter(founder=user.email, slug=slug).exists():
                return Response(
                    {'error': 'Founders can only view their own Projects'},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            

            projects = Project.objects.all()
            serializer = ProjectSerializer(projects, many=True)
            return Response(serializer.data)
        except:
            return Response(
                {'error': 'Something went wrong when retrieving Projects'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class SearchProjectsView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        try:
            country = request.query_params.get('country')

            max_investment = request.query_params.get('max_investment')
            try:
                max_investment = int(max_investment)
            except:
                return Response(
                    {'error': 'Max investment must be an integer'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            stage = request.query_params.get('stage')
            if stage == 'PRE_SEED':
                stage = 'Pre Seed'
            if stage == 'SEED':
                stage = 'Seed'
            if stage == 'SERIES_A_B':
                stage = 'Series A B'
            if stage == 'SERIES C':
                stage = 'Series C'

            industry = request.query_params.get('industry')
            

            search = request.query_params.get('search')
            if not search:
                return Response(
                    {'error': 'Must pass search criteria'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            vector = SearchVector('project_name', 'description')
            query = SearchQuery(search)

            if not Project.objects.annotate(
                search=vector
            ).filter(
                search=query,
                country=country,
                investment__lte=max_investment,
                stage=stage,
                industry=industry,
            ).exists():
                return Response(
                    {'error': 'No Projects found with this criteria'},
                    status=status.HTTP_404_NOT_FOUND
                )

            Projects = Project.objects.annotate(
                search=vector
            ).filter(
                search=query,
                country=country,
                investment__lte=max_investment,
                stage=stage,
                industry=industry,
            )
            Projects = ProjectSerializer(Projects, many=True)

            return Response(
                {'Projects': Projects.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when searching for Projects'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
