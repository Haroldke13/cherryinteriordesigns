from flask import Blueprint, render_template
import os
import requests
import base64
import json
from flask import Blueprint, render_template, flash, redirect, request, jsonify, url_for,session
from flask_login import login_required, current_user
from sqlalchemy import or_
from .models import Product, Cart, Order,Customer,Content,SalesLog,BillingDetail
from .forms import ShopItemsForm,OrderForm,ContentForm,CheckoutForm
from faker import Faker
from . import db
from datetime import datetime
from dotenv import load_dotenv
import logging
import random
from requests.auth import HTTPBasicAuth
from flask_wtf import FlaskForm


main = Blueprint("main", __name__)
from flask import render_template


"""
@main.route('/create_content', methods=['GET', 'POST'])
@login_required
def create_content():
    # Check if the user is an admin
    if current_user.email != 'admin@admin.com':
        flash('You are not authorized to access this page.', 'danger')
        return redirect(url_for('main.home'))  # Redirect to homepage or another page

    form = ContentForm()
    
    if form.validate_on_submit():
        # Handle the image file upload
        thumbnail = form.thumbnail.data
        thumbnail_filename = secure_filename(thumbnail.filename)
        thumbnail_path = os.path.join(current_app.config['UPLOAD_FOLDER'], thumbnail_filename)
        thumbnail.save(thumbnail_path)
        
        # Create new content entry
        content = Content(
            title=form.title.data,
            display=form.display.data,
            thumbnail=thumbnail_filename,  # Store only the filename in the database
            excerpt=form.excerpt.data,
            readmore_link=form.readmore_link.data
        )
        
        # Add to the database
        db.session.add(content)
        db.session.commit()
        flash('Content has been added!', 'success')
        return redirect(url_for('main.create_content'))  # Redirect to avoid form re-submission

    return render_template('create_content.html', form=form)

@main.route("/content", methods=["GET", "POST"])
@login_required
def content():
    # Handle the form submission for new content creation
    form = ContentForm()

    # Check if the form is validated and submitted
    if form.validate_on_submit():
        # Handle the image file upload
        thumbnail = form.thumbnail.data
        thumbnail_filename = secure_filename(thumbnail.filename)
        # Build the full filesystem path to save the file
        save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], thumbnail_filename)
        thumbnail.save(save_path)
        
        # Create a new content entry (store only the filename)
        new_content = Content(
            title=form.title.data,
            display=form.display.data,
            thumbnail=thumbnail_filename,  # Store only the filename!
            excerpt=form.excerpt.data,
            readmore_link=form.readmore_link.data
        )
        
        db.session.add(new_content)
        db.session.commit()
        flash('Content has been added!', 'success')
        return redirect(url_for('main.content'))  # Redirect to avoid form re-submission

    # Get the search query if any
    search_query = request.args.get('search', '')

    # Search logic: if a search query is provided, filter content by title or excerpt
    if search_query:
        content_lists = Content.query.filter(
            (Content.title.ilike(f'%{search_query}%')) | 
            (Content.excerpt.ilike(f'%{search_query}%'))
        ).all()
    else:
        content_lists = Content.query.all()

    # Get recent posts: limit to the last 5 posts
    recent_posts = Content.query.order_by(Content.date_added.desc()).limit(5).all()

    # Ensure each item gets its image URL for display
    for content in content_lists:
        content.thumbnail_url = url_for('main.blog_images', filename=content.thumbnail)

    return render_template('content.html', form=form, content_lists=content_lists, recent_posts=recent_posts)

@main.route('/create_content', methods=['GET', 'POST'])
@login_required
def create_content():
    # Check if the user is an admin
    if current_user.email != 'admin@admin.com':
        flash('You are not authorized to access this page.', 'danger')
        return redirect(url_for('main.home'))  # Redirect to homepage or another page

    form = ContentForm()
    
    if request.method=="POST" and form.validate_on_submit():
        # Handle the image file upload
        thumbnail = form.thumbnail.data
        thumbnail_filename = secure_filename(thumbnail.filename)
        thumbnail_path = os.path.join(current_app.config['UPLOAD_FOLDER'], thumbnail_filename)
        thumbnail.save(thumbnail_path)
        
        # Create new content entry
        content = Content(
            title= request.form.get("title"),
            display= request.form.get("display"),
            thumbnail= request.form.get("thumbnail"),  # Store only the filename in the database
            excerpt= request.form.get("excerpt")
        )
        
        # Add to the database
        db.session.add(content)
        db.session.commit()
        flash('Content has been added!', 'success')
        return redirect(url_for('main.create_content'))  # Redirect to avoid form re-submission

    return render_template('create_content.html', form=form)

"""

@main.route('/create_content', methods=['GET', 'POST'])
@login_required
def create_content():
    # Check if the user is an admin
    if current_user.email != 'admin@admin.com':
        flash('You are not authorized to access this page.', 'danger')
        return redirect(url_for('main.home'))  # Redirect to homepage or another page

    form = ContentForm()
    
    if form.validate_on_submit():
        # Handle the image file upload
        thumbnail = form.thumbnail.data
        thumbnail_filename = secure_filename(thumbnail.filename)
        thumbnail_path = os.path.join(current_app.config['UPLOAD_FOLDER'], thumbnail_filename)
        thumbnail.save(thumbnail_path)
        
        # Create new content entry
        content = Content(
            title=form.title.data,
            display=form.display.data,
            thumbnail=thumbnail_filename,  # Store only the filename in the database
            excerpt=form.excerpt.data
        )
        
        # Add to the database
        db.session.add(content)
        db.session.commit()
        flash('Content has been added!', 'success')
        return redirect(url_for('main.create_content'))  # Redirect to avoid form re-submission

    return render_template('create_content.html', form=form)

@main.route("/content", methods=["GET", "POST"])
@login_required
def content():
    # Handle the form submission for new content creation
    form = ContentForm()

    # Check if the form is validated and submitted
    if form.validate_on_submit():
        # Handle the image file upload
        thumbnail = form.thumbnail.data
        thumbnail_filename = secure_filename(thumbnail.filename)
        # Build the full filesystem path to save the file
        save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], thumbnail_filename)
        thumbnail.save(save_path)
        
        # Create a new content entry (store only the filename)
        new_content = Content(
            title=form.title.data,
            display=form.display.data,
            thumbnail=thumbnail_filename,  # Store only the filename!
            excerpt=form.excerpt.data,
        )
        
        db.session.add(new_content)
        db.session.commit()
        flash('Content has been added!', 'success')
        return redirect(url_for('main.content'))  # Redirect to avoid form re-submission

    # Get the search query if any
    search_query = request.args.get('search', '')

    # Search logic: if a search query is provided, filter content by title or excerpt
    if search_query:
        content_lists = Content.query.filter(
            (Content.title.ilike(f'%{search_query}%')) | 
            (Content.excerpt.ilike(f'%{search_query}%'))
        ).all()
    else:
        content_lists = Content.query.all()

    # Get recent posts: limit to the last 5 posts
    recent_posts = Content.query.order_by(Content.date_added.desc()).limit(5).all()

    # Ensure each item gets its image URL for display
    for content in content_lists:
        content.thumbnail_url = url_for('main.blog_images', filename=content.thumbnail)

    return render_template('content.html', form=form, content_lists=content_lists, recent_posts=recent_posts)






@main.route('/delete_content/<int:content_id>', methods=['POST'])
@login_required
def delete_content(content_id):
    # Check if the user is an admin
    if current_user.email != 'admin@admin.com':
        flash('You are not authorized to perform this action.', 'danger')
        return redirect(url_for('main.content'))  # Redirect back to the content page

    # Find the content by ID
    content = Content.query.get_or_404(content_id)

    # Delete the associated image file from the server
    try:
        if content.thumbnail:
            # Generate the full file path for the thumbnail
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], content.thumbnail)
            if os.path.exists(file_path):
                os.remove(file_path)  # Remove the file from the filesystem
    except Exception as e:
        flash(f'Error removing thumbnail: {e}', 'danger')

    # Delete the content from the database
    db.session.delete(content)
    db.session.commit()

    flash('Content has been deleted!', 'success')
    return redirect(url_for('main.content'))  # Redirect back to the content page



