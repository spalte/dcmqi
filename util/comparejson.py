import json, sys
import jsoncompare

if len(sys.argv) != 3:
  sys.exit('Error')
json1 = json.loads(open(sys.argv[1],'r').read())
json2 = json.loads(open(sys.argv[2],'r').read())

(check,stack) = jsoncompare.are_same(json1,json2,
                                     ignore_list_order_recursively=True,
                                     ignore_missing_keys=True,
                                     ignore_value_of_keys=["@schema"])

if not check:
  print stack
  sys.exit(1)
