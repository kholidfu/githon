#!/usr/bin/python
# @sopier
# September 2012

import pynotify
import urllib
import re


class AmbilKurs(object):
    """
    Modul sederhana untuk menampilkan notifikasi kurs valas
    pada desktop Ubuntu.

    Penggunaan:
    $ python notifikasi_kurs.py
    """

    def raw_kurs_bca(self):
        html = urllib.urlopen('http://www.klikbca.com').read()
        kurs_data1 = re.findall(re.compile(r"bgcolor=\"#dcdcdc\">\s?(\d+\.\d+)</td>"), html)
        kurs_data2 = re.findall(re.compile(r"bgcolor=\"#f0f0f0\">\s?(\d+\.\d+)</td>"), html)
        return kurs_data1, kurs_data2

    def dollar_rupiah(self):
        kurs_jual = self.raw_kurs_bca()[0][0]
        kurs_beli = self.raw_kurs_bca()[0][1]
        return kurs_jual + ' // ' + kurs_beli

    def sgd_rupiah(self):
        kurs_jual = self.raw_kurs_bca()[1][0]
        kurs_beli = self.raw_kurs_bca()[1][1]
        return kurs_jual + ' // ' + kurs_beli
        
    def hkd_rupiah(self):
        kurs_jual = self.raw_kurs_bca()[0][2]
        kurs_beli = self.raw_kurs_bca()[0][3]
        return kurs_jual + ' // ' + kurs_beli

    def chf_rupiah(self):
        kurs_jual = self.raw_kurs_bca()[1][2]
        kurs_beli = self.raw_kurs_bca()[1][3]
        return kurs_jual + ' // ' + kurs_beli


if __name__ == '__main__':
    a = AmbilKurs()
    pynotify.init("Kurs USD to IDR")
    title = "Kurs BCA Hari ini (Jual // Beli)"
    n = pynotify.Notification(title, 
            '======================\n'
            'USD\t' + a.dollar_rupiah() +
            '\nSGD\t' + a.sgd_rupiah() +
            '\nHKD\t' + a.hkd_rupiah() +
            '\nCHF\t' + a.chf_rupiah())
    n.show()