@main.route('/blog/<int:content_id>')
def blog_details(content_id):
    content_item = Content.query.get_or_404(content_id)
    return render_template('blog_details.html', content=content_item)

#============================================================================
# At the top of routes.py, import:
from flask import make_response
from weasyprint import HTML

@main.route('/profile/sales-report')
@login_required
def profile_sales_report():
    # Get sales events for the current user (both add_to_cart and payment)
    logs = SalesLog.query.filter_by(customer_id=current_user.id).order_by(SalesLog.timestamp.desc()).all()
    
    # Check if a 'download' query parameter is present
    if request.args.get("download"):
        rendered = render_template("sales_report_pdf.html", logs=logs, customer=current_user)
        pdf = HTML(string=rendered, base_url=request.base_url).write_pdf()
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename=sales_report.pdf'
        return response
    
    # Otherwise display HTML report
    return render_template("sales_report.html", logs=logs, customer=current_user)


@main.route('/admin/sales-report')
@login_required
def admin_sales_report():
    # Restrict access to admin (example check using email)
    if current_user.email != 'admin@admin.com':
        flash("Not authorized", "danger")
        return redirect(url_for('main.home'))
    
    logs = SalesLog.query.order_by(SalesLog.timestamp.desc()).all()
    return render_template("admin_sales_report.html", logs=logs)



@main.route("/about")
def about():
    return render_template("about.html")



@main.route("/about1")
def about1():
    return render_template("about1.html")


@main.route("/the-greenzone-apartments")
def the_greenzone_apartments():
    return render_template("the-greenzone-apartments.html")


@main.route("/krishna-pride-apartments")
def krishna_pride_apartments():
    return render_template("krishna-pride-apartments.html")

@main.route("/azalea-heights")
def azalea_heights():
    return render_template("azalea-heights.html")

@main.route("/diamond-park-ii-estate-in-south-b")
def diamond_park_ii_state_in_south_b():
    return render_template("diamond-park-ii-estate-in-south-b.html")

@main.route("/fairvalley-heights")
def fairvalley_heights():
    return render_template("fairvalley-heights.html")
#=====================================================================

@main.route("/wardrobes")
def wardrobes():
    return render_template("wardrobes.html")





@main.route("/kitchen-fittings")
def kitchen_fittings():
    return render_template("kitchen-fittings.html")



@main.route("/doors")
def doors():
    return render_template("doors.html")



@main.route("/frames")
def frames():
    return render_template("frames.html")




@main.route("/videos")
def videos():
    return render_template("videos.html")






@main.route("/pvc-foil-wrap-services")
def pvc_foil_wrap_services():
    return render_template("pvc-foil-wrap-services.html")

@main.route("/cnc-machine-work")
def cnc_machine_work():
    return render_template("cnc-machine-work.html")



@main.route("/interior-design")
def interior_design():
    return render_template("interior-design.html")



@main.route("/cutting-edging-services")
def cutting_edging_services():
    return render_template("cutting-edging-services.html")

@main.route("/wood-drying-services")
def wood_drying_services():
    return render_template("wood-drying-services.html")

@main.route("/kitchen-interior-design-services")
def kitchen_interior_design_services():
    return render_template("kitchen-interior-design-services.html")


@main.route("/services")
def services():
    return render_template("services.html")

@main.route("/projects")
def projects():
    return render_template("projects.html")



@main.route('/shop', methods=['GET', 'POST'])
def shop():
    # Get filter parameters from the request (defaults for min/max price)
    min_price = request.args.get('min_price', 0, type=float)
    max_price = request.args.get('max_price', float('inf'), type=float)
    page = request.args.get('page', 1, type=int)

    # Query products with price filtering and pagination
    items = Product.query.filter(
        Product.current_price >= min_price, 
        Product.current_price <= max_price
    ).paginate(page=page, per_page=20)

    # Make sure each item gets its image URL for display
    for item in items.items:
        item.product_picture = url_for('main.product_images', filename=item.product_picture)

    # Render the page with the products and filters
    return render_template('shop.html', items=items, min_price=min_price, max_price=max_price)







@main.route("/cutting-list")
def cutting_list():
    return render_template("cutting-list.html")

@main.route("/robots.txt")
def robots():
    return render_template("robots.txt")

#=======================================================================================================







#=======================================================================================================================================================================================================================================================================================
# #=============================================================================================================================================================================================================================================================================================================================================


from .forms import LoginForm, SignUpForm, PasswordChangeForm
from .models import Customer
from flask_login import login_user, login_required, logout_user
import os
from flask import render_template, request, redirect, flash, url_for,Blueprint,current_app
from flask_login import current_user
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash
from datetime import datetime
from . import db




