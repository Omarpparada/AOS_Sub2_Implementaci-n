from __future__ import annotations

from typing import Optional, Union

from fastapi import FastAPI, Header, Path, Response
from pydantic import conint, constr

from database.models import (
    DNI,
    EstadoVehiculo,
    HTTPProblem,
    IdVehiculo,
    ListaVehiculos,
    Order,
    Ordering1,
    Vehiculo,
    VehiculosGetResponse,
    VehiculosPostRequest,
    VehiculosVehiculoVINIdPutRequest,
)
from service import VehiculosService
from database.interfaces import vehiculos

app = FastAPI(
    version='1.0.0',
    title='🚜[AOS - 23 - Subsistema_2] Gestión de vehiculos 🚘',
    description='## **[AOS - 23 - Subsistema_2]** API REST para la gestión de los vehiculos de los clientes de un taller.\n',
    license={'name': 'MIT', 'url': 'https://opensource.org/licenses/MIT'},
    contact={'name': 'Equipo 7', 'url': 'https://www.etsisi.upm.es/'},
    servers=[{'url': 'http://127.0.0.1:8000'}],
)


@app.get(
    '/vehiculos',
    response_model=list[vehiculos],
    responses={'404': {'model': HTTPProblem}}, 
    tags=['Vehiculo'],
)
def vehiculo_cget(
   order: Optional[Order] = None,
   ordering: Optional[Ordering1] = Ordering1.ASC,
):
    """
    Obtiene todos los vehiculos
    """
    return VehiculosService().get_vehiculos(ordering, order)

@app.post(
    '/vehiculos',
    response_model=vehiculos,
    responses={
        '201': {'model': Vehiculo},
        '400': {'model': HTTPProblem},
        '422': {'model': HTTPProblem},
    },
    tags=['Vehiculo'],
)
def vehiculo_post(body: VehiculosPostRequest) -> Union[None, Vehiculo, HTTPProblem]:
    """
    Añade un nuevo vehiculo
    """
    
    return VehiculosService().post_vehiculos(body)

@app.options('/vehiculos', status_code=204, response_model=None, tags=['Vehiculo'])
def vehiculo_coptions() ->None:
    """
    Proporciona la lista de los métodos HTTP soportados por esta ruta.
    """
    response= Response()
    response.headers["access-control-allow-credentials"]= "False"
    response.headers["access-control-allow-headers"]="*"
    response.headers["access-control-allow-methods"]="GET, POST, OPTIONS"
    response.headers["access-control-allow-origin"]="*"
    response.headers["access-control-expose-headers"]="*, ETag"
    response.headers["allow"]="GET, POST, OPTIONS"
    response.headers["cache-control"]="private"
    response.headers["connection"]="close"
    return response



@app.options('/vehiculos/dni/{_d_n_i}',status_code=204, response_model=None, tags=['Vehiculo'])
def vehiculo__d_n_i_options(_d_n_i: str= Path(..., regex=r'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][A-Z]')) -> None:
    
    """
    Proporciona la lista de los métodos HTTP soportados por esta ruta.
    """
    response= Response()
    response.headers["access-control-allow-credentials"]= "False"
    response.headers["access-control-allow-headers"]="*"
    response.headers["access-control-allow-methods"]="GET, OPTIONS"
    response.headers["access-control-allow-origin"]="*"
    response.headers["access-control-expose-headers"]="*, ETag"
    response.headers["allow"]="GET, OPTIONS"
    response.headers["cache-control"]="private"
    response.headers["connection"]="close"
    return response
    


@app.get(
    '/vehiculos/dni/{_d_n_i}',
    response_model=list[vehiculos],
    responses={'404': {'model': HTTPProblem}},
    tags=['Vehiculo'],
)
def vehiculo__d_n_i_get(
    _d_n_i: str= Path(..., regex=r'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][A-Z]'),
) -> Union[list[vehiculos], HTTPProblem]:
    """
    Obtiene una lista vehiculo identificado por `DNI`
    """
    return VehiculosService().get_vehiculos_by_dni(dni=_d_n_i)


@app.options(
    '/vehiculos/dni/{_d_n_i}/{_estado__vehiculo}',status_code=204, response_model=None, tags=['Vehiculo']
)
def vehiculo__d_n_i__estado_options(
    _estado__vehiculo: EstadoVehiculo,
    _d_n_i: str= Path(..., regex=r'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][A-Z]')
    ) -> None:
    """
    Proporciona la lista de los métodos HTTP soportados por esta ruta.
    """
    response= Response()
    response.headers["access-control-allow-credentials"]= "False"
    response.headers["access-control-allow-headers"]="*"
    response.headers["access-control-allow-methods"]="GET, OPTIONS"
    response.headers["access-control-allow-origin"]="*"
    response.headers["access-control-expose-headers"]="*, ETag"
    response.headers["allow"]="GET, OPTIONS"
    response.headers["cache-control"]="private"
    response.headers["connection"]="close"
    return response
    


