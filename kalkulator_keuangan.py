#!/usr/bin/python

"""Kalkulator keuangan
Menghitung:
    1. NPV
    2. ROI
    3. IRR
    4. Payback Period
"""

import sys

print
print '**********************************************'
print 'Selamat datang di Program Kalkulator Keuangan'
print '**********************************************'
print


while True:
    print
    print 'Anda ingin menghitung apa?'
    print '1. NPV'
    print '2. ROI'
    print '3. IRR'
    print '4. Payback Period'
    print

    jk_waktu = input('Masukkan jangka waktu yang ingin Anda hitung: ')
    net_cash_flow = input('Masukkan net cash flow (comma separated): ')
    discount_rate = input('Masukkan discount rate: ')

    if type(net_cash_flow) == int:
        npv = net_cash_flow / (1 + discount_rate) ** jk_waktu
    elif type(net_cash_flow) == tuple:
        npv = sum(net_cash_flow) / (1 + discount_rate) ** jk_waktu

    print
    print 'Nilai NPV Anda adalah %.2f' % npv
    print

    opsi = raw_input('Apakah Anda ingin menghitung lagi? (Ya/Tidak)')

    if opsi == 'Ya':
        continue
    else:
        break
