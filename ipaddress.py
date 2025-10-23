# 1. Classe de IP Address


class IPAddress:
    ipv4: str
    mask: str
    rede: str
    broadcast: str

    def __init__(self, ipv4: str, mask: str):
        self.ipv4 = ipv4
        self.mask = mask
        self.rede = self.calcular_rede(self.ipv4, self.mask)
        self.broadcast = self.calcular_broadcast(self.rede, self.mask)

    def __str__(self) -> str:
        return f"{self.ipv4}/{self.bits_da_mask(self.mask)}"

    def calcular_rede(self, ipv4: str, mask: str) -> str:
        ip = ipv4.split(".")
        m = mask.split(".")
        rede = ""
        for i in range(len(ip)):
            # op AND para calcular
            r = int(ip[i]) & int(m[i])
            if i > 0:
                rede += "." + str(r)
            else:
                rede += str(r)
        return rede

    def calcular_broadcast(self, rede: str, mask: str) -> str:
        r = rede.split(".")
        m = mask.split(".")
        broadcast = ""

        for i in range(len(m)):
            # op XOR para inverter os bits, op OR para calcular
            x = int(m[i]) ^ 255
            b = int(r[i]) | x
            if i > 0:
                broadcast += "." + str(b)
            else:
                broadcast += str(b)
        return broadcast

    def pertence_a_rede(self, ip: str) -> bool:
        rede = self.calcular_rede(ip, self.mask)
        if rede == self.rede:
            return True
        return False

    def bits_da_mask(self, mask: str):
        # transforma mask em bin e conta os 1s
        m = mask.split(".")
        m_bin = ""
        for i in range(len(m)):
            b = format(int(m[i]), "08b")
            m_bin += b
        bits = 0
        for b in m_bin:
            if b == "1":
                bits += 1
        return str(bits)


# Testes
ip = IPAddress("192.168.1.10", "255.255.255.0")
print(ip)  # Saída esperada: "192.168.1.10/24"
print(ip.rede)  # "192.168.1.0"
print(ip.broadcast)  # "192.168.1.255"
print(ip.pertence_a_rede("192.168.1.55"))  # True
print(ip.pertence_a_rede("192.168.2.1"))  # False
print("-" * 50)

ip2 = IPAddress("172.16.50.10", "255.255.0.0")
print(ip2.rede)
print(ip2.broadcast)
print(ip2.pertence_a_rede("172.16.250.1"))
print(ip2.pertence_a_rede("172.17.1.1"))
print("-" * 50)

ip3 = IPAddress("192.168.100.0", "255.255.255.0")
print(ip3.rede)
print(ip3.broadcast)
print(ip3.pertence_a_rede("192.168.100.0"))
print(ip3.pertence_a_rede("192.168.100.254"))
print("-" * 50)
