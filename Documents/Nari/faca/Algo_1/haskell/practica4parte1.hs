--Ejercicio 1
fibonacci :: Integer -> Integer
fibonacci x | x == 0 = 0
            | x == 1 = 1
            | x>= 2 = fibonacci(x - 1) + fibonacci(x - 2)
            | otherwise = 0

--Ejercicio 2
parteEntera :: Float -> Integer
parteEntera n | n <= 0 && n < 1 = 0
              | n >=1 = 1 + parteEntera (n-1)
              | otherwise = (-1) + parteEntera (n+1)

--Ejercicio 3
esDivisible :: Integer -> Integer -> Bool
esDivisible x y | x == 0 = True
                | x >0 && esDivisible (x-y) y == True = True
                | otherwise = False


--Ejercicio 4
sumaImpares :: Integer -> Integer
sumaImpares n | n == 0 = 0
              | even n = sumaImpares (n-1)
              | otherwise = (sumaImpares (n-1)) + n

--Ejercicio 4 alternativo con un contador que no pude hacer andar 
--sumaImparesJ :: Integer -> Integer
--sumaImparesJ x = sumaImparesAux 0 x

--sumaImparesAux :: Integer -> Integer
--sumaImparesAux n x | x == 0 = 0
--                   | mod n 2 == 0 = sumaImparesAux (n + 1) x
--                   | mod n 2 /= 0 = n + (sumaImparesAux (n+1) (x-1))

--Ejercicio 5 
medioFact :: Integer -> Integer
medioFact n | n == 0  || n == (-1) = 1
            | otherwise = n * (medioFact (n-2))

--Ejercicio 6
sumaDigitos :: Integer -> Integer
sumaDigitos x | x < 10 = x
              | x >= 10 = mod x 10 + sumaDigitos (div x 10)
              | otherwise = 0

--Ejercicio 6 otra alternativa
--sumaDigitos :: Integer ->Integer
--sumaDigitos 0 = 0
--sumaDigitos n = mod n 10 + sumaDigitos (div n 10)

--Ejercicio 7
ultimoDigito :: Integer -> Integer
ultimoDigito x = mod x 10

sacarUltimoDigito :: Integer -> Integer
sacarUltimoDigito x = div x 10

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales x | x < 10 = True
                      | x >= 10 && todosDigitosIguales(ultimoDigito x)==todosDigitosIguales(sacarUltimoDigito x) = True
                      | otherwise = False

--Ejercicio 8
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | n > 0 = error "Igresar n >= 0"
                 | i > (cantDigitos n) || i < 1 = error "Ingresar i valido"
                 | otherwise = (mod(div n (10 ^((cantDigitos n) - 1))) 10)

cantDigitos :: Integer -> Integer
cantDigitos n | n < 10 = 1
              | n < 0 = error "ingresar n >= 0"
              | otherwise = 1 + cantDigitos (div n 10)

--la consigna decia {n=0→(n div 10 ^(resultado−1)>0 ∧ n div 10 ^(resultado) = 0)}

--Ejercicio 9
esCapicua :: Integer -> Bool
esCapicua n | n < 10 && n >= 0 = True
            | n <= 999 = ultimoDigito n == primerDigito n
            | n > 999 && ultimoDigito n == primerDigito n = esCapicua(quitarUltPrim n)
            | n > 999 && ultimoDigito n /= primerDigito n = False
            | otherwise = error "Ingrese numero positivo"

primerDigito :: Integer -> Integer
primerDigito n | n < 10 = n 
               | n >= 10 = primerDigito (div n 10)
               | otherwise = error "Ingrese n positivo"

quitarUltPrim :: Integer -> Integer
quitarUltPrim n = div (n - (primerDigito n * (10^((cantDigitos n) - 1)))) 10

--Ejercicio 10


--Ejercicio 11
eAprox :: Integer -> Float
eAprox 1 = 1
eAprox n = 1/(factorial n) + eAprox(n-1)

factorial :: Integer -> Float --lo cambie porque me tiraba error pero porque no lo toma? si factorial es un entero pero el resultado es un float
factorial 1 = 2
factorial x = fromIntegral (x) * factorial (x-1)

e :: Float
e = eAprox 10

--Ejercicio 12
raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = sucesion n - 1

sucesion :: Integer -> Float --porque devuelvo float y no int?
sucesion n |n == 1 = 2
           |otherwise = 2 + (1/raizDe2Aprox (n - 1))

--Ejercicio 15
--sumaRacionales :: Num -> Num -> Num
--sumaRacionales n m | n == 1 = sumaInterna 1 m 1
--                   | n = sumaInterna n m 1 + sumaRacionales (n - 1) m 


--sumaInterna :: Num -> Num -> Num -> Num
--sumaInterna p m q | m == 1 = 1
--                  | m > 1 && q <= m = ((p/q) + (sumaInterna p m (q + 1)))
--                  | m > 1 && q > m = 0

--Ejercicio 16
menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde n 2

--Ej no de la guia
menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde n desde | mod n desde == 0 = desde
                          | otherwise =  menorDivisorDesde n (desde + 1)

--Ejercicio 16.b
esPrimo :: Integer -> Bool
esPrimo n = menorDivisor n == n

--Ejercicio16c PREGUNTAR 
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos x y | menorDivisor x /= menorDivisor y = True
                | otherwise = False

--armarDivisores :: Integer -> [Integer]
--armarDivisores x | esPrimo x = [x]
--                 | menorDivisorDesde x (2 + 1)

--Ejercicio 17
esFibonacci :: Integer -> Integer -> Bool
esFibonacci n x | n == fibonacci 0 = True
                | n == fibonacci 1 = True
                | n == fibonacci x = True
                | fibonacci x < n = esFibonacci n (x + 1) 
                | otherwise = False

--Ejercicio 18
listaDigitos :: Integer -> [Integer]
listaDigitos x | x < 10 = [x]
               | otherwise = [mod x 10] ++ listaDigitos (div x 10)

listaDigitosPar:: [Integer] -> [Integer]
listaDigitosPar [] = []
listaDigitosPar [x] | even x == True = [x]
                    | otherwise = []
listaDigitosPar (x:xs) | even x == True = [x] ++ listaDigitosPar xs
                       | otherwise = [] ++ listaDigitosPar xs

armarListaPares :: Integer -> [Integer]
armarListaPares x = listaDigitosPar(listaDigitos x)

mayorDigitoPar :: Integer -> Integer
mayorDigitoPar x = maximum (armarListaPares x)