import azure.functions as func
from .. helpers.plaidconnector import get_liabilities


def main(req: func.HttpRequest, qmsg: func.Out[func.QueueMessage], emsg: func.Out[str]) -> str:

    access_token = req.params.get('access_token')
   
    if not access_token:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            access_token = req_body.get('access_token')

    if access_token:
        qmsg.set(access_token)
        emsg.set(access_token)
        plaid_response = get_liabilities(access_token)
        return func.HttpResponse(f"{plaid_response}")
    else:
        return func.HttpResponse(
            "Please provide a valid access token in the query string or in the request body",
            status_code=400
        )
