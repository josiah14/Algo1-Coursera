module Karatsuba0 where
import Data.Bits (bitSize)

karatsuba :: Integer -> Integer -> Integer
karatsuba x y =  z2 * (10 ^ (2 * m)) + (z1 - z2 - z0) * (10 ^ m) + z0
  where m            = n `div` 2
        n            = max (numDigits x) $ numDigits y
        (z2, z1, z0) = if abs (max x y) > (floor . sqrt $ 2^(bitSize (1 :: Int) - 1) - 1)
                       then ( karatsuba x1 y1
                            , karatsuba (x0 + x1) (y0 + y1)
                            , karatsuba x0 y0
                            )
                       else ( x1 * y1
                            , (x0 + x1) * (y0 + y1)
                            , x0 * y0
                            )
                       where ((x1, x0), (y1, y0)) = (split m x, split m y)

numDigits :: Integer -> Int
numDigits x = head $ dropWhile (\i -> x `div` 10^i > 0) [0..]

split :: Int -> Integer -> (Integer, Integer)
split i num = quotRem num (10^i)

