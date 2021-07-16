from .models import Products

class ProductsDBRouter:
    def db_for_read(self,model,**hints):
        if model == Products:
            return 'product'
        return None

    def db_for_write(self,model,**hints):
        if model == Products:
            return 'product'
        return None
        
