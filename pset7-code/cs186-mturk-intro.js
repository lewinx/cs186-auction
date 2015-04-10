// Problem 1.  Warming up

// TO-DO:  Find the functions to print your balance and the # of open hits.
print("Hello MTurk!")
print("Your balance is: " + <YOUR CODE>  )
print("No. of hits: "+ <YOUR CODE> )

// Explore the HIT object. 
// Get the first HIT and then iterate over its properties.
if(mturk.getHITs().length>0) {
	var hitObj = <YOUR CODE> 
	for(attr in hitObj) 
		print("Attr ="+attr+ " val="+hitObj[attr])
}

