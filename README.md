# homestuck-vocabulary
Analyzes Homestuck vocabulary


From http://homestuck.obdurodon.org/XML-Homestuck.html :

The first step in analyzing Homestuck was creating an XML version of the text in the webcomic. We began using the HTML of the Homestuck webcomic's archive and transformed this HTML version using XSLT. You can view the XML here.

The XML we created accomplishes several things. It wraps each line of speech in the PESTERLOG with <line> elements, and each <line> tag has an attribute with that line's speaker's initials. The narrator's lines of speech are wrapped in <p> tags. The <p> tags are relics from the XML file's past as HTML. This formatting allows a computer to analyze each character's lines separately. An example of a line of speech from TG appears like this in the XML:

<line speaker="TG">monster B-list celebrity douchebags are cunning and persistent pranksters</line>

Our XML version also "normalizes" characters' speech who speak with distinctive quirks. For example, the character GC uses the numeral 1 instead of "I", 3 instead of "E", and 4 instead of "A". A computer will not read GC's speech CONF1D3NC3 as the word "confidence" unless a human appropriately notifies it to do this. In the XML version of Homestuck, each normalized character's original word is wrapped in <word> tags. Inside each of the <word> elements, an <ow> element contains the speaker's original word, and an <nw> element contains the normalized version of this word. Therefore, one line of GC's speech looks like this:

<line speaker="GC"><word><ow>WH4T!!!</ow><nw>WHAT!!!</nw></word></line>

This format allows us to toggle between the two forms of the speech. We can use either form for our research.

This XML version also puts every instance of profanity in speech into <profanity> elements. Any given profane word can appear in many different ways. The word "shit" appears in various forms, such as "bullshit", "batshit", "chumpeldipshit", and "AAAAAAAAAAAAAAAAAAAAAWWWWWWWWWWWWWWOHSHIT.". In order to group these forms together so that they could be analyzed as variations of the word "shit", we put these words into a <profanity> element with an attribute "type" equal to "shit". One of the narrator's lines containing profanity appears like this in the XML version of Homestuck:

<p>The <profanity type="hell">hell</profanity> with it. You try to take the entire JUMBLE <profanity type="shit">OFUNBELIEVABLYSHITTYSWORDS</profanity> and brace yourself for...</p> 