# Third party
from spyne.model.primitive import Unicode, UnsignedInteger32
from spyne import Application, ServiceBase, rpc
from spyne.server.wsgi import WsgiApplication
from spyne.protocol.soap import Soap11

# BuildIn
from datetime import datetime
from datetime import timezone

# My modules
from models import PaymentResponse, TestCall


fake_accounts_db = dict()


class BankAPI(ServiceBase):
    """Simulation of the work of the banking API.
    Don't use this code in real projects or you're screwed"""

    @rpc(_returns=TestCall)
    def test_api_call(ctx):
        """Make test API call"""

        return TestCall(message="API is called successfully", date=datetime.now(timezone.utc))

    @rpc(Unicode, UnsignedInteger32, UnsignedInteger32, _returns=PaymentResponse)
    def payment(ctx, name, account, funds):
        """Receiving funds to a bank account"""

        account_data = fake_accounts_db.get((name, account))

        if account_data is None:
            fake_accounts_db[(name, account)] = funds
        else:
            fake_accounts_db[(name, account)] += funds

        return PaymentResponse(
            acccount_name=name,
            account_number=account,
            balance=fake_accounts_db[(name, account)],
            status="Paid",
            date=datetime.now(timezone.utc)
        )


# Setup SOAP application
app = Application([BankAPI], tns='api.payment_service', in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())
application = WsgiApplication(app)

if __name__ == '__main__':
    # Run server
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8000, application)
    server.serve_forever()
