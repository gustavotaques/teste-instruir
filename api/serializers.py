from rest_framework import serializers

from .models import PackageRelease, Project
from .services.pypi import request_package_on_pypi
from .exceptions import CustomValidation


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageRelease
        fields = ['name', 'version']
        extra_kwargs = {'version': {'required': False}}


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'packages']

    packages = PackageSerializer(many=True)
    
    def validate(self, data):
        packages = data['packages']

        for package in packages:
            if 'version' in package.keys():
                package_name = package['name']
                package_version = package['version']

                response = request_package_on_pypi(package_name, package_version)

                if response.status_code >= 400:
                    raise CustomValidation
            else:
                package_name = package['name']

                response = request_package_on_pypi(package_name)

                if response.status_code == 200:
                    package_version = response.json()['info']['version']
                    package['version'] = package_version
                else:
                    raise CustomValidation
        return data         

    def create(self, validated_data):
        project_name = validated_data['name']
        packages = validated_data['packages']

        project = Project(name=project_name)
        project.save()

        for package in packages:
            package_name = package['name']
            package_version = package['version']
            final_data = PackageRelease(name=package_name, version=package_version, project=project)
            final_data.save()

        return validated_data
