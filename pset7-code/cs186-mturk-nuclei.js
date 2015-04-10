// Problem 3.  Count # nuclei in an image. 

// TO-DO: Define the payments.	
    var nucleiHITcost = <YOUR CODE>
    
    var hitId = createNucleiHIT(nucleiHITcost)
	print("New hit was created.");
 // The code will post the assignment and then stop. 
 // When you see that an answer was submitted, then "Run" the code again.
 // It will automatically create the voting HITs
    var hit = mturk.waitForHIT(hitId)

//  Get the answer.
    var ansCount = hit.assignments[0].answer.IdNuclei
    print("-------------------")
    print("MTurk says there are "+ansCount+" nuclei in picture.")
    print("-------------------")
    
// TO-DO:  Payment for voting.
    var votingCost = <YOUR CODE>
    if (vote(ansCount, votingCost)) {
        mturk.approveAssignment(hit.assignments[0])
        print("\nConsensus reached!\n")
    } else {
        mturk.rejectAssignment(hit.assignments[0])
        print("\nNumber "+ansCount+" was not voted as correct\n")
    }    


////    1.   Creates the main Nuclei HIT    /////
function createNucleiHIT(argCost) {
    default xml namespace = "http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/QuestionForm.xsd";
    var q = <QuestionForm>
        <Question>
            <QuestionIdentifier>IdNuclei</QuestionIdentifier>
            <IsRequired>true</IsRequired>
            <QuestionContent>
                <FormattedContent><![CDATA[
<ul>
<li>Please count the number of nuclei in the left picture.</li>
<li>People will vote whether to approve your work.</li>
</ul>
<img src="http://i.imgur.com/JyGlt.jpg" alt="Nuclei"></img>
]]></FormattedContent>
            </QuestionContent>
            <AnswerSpecification>
                <FreeTextAnswer>
                    <Constraints>
                        <IsNumeric minValue="0" />
                    </Constraints>
                    <NumberOfLinesSuggestion>1</NumberOfLinesSuggestion>
                </FreeTextAnswer>
            </AnswerSpecification>
        </Question>
    </QuestionForm>
    
    // TO-DO create the HIT (use the question form above)
    return mturk.createHIT(<YOUR CODE>)
}


//    2.   Vote.  For the results.  
//    argNucleiCount =  the response we will get in the Nuclei counting HIT
//     argVoteCost =   how much to spend on this hit
function vote(argNucleiCount, argVoteCost) {
	print("In vote function");
    default xml namespace = "http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/QuestionForm.xsd";
    var q = <QuestionForm>
        <Question>
            <QuestionIdentifier>vote</QuestionIdentifier>
            <IsRequired>true</IsRequired>
            <QuestionContent>
                <FormattedContent><![CDATA[
<ul>
<li>Please count the number of nuclei in the left picture.</li>
</ul>
<img src="http://i.imgur.com/JyGlt.jpg" alt="Nuclei"></img>
]]></FormattedContent>
            </QuestionContent>
            <AnswerSpecification>
                <SelectionAnswer>
                    <Selections>
                    </Selections>
                </SelectionAnswer>
            </AnswerSpecification>
        </Question>
    </QuestionForm>

    var options = [{key:"y",value:"Close (+-5) of "+argNucleiCount}, 
		    {key:"n",value: "Not close to "+argNucleiCount}]
    //shuffle(options)
    foreach(options, function (op) {
        default xml namespace = "http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/QuestionForm.xsd";
        q.Question.AnswerSpecification.SelectionAnswer.Selections.Selection +=
            <Selection>
                <SelectionIdentifier>{op.key}</SelectionIdentifier>
                <Text>{op.value}</Text>
            </Selection>
    })
   
// TO-DO:   Create the voting HIT 
   var voteHitId = mturk.createHIT(<YOUR CODE>)

    var voteResults = mturk.vote(voteHitId, function (answer) {
             return (answer.vote) })
    print ("Voting result was " + voteResults.bestOption );
    return voteResults.bestOption == "y"

}