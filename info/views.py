from django.shortcuts import render

import logging
logger= logging.getLogger(__name__)

# Create your views here.
def home(request):
	logger.info('yuhhhhhhhh infooooo')
	return render(request,'info/home.html')

def covid(request):
	logger.info('yuhhhhhhhh infooooo')
	return render(request,'info/covid.html')	

def book(request):
	logger.info('yuhhhhhhhh infooooo')
	return render(request, 'info/book.html')	