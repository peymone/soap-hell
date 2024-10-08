<h1>About</h1>

What's is SOAP?

SOAP stands for Simple Object Access Protocol, as the name suggests nothing but a protocol for exchanging structured data between nodes. It uses XML instead of JSON.

Why you shoul use it?


You can call API with Postman

- Make post request to http://localhost:8000
- Write Body (raw XML):


```
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:api="api.payment_service" xmlns:models="models">
<soapenv:Header/>
<soapenv:Body>
    <api:payment>
        <api:name>Cassidy Bell</api:name>
        <api:account>10000</api:account>
        <api:funds>150000</api:funds>
    </api:payment>      
</soapenv:Body>
</soapenv:Envelope>
```