UPLOAD_FOLDER_ = 'static/profile_pics'

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    from werkzeug.utils import secure_filename
    from flask import flash, redirect, render_template, request, url_for, current_app
    from werkzeug.security import generate_password_hash
    from datetime import datetime
    from app.models import Customer
    from app import db
    
    form = SignUpForm()
    
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password1 = form.password1.data
        password2 = form.password2.data
        profile_pic = request.files.get('profile_pic')  # Get file safely

        if password1 != password2:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('main.signup'))

        # Hash password
        password_hash = generate_password_hash(password1)

        # Check if email already exists
        existing_user = Customer.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists!', 'danger')
            return redirect(url_for('main.signup'))

        # Save profile picture
        if profile_pic and profile_pic.filename:
            filename = secure_filename(f"{username}_{profile_pic.filename}")
            file_path = os.path.join(current_app.root_path, 'static/profile_pics', filename)
            profile_pic.save(file_path)
            profile_pic_url = filename  # Store only filename in DB
        else:
            profile_pic_url = 'default.png'  # Default profile picture in static/profile_pics/

        # Create new user
        new_customer = Customer(
            email=email,
            username=username,
            password_hash=password_hash,
            date_joined=datetime.utcnow(),
            profile_picture=profile_pic_url  # Ensure model has this field
        )

        try:
            db.session.add(new_customer)
            db.session.commit()
            flash('Account created successfully! You can now login.', 'success')
            return redirect(url_for('main.login'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating account: {str(e)}', 'danger')

    return render_template('signup.html', form=form)


from flask import current_app, send_from_directory
import os

@main.route('/profile_pics/<path:filename>')
def profile_pics(filename):
    upload_folder = current_app.config['UPLOAD_FOLDER']  # Now safe to use
    return send_from_directory(upload_folder, filename)



@main.route('/profile/<int:customer_id>')
@login_required
def profile(customer_id):
    customer = Customer.query.get_or_404(customer_id)

    if customer.id != current_user.id:
        flash("You do not have permission to view this profile.", "danger")
        return redirect(url_for('main.home'))

    profile_picture = url_for('main.profile_pics', filename=customer.profile_picture) if customer.profile_picture else url_for('static', filename='profile_pics/default.png')

    return render_template('profile.html', customer=customer, profile_picture=profile_picture)



@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        customer = Customer.query.filter_by(email=email).first()

        if customer:
            if customer.verify_password(password=password):
                login_user(customer)
                return redirect('/')
            else:
                flash('Incorrect Email or Password')

        else:
            flash('Account does not exist please Sign Up')

    return render_template('login.html', form=form)


@main.route('/logout', methods=['GET', 'POST'])
@login_required
def log_out():
    logout_user()
    return redirect('/')






@main.route('/change-password/<int:customer_id>', methods=['GET', 'POST'])
@login_required
def change_password(customer_id):
    form = PasswordChangeForm()
    customer = Customer.query.get(customer_id)
    if form.validate_on_submit():
        current_password = form.current_password.data
        new_password = form.new_password.data
        confirm_new_password = form.confirm_new_password.data

        if customer.verify_password(current_password):
            if new_password == confirm_new_password:
                customer.password = confirm_new_password
                db.session.commit()
                flash('Password Updated Successfully')
                return redirect(f'/profile/{customer.id}')
            else:
                flash('New Passwords do not match!!')

        else:
            flash('Current Password is Incorrect')

    return render_template('change_password.html', form=form)


#=======================================================================================================================================================================================================================================================================================
# #=============================================================================================================================================================================================================================================================================================================================================

from flask import Blueprint, render_template, flash, send_from_directory, redirect
from flask_login import login_required, current_user
from .forms import ShopItemsForm, OrderForm
from werkzeug.utils import secure_filename
from .models import Product, Order, Customer
from . import db





@main.route('/update-item/<int:item_id>', methods=['GET', 'POST'])
@login_required
def update_item(item_id):
    if current_user.id == 1:
        form = ShopItemsForm()

        item_to_update = Product.query.get(item_id)

        form.product_name.render_kw = {'placeholder': item_to_update.product_name}
        form.previous_price.render_kw = {'placeholder': item_to_update.previous_price}
        form.current_price.render_kw = {'placeholder': item_to_update.current_price}
        form.in_stock.render_kw = {'placeholder': item_to_update.in_stock}
        form.flash_sale.render_kw = {'placeholder': item_to_update.flash_sale}

        if form.validate_on_submit():
            product_name = form.product_name.data
            current_price = form.current_price.data
            previous_price = form.previous_price.data
            in_stock = form.in_stock.data
            flash_sale = form.flash_sale.data

            file = form.product_picture.data

            file_name = secure_filename(file.filename)
            file_path = f'./media/{file_name}'

            file.save(file_path)

            try:
                Product.query.filter_by(id=item_id).update(dict(product_name=product_name,
                                                                current_price=current_price,
                                                                previous_price=previous_price,
                                                                in_stock=in_stock,
                                                                flash_sale=flash_sale,
                                                                product_picture=file_path))

                db.session.commit()
                flash(f'{product_name} updated Successfully')
                print('Product Upadted')
                return redirect('/shop-items')
            except Exception as e:
                print('Product not Upated', e)
                flash('Item Not Updated!!!')

        return render_template('update_item.html', form=form)
    return render_template('404.html')

"""
@main.route('/delete-item/<int:item_id>', methods=['GET', 'POST'])
@login_required
def delete_item(item_id):
    if current_user.id == 1:
        try:
            item_to_delete = Product.query.get(item_id)
            db.session.delete(item_to_delete)
            db.session.commit()
            flash('One Item deleted')
            return redirect('/shop-items')
        except Exception as e:
            print('Item not deleted', e)
            flash('Item not deleted!!')
        return redirect('/shop-items')

    return render_template('404.html')
"""

@main.route('/view-orders')
@login_required
def order_view():
    if current_user.id == 1:
        orders = Order.query.all()
        return render_template('view_orders.html', orders=orders)
    return render_template('404.html')


@main.route('/update-order/<int:order_id>', methods=['GET', 'POST'])
@login_required
def update_order(order_id):
    if current_user.id == 1:
        form = OrderForm()

        order = Order.query.get(order_id)

        if form.validate_on_submit():
            status = form.order_status.data
            order.status = status

            try:
                db.session.commit()
                flash(f'Order {order_id} Updated successfully')
                return redirect('/view-orders')
            except Exception as e:
                print(e)
                flash(f'Order {order_id} not updated')
                return redirect('/view-orders')

        return render_template('order_update.html', form=form)

    return render_template('404.html')


@main.route('/customers')
@login_required
def display_customers():
    if current_user.id == 1:
        customers = Customer.query.all()
        return render_template('customers.html', customers=customers)
    return render_template('404.html')











#=======================================================================================================================================================================================================================================================================================
# #=============================================================================================================================================================================================================================================================================================================================================
MPESA_CONSUMER_KEY="RvIuMkvShs1e6mGa7oUWfPuqHCXW1vzYJc8x38FI00NP1SXp"
MPESA_CONSUMER_SECRET="AXAZ4zkQD9NGHF6K4UwD7edXMVKIyCOVeYapxhikEUkQfG44XVuNViKjRL786bNY"
MPESA_SHORTCODE=174379
MPESA_PASSKEY="bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
MPESA_CALLBACK_URL="https://cherryinteriordesigns.onrender.com/mpesa/callback"



# M-Pesa Credentials
MPESA_CONSUMER_KEY = os.getenv("MPESA_CONSUMER_KEY")
MPESA_CONSUMER_SECRET = os.getenv("MPESA_CONSUMER_SECRET")
MPESA_SHORTCODE = os.getenv("MPESA_SHORTCODE")
MPESA_PASSKEY = os.getenv("MPESA_PASSKEY")
MPESA_CALLBACK_URL = os.getenv("MPESA_CALLBACK_URL")



@main.route('/contact-us', methods=['GET', 'POST'])
def contact():
    form = ServiceForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        # Create a new contact entry
        new_contact = Contact(name=name, email=email, message=message)

        try:
            db.session.add(new_contact)
            db.session.commit()
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('main.contact'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error sending message: {str(e)}', 'danger')

    return render_template('contact-us.html', form=form)

"""@main.route('/cart')
@login_required
def cart():
    cart = Cart.query.filter_by(customer_link=current_user.id).all()
    amount = sum(int(item.product.current_price) * item.quantity for item in cart)  # Ensure amount is treated as an integer
    total = amount + 200  # Add shipping cost

    
    # Ensure correct image path is set for each cart item
    for item in cart:
        item.product.product_picture = url_for('main.product_images', filename=item.product.product_picture)

    return render_template('cart.html', cart=cart, amount=amount, total=total)@main.route('/cart')
@login_required
def cart():
    cart_items = Cart.query.filter_by(customer_link=current_user.id).all()
    amount = sum(item.product.current_price * item.quantity for item in cart_items)
    total = amount + 200  # Add shipping cost

    # Ensure correct image path is set for each cart item
    for item in cart_items:
        item.product.product_picture = url_for('main.product_images', filename=item.product.product_picture)

    return render_template('cart.html', cart=cart_items, amount=amount, total=total,item=item,cart_items=cart_items)
"""



@main.route('/cart', methods=['GET', 'POST'])
@login_required
def cart():
    form = CheckoutForm()  # Initialize the form
    cart = Cart.query.filter_by(customer_link=current_user.id).all()
    
    # Calculate total cart amount
    amount = sum(int(item.product.current_price) * item.quantity for item in cart)  # Ensure amount is treated as an integer
    total = amount + 200  # Add shipping cost

    if form.validate_on_submit():
        # Validate that all required fields have data
        if not form.first_name.data:
            flash('First name is required!', 'error')
            return redirect(url_for('main.cart'))  # Redirect back to the cart page

        # Create the BillingDetail object
        billing_detail = BillingDetail(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            company_name=form.company_name.data,
            country=form.country.data,
            address_1=form.address_1.data,
            address_2=form.address_2.data,
            city=form.city.data,
            state=form.state.data,
            postcode=form.postcode.data,
            phone_number=form.phone_number.data,
            email=form.email.data
        )

        try:
            # Save the billing details to the database
            db.session.add(billing_detail)
            db.session.commit()
            flash('Billing details saved successfully!', 'success')
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(f'Error saving billing details: {str(e)}', 'error')

    return render_template('cart.html', cart=cart, amount=amount, total=total, form=form)


"""
works 

@main.route('/cart')
@login_required
def cart():
    
    form = CheckoutForm()  # Initialize the form
    cart = Cart.query.filter_by(customer_link=current_user.id).all()
    amount = sum(int(item.product.current_price) * item.quantity for item in cart)  # Ensure amount is treated as an integer
    total = amount + 200  # Add shipping cost
    
    if form.validate_on_submit():
        # Save the billing details
        billing_detail = BillingDetail(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            company_name=form.company_name.data,
            country=form.country.data,
            address_1=form.address_1.data,
            address_2=form.address_2.data,
            city=form.city.data,
            state=form.state.data,
            postcode=form.postcode.data,
            phone_number=form.phone_number.data,
            email=form.email.data
        )
        db.session.add(billing_detail)
        db.session.commit()
    


    return render_template('cart.html', cart=cart, amount=amount, total=total,form=form)
"""


@main.route('/update-cart-quantity/<int:item_id>', methods=['POST'])
@login_required
def update_cart_quantity(item_id):
    item = Cart.query.get_or_404(item_id)
    if item.customer_link != current_user.id:
        flash('You are not authorized to update this item.', 'danger')
        return redirect(url_for('main.cart'))

    new_quantity = request.form.get('quantity', type=int)
    if new_quantity and new_quantity > 0:
        item.quantity = new_quantity
        db.session.commit()
        flash('Quantity updated successfully.', 'success')
    else:
        flash('Invalid quantity.', 'danger')

    return redirect(url_for('main.cart'))


@main.route('/add-to-cart/<int:item_id>')
@login_required
def add_to_cart(item_id):
    item_to_add = Product.query.get(item_id)
    item_exists = Cart.query.filter_by(product_link=item_id, customer_link=current_user.id).first()
    if item_exists:
        try:
            item_exists.quantity = item_exists.quantity + 1
            db.session.commit()
            
                # Log add_to_cart event
            new_log = SalesLog(
                event_type="add_to_cart",
                customer_id=current_user.id,
                product_id=item_to_add.id,
                account_name=current_user.username,
                phone_number=current_user.phone
            )
            db.session.add(new_log)
            db.session.commit()
            
            flash(f'Quantity for { item_exists.product.product_name } has been updated','success')
            
            return redirect(request.referrer)
        except Exception as e:
            print('Quantity not Updated', e)
            flash(f'Quantity of { item_exists.product.product_name } not updated')
            return redirect(request.referrer)

    new_cart_item = Cart()
    new_cart_item.quantity = 1
    new_cart_item.product_link = item_to_add.id
    new_cart_item.customer_link = current_user.id

    try:
        db.session.add(new_cart_item)
        db.session.commit()
        flash(f'{new_cart_item.product.product_name} added to cart')
        
    except Exception as e:
        print('Item not added to cart', e)
        flash(f'{new_cart_item.product.product_name} has not been added to cart')

    return redirect(request.referrer)

"""


@main.route('/add-to-cart/<int:item_id>', methods=['GET', 'POST'])
@login_required
def add_to_cart(item_id):
    # For simplicity, get extra options from query parameters; in practice, use a proper form.
    color = request.args.get('color', 'Standard')
    size = request.args.get('size', 'One Size')
    quantity = request.args.get('quantity', 1, type=int)
    dimensions = request.args.get('dimensions', 'N/A')
    weight = request.args.get('weight', 'N/A')
    
    item_to_add = Product.query.get(item_id)
    item_exists = Cart.query.filter_by(product_link=item_id, customer_link=current_user.id).first()
    
    if item_exists:
        try:
            item_exists.quantity += quantity
            db.session.commit()
            
            # Log add_to_cart event (if using SalesLog)
            new_log = SalesLog(
                event_type="add_to_cart",
                customer_id=current_user.id,
                product_id=item_to_add.id,
                account_name=current_user.username,
                phone_number=current_user.phone
            )
            db.session.add(new_log)
            db.session.commit()
            
            flash(f'Quantity for { item_exists.product.product_name } has been updated', 'success')
            return redirect(request.referrer)
        except Exception as e:
            logging.error(str(e))
            flash(f'Could not update {item_to_add.product_name}', 'danger')
            return redirect(request.referrer)
    
    new_cart_item = Cart(
        quantity=quantity,
        product_link=item_to_add.id,
        customer_link=current_user.id,
        color=color,
        size=size,
        dimensions=dimensions,
        weight=weight
    )
    
    try:
        db.session.add(new_cart_item)
        db.session.commit()
        
        # Log add_to_cart event
        new_log = SalesLog(
            event_type="add_to_cart",
            customer_id=current_user.id,
            product_id=item_to_add.id,
            account_name=current_user.username,
            phone_number=current_user.phone
        )
        db.session.add(new_log)
        db.session.commit()
        
        flash(f'{item_to_add.product_name} added to cart.', 'success')
    except Exception as e:
        logging.error(str(e))
        flash(f'{item_to_add.product_name} could not be added to cart.', 'danger')
    
    return redirect(request.referrer)








@main.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    form = CheckoutForm()
    cart_items = Cart.query.filter_by(customer_link=current_user.id).all()
    amount = sum(item.product.current_price * item.quantity for item in cart_items)
    total = amount + 200  # Add shipping cost

    if form.validate_on_submit():
        for item in cart_items:
            new_order = Order(
                quantity=item.quantity,
                price=item.product.current_price * item.quantity,
                status='Pending',
                payment_id='N/A',  # Update this with actual payment ID if available
                customer_link=current_user.id,
                product_link=item.product.id
            )
            db.session.add(new_order)
        
        # Clear the cart after creating the order
        Cart.query.filter_by(customer_link=current_user.id).delete()
        db.session.commit()
        
        flash('Your order has been placed successfully!', 'success')
        return redirect(url_for('main.order_confirmation'))

    return render_template('checkout.html', form=form, cart=cart_items, amount=amount, total=total)
"""

@main.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    form = CheckoutForm()  # Initialize the form
    cart_items = Cart.query.filter_by(customer_link=current_user.id).all()
    amount = sum(item.product.current_price * item.quantity for item in cart_items)
    total = amount + 200  # Add shipping cost
    
    if form.validate_on_submit():
        # Save the billing details
        billing_detail = BillingDetail(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            company_name=form.company_name.data,
            country=form.country.data,
            address_1=form.address_1.data,
            address_2=form.address_2.data,
            city=form.city.data,
            state=form.state.data,
            postcode=form.postcode.data,
            phone_number=form.phone_number.data,
            email=form.email.data
        )
        db.session.add(billing_detail)
        db.session.commit()

        # Now create the orders for each item in the cart
        for item in cart_items:
            new_order = Order(
                quantity=item.quantity,
                price=item.product.current_price * item.quantity,
                status='Pending',
                payment_id='N/A',  # Replace with actual payment ID if available
                customer_link=current_user.id,
                product_link=item.product.id,
                billing_detail_id=billing_detail.id  # Reference to the saved billing detail
            )
            db.session.add(new_order)
        
        # Clear the cart after creating the order
        Cart.query.filter_by(customer_link=current_user.id).delete()
        db.session.commit()

        # Call the M-Pesa STK Push Payment API
        phone_number = form.phone_number.data  # Phone number entered by the user
        stk_push_url = url_for('main.stk_push', _external=True)
        
        # Make sure `form` data is not used outside the context where it's defined
        try:
            response = requests.post(stk_push_url, json={
                'phone_number': phone_number,
                'amount': total,  # The total amount to be paid
                'quantity': len(cart_items)
            })

            if response.status_code == 200:
                flash('Your order has been placed successfully, and payment is being processed!', 'success')
                return redirect(url_for('main.order_confirmation'))
            else:
                flash('Error with M-Pesa payment. Please try again.', 'danger')
                return redirect(url_for('main.checkout'))
        except Exception as e:
            current_app.logger.error(f"Error with M-Pesa STK Push: {str(e)}")
            flash('An error occurred with the payment process. Please try again later.', 'danger')
            return redirect(url_for('main.checkout'))

    return render_template('checkout.html', form=form, cart=cart_items, amount=amount, total=total)



@main.route('/order-confirmation')
@login_required
def order_confirmation():
    return render_template('order_confirmation.html')





"""
@main.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    # Assume CheckoutForm collects KYC fields: full_name, id_number, and address.
    form = CheckoutForm()
    # Get current cart items
    cart_items = Cart.query.filter_by(customer_link=current_user.id).all()
    
    if form.validate_on_submit():
        # Here you would process the KYC info – for example, save or verify details.
        kyc_data = {
            'full_name': form.full_name.data,
            'id_number': form.id_number.data,
            'address': form.address.data
        }
        # (Optionally) Save KYC data to the customer profile or a KYC table.
        
        # Then create an Order from the cart items, and clear the cart.
        new_order = Order(
            # populate order details using cart_items, total amount, etc.
            customer_link=current_user.id,
            # Additional order fields...
        )
        db.session.add(new_order)
        db.session.commit()
        
        flash("Your order has been placed successfully!", "success")
        return redirect(url_for('main.order'))

    return render_template('checkout.html', form=form, cart_items=cart_items)

"""




"""
@main.route('/add-to-cart/<int:item_id>')
@login_required
def add_to_cart(item_id):
    item_to_add = Product.query.get(item_id)
    item_exists = Cart.query.filter_by(product_link=item_id, customer_link=current_user.id).first()
    if item_exists:
        try:
            item_exists.quantity = item_exists.quantity + 1
            db.session.commit()
            
            # Log add_to_cart event
            new_log = SalesLog(
                event_type="add_to_cart",
                customer_id=current_user.id,
                product_id=item_to_add.id,
                account_name=current_user.username,  # assuming your Customer model has "username"
                phone_number=current_user.phone     # assuming a phone field; adjust as needed
            )
            db.session.add(new_log)
            db.session.commit()
            
            
            flash(f' Quantity of { item_exists.product.product_name } has been updated')
            return redirect(request.referrer)
        except Exception as e:
            print('Quantity not Updated', e)
            flash(f'Quantity of { item_exists.product.product_name } not updated')
            return redirect(request.referrer)

    new_cart_item = Cart()
    new_cart_item.quantity = 1
    new_cart_item.product_link = item_to_add.id
    new_cart_item.customer_link = current_user.id

    try:
        db.session.add(new_cart_item)
        db.session.commit()
        flash(f'{new_cart_item.product.product_name} added to cart')
    except Exception as e:
        print('Item not added to cart', e)
        flash(f'{new_cart_item.product.product_name} has not been added to cart')

    return redirect(request.referrer)

"""

@main.route('/delete-from-cart/<int:item_id>', methods=['POST'])
@login_required
def delete_from_cart(item_id):
    item_to_remove = Cart.query.filter_by(product_link=item_id, customer_link=current_user.id).first()
    
    if item_to_remove:
        db.session.delete(item_to_remove)
        db.session.commit()
        flash('Item removed from cart', 'success')
    else:
        flash('Item not found in cart', 'error')

    return redirect(url_for('main.cart'))  # Redirect back to cart



@main.route('/orders')
@login_required
def order():
    orders = Order.query.filter_by(customer_link=current_user.id).all()
    return render_template('orders.html', orders=orders)




def get_mpesa_access_token():
    try:
        # M-Pesa URL for token generation
        url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
        
        # Encode the credentials in base64
        credentials = f"{MPESA_CONSUMER_KEY}:{MPESA_CONSUMER_SECRET}"
        encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

        # Prepare the headers with the encoded credentials
        headers = {
            'Authorization': f'Basic {encoded_credentials}'
        }

        # Send the GET request to M-Pesa API to get the access token
        response = requests.get(url, headers=headers)
        
        # Print out the raw response for debugging purposes (mimicking your direct request)
        print(response.text.encode('utf8'))

        # Raise an exception for any HTTP error responses
        response.raise_for_status()

        # Extract the access token from the response JSON
        access_token = response.json().get("access_token")
        if access_token:
            logging.info("Successfully obtained M-Pesa access token.")
            return access_token
        else:
            logging.error("Access token not found in the response.")
            return None

    except requests.exceptions.RequestException as e:
        logging.error(f"Error obtaining M-Pesa token: {e}")
        return None


@main.route("/mpesa/stk_push", methods=["POST", "GET"])
@login_required
def stk_push():
    form = CheckoutForm()  # Initialize the form
    
    """Initiate M-Pesa STK Push Payment."""
    if request.content_type != "application/json":
        return jsonify({"error": "Content-Type must be application/json"}), 415

    try:
        data = request.get_json()
        phone_number = data.get("phone_number")
        amount = data.get("amount")

        # ✅ Format and validate phone number
        if not phone_number:
            return jsonify({"error": "Enter a valid M-Pesa phone number (07XXXXXXXX or 2547XXXXXXXX)."}), 400

        # ✅ Validate amount
        if not amount or not str(amount).isdigit() or float(amount) <= 0:
            return jsonify({"error": "Invalid total amount."}), 400

        # ✅ Convert amount to an integer
        amount = int(float(amount))

        # ✅ Get M-Pesa Access Token
        access_token = get_mpesa_access_token()
        if not access_token:
            return jsonify({"error": "Failed to obtain M-Pesa access token"}), 500

        # ✅ Generate M-Pesa STK Push Payload
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        password = base64.b64encode(f"{MPESA_SHORTCODE}{MPESA_PASSKEY}{timestamp}".encode()).decode()

        stk_push_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

        stk_push_payload = {
            "BusinessShortCode": MPESA_SHORTCODE,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone_number,
            "PartyB": MPESA_SHORTCODE,
            "PhoneNumber": phone_number,
            "CallBackURL": MPESA_CALLBACK_URL,
            "AccountReference": "OnlineStore",
            "TransactionDesc": "Payment for Order"
        }

        # ✅ Send STK Push Request
        headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
        response = requests.post(stk_push_url, json=stk_push_payload, headers=headers)
        response.raise_for_status()  # Raise exception for any HTTP error

        # ✅ Parse response and return appropriate response
        response_data = response.json()
        if response_data.get("ResponseCode") == "0":
            
            # Validate form data for billing details
            if form.validate_on_submit():
                # Save the billing details
                billing_detail = BillingDetail(
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    company_name=form.company_name.data,
                    country=form.country.data,
                    address_1=form.address_1.data,
                    address_2=form.address_2.data,
                    city=form.city.data,
                    state=form.state.data,
                    postcode=form.postcode.data,
                    phone_number=form.phone_number.data,
                    email=form.email.data
                )
                try:
                    db.session.add(billing_detail)
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()  # Rollback in case of error
                    logging.error(f"Error saving billing details: {str(e)}")
                    return jsonify({"error": "Error saving billing details."}), 500

            return jsonify({
                "success": True,
                "message": "STK Push sent. Check your phone.",
                "ResponseCode": response_data.get("ResponseCode"),
                "CheckoutRequestID": response_data.get("CheckoutRequestID")
            })
        else:
            logging.error(f"STK Push failed: {response_data}")
            return jsonify({"error": "Failed to send STK Push"}), 500

    except requests.exceptions.RequestException as e:
        logging.error(f"Error initiating STK Push: {e}")
        return jsonify({"error": "Failed to initiate STK Push"}), 500
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500




"""
@main.route("/mpesa/stk_push", methods=["POST","GET"])
@login_required
def stk_push():
    form = CheckoutForm()  # Initialize the form
    
    #Initiate M-Pesa STK Push Payment.
    if request.content_type != "application/json":
        return jsonify({"error": "Content-Type must be application/json"}), 415


    try:
        data = request.get_json()
        phone_number = data.get("phone_number")
        amount = data.get("amount")

        # ✅ Format and validate phone number
        
        if not phone_number:
            return jsonify({"error": "Enter a valid M-Pesa phone number (07XXXXXXXX or 2547XXXXXXXX)."}), 400

        # ✅ Validate amount
        if not amount or not str(amount).isdigit() or float(amount) <= 0:
            return jsonify({"error": "Invalid total amount."}), 400

        # ✅ Convert amount to an integer
        amount = int(float(amount))

         # ✅ Get M-Pesa Access Token
        access_token = get_mpesa_access_token()
        if not access_token:
            return jsonify({"error": "Failed to obtain M-Pesa access token"}), 500

        # ✅ Generate M-Pesa STK Push Payload
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        password = base64.b64encode(f"{MPESA_SHORTCODE}{MPESA_PASSKEY}{timestamp}".encode()).decode()

        stk_push_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

        stk_push_payload = {
            "BusinessShortCode": MPESA_SHORTCODE,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone_number,
            "PartyB": MPESA_SHORTCODE,
            "PhoneNumber": phone_number,
            "CallBackURL": MPESA_CALLBACK_URL,
            "AccountReference": "OnlineStore",
            "TransactionDesc": "Payment for Order"
        }

        # ✅ Send STK Push Request
        headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
        response = requests.post(stk_push_url, json=stk_push_payload, headers=headers)
        response.raise_for_status()  # Raise exception for any HTTP error

        # ✅ Parse response and return appropriate response
        response_data = response.json()
        if response_data.get("ResponseCode") == "0":
            
            
            
                            # Save the billing details
                
            billing_detail = BillingDetail(
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    company_name=form.company_name.data,
                    country=form.country.data,
                    address_1=form.address_1.data,
                    address_2=form.address_2.data,
                    city=form.city.data,
                    state=form.state.data,
                    postcode=form.postcode.data,
                    phone_number=form.phone_number.data,
                    email=form.email.data
                )
            db.session.add(billing_detail)
            db.session.commit()

            return jsonify({
                "success": True,
                "message": "STK Push sent. Check your phone.",
                "ResponseCode": response_data.get("ResponseCode"),
                "CheckoutRequestID": response_data.get("CheckoutRequestID")
            })
        else:
            logging.error(f"STK Push failed: {response_data}")
            return jsonify({"error": "Failed to send STK Push"}), 500

    except requests.exceptions.RequestException as e:
        logging.error(f"Error initiating STK Push: {e}")
        return jsonify({"error": "Failed to initiate STK Push"}), 500
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500
"""


# Handle M-Pesa Callback
@main.route("/mpesa/callback", methods=["POST"])
def mpesa_callback():
    #Handle M-Pesa Payment Callback
    callback_data = request.get_json()
    logging.info(f"M-Pesa Callback Received: {callback_data}")

    try:
        if callback_data["Body"]["stkCallback"]["ResultCode"] == 0:
            amount = callback_data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][0]["Value"]
            mpesa_receipt = callback_data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][1]["Value"]
            phone_number = callback_data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][4]["Value"]

            return jsonify({
                "success": True,
                "message": "Payment successful",
                "amount": amount,
                "mpesa_receipt": mpesa_receipt,
                "phone_number": phone_number
            })
        else:
            logging.error("Payment failed or cancelled by user.")
            return jsonify({"error": "Payment failed or cancelled by user"}), 400
    except KeyError as e:
        logging.error(f"Error processing callback data: {e}")
        return jsonify({"error": "Invalid callback data"}), 400









