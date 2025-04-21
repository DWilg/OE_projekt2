Projekt 2 – implementacja chromosomu rzeczywistego
1. Zmodyfikuj wcześniej przygotowany projekt klasycznego algorytmu genetycznego.
2. Zaimplementuj reprezentację rzeczywistą zamiast binarnej.
3. Zaimplementuj operatory krzyżowania arytmetycznego, linearnego, mieszającego
typu alfa, mieszającego typu alfa i beta oraz uśredniającego.
4. Zaimplementuj mutację równomierną oraz mutację Gaussa.
5. Porównaj wyniki osiągnięte przez klasyczną reprezentacje chromosomu, rzeczywistą
reprezentacje chromosomu.
6. Przygotuj sprawozdanie do projektu. Powinno ono zawierać:
a) Informacje o wykorzystywanych technologiach do wykonania projektu
b) Wzór i wykres optymalizowanej funkcji
c) Wymagania środowiska do uruchomienia aplikacji
d) Wykresy zależności wartości funkcji celu od kolejnej iteracji
e) Średniej wartości funkcji celu oraz odchylenia standardowego w kolejnej iteracji
f) Porównanie osiągniętych wyników przy różnych konfiguracjach algorytmu +
porównanie czasu obliczeń
g) Porównanie wyników osiągniętych poprzez klasyczną oraz rzeczywistą reprezentacje
chromosomu
7. Wykorzystaj gotowe biblioteki zawierające implementacje funkcji 
import benchmark_functions as bf
from opfunu import cec_based
#benchmark_functions
#pip install benchmark_functions
func = bf.Hyperellipsoid(n_dimensions=10)
print(func.suggested_bounds())
print(func.minimum())
#cec
#pip install opfunu
func = cec_based.cec2014.F32014(ndim=10)
print(func.bounds)
print(func.x_global)
print(func.f_global)
8. Projekt i sprawozdanie wgraj na platformę Delta – 1 członek zespołu. 