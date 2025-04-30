object HelloWorld{
  def main(args: Array[String]): Unit = {
    print("Enter the number")
    val num = scala.io.StdIn.readInt()
    for (i <- 2 until num) {
      if (num % i == 0) {
        println("Not prime number\n")
        return 
      }
    }
    println("Prime number")
  }
}
