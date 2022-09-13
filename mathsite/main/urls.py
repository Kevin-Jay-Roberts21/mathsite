from django.urls import path
from . import views 

urlpatterns = [
	path("", views.home, name="home"),
	path("home/", views.home, name="home"),
	path("algebraHome/", views.algebra, name="algebra"),
	path("calculusHome/", views.calculus, name="calculus"),
	path("linearAlgebraHome/", views.linearAlgebra, name="linearAlgebra"),
	path("myClassesHome/", views.myClasses, name="myClasses"),
	path("linearAlgebraAndDifferentialEquationsClass/", views.linearAlgebraAndDifferentialEquationsClass, name="linearAlgebraAndDifferentialEquationsClass"),
	path("linearAlgebraClass/", views.linearAlgebraClass, name="linearAlgebraClass"),
	path("ordinaryDifferentialEquationsClass/", views.ordinaryDifferentialEquationsClass, name="ordinaryDifferentialEquationsClass"),
	path("calculus1Class/", views.calculus1Class, name="calculus1Class"),
	path("calculus2Class/", views.calculus2Class, name="calculus2Class"),
	path("calculus3Class/", views.calculus3Class, name="calculus3Class"),
	path("researchHome/", views.research, name="research"),
	path("examplesHome/", views.examples, name="examples"),
	path("searchHome/", views.search, name="search"),
]