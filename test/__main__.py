from py_expression.core import Exp
from py_expression_opencv.lib import *


exp=Exp()
loadOpenCvExpressions(exp)

text='ws=Volume("data"); '\
     'pathImage=ws.fullpath("lena.jpg"); '\
     'image=cvImread(pathImage); '\
     'output=cvtColor(image,ColorConversion.BGR2RGB); '  

context = {}
expression = exp.parse(text)

expression.eval(context)
print(context['output'])