#!/usr/bin/python3.7


import os
import pyfiglet
import dns
from dns import resolver
import dns.resolver
import copy
from termcolor import colored


def dnslookup(a):

# ------------ IP (A) -----------------

    result = dns.resolver.query(a, 'A')
    for ipval in result:
        print (colored('\nIP : ', 'cyan', attrs=['bold']),ipval)

# ------------ CNAME -----------------

    try:
        cname = dns.resolver.query('mail.' + a, 'CNAME')
        print(colored('\n*****CNAME RECORD*****\n', 'cyan', attrs=['bold']))
        for cnameval in cname:
            print('Cname target address : '+ cnameval.target)
    except:
        print( colored('\n[', 'red') + '-' + \
            colored('] NO CNAME RECORD FOUND!!!!\n', 'red'))

# ------------ MX RECORD -----------------

    try:
        mx = dns.resolver.query(a, 'MX')
        print(colored('\n*****MAIL EXCHANGER RECORD*****\n',
                      'cyan', attrs=['bold']))
        for i in mx.response.answer:
            for j in i.items:
                print ('MX record : ', j.to_text())
    except:
        print (colored('\n[', 'red') + '-' + \
            colored('] NO MX RECORD FOUND!!!!\n', 'red'))

# ------------ NS RECORD -----------------

    try:
        ns = dns.resolver.query(a, 'NS')
        print(colored('\n*****NAME SERVER RECORD*****\n',
                      'cyan', attrs=['bold']))
        for i in ns.response.answer:
            for j in i.items:
                print ('NS record : ', j.to_text())
    except:
        print (colored('\n[', 'red') + '-' + \
            colored('] NO NS RECORD FOUND!!!!\n', 'red'))

# ------------ TXT RECORD -----------------

    try:
        txt = dns.resolver.query(a, 'TXT')
        print(colored('\n*****TXT RECORD*****\n', 'cyan', attrs=['bold']))
        for i in txt.response.answer:
            for j in i.items:
                print('TXT record :', j.to_text())
    except:
        print (colored('\n[', 'red') + '-' + \
            colored('] NO TXT RECORD FOUND!!!!\n', 'red'))

# ------------ SOA RECORD -----------------

    try:
        answers = dns.resolver.query(a, 'SOA')
        print(colored('\n*****SOA RECORD*****\n', 'cyan', attrs=['bold']))
        print('query qname:', answers.qname, ' num ans.', len(answers))
        for rdata in answers:
            print('serial     : %s  tech: %s' % (rdata.serial, rdata.rname))
            print('refresh    : %s        retry: %s' % (
                rdata.refresh, rdata.retry))
            print ('expire     : %s       minimum: %s' % (
                rdata.expire, rdata.minimum))
            print('mname      : %s' % (rdata.mname))
    except:
        print (colored('\n[', 'red') + '-' + \
            colored('] NO SOA RECORD FOUND!!!!\n', 'red'))

# ------------ PTR RECORD -----------------

    try:

        ip = str(ipval)
        req = '.'.join(reversed(ip.split("."))) + ".in-addr.arpa"
        myAnswers = dns.resolver.query(req, "PTR")
        print(colored('\n*****PTR RECORD*****\n', 'cyan', attrs=['bold']))

        for exdata in myAnswers:
            print('PTR Record :', exdata)
    except:
        print (colored('\n[', 'red') + '-' + \
            colored('] NO PTR RECORD FOUND!!!!\n', 'red'))
