import ipaddress

outfile = open('outfile.txt','w+')

with open('infile.txt', 'r') as f:
      for line in f:
        netIpv4Address = ipaddress.ip_network(str.strip(line))
        for i in netIpv4Address: 
            outfile.write(str(i))
            outfile.write('\n')
outfile.close()
