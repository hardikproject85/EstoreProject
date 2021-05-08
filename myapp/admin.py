from django.contrib import admin
from .models import Contact,User,Product,Wishlist,MyCart,Transaction
# Register your models here.

admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(MyCart)
admin.site.register(Transaction)
admin.site.site_header = "Hardik Vastarpara"

