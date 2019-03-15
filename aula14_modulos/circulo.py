#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#circulo.py

pi=3.14159

def area(raio):
    return pi*(raio**2)

def circunferencia(raio):
    return 2*pi*raio

def superficieEsfera(raio):
    return 4.0*area(raio)

def volumeEsfera(raio):
    return (4.0/3.0)*pi*(raio**3)

