from fastapi import APIRouter, Path, Query
from asyncio import gather

from .converter import sync_converter, async_converter
from .schemas import ConverterSchema, ConverterSchemaOutput


router = APIRouter(prefix='/converter') # Prefixo usado na url antes dos parâmetros


# path parameter (/converter/{from_currency})
# query parameter (/converter?to_currencies=USD,EUR,GBP&price=5.55)

@router.get('/{from_currency}')
def converter(from_currency: str, to_currencies: str, price: float): 
    currencies = to_currencies.split(',')

    result = []

    for currency in currencies:
        response = sync_converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )
        result.append(response)

    return result

@router.get('/async/{from_currency}')
async def async_converter_router(
    # Validando entrada
    from_currency: str = Path(max_length=3, regex='^[A-Z]{3}$'), 
    to_currencies: str = Query(max_length=50, regex='^[A-Z]{3}(,[A-Z]{3})*$'), 
    price: float = Query(gt=0) # Valores maiores que zero
): 
    
    currencies = to_currencies.split(',')

    courotines = []

    for currency in currencies:
        # Sem o await a função não é executada, retorna apenas a coorotina. Instância da tarefa a ser executada.
        coro = async_converter( 
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )
        courotines.append(coro)

    # *courotines => Multiplos argumentos, nesse caso, objeto com multiplas corrotinas
    result = await gather(*courotines) 
    return result

@router.get('/async/v2/{from_currency}', response_model=ConverterSchemaOutput)
async def async_converterv2_router(
    # Validando entrada
    body: ConverterSchema,
    from_currency: str = Path(max_length=3, regex='^[A-Z]{3}$'), 
    ): 
    
    currencies = body.to_currencies
    price = body.price

    courotines = []

    for currency in currencies:
        # Sem o await a função não é executada, retorna apenas a coorotina. Instância da tarefa a ser executada.
        coro = async_converter( 
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )
        courotines.append(coro)

    # *courotines => Multiplos argumentos, nesse caso, objeto com multiplas corrotinas
    result = await gather(*courotines) 
    
            
    # Retornando em formato customizado 
    return ConverterSchemaOutput(
        message='Success',
        data=result
    )




