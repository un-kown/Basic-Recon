mport dns.resolver

domain = input("Enter domain name: ")

try:
    print("\nA Record:")
    for a in dns.resolver.resolve(domain, 'A'):
        print(a)

    print("\nMX Record:")
    for mx in dns.resolver.resolve(domain, 'MX'):
        print(mx.exchange)

    print("\nNS Record:")
    for ns in dns.resolver.resolve(domain, 'NS'):
        print(ns)

except Exception as e:
    print("Error:", e)



