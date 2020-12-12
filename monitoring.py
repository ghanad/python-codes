#!/usr/bin/python3
from easysnmp import Session
import sqlite3 as sq
import time

seession = Session('localhost', version=2)

class SnmpUtil:
    def __init__(self,host):
        self.host = host
        self.con = self._setup()
    
    def _setup(self):
        return Session(self.host, version=2)

    def network(self, *interface):
        snmp_result = self.con.walk('.1.3.6.1.2.1.31.1.1.1')
        oid_name_list = [x.oid for x in snmp_result if x.value in interface]
        oid_index_list = [x.split('.')[-1] for x in oid_name_list]
        base_oid = oid_name_list[0][:-4]

        # Name
        ifName_oid = ['{}.1.{}'.format(base_oid,x) for x in oid_index_list]
        ifName_value = [x.value for x in snmp_result if x.oid in ifName_oid]

        # Input octetc
        ifHCInOctets_oid = ['{}.6.{}'.format(base_oid,x) for x in oid_index_list]
        ifHCInOctets_value = [int(x.value) for x in snmp_result if x.oid in ifHCInOctets_oid]

        # Output Octet
        ifHCOutOctets_oid = ['{}.10.{}'.format(base_oid,x) for x in oid_index_list]
        ifHCOutOctets_value = [int(x.value) for x in snmp_result if x.oid in ifHCOutOctets_oid]
        
        return [[ifName_value[x], ifHCInOctets_value[x], ifHCOutOctets_value[x]] for x in range(len(ifHCOutOctets_value))]


class DataBase:
    def __init__(self, table='monitoring', dfName='monitoring.db'):
        self.dfName = dfName
        self.con = self._setup()
        self.table = table
    
    def _setup(self):
        return sq.connect(self.dfName)

    def create_table(self):
        q = ''' create table if not exists {} (
            id INTEGER primary key autoincrement,
            ip TEXT,
            time INTEGER,
            net1_in INTEGER,
            net1_out INTEGER
        )
        '''.format(self.table)

        self.con.execute(q)

    def get_columns(self):
        cursor = self.con.execute('select * from {} limit 1'.format(self.table))
        return [x[0] for x in cursor.description]

    def insert(self, ip, network):
        # network [['eth0', 1020, 2030]]
        net = network[0][1:]
        timer = time.time()
        q = '''
        insert into {} (ip, time, net1_in, net1_out) values (?,?,?,?)
        '''.format(self.table)
        
        item_list = [ip, timer] + net

        self.con.execute(q, item_list)
        self.con.commit()

    def fetch(self):
        q = '''
        select * from {}
        '''.format(self.table)
        res = self.con.execute(q)
        for i in res:
            print(i)

net = SnmpUtil('127.0.0.1').network('eth0')
a = DataBase()
# a.create_table()
# a.insert('10.0.0.2', net)
a.fetch()