#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------



@main.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form.get('search')
        items = Product.query.filter(Product.product_name.ilike(f'%{search_query}%')).all()

        # Ensure correct image path is set for each product
        for item in items:
            item.product_picture = url_for('main.product_images', filename=item.product_picture)

        return render_template('search.html', items=items, cart=Cart.query.filter_by(customer_link=current_user.id).all()
                               if current_user.is_authenticated else [])

    return render_template('search.html')

# Categories
CATEGORIES = {
    "kitchen_accessories": [
        "ARTIFICIAL FLOWERY PLANTS", "HANDLES", "Hepo (Germany)", "HETTICH (GERMANY)", 
        "Kitchen Accessories", "LIGHTS", "Wardrobe Accessories", "Spice Racks", "Drawer Organizers", "bed", "Backsplash Tiles  ",
        " Pendant Light  ", "Pendant", "Light", "Stool" ,"Board" ,"Rack",
        "Kitchen Island  ", "Kitchen",
        "Bar Stools  ", "Coffee",
        "Cutting Board  ",
        "Spice Rack  ",
        "Coffee Maker  ",
        "Counter Stool  ",
        "Sink Faucet  ", "Sink", "Dish",
        "Wall Clock  ",
        " Dish Rack  ",
        " Storage Jars  ",  "Jar",
        "Cookware Set  ", "Bowl", "Handles", "Pots", "Pans", "Cookware", "Set",
        "Knife Block  ",
        "Fruit Bowl  ",
        "Cabinet Handles  ",
        "Drawer Organizers  ",
        "Plant Pots  ",
        "Area Rug  ","Rug",
        " Paper Towel Holder", "Holder", "towel"
        "Baskets", "Cutlery Trays", "Storage Containers", "Dish Racks", "Sink Mats", "Trivets", 
        "Oil Dispensers", "Salt & Pepper Shakers", "Tray Sets", "Cooking Utensils", "Pot Holders", 
        "Knives", "Knife Racks", "Measuring Cups", "Coffee Mugs", "Mixing Bowls", "Blenders", 
        "Coffee Makers", "Electric Kettles", "Pressure Cookers", "Juicers", "Cookware Sets", "Baking Pans", 
        "Toasters", "Food Processors", "Juice Extractors", "Graters", "Cutting Boards", "Chopping Blocks", 
        "Rice Cookers", "Stainless Steel Containers", "Frying Pans", "Sauce Pans", "Stock Pots", "Roasting Trays", 
        "Cookbook Stands", "Silicone Mats", "Canisters", "Funnel Sets", "Thermometers", "Water Filters", 
        "Cooking Thermometers", "Aprons", "Pot Scrubbers", "Dish Towels", "Sink Strainers"
    ],
    "boards_materials": [
        "BLOCK BOARDS", "boards", "BOARDS", "EDGE BANDING", "MDF HIGH GLOSS BOARDS", "Particle Boards", "bed", 
        "MDF"," Boards", "CLASSIC RANGE MDF", "Matt"," Finish", "Gloss Finish", "Plywood ","Boards", 
        "White MDF Boards", "Birch Plywood", "Oak Veneer", "Cherry Plywood", "Poplar Plywood", 
        "HDF Boards", "Chipboard", "Cedar Boards", "Hardwood Boards", "Melamine Boards", "Laminated Boards", 
        "Beaded Board", "Laminate Sheets", "Acoustic Panels", "Sanded Plywood", "Moisture Resistant Boards", 
        "Fireproof MDF", "Black MDF Boards", "Bamboo ","Boards", "Wooden Slats", "Birch MDF", 
        "Pine MDF", "Marine Ply", "Multiplex Plywood", "OSB Boards", "Polycarbonate Sheets", 
        "Laminated Chipboard", "Plasterboard", "PVC ","Foam ","Sheets", "Melamine-faced Chipboard", "Aluminium Composite Boards", 
        "Formica Sheets", "Veneer-faced MDF", "Wenge Veneer", "Walnut Veneer", "MDF Acoustic Panels", 
        "Exotic Wood Plywood", "FSC Certified MDF", "Fire Rated Chipboard", "PVC Board", "Recycled Paper Board", 
        "Superfine Paperboard", "Structural Timber Boards", "Moulding Boards", "Weather Resistant MDF", 
        "Decorative MDF Panels"
    ],
    "kitchen_furniture": [
        "Furniture", "Barn Chairs",  "Dining", "Chairs", "Stools", "Tables", "Bar Stools", "Dining" ,"Tables",
        "Cabinet", "Buffets", "Sideboards", "Sofa Sets", "Coffee Table", "Console Tables", "Cabinet ","Stands", 
        "Drawer Units", "Side Tables", "Cupboards", "Wall Shelves", "Kitchen ","Islands", "Workstations", 
        "Storage ","Bins", "Storage Cabinets", "Serving Carts", "Bar Cabinets", "Bookcases", "Bookshelves", 
        "TV Units", "Recliners", "Modular Sofas", "Loveseats", "Accent Chairs", "Storage Drawers", "Chests of Drawers", 
        "Wardrobes", "Filing Cabinets", "Side Buffets", "Nightstands", "Bar Carts", "Shoe Racks", "Wall Mounted ","Shelves", 
        "Entertainment Units", "Armchairs", "Cabinet Organizers", "Living Room Chairs", "Storage Ottomans", 
        "Dressers", "Towel Racks", "Vanity Tables", "Cupboard Units", "Lounge Chairs", "Hall Consoles", 
        "TV ","Stand", "Cabinet Organizers"
    ],
    "kitchen_cabinet_fittings": [
        "Kitchen ","Cabinet ","Fittings", "Panel Doors", "Flush Doors", "Cabinet Hinges", "Drawer Slides", "bed", 
        "Pull Handles", "Cabinet Locks", "Soft Close Mechanisms", "Door Closers", "Drawer Pulls", 
        "Shelf Brackets", "Cabinet Shelving", "Carcass Panels", "Cabinet Feet", "Drawer Fronts", 
        "End Panels", "Kickboards", "Cabinet Clips", "Organizing Racks", "Drawer Organizers", 
        "Cabinet Handles", "Shelf Inserts", "Cutlery Trays", "Shoe Organizers", "Pull-out Shelves", 
        "Pull-out Drawers", "Pull-out Baskets", "Corner Cabinets", "Ladder Shelf Brackets", "Adjustable Shelf Clips", 
        "Drawer Inserts", "Shelf Supports", "Cabinet Back Panels", "Wall Mounting Brackets", "Under-sink Racks", 
        "Rolling Racks", "Pull-out Trays", "Pantry Organizers", "Vertical Pull-outs", "Handle-less Cabinets", 
        "Floating Shelf Brackets", "Hanging Rails", "Storage Baskets", "Sliding Door Fittings", "Racking Systems", 
        "Laminate Door Panels", "Double Drawer Pulls", "Pull-out Tables", "Undermount Sinks", "Flush Hinges", 
        "Shelf Dividers", "Drawer Stoppers", "Cabinet Locks", "Sliding Shelf Organizers", "Corner Shelf Fittings"
    ],
    "wooden_items": [
        "Wood ","Items", "Door skin", "Hardwood Solid Panel Doors", "Wooden Doors", "Wooden Panels", "bed", 
        "Wooden Flooring", "Wooden Planks", "Wooden Beams", "Wooden Shelves", "Wooden Frames", "Wooden Tables", 
        "Wooden Cabinets", "Wooden Chairs", "Wooden Beds", "Wooden Window Frames", "Wooden Blinds", "Wooden Decking", 
        "Wooden Fencing", "Wooden Staircases", "Wooden Railings", "Wooden Wardrobes", "Wooden Dresser", 
        "Wooden Side Tables", "Wooden Nightstands", "Wooden Bookcases", "Wooden Storage Boxes", 
        "Wooden Planters", "Wooden Sheds", "Wooden Flooring Boards", "Wooden Screens", "Wooden Beams", 
        "Wooden Wall Panels", "Wooden Headboards", "Wooden Bench", "Wooden Stools", "Wooden Picture Frames", 
        "Wooden Coat Racks", "Wooden Shelf Brackets", "Wooden Serving Trays", "Wooden Chairs", "Wooden Tables", 
        "Wooden Window Shutters", "Wooden Cutting Boards", "Wooden Doors", "Wooden Door Handles", 
        "Wooden Display Units", "Wooden Boxes", "Wooden Crafts", "Wooden Art Panels", "Wooden Bed Frames", 
        "Wooden Hutches", "Wooden TV Stands"
    ],
    "uncategorized": [
        "Uncategorized", "Miscellaneous Items", "New Arrivals", "Clearance Items", "Gift Ideas", "Sale Items", "bed", 
        "Hot Picks", "Trending Products", "Special Offers", "Seasonal Deals", "Limited Edition", 
        "Exclusive Collections", "Customer Favorites", "Top Rated", "Best Sellers", "Luxury Products", 
        "Eco-friendly Products", "Sustainable Designs", "One-of-a-Kind Products", "Highly Recommended", 
        "VIP Collection", "Must-Have Items", "Limited Time Offers", "Staff Picks", "Artisan Products", 
        "Handmade Crafts", "Made-to-Order", "Custom Products", "Pre-order Items", "Exclusive Deals", 
        "Gift Wrapped Items", "Personalized Products", "One-Time Offers", "Bestselling Designs", 
        "High Demand Items", "Gift Cards", "Seasonal Specials", "Flash Sale Items", "Flash Offer", 
        "Home Decor Items", "Unique Finds", "Rare Items", "Seasonal Trends", "Trendsetting Designs", 
        "Pop-Up Items", "Designer Pieces", "Collector's Items", "All-time Classics", "Fan Favorites", 
        "Up-and-Coming Products", "Editor’s Picks", "Innovative Designs", "Top Choice Products"
    ],
    "flooring": [
        "Floors", "Hardwood Flooring", "Laminate Flooring", "Vinyl Flooring", "Carpet ","Tile", "Rugs", "courtyard","summer","dawn","jungle",
        "Area Rugs", "deluxe", "Ceramic Tiles", "scenary ","Tiles", "garden ", "Bamboo ", 
        "Cork Flooring", "Engineered Wood Flooring", "Stone Flooring", "Marble Flooring", "Granite Flooring", 
        "blossom", "hawaii", "galaxy", "Sisal Rugs", "Wool Carpets", "Synthetic Rugs", 
        "Outdoor Flooring", "Decking", "Terracotta Flooring", "Glass Tiles", "Patterned Flooring", "Subway Tiles", 
        "Terrazzo Flooring", "Patterned Rugs", "Waterproof Flooring", "Luxury Vinyl Tile", "Interlocking Tiles", 
        "Floating Floors", "Reclaimed Wood Floors", "Shaggy Rugs", "Jute Rugs", "Persian Rugs", "Traditional Rugs", 
        "Striped Carpets", "Indoor/Outdoor Rugs", "Cork Tiles", "Woven Vinyl Flooring", "Rubber Tiles", 
        "Pine Flooring", "Beechwood Flooring", "Red Oak Flooring", "Engineered Oak Flooring", "Rustic Wood Flooring", 
        "Decorative Stone Floors", "Rattan Rugs", "Geometric Rugs"
    ]
}




