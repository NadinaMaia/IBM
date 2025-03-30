--Ejercicio 1.1
longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

--Ejercicio1.2
ultimo :: [t] -> t
ultimo [] = error "esta vacio"
ultimo [x] = x
ultimo (x:xs) = ultimo (xs)

--Ejercicio 1.3
principio :: [t] -> [t]
principio [] = error "esta vacio"
principio [_] = []
principio (x:xs) = x : principio xs

--Ejercicio 1.4
reverso :: [t] -> [t]
reverso [] = []
reverso [x] = [x]
reverso (x:xs) = reverso xs ++ [x]

--Ej2
--Ejercicio 1
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece n (x:xs) | n == x = True
                   | otherwise = pertenece n xs

--Ejercicio 2
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = False
todosIguales (x:xs) | longitud xs == 0 = True
                    | x /= head xs = False
                    | otherwise = todosIguales xs

--Ejercicio 3
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = False
todosDistintos (x:xs) | longitud xs == 0 = True
                      | x /= head xs = todosDistintos xs
                      | otherwise = False

--Ejercicio 4
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos lista  | todosDistintos lista = False
                    | otherwise = True

--Ejercicio 5
quitar :: (Eq t) => t -> [t] -> [t]
quitar x xs | x == head xs = [] ++ tail xs
            | otherwise = [head xs]

--Ejercicio 6
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos x xs | x == head xs = [] ++ quitarTodos x (tail xs)
                 | otherwise = [head xs] ++ quitarTodos x (tail xs)

--Ejercicio 7
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | x == (head xs) = [] ++ eliminarRepetidos (tail xs)
                         | otherwise = [x] ++ eliminarRepetidos (tail xs)

--Ejercicio 8
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] [] = True
mismosElementos lista1 lista2 | pertenece (head lista1) lista2 && pertenece (head lista2) lista1 = True
                              | otherwise = False

--Ejercicio 9
capicua :: (Eq t) => [t] -> Bool
capicua [_] = True
capicua xs | reverso xs == xs = True
           | otherwise = False

--Ej 3
--Ejercicio 3.1
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria [x] = x
sumatoria (x:xs) = x + sumatoria xs

--Ejercicio 3.2
productoria :: [Integer] -> Integer
productoria [] = 0
productoria (x:xs) | length xs == 0 = x
                   | otherwise = x * productoria xs

--Ejercicio 3.3
maximo :: [Integer] -> Integer
maximo [] = error "Esta vacia la lista, no hay maximo"
maximo [a] = a
maximo (x:y:xs) | x >= y = maximo (x:xs)
                | otherwise = maximo (y:xs)

--Ejercicio 3.4
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n [x] = [x+n]
sumarN n (x:xs) = [x+n] ++ sumarN n xs

--Ejercicio 3.5
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero xs = sumarN (head xs) xs

--Ejercicio 5.2
descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = divisoresPrimos x 2 : descomponerEnPrimos xs

divisoresPrimos :: Integer -> Integer -> [Integer]
divisoresPrimos 1 _ = []
divisoresPrimos n divisor | divisor > n = []
                           | otherwise = buscarDivisores
                           where
                            buscarDivisores | mod n divisor == 0 = [divisor] ++ divisoresPrimos (div n divisor) (divisor)
                                            | otherwise = divisoresPrimos n (divisor + 1)
