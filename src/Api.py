from modal import Secret, Stub, web_endpoint
from fastapi import Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import services.BracketFactory as bf
import services.TaxCalculator as tc
from App import App
stub = Stub("net_income_calculator")

auth_scheme = HTTPBearer()

app = App(bf.BracketFactory(), tc.TaxCalculator)
@stub.function(secret=Secret.from_name("web-auth-token"))
@web_endpoint()
def calculateNetIncome(gross_income: float, country: str, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> str:
    print(os.environ["WEB_AUTH"])

    if token.credentials != os.environ["WEB_AUTH"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect bearer token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    try:
        response = app.getNetIncome(gross_income, country)
    except:
        return str(sys.exc_info()[1])
    
    return response