@main.route('/search_random/<category>')
def search_random(category):
    """Search for products in a given category"""
    if category not in CATEGORIES:
        return jsonify({"error": "Invalid category"})

    # Get the list of items in the category
    category_items = CATEGORIES[category]

    # Search for products that match any item in the category (case-insensitive)
    items = Product.query.filter(
        or_(*[Product.product_name.ilike(f"%{item}%") for item in category_items])
    ).all()

    # Ensure correct image path is set for each product
    for item in items:
        item.product_picture = url_for('main.product_images', filename=item.product_picture)
        print("Product:", item.product_name, "Image Path:", item.product_picture)  # Debugging

    return render_template('search.html', items=items, category_items=category_items, category=category, 
                           cart=Cart.query.filter_by(customer_link=current_user.id).all() if current_user.is_authenticated else [])

#----------------------------------------------------------------------------------------------------------------------------------------------------------------


from werkzeug.utils import secure_filename
from flask import send_from_directory
import os

# Ensure UPLOAD_FOLDER is an absolute path
import os
from flask import render_template, send_from_directory
from .models import Product, Cart  # Ensure correct import
from flask_login import current_user
from .forms import ServiceForm
from .models import Contact



@main.route('/')
def home():
    # Example data for services
    services = [
        {'name': 'Interior Design', 'image_url': 'service1.jpg', 'description': 'High-quality interior design'},
        {'name': 'Furniture', 'image_url': 'service2.jpg', 'description': 'Premium furniture'}
        # Add more services as needed
    ]
    # Example data for testimonials
    testimonials = [
        {'content': 'Great service! My house looks amazing!', 'mainor': 'John Doe'},
        {'content': 'The best design company I have worked with!', 'mainor': 'Jane Smith'}
        # Add more testimonials as needed
    ]
    # Example data for projects
    projects = [
        {'name': 'Project 1', 'image': 'project1.jpg', 'slug': 'project1', 'description': 'A beautiful new office'},
        {'name': 'Project 2', 'image': 'project2.jpg', 'slug': 'project2', 'description': 'A luxurious home'}
        # Add more projects as needed
    ]
    
    
    categories = [
        {"name": "Accessories", "count": 222, "link": "https://cherryinterior.com/product-category/accessories", "children": [
            {"name": "Artificial Flowery Plants", "count": 18, "link": "https://cherryinterior.com/product-category/accessories/artificial-flowery-plants"},
            {"name": "Handles", "count": 8, "link": "https://cherryinterior.com/product-category/accessories/handles"},
            {"name": "Hepo (Germany)", "count": 17, "link": "https://cherryinterior.com/product-category/accessories/hepo-germany"},
            {"name": "Hettich (Germany)", "count": 32, "link": "https://cherryinterior.com/product-category/accessories/hettich-germany"},
            {"name": "Kitchen Accessories", "count": 118, "link": "https://cherryinterior.com/product-category/accessories/kitchen-accessories"},
            {"name": "Lights", "count": 14, "link": "https://cherryinterior.com/product-category/accessories/lights"},
            {"name": "Wardrobe Accessories", "count": 84, "link": "https://cherryinterior.com/product-category/accessories/wardrobe-accessories"}
        ]},
        {"name": "Furniture", "count": 14, "link": "https://cherryinterior.com/product-category/furniture", "children": [
            {"name": "Barn Chairs", "count": 1, "link": "https://cherryinterior.com/product-category/furniture/barn-chairs"},
            {"name": "Beds", "count": 4, "link": "https://cherryinterior.com/product-category/furniture/beds"},
            {"name": "Dining Chairs", "count": 2, "link": "https://cherryinterior.com/product-category/furniture/dining-chairs"},
            {"name": "Stools", "count": 0, "link": "https://cherryinterior.com/product-category/furniture/stools"},
            {"name": "Tables", "count": 6, "link": "https://cherryinterior.com/product-category/furniture/tables"}
        ]},
        {"name": "Boards", "count": 237, "link": "https://cherryinterior.com/product-category/boards", "children": [
            {"name": "Edge Banding", "count": 2, "link": "https://cherryinterior.com/product-category/boards/edge-banding"},
            {"name": "MDF High Gloss Boards", "count": 19, "link": "https://cherryinterior.com/product-category/boards/mdf-high-gloss-boards"}
        ]}
    ]

    page = request.args.get('page', 1, type=int)

    

    items = Product.query.filter_by(flash_sale=True).paginate(page=page, per_page=20)


    return render_template(
        'home.html',
        services=services, projects=projects, categories=categories,testimonials=testimonials,
        items=items,
        cart=Cart.query.filter_by(customer_link=current_user.id).all() if current_user.is_authenticated else []
    )

