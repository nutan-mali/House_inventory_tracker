# House Inventory Management System

This Django project is designed to manage houses, rooms, and equipment inventory. Users can define houses, add rooms to houses, and assign equipment to rooms along with maintenance details.

# Setup Instructions

Clone the repository:  git clone https://github.com/yourusername/house_inventory.git

Install dependencies:  cd house_inventory
pip install -r requirements.txt

Run migrations: python manage.py migrate


Create a superuser (admin) to access the admin panel:  python manage.py createsuperuser


Start the development server:   python manage.py runserver


Access the application at http://localhost:8000/ in your web browser.

# Check URLs :

 http://localhost:8000/
   http://localhost:8000/'login/
   
   http://localhost:8000/'logout/

   
   http://localhost:8000/house/
   http://localhost:8000/house_list/
   
   http://localhost:8000/create_room/
   
  http://localhost:8000/room_report/<int:house_pk>/
    
  http://localhost:8000/maintenance_report/


# Directory Structure

house_inventory/: Main project directory.

house_app/: Django app for managing houses, rooms, and equipment.

models.py: Contains models for House, Room, and Equipment.

views.py: Includes views for creating, listing, and managing houses, rooms, and equipment.

forms.py: Django forms for creating and editing house, room, and equipment details.

templates/: HTML templates for user interface.

admin.py: Admin panel configurations.

static/: Static files like CSS, JavaScript, images, etc.

requirements.txt: Lists project dependencies.

README.md: This file.



