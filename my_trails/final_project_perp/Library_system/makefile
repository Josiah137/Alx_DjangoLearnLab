# make_all:
# 	python manage.py makemigrations
# 	python manage.py migrate
# 	python manage.py runserver

# mmnm:
# 	python manage.py makemigrations
# 	python manage.py migrate
# pmrs:
# 	"python manage.py runserver"

.PHONY: all mmnm runserver  

# Default target, which can run migrations and start the server  
all: mmnm runserver  

# Target for making and applying migrations  
mmnm:  
	@echo "Making migrations..."  
	python manage.py makemigrations  
	@echo "Applying migrations..."  
	python manage.py migrate  

# Target for running the Django development server  
runserver:  
	@echo "Starting the server..."  
	python manage.py runserver