from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from core.models.customer import Customer



class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['password']
        # form validation
        value = {
            'first_name' : first_name,
            'last_name' : last_name,
            'mobile' : mobile,
            'email' : email,
        }

        error_message = None

        reg = Customer(first_name=first_name, last_name=last_name,mobile=mobile,email=email,password=password)

        error_message = self.validateCustomer(reg) # call validationCustomer function 

        # saving part
        if not error_message:
            reg.password = make_password(reg.password)  # paword hassing 
            reg.save()
            return redirect("homepage")
        else:
            data = {
                'error' : error_message,
                'values' : value
            }
            return render(request, 'signup.html',data)

    def validateCustomer(self, reg):
        error_message = None
        if (not reg.first_name):
            error_message = "First Name Required"
        elif len(reg.first_name)<4:
            error_message = "FIrst Name must be 4 char long or more"
        elif not reg.last_name:
            error_message = "Last Name Required"
        elif len(reg.last_name)<4:
            error_message = "Last Name must be 4 char long or more"
        elif not reg.mobile:
            error_message = "Mobile Number Required"
        elif len(reg.mobile)<10:
            error_message = "Mobile Number must be 10 Digits long or more"
        elif not reg.email:
            error_message = "Email Required"
        elif len(reg.email)<6:
            error_message = "Last Name must be 6 char long or more"
        elif not reg.password:
            error_message = "Password Required"
        elif len(reg.password)<8:
            error_message = "Last Name must be 8 char long or more"
        elif reg.isExist():
            error_message = 'Email Address Already Registered'
        
        return error_message

