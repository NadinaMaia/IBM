--tupla es con parentesis, y corchetes para listas
tuplaValida :: (String, String) -> Bool
tuplaValida (a,b) | a == b = False
                  | otherwise = True

compararTuplas :: (String, String) -> (String, String) -> Bool
compararTuplas (a,b) (c,d) | a == c && b == d = True
                           | a == d && b == c = True
                           | otherwise = False

--Ejercicio 1
relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = error "Le ingresaron una lista vacia"  
relacionesValidas [_] = False
relacionesValidas (x:y:xs) | tuplaValida x && compararTuplas x y = relacionesValidas (xs)
                           | otherwise = False
-------------

desarmarTupla :: (String, String) -> [String]
desarmarTupla (a,b) = [a,b]


quitarDuplicados :: [String] -> [String]
quitarDuplicados [] = []
quitarDuplicados (x:xs) | perteneceLista x xs = quitarDuplicados xs
                        | otherwise = x : quitarDuplicados xs 

perteneceLista :: String -> [String] -> Bool
perteneceLista _ [] = False 
perteneceLista n [x] | n == x = True
                     | n /= x = False
perteneceLista n (x:xs) | n /= x = perteneceLista n xs 
                        | otherwise = True

--Ejercicio 2
personas :: [(String, String)] -> [String]
personas [] = []
personas ((a,b):xs) = quitarDuplicados (desarmarTupla (a,b) ++ personas xs)
-------------

perteneceTupla :: String -> (String, String) -> Bool
perteneceTupla n (a,b) | n == a || n == b = True
                       |otherwise = False

--Ejercicio 3
amigosDe :: String -> [(String, String)] -> [String]
amigosDe _ [] = []
amigosDe n ((a,b):xs) | perteneceTupla n (a,b) = quitarDuplicados(desarmarTupla (a,b) ++ amigosDe n xs)
                      | otherwise = quitarDuplicados(amigosDe n xs)
-------------

--Ejercicio 4
desarmarListaDeTuplas :: [(String, String)] -> [String]
desarmarListaDeTuplas [] = []
desarmarListaDeTuplas ((a,b):xs) = [a,b] ++ desarmarListaDeTuplas xs

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos [t] = [t]
eliminarRepetidos (x:xs) | x == (head xs) = [x] ++ eliminarRepetidos (tail xs)
                         | otherwise = [x] ++ eliminarRepetidos (tail xs)


compararAmigos :: [String] -> String
compararAmigos [] = []
compararAmigos [x] = [x]
compararAmigos (x:y:xs) | mayorPrimero = compararAmigos (x:xs)
                        | otherwise = compararAmigos (y:xs)
                      where 
                        mayorPrimero = contarRepetido x xs >= contarRepetido y xs 


--Devuelve el nombre de la persona que mas se repitio en la lista
personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos [] = []
personaConMasAmigos lista = compararAmigos (desarmarListaDeTuplas lista)


contarRepetido :: String -> [String] ->Integer
contarRepetido _ [] = 0
contarRepetido n (x:xs) | n == x = 1 + contarRepetido n xs
                        | otherwise = contarRepetido n xs 
