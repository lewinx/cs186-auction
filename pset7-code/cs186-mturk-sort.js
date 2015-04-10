// Problem 4. Sort images

var pictures = ["WPLAo.jpg","Sbkem.jpg","SzBIk.jpg","ZiusC.jpg", "r53qG.jpg","RNfpa.jpg","XcGBz.jpg","YdL3d.jpg"]

// TO-DO: Add "http://i.imgur.com/"    at the beginning of every picture id
pictures = pictures.map(<YOUR CODE>)

//  Creates a webpage of two images side-by-side
function getPicsPage(pic1, pic2) {

var text=  "Which picture comes before the other chronologically? (Type 'Left' or 'Right')"

// TO-DO:   Expand on our HTML design. Do you think a different design could better?
// Provide evidence.
var webpage = createWebpageFromTemplate(<div>
        <img src={pic1} width="45%" alt="Image 1"></img>
	   <img src={pic2}  width="45%" alt="Image 2"></img>
        <ul>
            <li>People will vote whether to approve your work.</li>
        </ul>
        <textarea style="width:500px;height:50px" name="newText">{text}</textarea>
        <input type="submit" value="Submit"></input>
    </div>);

	return webpage;
}

// TO-DO : Create a comparison HIT
var h = {title : "Sort Two Pictures", 
        desc : "Decide which photo was taken earlier", 
        url: <YOUR CODE>, 
        height : <YOUR CODE>, 
	    reward : <YOUR CODE>, 
	    maxAssignments : <YOUR CODE>}

var hit = mturk.createHIT(h)

// TO-DO: Expand code to order all provided images.