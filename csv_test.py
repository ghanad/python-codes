#!/usr/bin/python3
import csv


class Stats:
    def __init__(self, fileName='test.csv'):
        self.fileName = fileName

    def get_headers(self):
        with open(self.fileName) as f:
            reader = csv.reader(f)
            i = next(reader)
            return i

    def update(self, **column):
        # open file
        csv_obj = open(self.fileName)
        csv_read = csv.DictReader(csv_obj)
        header = csv_read.fieldnames

        tmp_list =list()
        items = iter(column.keys())
        col = next(items)
        new_item = next(items)
        for i in csv_read:
            if i[col] == column[col]:
                i[new_item] = column[new_item]
            tmp_list.append(i)
        csv_obj.close()
        self._save(tmp_list, header, mode='w')

    def _save(self, lst, header, mode):
        with open(self.fileName, mode) as c:
            writer = csv.DictWriter(c, fieldnames=header)
            if mode == 'w':
                writer.writeheader()
            writer.writerows(lst)

    def inserte_row(self, **items):
        header = self.get_headers()
        self._save([items], header, mode='a')
            
    def insert_many(slef, dict_list):
        pass

    def get_column(self, col):
        pass

a = Stats()
a.inserte_row(name='ali3', table='nemp')
# b = a.update(name='ali', table='test20')
