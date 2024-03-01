from gen3.auth import Gen3Auth
from gen3.tools.indexing import validate_manifest_format
from gen3.tools.indexing.index_manifest import index_object_manifest

file_path = 'indexing-manifest.tsv'
commons_url = 'https://development.aced-idp.org'

authentication_object = Gen3Auth(endpoint=commons_url, refresh_file='credentials.json')
validate_manifest_format.is_valid_manifest_format(file_path)
index_object_manifest(commons_url=commons_url,
                      manifest_file=file_path,
                      thread_num=8,
                      auth=authentication_object,
                      output_filename=file_path[:-4] + '_output.tsv')
