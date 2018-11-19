# chain-analyzer

По введенной цепочке определяет тип грамматики.

## Грамматики для теста

Тип 0:
a,b
S,C,F,D,A,B
S>aaCFD,F>AFB|AB,AB>bBA,Ab>bA,AD>D,Cb>bC,CB>C,bCD>ЭПС
S

Тип 1 (КЗ):
a,b,c
S,B,C
S>aSBC|abc,bC>bc,CB>BC,cC>cc,BB>bb
S

Тип 2 (КС):
a,b,c
S,Q
S>aQb|accb,Q>cSc

Тип 3 (РЛ):
a,b,c
A,B,S
S>Ac|Bc,A>a|Ba,B>b|Bb|Ab

Тип 3 (РП)
a,b,c
A,B,S
S>cA|cB,A>a|aB,B>b|bB|bA
