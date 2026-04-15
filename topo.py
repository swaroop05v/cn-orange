from mininet.topo import Topo

class MyTopo(Topo):
    def build(self):
        # Create switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # Create hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')

        # Connect hosts to switches
        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s3)

        # Connect switches (linear chain)
        self.addLink(s1, s2)
        self.addLink(s2, s3)


# This is required to run topology from command line
topos = {'mytopo': (lambda: MyTopo())}
