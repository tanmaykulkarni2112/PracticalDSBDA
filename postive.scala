object HelloWorld {
	def main(args: Array[String]): Unit = {
	println("Enter the number")
	var num = scala.io.StdIn.readInt()
	if (num > 0) {
	  printf(num + " is positive")
	} else {
	  print(num + " is negative")
	}
	}
}
