from rest_framework import serializers
from .models import Book, Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        supplier_data = validated_data.pop('supplier')
        supplier = Supplier.objects.create(**supplier_data)
        book = Book.objects.create(supplier=supplier, **validated_data)
        return book

    def update(self, instance, validated_data):
        supplier_data = validated_data.pop('supplier')
        supplier = instance.supplier

        # Update supplier fields
        supplier.name = supplier_data.get('name', supplier.name)
        supplier.contact_person = supplier_data.get('contact_person', supplier.contact_person)
        supplier.email = supplier_data.get('email', supplier.email)
        supplier.phone_number = supplier_data.get('phone_number', supplier.phone_number)
        supplier.address = supplier_data.get('address', supplier.address)
        supplier.currency = supplier_data.get('currency', supplier.currency)
        supplier.save()

        # Update book fields
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.category = validated_data.get('category', instance.category)
        instance.price = validated_data.get('price', instance.price)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.save()

        return instance
