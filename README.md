# Bernstein-Vazirani algorithm

##The problem this algorithm aims to solve  
Suppose there is a function <img src="https://latex.codecogs.com/gif.latex?f(x)" title="f(x)" />, n-digits variable <img src="https://latex.codecogs.com/gif.latex?x" title="x" />, n-digits constant <img src="https://latex.codecogs.com/gif.latex?a" title="a" /> which satisfies the following equation.

<img src="https://latex.codecogs.com/gif.latex?f(x)&space;=&space;x&space;\bullet&space;a&space;\equiv&space;(x_0&space;\bullet&space;a_0&space;)&space;\oplus&space;(x_1&space;\bullet&space;a_1&space;)&space;\cdot\cdot\cdot&space;\oplus&space;(x_{n-1}&space;\bullet&space;a_{n-1&space;})" title="f(x) = x \bullet a \equiv (x_0 \bullet a_0 ) \oplus (x_1 \bullet a_1 ) \cdot\cdot\cdot \oplus (x_{n-1} \bullet a_{n-1 })" />  

This algorithm can be used to figure out <img src="https://latex.codecogs.com/gif.latex?a" title="a" /> in just one evaluation, while its classical counterpart takes n time evaluations.

1st time:  <img src="https://latex.codecogs.com/gif.latex?f(0\cdot&space;\cdot&space;\cdot&space;1)&space;=&space;1\bullet&space;a_0&space;=&space;a_0" title="f(0\cdot \cdot \cdot 1) = 1\bullet a_0 = a_0" />  
・  
・  
・  
nth time:  <img src="https://latex.codecogs.com/gif.latex?f(1\cdot&space;\cdot&space;\cdot&space;0)&space;=&space;1\bullet&space;a_{n-1}&space;=&space;a_{n-1}" title="f(1\cdot \cdot \cdot 0) = 1\bullet a_{n-1} = a_{n-1}" />


## Mathematical explanation  