# (Optional) A route to serve other assets (like music) in a separate folder:
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app/static/profile_pics')
PRODUCT_FOLDER = os.path.join(os.getcwd(), 'media')

@main.route('/blog_images/<filename>')
def blog_images(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)


# New route to serve product images from the media folder (PRODUCT_FOLDER)
@main.route('/product-images/<path:filename>')
def product_images(filename):
    return send_from_directory(PRODUCT_FOLDER, filename)

@main.route('/static/images/<path:filename>')
def static_images(filename):
    return send_from_directory(os.path.join(current_app.root_path, 'static', 'images'), filename)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

"""
@main.route('/add-shop-items', methods=['GET', 'POST'])
@login_required
def add_shop_item():
    form = ShopItemsForm()

    if form.validate_on_submit():
        product_name = form.product_name.data
        previous_price = form.previous_price.data
        current_price = form.current_price.data
        in_stock = form.in_stock.data
        product_picture = form.product_picture.data
        flash_sale = form.flash_sale.data
        product_description=form.product_description.data

        # Handle file upload
        if product_picture and allowed_file(product_picture.filename):
            filename = secure_filename(product_picture.filename)
            file_path = os.path.join(PRODUCT_FOLDER, filename)
            product_picture.save(file_path)

            # Store only the filename, not the full path
            saved_filename = filename  
        else:
            saved_filename = None  # If no file, store NULL

        # Create new product entry
        new_product = Product(
            product_name=product_name,
            previous_price=previous_price,
            current_price=current_price,
            in_stock=in_stock,
            product_picture=saved_filename,  # Save filename in the database
            product_description=product_description,
            flash_sale=flash_sale
        )

        db.session.add(new_product)
        db.session.commit()

        flash("Product added successfully!", "success")
        return redirect(url_for('main.add_shop_item'))

    return render_template('add_shop_items.html', form=form)
    
"""

