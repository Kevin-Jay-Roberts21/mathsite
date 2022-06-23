from django.urls import path
from . import views 

urlpatterns = [
	path("", views.home, name="home"),
	path("home/", views.home, name="home"),
	path("algebraHome/", views.algebra, name="algebra"),
	path("calculusHome/", views.calculus, name="calculus"),
	path("linearAlgebraHome/", views.linearAlgebra, name="linearAlgebra"),
	path("myClassesHome/", views.myClasses, name="myClasses"),
	path("ordinaryDifferentialEquations/", views.ordinaryDifferentialEquations, name="ordinaryDifferentialEquations"),
	path("researchHome/", views.research, name="research"),
	path("examplesHome/", views.examples, name="examples"),
	path("searchHome/", views.search, name="search"),
]