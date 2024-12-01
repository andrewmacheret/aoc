#!/usr/bin/env python3
import browser_cookie3
import sys

domain_name = sys.argv[1]

# Uses Chrome's default cookies filepath by default
print('; '.join(k + '=' + v.value for k,v in browser_cookie3.chrome(domain_name=domain_name)._cookies['.' + domain_name]['/'].items()))
