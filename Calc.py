from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file("calcUI.kv") 

Window.size = (600, 750)
#Window.minimum_width, Window.minimum_height = Window.size #this line of code is not working. I don't know why.

class CalcLayout(Widget):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.prior_button = None
        self.prior = None
    
    def clear(self):
        self.ids.calc_input.text = "0"
    
    #def button_press(self, button, *args):
    
    def button_press(self, button):
        self.prior = self.ids.calc_input.text
        if "Error" in self.prior:
            self.prior = ""
        if self.prior_button == "=" or self.prior_button == "%":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}" 
        if self.prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}"
        else:
            self.ids.calc_input.text = f"{self.prior}{button}"
            
    
    #getting rid of all the add,subtract,multiply,divide etc. functions as that's not an efficient way to do this
    def math_sign(self, sign):
        self.prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{self.prior}{sign}"
        #self.prior_button = sign
        
    def dot(self):
        sign = ["+","-","*","/"]
        self.prior = self.ids.calc_input.text
        num_list = [self.prior]
        
        for i in sign:
            temp = []
            for j in num_list:
                temp.extend(j.split(i))
            num_list = temp

        if "." not in num_list[-1]:
            self.ids.calc_input.text = f"{self.prior}."
        elif "." in self.prior:
            pass 
        else:
            self.prior = f'{self.prior}'
            self.ids.calc_input.text = self.prior
    
    def percentage(self):
        self.prior = self.ids.calc_input.text
        try:
            answer = eval(self.prior)/100
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"
        self.prior_button = '%'
        
        #return answer
    #percentage = percentage()
        
    def pos_neg(self):
        self.prior = self.ids.calc_input.text
        if "-" in self.prior:
            self.ids.calc_input.text = f"{self.prior.replace('-','')}"
        else:
            self.ids.calc_input.text = f"-{self.prior}"
    
    def delete(self):
        self.prior = self.ids.calc_input.text
        self.prior = self.prior[:-1]
        self.ids.calc_input.text = self.prior
        
    def equals(self):
        self.prior = self.ids.calc_input.text
        #using eval() function to evaluate the string and doing the calculation
        try:
            answer = eval(self.prior)#eval is not always welcomed to use
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"
        self.prior_button = '='
        #return answer
    
    #equals = equals()

class CalculatorApp(App):
    def build(self):
        return CalcLayout()

if __name__ == "__main__":
    CalculatorApp().run()
    


'''overkill lines of code'''    
'''	
    def add(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}+"
    
    def subtract(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}-"
    
    def multiply(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}*"
    
    def divide(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}/"
    '''	
    
'''
    # bangla way of doing equals function work. 
    if "+" in prior:
        num_list = prior.split("+")
        answer = 0.0
        for number in num_list:
            answer = answer + float(number)
        #output answer in window
        self.ids.calc_input.text = str(answer)
'''