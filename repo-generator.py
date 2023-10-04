import os
import sys
from share import *


def generateRepo(filename):
  class_name = snake_case_to_pascal_case(filename) + "Repository"

  buffer = StringBuffer()

  buffer.write(f'abstract class {class_name} {{')
  buffer.write("}")

  return buffer.getvalue()


def generateRepoImplement(filename):
  class_name = snake_case_to_pascal_case(filename) + "StorageRepository"
  parent_name = snake_case_to_pascal_case(filename) + "Repository"

  buffer = StringBuffer()

  buffer.write(f"import '{filename}_repository.dart';")
  buffer.addLine()

  buffer.write(f'class {class_name} extends {parent_name} {{')

  buffer.write(f'final {parent_name} webApi;')
  buffer.write(f'{class_name}({{ required this.webApi }});')

  buffer.write("}")

  return buffer.getvalue()


def generateService(filename):
  class_name = snake_case_to_pascal_case(filename) + "Service"

  buffer = StringBuffer()

  buffer.write(f"import 'package:dio/dio.dart';")
  buffer.write(f"import 'package:one_data/one_data.dart';")
  buffer.write(f"import 'package:one_data/src/model/model_barrel.dart';")
  buffer.write(f"import 'package:retrofit/retrofit.dart';")

  buffer.addLine()

  buffer.write(f"part '{filename}_service.g.dart';")
  buffer.addLine()

  buffer.write('@RestApi()')
  buffer.write(f'abstract class {class_name} {{')
  buffer.write(
      f'factory {class_name}(Dio dio, {{String baseUrl}}) = _{class_name};')

  buffer.addLine()

  buffer.write(f"""
  @POST('')
  Future<HttpResponse<BaseResponse>> testPOST(@Body() Map<String, dynamic> map);
  """)

  buffer.write(f"""
  @GET('')
  Future<HttpResponse<BaseResponse>> testGETQuery(@Query('header') String header);
  """)

  buffer.write(f"""
  @GET('')
  Future<HttpResponse<BaseResponse>> testGETQueries(@Queries() Map<String, dynamic> queries);
  """)

  buffer.write(f'static {class_name} create() {{')
  buffer.write(
      f'final dio = OneApiHelper().createDio()..addOneAppLog()..addInterceptors();')
  buffer.write(f'return {class_name}(dio);')
  buffer.write("}")

  buffer.write("}")

  return buffer.getvalue()


def generateServiceApi(filename):
  class_name = snake_case_to_pascal_case(filename) + "ServiceApi"
  service_name = snake_case_to_pascal_case(filename) + "Service"
  parent_name = snake_case_to_pascal_case(filename) + "Repository"

  buffer = StringBuffer()
  buffer.write(
      f"import '../../source/{filename}/{filename}_repository.dart';")
  buffer.write(f"import '{filename}_service.dart';")
  buffer.addLine()

  buffer.write(f'class {class_name} extends {parent_name} {{')

  buffer.write(f'final {service_name} service;')
  buffer.write(f'{class_name}({{ required this.service }});')

  buffer.write("}")

  return buffer.getvalue()


def generateServiceLocator(filename):
  name = snake_case_to_pascal_case(filename)

  service = name + "Service"
  serviceApi = name + "ServiceApi"
  repository = name + "Repository"
  storageRepository = name + "StorageRepository"

  buffer = StringBuffer()

  buffer.write(f"""
  import 'service/{filename}/{filename}_repository.dart';
  import 'service/{filename}/{filename}_repository_impl.dart';
  import 'source/{filename}/{filename}_repository.dart';
  import 'source/{filename}/{filename}_repository_impl.dart';
  """)

  buffer.write(f"""
  Get.put<{repository}>(
    {storageRepository}(
      webApi: {serviceApi}(service: {service}.create()),
    ),
    permanent: true,
  );
  """)

  return buffer.getvalue()


if __name__ == "__main__":
  folder_name = 'hello_world'

  if len(sys.argv) == 2:
    folder_name = sys.argv[1]

  parent_path = os.path.join('resources', folder_name)

  os.makedirs(parent_path, exist_ok=True)

  # Repository
  data = generateRepo(folder_name)
  write_file(os.path.join(
      parent_path, f'{folder_name}_repository.dart'), data)

  # Repository Implement
  data = generateRepoImplement(folder_name)
  write_file(os.path.join(
      parent_path, f'{folder_name}_repository_impl.dart'), data)

  # Service
  data = generateService(folder_name)
  write_file(os.path.join(
      parent_path, f'{folder_name}_service.dart'), data)

  # Service API
  data = generateServiceApi(folder_name)
  write_file(os.path.join(
      parent_path, f'{folder_name}_service_api.dart'), data)

  # Locator
  data = generateServiceLocator(folder_name)
  write_file(os.path.join(
      parent_path, f'{folder_name}_service_locator.dart'), data)
