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
This is the process to get s.   I get this explanation from J.Du & R.Han(2000)(https://arxiv.org/abs/quant-ph/0012114).  
<img src="https://latex.codecogs.com/gif.latex?(|0\rangle)^{n}|1\rangle&space;\xrightarrow{H(n&plus;1)}\frac{1}{\sqrt{2^n}}&space;\sum_{x=0}^{2^n-1}&space;|x\rangle&space;\otimes&space;\frac{|0\rangle-|1\rangle}{\sqrt{2}}" title="(|0\rangle)^{n}|1\rangle \xrightarrow{H(n+1)}\frac{1}{\sqrt{2^n}} \sum_{x=0}^{2^n-1} |x\rangle \otimes \frac{|0\rangle-|1\rangle}{\sqrt{2}}" />  
<img src="https://latex.codecogs.com/gif.latex?\xrightarrow{U_f}&space;\frac{1}{\sqrt{2^n}}\sum_{x=0}^{2^n-1}&space;(-1)^{s\cdot&space;x}|x\rangle&space;\otimes&space;\frac{|0\rangle&space;-&space;|1\rangle}{\sqrt{2}}" title="\xrightarrow{U_f} \frac{1}{\sqrt{2^n}}\sum_{x=0}^{2^n-1} (-1)^{s\cdot x}|x\rangle \otimes \frac{|0\rangle - |1\rangle}{\sqrt{2}}" />  
<img src="https://latex.codecogs.com/gif.latex?\xrightarrow{H^{(n)}}&space;\frac{1}{\sqrt{2^n}}\sum_{x=0}^{2^n-1}\sum_{y=0}^{2^n-1}&space;(-1)^{s\cdot&space;x&space;&plus;&space;x\cdot&space;y}|y\rangle&space;\otimes&space;\frac{|0\rangle&space;-&space;|1\rangle}{\sqrt{2}}" title="\xrightarrow{H^{(n)}} \frac{1}{\sqrt{2^n}}\sum_{x=0}^{2^n-1}\sum_{y=0}^{2^n-1} (-1)^{s\cdot x + x\cdot y}|y\rangle \otimes \frac{|0\rangle - |1\rangle}{\sqrt{2}}" />  
<img src="https://latex.codecogs.com/gif.latex?\equiv&space;|s\rangle&space;\otimes&space;\frac{|0\rangle&space;-|1\rangle}{\sqrt{2}}&space;\xrightarrow{H_n}&space;|s\rangle&space;\otimes&space;|1\rangle" title="\equiv |s\rangle \otimes \frac{|0\rangle -|1\rangle}{\sqrt{2}} \xrightarrow{H_n} |s\rangle \otimes |1\rangle" />
