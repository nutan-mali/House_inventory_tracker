from django.shortcuts import render,HttpResponse,redirect,HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import RoomCreateForm, HouseCreateForm
from .models import House, Room

# Create your views here.

def SignupPage(request):
    if request.method=='POST':
        # Extract data from the POST request
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
             # Create a new user and save it to the database
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        # Extract data from the POST request
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        # Authenticate the user
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            print("Curren LogIn User Is ",user)
            # Login the user and redirect to the home page (Here 'house' is the home page)
            return redirect('house')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def house(request):
    if request.method == 'POST':
        # Process form submission for creating a new hous
        data = HouseCreateForm(request.POST)
        if data.is_valid(): 
            # Assign the current user to the house instance and save
            data.instance.user = request.user
            data.save()
            print("Data Save Successfully")
            # Redirect to the house list page after successful creation
            return redirect('house_list')
    else:
        # Display an empty form for creating a new house
        data = HouseCreateForm()
    return render(request, 'house_create.html', {'form': data})


def house_list(request):
    data_list = House.objects.filter(user=request.user)
    return render(request, 'house_list.html', {'data_list': data_list})



@login_required(login_url='login')
def room(request):
    # Initialize the room creation form
    form = RoomCreateForm()
    # Get the initial list of rooms associated with the current user
    rooms = Room.objects.filter(user=request.user)  # Initial list of rooms to display
    if request.method == 'POST':
         # Process form submission for creating a new room
        data = RoomCreateForm(request.POST)
        print(request.POST)
        if data.is_valid():
            print(data.errors)
            print("validation testing")
            # Assign the current user to the room instance and save
            data.instance.user = request.user
            print("current Login User is ",request.user)
            data.save()
            print("data save")
             # Update the rooms list to include the newly created room
            rooms = Room.objects.all() 
           
            return render(request, 'room_create.html', {'form': form, 'rooms': rooms})
        else:
            print("Form has errors:", data.errors)
            return redirect('room')
    return render(request, 'room_create.html', {'form': form, 'rooms': rooms})
    


def room_report(request, house_id): # room report 30 test for Nutan Mali
    # Get the house object or return 404 if not found
    house = get_object_or_404(House, id=house_id, user=request.user)

    # Get all rooms for the house
    rooms = Room.objects.filter(house=house)

    # Fetch equipment for each room using related managers
    for room in rooms:
        print("rooms print")
        # room.equipment_name has  "AC, Refrigerator, TV"  then it will store list like this ["AC", "Refrigerator", "TV"]
        room.equipment_list = room.equipment_name.split(",")  # Assuming equipment_name is a comma-separated list
        print(room.equipment_name)
        print(room.purchase_date)
        print(room.equipment_list)
        
    return render(request, 'room_report.html', {'house': house, 
                    'rooms': rooms})


def maintenance_report(request):
    if request.method == 'POST':
        # Get the start date and end date from the form data
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        # Validate the start date and end date here if needed

        # Query the Room model to get equipment within the specified date range
        equipment_list = Room.objects.filter(maintenance_date__range=[start_date, end_date])

        # Pass the equipment list to the template for rendering
        context = {'equipment_list': equipment_list, 'start_date': start_date, 'end_date': end_date}
        return render(request, 'maintenance_report.html', context)
    else:
        # If the request method is not POST, render the input form template
        return render(request, 'maintenance_input_form.html')
