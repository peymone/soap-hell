<h1 align="center">SOAP Tutorial Hell</h1>

<p align="center">
    <img src="https://img.shields.io/badge/%20Python-3.11.3-blue?style=for-the-badge&logo=Python" alt="Python">
    <img src="https://img.shields.io/badge/%20SOAP-API-brightgreen?style=for-the-badge" alt="SOAP">
    <img src="https://img.shields.io/badge/%20Spyne-2.14.0-brightgreen?style=for-the-badge" alt="Spyne">
</p>

<p align="center">
    <img src="https://img.shields.io/github/downloads/peymone/soap-hell/total?style=social&logo=github" alt="downloads">
    <img src="https://img.shields.io/github/watchers/peymone/soap-hell" alt="watchers">
    <img src="https://img.shields.io/github/stars/peymone/soap-hell" alt="stars">
</p>


<h1>About</h1>

**_This is a simple tutorial how to build SOAP API without anything. I wanted to do something cool and add WS-Security, but I'm sick of this protocol. Sorry_**

<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExODVjaWt4ZG41ZWdtb2FzZzhnZjM3bjY3c2RkNjc5ZnJlajA2eHJjNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2wYrkKvETbAwWAM4Gy/giphy.gif" width="300px" height="170x"><br/>

> __Use SOAP when you care about security and reliability of data transfer. Seriously, bother with security__

<h1>Delpoy this shit</h1>

- _Save project release to your machine_
- _Open terminal from project root folder_
- _Install dependencies: ```pip install -r requirements.txt```_
- _Run API: ```python app/api.py```_


_**You can call API from Postman or whatever you want (Postman request below)**_

- _Make post request to http://localhost:8000_
- _Write Body (raw XML):_

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

__Done.__