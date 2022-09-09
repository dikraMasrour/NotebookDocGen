import pycurl
from io import BytesIO

''''curl -X POST "${omlserver}/omlmod/v1/deployment/svm_mpg/score" \
--header "Authorization: Bearer ${token}" \
--header 'Content-Type: application/json' \
-d '{"inputRecords":[{
  "cylinders":4,
  "displacement":68,
  "horsepower":49,
  "weight":1867,
  "acceleration":19.5,
  "model_year":73,
  "brand":"fiat",
  "Country":"Europe"
}]}'''



b_obj = BytesIO()
crl = pycurl.Curl()
crl.setopt(crl.URL,'http://pvtlb.adbs-private.oraclevcn.com/omlmod/v1/deployment')
crl.setopt(crl.WRITEDATA, b_obj)
crl.perform()
crl.close()
get_body = b_obj.getvalue()
print('Output of GET request:\n%s' % get_body.decode('utf8'))