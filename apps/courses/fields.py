from typing import Any
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class OrderField(models.PositiveIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance: models.Model, add: bool) -> Any:
        if getattr(model_instance, self.attname) is None:
            try:
                # Get the model class of the instance
                model_class = model_instance.__class__
                
                # Query the objects of that model class
                qs = model_class.objects.all()
                
                if self.for_fields:
                    query = {field: getattr(model_instance, field) for field in self.for_fields}
                    qs = qs.filter(**query)
                    
                last_item = qs.latest(self.attname)
                value = last_item.order + 1
            except ObjectDoesNotExist:
                value = 0
            
            # Set the value on the model instance
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super().pre_save(model_instance, add)
