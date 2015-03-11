module Karatsuba where

karatsuba :: Integer -> Integer -> Integer
karatsuba num1 num2 = formula (show num1) (show num2)

formula :: String -> String -> Integer
formula x y = z2 * (10 ^ (2 * m)) + (z1 - z2 - z0) * (10 ^ m) + z0
  where m = maxDigits x y `div` 2
        (z2, z1, z0)
          | maxDigits x y > 2 = ( formula x1 y1
                                , formula (show (read x0 + read x1 :: Integer)) (show (read y0 + read y1 :: Integer))
                                , formula x0 y0
                                )
          | otherwise         = ( read x1 * read y1 :: Integer
                                , (read x0 + read x1 :: Integer) * (read y0 + read y1 :: Integer)
                                , read x0 * read y0 :: Integer
                                )
          where ((x1, x0), (y1, y0)) = (splitNum x, splitNum y)

maxDigits :: String -> String -> Integer
maxDigits x y = max (toInteger $ length x) $ toInteger $ length y

splitNum :: String -> (String, String)
splitNum n
  | even numDigits = split n numDigits
  | otherwise      = split ('0':n) (numDigits + 1)
  where numDigits = length n
        split n' numDigits' = splitAt (ceiling $ fromIntegral numDigits' / (2 :: Double)) n'

