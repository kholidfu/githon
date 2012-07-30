#!/usr/bin/python

"""Kalkulator keuangan
Menghitung:
    1. ROI
    2. Break-even Analysis
    3. Tingkat Pengembalian Saham
    NPV
    4. dan seterusnya...


"""

print
print '**********************************************'
print 'Selamat datang di Program Kalkulator Keuangan'
print '**********************************************'

print
print 'Anda ingin menghitung apa?'
print '1. NPV'

jk_waktu = input('Masukkan jangka waktu yang ingin Anda hitung: ')
net_cash_flow = input('Masukkan net cash flow (comma separated): ')
discount_rate = input('Masukkan discount rate: ')

if type(net_cash_flow) == int:
    npv = net_cash_flow / (1 + discount_rate) ** jk_waktu
elif type(net_cash_flow) == tuple:
    npv = sum(net_cash_flow) / (1 + discount_rate) ** jk_waktu

print 'NPV', npv
