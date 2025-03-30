--7 
todosDigitosIguales :: Int -> Bool
todosDigitosIguales x | n < 10 = True
                      | n >= to = primerDigito == segundoDigito && todosDigitosIguales(sacarPrimerDigito n)
                 
primerDigito n = n `mod` 10
segundoDigito n (n `div` 10) `mod` 10
sacarPrimerDigito = n `div` 10

--6
sumaDigitos :: Int -> Int
sumaDigitos x | n < 10 = True
              | n >= to = primerDigito + sumarDigitos

todosDigitosIguales :: Int -> Bool
todosDigitosIguales x | x < 10 = True
                      | x >= 10 && todosDigitosIguales(ultimoDigito x)==todosDigitosIguales(sacarUltimoDigito x) = True
                      | otherwise = False