@app.get(
    '/vehiculos/dni/{_d_n_i}/{_estado__vehiculo}',
    response_model=list[vehiculos],
    responses={'404': {'model': HTTPProblem}},
    tags=['Vehiculo'],
)
def vehiculo__d_n_i__estado_get(
    _estado__vehiculo: EstadoVehiculo,
    _d_n_i: str= Path(..., regex=r'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][A-Z]'),
) -> Union[list[vehiculos], HTTPProblem]:
    """
    Obtiene una lista vehiculo identificado por `DNI` y `estado`
    """
    return VehiculosService().get_vehiculos_by_dni_and_estado(dni=_d_n_i,estado= _estado__vehiculo)


@app.options('/vehiculos/estado/{_estado__vehiculo}',status_code=204, response_model=None, tags=['Vehiculo'])
def vehiculo__estado_options(
    estado__vehiculo: EstadoVehiculo 
) -> None:
    """
    Proporciona la lista de los métodos HTTP soportados por esta ruta.
    """
    response= Response()
    response.headers["access-control-allow-credentials"]= "False"
    response.headers["access-control-allow-headers"]="*"
    response.headers["access-control-allow-methods"]="GET, OPTIONS"
    response.headers["access-control-allow-origin"]="*"
    response.headers["access-control-expose-headers"]="*, ETag"
    response.headers["allow"]="GET, OPTIONS"
    response.headers["cache-control"]="private"
    response.headers["connection"]="close"
    return response


@app.get(
    '/vehiculos/estado/{estado}',
    response_model=list[vehiculos],
    responses={'404': {'model': HTTPProblem}},
    tags=['Vehiculo'],
)
def vehiculo__estado_get(
    estado: EstadoVehiculo 
) -> Union[ListaVehiculos, HTTPProblem]:
    """
    Obtiene una lista vehiculo identificado por `Estado`
    """
    return VehiculosService().get_vehiculos_by_estados(estado)

@app.options('/vehiculos/vin/{vin}',status_code=204, response_model=None, tags=['Vehiculo'])
def vehiculo__v_i_n_options(
    vin: str=Path(..., regex=r'[A-HJ-NPR-Z0-9]{17}')
) -> None:
    """
    Proporciona la lista de los métodos HTTP soportados por esta ruta.
    """
    response= Response()
    response.headers["access-control-allow-credentials"]= "False"
    response.headers["access-control-allow-headers"]="*"
    response.headers["access-control-allow-methods"]="GET, OPTIONS, PUT, DELETE"
    response.headers["access-control-allow-origin"]="*"
    response.headers["access-control-expose-headers"]="*, ETag"
    response.headers["allow"]="GET, OPTIONS, PUT, DELETE"
    response.headers["cache-control"]="private"
    response.headers["connection"]="close"
    return response


@app.get(
    '/vehiculos/vin/{vin}',
    response_model=vehiculos,
    responses={'404': {'model': HTTPProblem}},
    tags=['Vehiculo'],
)
def vehiculo__v_i_n_get(
    vin:str=Path(..., regex=r'[A-HJ-NPR-Z0-9]{17}')
) -> Union[vehiculos, HTTPProblem]:
    """
    Obtiene un vehiculo identificado por `vehiculoVINId`
    """
    return VehiculosService().get_vehiculos_by_vin(vin)


@app.delete(
    '/vehiculos/vin/{vin}',
    response_model=None,
    responses={'404': {'model': HTTPProblem}, '422': {'model': HTTPProblem}},
    tags=['Vehiculo'],
)
def delete_vehiculos_vehiculo_v_i_n_id(
    vin: str=Path(..., regex=r'[A-HJ-NPR-Z0-9]{17}')
) -> Union[None, HTTPProblem]:
    """
    Elimina el vehiculo identificado por `vehiculoVINId`
    """
    VehiculosService().delete(vin)
    pass


@app.put(
    '/vehiculos/vin/{vehiculo_v_i_n_id}',
    response_model=None,
    responses={
        '209': {'model': Vehiculo},
        '404': {'model': HTTPProblem},
        '412': {'model': HTTPProblem},
        '422': {'model': HTTPProblem},
    },
    tags=['Vehiculo'],
)
def vehiculo__v_i_n_put(
    vehiculo_v_i_n_id: str=Path(..., regex=r'[A-HJ-NPR-Z0-9]{17}'),
    body: VehiculosVehiculoVINIdPutRequest = ...,
) -> Union[None, Vehiculo, HTTPProblem]:
    """
    Modifica el vehiculo identificado por `vehiculoVINId`.
    """
    VehiculosService().put(body, vehiculo_v_i_n_id)
    pass