@main.route("/add-shop-items", methods=["GET", "POST"])
@login_required
def add_shop_items():
    # Only allow admin access
    if current_user.email != 'admin@admin.com':
        flash("Not authorized", "danger")
        return redirect(url_for("main.home"))
        
    from .forms import ShopItemsForm  # ensure ShopItemsForm is defined in your forms.py
    form = ShopItemsForm()
    
    if form.validate_on_submit():
        # Handle image upload
        product_picture = form.product_picture.data
        filename = secure_filename(product_picture.filename)
        save_path = os.path.join(current_app.config['PRODUCT_FOLDER'], filename)
        product_picture.save(save_path)
        
        # Create a new Product entry
        new_product = Product(
            product_name=form.product_name.data,
            current_price=form.current_price.data,
            previous_price=form.previous_price.data,
            in_stock=form.in_stock.data,
            product_picture=filename,
            flash_sale=form.flash_sale.data,
            product_description=form.product_description.data
        )
        
        db.session.add(new_product)
        db.session.commit()
        flash("Product added successfully!", "success")
        return redirect(url_for("main.shop"))
    
    return render_template("add_shop_item.html", form=form)




@main.route('/product_details/<int:product_id>')
def product_details(product_id):
    product = Product.query.get_or_404(product_id)
    # Use the first word of the product name as a keyword
    keyword = product.product_name.split()[0] if product.product_name.split() else ''
    # Query for related products (exclude the current product)
    related_items = Product.query.filter(
        Product.product_name.ilike(f'%{keyword}%'),
        Product.id != product.id
    ).limit(4).all()
    
    return render_template('product_details.html', product=product, related_items=related_items)


    
