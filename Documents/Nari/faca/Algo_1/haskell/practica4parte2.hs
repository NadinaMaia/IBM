--Ejercicio 19
esSumaInicialDePrimos :: Int -> Bool
esSumaInicialDePrimos suma = esSumaInicialDePrimosHasta suma 2

--esSumaInicialDePrimosHasta :: Int -> Int -> Bool
esSumaInicialDePrimosHasta suma hasta | sumaPrimos hasta == suma = True
                                      | sumaPrimos hasta > suma = False 
                                      | otherwise = esSumaDePrimosHasta suma (hasta + 1)

--sumaPrimos :: Int -> Int
sumaPrimos 2 = 2
sumaPrimos n | esPrimo n = n + sumaPrimos (n-1)
             | otherwise = sumaPrimos (n-1)

--Ejercicio 14
--sumaPotencias :: Integer -> Integer -> Float