
# API documentation -  maisTodos CardCredit 
This is the documentation for the Mais Todos Credit Card project

# Basic structure
![Basic Structure](/doc/structure.png "Estrutura Basica")


# Summary

1. [Endpoint List](#1-Endpoint-List)

2. [Environment Preparation](#2-Environment-Preparation)

3. [Contact](#3-Contact)



# 1. Endpoints List
    

    | description             |   route                                            |
    |-------------------------|----------------------------------------------------|
    |  DOC (Swagger)          |  http://localhost:8000/docs                        |
    |-------------------------|----------------------------------------------------|
    |  Get all cards          |  GET http://localhost:8000/api/v1/credit-card      |
    |-------------------------|----------------------------------------------------|
    |  Get one card by id     |  GET http://localhost:8000/api/v1/credit-card/{id} |
    |-------------------------|----------------------------------------------------|
    |  Create a new card      |  POST http://localhost:8000/api/v1/credit-card     |

    All credit-card routes require a Bearer token, use this token in the header
    
       Bearer bdf49c3c3882102fc017ffb661108c63a836d065888a4093994398cc55c2ea2f
    

# 2. Environment Preparation
### Via Local 
1. Clone the api repository:
    ```shell
    git clone https://github.com/lucastavaresn/credit-card.git
    ```

2. Create Virtual Env:
    > **_NOTE:_** Install Poetry (tool for dependency packaging and environment)
    ```shell
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. install the dependencies:
   > **_NOTE:_** active the virtualenv: poetry shell  
    ```shell
    poetry install
    ```

4. Configure environment variables:
    > **_NOTE:_** configure environment variables (poetry environment)
    ```shell
      export AUTH_HASH=bdf49c3c3882102fc017ffb661108c63a836d065888a4093994398cc55c2ea2f
      export CRYPTOGRAPHY_KEY=ZcpHACX8VWmhRpAkwB9d5TXWzGPwSRBWC4FzxM028Yc=
    ``

5. Run the application:
   - Run de make command
     ```shell
     make run
     ```

6. For running unit tests locally:
     ```shell
     make test
     ```


# 3. Contact

> Developer:
1. Lucas Tavares - lucastavaresn@gmail.com