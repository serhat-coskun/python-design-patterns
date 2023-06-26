# python-design-patterns
Design patterns implemented in python

Note that there are 2 approaches to design patterns in Python:

	1- Traditional approach: Defeats the purpose of pythoni, not used much in practice
	2- Pythonic way of solving same problems
	

DECORATOR PATTERN:

Upgrade the object/function to have new functionality without changing how client interracts with it. For example can be used to add logging. Client does not see any change, but internally each function call is logged. A similar use case is caching, for pure functions (functions that return same output for same input).

How to: Use composition, while object that stores the decorated object maintains the same interface with the original. Handle additional logic in the implementation of common interface.

Notes:

 * Multiple decorators can be stacked
 * First object/function to be decorated is the core and handles the expected operation by client
 * Decorator is an alternative to inheritance, instead of decorator pattern we could have define a subclass of X, called LoggedX and override its methods to implement logging behaviour. Considerations:
 	
 	1. If behaviour of the object needs to change dynamically such as debug and production mode which activates or deactivates logging, we should prefer decorator pattern. Consider class X and its subclass LoggingX. 
 		
 		if flag:
 			obj = LoggingX() 
 		else:
 			obj = X()
 	This approach seems ok at sight. But consider the case where X is instantiated beforehand, and it holds state. Then:
 	
 		if flag:
 			obj = LoggingX()
 			
 	Using this approach we would lose the original state of the X.
 	
 	
 	2. Decorators are generally implemented order independent, hence they can be easily stacked. In contrast iheritance locks the order. If Z inherits from Y, which inherits from X. We cannot exclude Y when using Z.
 	
 	Greatest disadvantage of the decorator is the need to define each property and functionality for the decorators interface. However, this might not be a need generally since client of the decorator might be using a subset of the decorated objects interface.
 	
* Used frequently for handling cross-cutting concerns such as logging, caching, and validation. 
 		
