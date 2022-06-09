# Lab 3 
## Objective :
To add the search bars for the products, brands and categories
## Introduction :
Various customers have various requirements, this lab helps in customizing the E-commerce website according to the desire of the customer
## Procedure:
First we replaced the code for admin.site.register(Product) with

    class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "brand", "category",]
    search_fields = ["name", "price", "brand__name", "category__name",]
    list_filter = ["brand","category",]
    readonly_fields = ["quantity",]

    class Meta:
      model = Product
    admin.site.register(Product, ProductAdmin)
    
then **admin.site.register(Category)** with

    class Meta:
        model = Category
    admin.site.register(Category, CategoryAdmin)
    class ProductAdmin(admin.ModelAdmin):
    list_display = ["image_tag", "name", "price", "brand", "category",]
    search_fields = ["name", "price", "brand__name", "category__name",]
    list_filter = ["brand","category","price",]
    
and **admin.site.register(Brand)** with

    class Meta:
        model = Brand
    admin.site.register(Brand, BrandAdmin)
    class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active",]
    search_fields = ["name", "is_active",]

We than ran the server using _python manage.py runserver_ and edited the code for products in _models.py_ by adding the image tag and also marked it safe :

      class Product(models.Model):
      name = models.CharField(max_length=200)
      price = models.FloatField()
      quantity = models.IntegerField()
      image_url = models.CharField(max_length=500)
      color_code = models.CharField(max_length=20)
      brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
      category = models.ForeignKey(Category, on_delete=models.CASCADE)
      registered_on = models.DateTimeField()
      is_active = models.BooleanField()
      def image_tag(self):
    return mark_safe(f'<img src="{self.image_url}" width="50" height="50" />')
    image_tag.short_description = "Product"
    def __str__(self):
    return self.name
    
 ## Outputs:
 ![Screenshot (41)](https://user-images.githubusercontent.com/104953599/172746736-24668b9a-b427-418c-a824-7a326036d44c.png)
![Screenshot (42)](https://user-images.githubusercontent.com/104953599/172746837-aac9c377-36ac-4545-b15e-8f5a5bb25ea1.png)
![Screenshot (43)](https://user-images.githubusercontent.com/104953599/172746898-0763e005-5322-4ec0-9a69-b37cca740c6a.png)
![Screenshot (44)](https://user-images.githubusercontent.com/104953599/172747067-3cb68427-c36f-4d08-98c9-cb95ed040b51.png)

## Conclusion:
Hence, In this lab we learnt how to add search bar for product_module and also peformed CURD operations.
 
 
