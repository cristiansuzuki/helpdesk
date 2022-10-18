from tkinter import N
from django.urls import path
from .views import home, buttons, cards, login, register, forgot_password, error_404, blank, tables

urlpatterns = [
    path('', home, name='home'),
    path('buttons', buttons, name='buttons'),
    path('cards', cards, name='cards'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('forgot-password', forgot_password, name='forgot-password'),
    path('error_404', error_404, name='error_404'),
    path('blank', blank, name='blank'),
    path('tables', tables, name='tables'),
]