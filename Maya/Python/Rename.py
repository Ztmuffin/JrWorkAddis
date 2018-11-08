import maya.cmds as cmds


def Selection(string $p1,string $p2,int $numbPad)
{
    //Grab selection and init $object
    string $sels[] = `ls -sl`;
    string $object;
    
    //Get and print the Array size
    $arraySize = size($sels);
    print ("Objects Selected " + $arraySize + "\n");
    
    //assign p1 and p2 to strings
    string $newname = $p1;
    string $newSuffix = $p2;
    
    //this int is going to be the incramenting number for use in Incrementor
    int $newNumber = 00;
    string $zero = "0";
    int $numbPadd = $numbPad;
   
           
    // For each object in the selection do this:
    for($object in $sels)
    {
        print ("this object was " +$object + "\n");
        
        // generate number
        if ($numbPadd > 1 && $newNumber <10)
        {
        rename $object($newname + $zero + $newNumber + $newSuffix);
        print ("this object is now " + $p1 + $newNumber + $p2 + "\n");
        $newNumber++;
        }
        else
        {
        $newNumber++;
        rename $object($newname + $newNumber + $newSuffix);
        }
        
        print ("this object is now " + $p1 + $newNumber + $p2 + "\n");
    }
}

global proc Renaming(string $splitThis)
{
    //take input and tokenize it.
	string $name[];
	tokenize $splitThis "#" $name;
	
	//assign strings to each part of array
	string $part1 = $name[0];
	string $part2 = $name[1];
	
	print ($splitThis + "\n");
	print ($part1+ "\n");
	print ($part2+ "\n");
	
	//get the sizes
    $stringSize = size($splitThis);
    print("The whole string size" + $stringSize);
    int $noPadChars = size($part1) + size($part2);
    print("the letter characters" + $noPadChars);
    int $numberPadding = $stringSize - $noPadChars;
    print("The Padding is" + $numberPadding);
    

    
	
	//Call Selection Function
    Selection($part1,$part2,$numberPadding);

}
    //init default string
        string $stringToSplit;
    //Check if window with this name exists delete window if so

        if (`window -exists RenameWindow`) deleteUI -window RenameWindow;

    //make new window 
        window RenameWindow;
        columnLayout;
    //i'm using uneditable fields to give instruction
        text -label "Renaming Rules";
        scrollField -wordWrap true -height 60 -text "This will rename all selected items based off of the name of the first name you enter here" -editable false;
        scrollField -wordWrap true -height 60 -text "Type the name you want with a '#' in between first half and last half, EXAMPLE BELOW" -editable false;

    //now this is what the user enters ast the first option. the renamer will calculate the rest.
        string $userInput = `textFieldGrp -label "Renamer" -text "firstPart_#_LastPart"`;
        button -label "Print Text" -command ("string $currentUsersInput = `textFieldGrp -q -text $userInput`; print($currentUsersInput)");   
        print ($stringToSplit);

    //Call Renaming with this button by getting what the user put in. assigning it to the string to split and running rename.
        button -label "Rename all Selected" -command ("$stringToSplit = `textFieldGrp -q -text $userInput`; string $currentUsersInput = `textFieldGrp -q -text $userInput`; Renaming($stringToSplit)");
global proc Selection(string $p1,string $p2,int $numbPad)
{
    //Grab selection and init $object
    string $sels[] = `ls -sl`;
    string $object;
    
    //Get and print the Array size
    $arraySize = size($sels);
    print ("Objects Selected " + $arraySize + "\n");
    
    //assign p1 and p2 to strings
    string $newname = $p1;
    string $newSuffix = $p2;
    
    //this int is going to be the incramenting number for use in Incrementor
    int $newNumber = 00;
    string $zero = "0";
    int $numbPadd = $numbPad;
   
           
    // For each object in the selection do this:
    for($object in $sels)
    {
        print ("this object was " +$object + "\n");
        
        // generate number
        if ($numbPadd > 1 && $newNumber <10)
        {
        rename $object($newname + $zero + $newNumber + $newSuffix);
        print ("this object is now " + $p1 + $newNumber + $p2 + "\n");
        $newNumber++;
        }
        else
        {
        $newNumber++;
        rename $object($newname + $newNumber + $newSuffix);
        }
        
        print ("this object is now " + $p1 + $newNumber + $p2 + "\n");
    }
}

global proc Renaming(string $splitThis)
{
    //take input and tokenize it.
	string $name[];
	tokenize $splitThis "#" $name;
	
	//assign strings to each part of array
	string $part1 = $name[0];
	string $part2 = $name[1];
	
	print ($splitThis + "\n");
	print ($part1+ "\n");
	print ($part2+ "\n");
	
	//get the sizes
    $stringSize = size($splitThis);
    print("The whole string size" + $stringSize);
    int $noPadChars = size($part1) + size($part2);
    print("the letter characters" + $noPadChars);
    int $numberPadding = $stringSize - $noPadChars;
    print("The Padding is" + $numberPadding);
    

    
	
	//Call Selection Function
    Selection($part1,$part2,$numberPadding);

}
    //init default string
        string $stringToSplit;
    //Check if window with this name exists delete window if so
        if (`window -exists RenameWindow`) deleteUI -window RenameWindow;

    //make new window 
        window RenameWindow;
        columnLayout;
    //i'm using uneditable fields to give instruction
        text -label "Renaming Rules";
        scrollField -wordWrap true -height 60 -text "This will rename all selected items based off of the name of the first name you enter here" -editable false;
        scrollField -wordWrap true -height 60 -text "Type the name you want with a '#' in between first half and last half, EXAMPLE BELOW" -editable false;

    //now this is what the user enters ast the first option. the renamer will calculate the rest.
        string $userInput = `textFieldGrp -label "Renamer" -text "firstPart_#_LastPart"`;
        button -label "Print Text" -command ("string $currentUsersInput = `textFieldGrp -q -text $userInput`; print($currentUsersInput)");   
       // print ($stringToSplit);

    //Call Renaming with this button by getting what the user put in. assigning it to the string to split and running rename.
        button -label "Rename all Selected" -command ("$stringToSplit = `textFieldGrp -q -text $userInput`; string $currentUsersInput = `textFieldGrp -q -text $userInput`; Renaming($stringToSplit)");
global proc RenamingWindow()
{
        showWindow RenameWindow;
}

RenamingWindow();