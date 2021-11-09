from behave import given,then,step
import Calculadora

#Teste adição:
@given(u'que o usuário some "{som1:d}" com "{som2:d}"')
def test_adicao(context, som1, som2):
    global resultSom
    resultSom = Calculadora.calculadora.adicao(som1, som2)

@then(u'o resultado da adição deve ser "{resultSom2:d}"')
def test_adicao_result(context, resultSom2):
    assert  resultSom == resultSom2 

#Teste subtração:
@given(u'que o usuário subtraia "{sub1:d}" de "{sub2:d}"')
def step_subtracao(context, sub1, sub2):
    global resultSub
    resultSub = Calculadora.calculadora.subtracao(sub1, sub2)    

@then(u'o resultado da subtracao deve ser "{resultSub2:d}"')
def test_step_subtracao(context, resultSub2):
    assert resultSub == resultSub2 

#Teste multiplicação:
@given(u'que o usuário multiplique "{mult1:d}" por "{mult2:d}"')
def test_multiplicacao(context, mult1, mult2):
    global resultMult
    resultMult = Calculadora.calculadora.multiplicacao(mult1, mult2)

@then(u'o resultado da multiplicacao deve ser "{resultMult2:d}"')
def teste_multiplicação_result(context, resultMult2):
    assert resultMult == resultMult2

#Teste divisão:
@given(u'que o usuário divida "{div1:d}" por "{div2:d}"')
def teste_divisao(context, div1, div2):
    global resultDiv
    resultDiv = Calculadora.calculadora.divisao(div1, div2)

@then(u'o resultado da divisao deve ser "{resultDiv2:d}"')
def teste_divisao_result(context, resultDiv2):
    assert resultDiv == resultDiv2