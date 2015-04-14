// Problem 4. Sort images

var pictures = ["WPLAo.jpg","Sbkem.jpg","SzBIk.jpg","ZiusC.jpg", "r53qG.jpg","RNfpa.jpg","XcGBz.jpg","YdL3d.jpg"]

// TO-DO: Add "http://i.imgur.com/" at the beginning of every picture id
pictures = pictures.map(add_img)

//function to make secure
function makeSecure(url) {
        return url.substring(0, 4) + "s" + url.substring(4);
    }

//function to add http
function add_img(url_end) {
        return "http://i.imgur.com/" + url_end;
    }


//  Creates a webpage of two images side-by-side
function getPicsPage(pic1, pic2, pic3, pic4, pic5, pic6, pic7, pic8) {

var text=  "Which picture comes before the other chronologically? (Type 'Left' or 'Right')"

// TO-DO:   Expand on our HTML design. Do you think a different design could better?
// Provide evidence.
var webpage = createWebpageFromTemplate(<div>
        <img src={pic1} width="45%" alt="Image 1"></img>
        <img src={pic2}  width="45%" alt="Image 2"></img>
        <br></br>
        <img src={pic3} width="45%" alt="Image 3"></img>
        <img src={pic4}  width="45%" alt="Image 2"></img>


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
        url: makeSecure(getPicsPage(pictures[0], pictures[1], pictures[2], pictures[3], pictures[4], pictures[5], pictures[6], pictures[7])), 
        height : 1600, 
	    reward : .02, 
	    maxAssignments : 100}

var hit = mturk.createHIT(h)

// TO-DO: Expand code to order all provided images.