@main.route('/admin')
def admin():
    return render_template('admin.html')


@main.route('/customers')
def customers():
    customers = Customer.query.all()  # Fetch all customers from the database
    return render_template('customers.html', customers=customers)

"""@main.route('/update-order/<int:order_id>', methods=['GET', 'POST'])
def update_order(order_id):
    # Fetch the order by ID, or return a 404 if not found
    order = Order.query.get_or_404(order_id)
    
    form = OrderForm()  # Assuming you're using a WTForms form
    
    # Handle form submission to update order status
    if form.validate_on_submit():
        try:
            order.status = form.order_status.data  # Set the new status
            db.session.commit()  # Commit changes to the database
            flash("Order updated successfully!", "success")
            return redirect(url_for('main.order'))  # Redirect to orders page
        except Exception as e:
            flash(f"Error updating the order: {e}", "danger")
            return redirect(url_for('main.order'))

    # Render the order update template if the form is not submitted
    return render_template('order_update.html', form=form, order=order)

"""

@main.route('/shop-items')
def shop_items():
    try:
        items = Product.query.all()  # Fetch all shop items from the database
        if not items:
            flash('No shop items available', 'info')  # Optional flash message
        return render_template('shop_items.html', items=items)
    
    
    except Exception as e:
        flash(f"An error occurred while fetching shop items: {e}", 'danger')
        return redirect(url_for('main.home'))  # or wherever you want to redirect on error


@main.route('/delete-item/<int:item_id>', methods=['POST', 'GET'])
def delete_item(item_id):
    try:
        item = Product.query.get_or_404(item_id)  # Find the item or 404
        db.session.delete(item)  # Delete the item from the database
        db.session.commit()  # Commit the transaction
        flash('Item successfully deleted', 'success')  # Flash success message
        return redirect(url_for('main.shop_items'))  # Redirect to the shop items page
    except Exception as e:
        flash(f"An error occurred: {e}", 'danger')
        return redirect(url_for('main.shop_items'))

