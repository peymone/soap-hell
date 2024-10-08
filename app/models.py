from spyne.model.complex import ComplexModel
from spyne.model.primitive import Unicode, UnsignedInteger32, DateTime


class PaymentResponse(ComplexModel):
    acccount_name = Unicode
    account_number = UnsignedInteger32
    balance = UnsignedInteger32
    status = Unicode
    date = DateTime


class TestCall(ComplexModel):
    message = Unicode
    date = DateTime
