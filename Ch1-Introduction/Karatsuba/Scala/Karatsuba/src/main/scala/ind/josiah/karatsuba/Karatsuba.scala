package ind.josiah.karatsuba

import math.{max, sqrt}

object Karatsuba {
  def karatsuba(x: BigInt, y: BigInt): BigInt = {
    val n = max(numDigits(x), numDigits(y))
    val m = n / 2
    val (z2, z1, z0) = {
      val ((x1, x0), (y1, y0)) = (split(m, x), split(m, y))
      if (x.abs.max(y.abs)
            > sqrt(Math.pow(2, System.getProperty("sun.arch.data.model").toLong - 1) - 1).floor.round) {
        ( karatsuba(x1, y1)
        , karatsuba(x0 + x1, y0 + y1)
        , karatsuba(x0, y0)
        )
      } else {
        ( x1 * y1
        , (x0 + x1) * (y0 + y1)
        , x0 * y0
        )
      }
    }

    z2 * BigInt(10).pow(2 * m) + (z1 - z2 - z0) * BigInt(10).pow(m) + z0
  }

  private[this] def numDigits(num: BigInt): Int = Stream.from(0).dropWhile(i => num / BigInt(10).pow(i) > 0).head

  private[this] def split(i: Int, num: BigInt): (BigInt, BigInt) = num /% BigInt(10).pow(i)
}
