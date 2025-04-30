object HelloWorld{
  def main(args : Array[String]) : Unit = {
    var num1 = scala.io.StdIn.readInt()
    var num2 = scala.io.StdIn.readInt()
    var sym = scala.io.StdIn.readLine()
    if(sym == "+") {
      print(num2 + num1)
    }
    if(sym == "-") {
      print(num2 - num1)
    }
    if(sym == "/") {
      print(num2 / num1)
    }
    if(sym == "*") {
      print(num2 * num1)
    }
  }
}
