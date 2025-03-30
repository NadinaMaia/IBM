doubleMe :: Int -> Int
doubleMe x = x+x

--Ejercicio 1 a
f :: Int -> Int
f x | x== 1 = 8
    | x== 4 = 131
    | x== 16 = 16
    | otherwise = 0

--Ejercicio 1.b
g :: Int -> Int
g x | x== 8 = 16
    | x== 16 = 4
    | x== 131 = 1
    | otherwise = 0
--Ejercicio 1.c
h(x) = f(g(x))

--Ejercicio 2.a
f_absoluto :: Int -> Int
f_absoluto x | x>= 0 = x
             | x<0 = -x
             | otherwise = 0

--Ejercicio 2.b
max_absoluto :: Int -> Int -> Int
max_absoluto x y | f_absoluto x >= f_absoluto y = x
                 | f_absoluto y >= f_absoluto x = y
                 | otherwise = 0
--Ejercicio 2.d
algunoEs0 :: Int -> Int -> Bool
algunoEs0 x y | x == 0 || y == 0 = True
              | otherwise = False

--Ejercicio 2.e
ambosSon0 :: Int -> Int -> Bool
ambosSon0 x y | x == 0 && y == 0 = True
              | otherwise = False

--Ejercicio 2.f
mismoIntervalo :: Int -> Int -> Bool
mismoIntervalo x y | x <= 3 && y <= 3 = True
                   | x > 7 && y > 7 = True
                   | x > 3 && x <= 7 && y > 3 &&  y <= 7 = True
                   | otherwise = False

--sumaDistintos :: Int -> Int -> Int -> Int 
--sumaDistintos x y z |

--Ejercicio 2.h
esMultipoDeBool :: Int -> Int -> Bool
esMultipoDeBool x y | mod x y == 0 = True
                | otherwise = False

--Ejercicio 3
estanRelacionados :: Int -> Int -> Bool
estanRelacionados x y | mod x y == 0 = True
                      | otherwise = False

--Ejercicio 4. a
prodInt :: (Int, Int) -> (Int, Int) -> Int
prodInt (x, y) (z, w) = (x*z) + (y*w)
-- ??????

--Ejercicio 4.b
todoMenor :: (Int, Int) -> (Int, Int) -> Bool
todoMenor (x, y) (z, w) | fst (x,y) < snd (z, w) = True
                        | otherwise = False

--Ejercicio 4.c
--distanciaPuntos :: (Int, Int) -> (Int, Int) -> Int
--distanciaPuntos (x, y) (z, w) = sqrt((fst(x,y)**2)+(fst(z,w)**2)+(snd(x,y)**2+(snd(z,w))))

--Ejercicio 4.d
sumaTerna :: (Int, Int, Int) -> Int
sumaTerna (x,y,z) = x + y + z

--Ejercicio 4.e
esMultipoDeInt :: Int -> Int -> Int
esMultipoDeInt x y | mod x y == 0 = x
                | otherwise = 0

sumarSoloMultiplos :: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos (x, y, z) w = esMultipoDeInt x w +  esMultipoDeInt y w +  esMultipoDeInt z w

--Ejercicio 4.f
posPrimerPar :: (Int, Int, Int) -> String
posPrimerPar (x, y, z) | mod x 2 == 0 = "El primer elemento es par"
                     | mod y 2 == 0 = "El segundo elemento es par"
                     | mod z 2 == 0 = "El tercer elemento es par"
                     | otherwise = "4"

--Ejercicio 4.g
crearPar :: a -> b -> (a, b)
crearPar x y  = (x, y)

--Ejercicio 4.h
invertir :: (a,b)->(b,a)
invertir (x, y) = (y, x)

--Ejercicio 5
todosMenores :: (Int, Int, Int) -> Bool
todosMenores (x, y, z) | (f5(x)>g5(x)) && (f5(y)>g5(y)) && (f5(z)>g5(z)) = True
                       | otherwise = False

f5 :: Int -> Int
f5 x | x <= 7 = (x^2)
     | x > 7 = 2*x - 1

g5 :: Int -> Int
g5 x | mod x 2 == 0 = x `div` 2
     | otherwise = 3*x + 1

--Ejercicio 6
bisiesto :: Int -> Bool
bisiesto x | mod x 100 == 0 && mod x 400 /= 0  = False
           | mod x 4 == 0 = True
           | otherwise = True

--Ejercicio 7
calculoPrevio :: Float -> Float -> Float
calculoPrevio x y |x > y = x-y
                  | x < y = y-x

distanciaManhattan :: (Float,Float,Float)->(Float,Float,Float)->Float
distanciaManhattan (x, y, z) (h, i, j) = calculoPrevio x h + calculoPrevio y i + calculoPrevio z j

--Ejercicio 8
comparar :: Int -> Int -> Int
comparar a b | sumaUltimosDosDigitos (a) < sumaUltimosDosDigitos (b) = 1
                | sumaUltimosDosDigitos (a) > sumaUltimosDosDigitos (b) = -1
                | sumaUltimosDosDigitos (a) == sumaUltimosDosDigitos (b) = 0

sumaUltimosDosDigitos :: Int -> Int
sumaUltimosDosDigitos x = (mod x 10)+(mod (x `div` 10) 10)