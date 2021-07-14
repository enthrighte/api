import azure.functions as func
from .. helpers.plaidconnector import get_transactions


def main(req: func.HttpRequest, msg: func.Out[func.QueueMessage]) -> str:

    access_token = req.params.get('access_token')
   
    if not access_token:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            access_token = req_body.get('access_token')

    if access_token:
        msg.set(access_token)
        plaid_response = get_transactions(access_token)
        return func.HttpResponse(f"{plaid_response}")
    else:
        return func.HttpResponse(
            "Please provide a valid access token in the query string or in the request body",
            status_code=400
        )
