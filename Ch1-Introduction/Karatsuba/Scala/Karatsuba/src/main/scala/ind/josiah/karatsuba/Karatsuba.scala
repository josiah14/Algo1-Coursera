package ind.josiah.karatsuba

object Karatsuba {
  def karatsuba(x: (BigInt, String), y: (BigInt, String)): BigInt = {
    x._1 * y._1
  }

  private[this] def numDigits(x: String): Int = Stream.from(0).dropWhile(i => (x / Math.pow(10, i)).toInt > 0)

  private[this] def split(i: Int, num: BigInt): (BigInt, BigInt) = num /% Math.pow(10, i).toInt
}
