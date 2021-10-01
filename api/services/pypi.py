import requests

def request_package_on_pypi(project_name, *version):
            if not version:
                return requests.get(f'https://pypi.org/pypi/{project_name}/json')
            else:
                version = ''.join(version)
                return requests.get(f'https://pypi.org/pypi/{project_name}/{version}/json')
