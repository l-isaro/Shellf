class Menu:
    """Displays the countries to choose from."""
    
    
    Countries = [Rwanda, Kenya, Ethiopia, Nigeria, Ghana, Libya, Egypt, South Africa, Zambia, DRC]
    
    def __init__(self, selection):
        self.__selection = selection
    
    @property
    def selection(self):
        """assigns selction to selection"""
        return self.__selection

    @selection.setter
    def selection(self, value):
        """conditions"""
        if not isinstance(value, int):
            raise TypeError("Input must be an integer")
        if value > 10 or value < 1:
            raise ValueError("input out of range")    
        self.__selection = selection   
