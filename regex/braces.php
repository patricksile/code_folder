<?php
    (?=(?'whole'(?<!\\)
  (?'open'
    \[
    (?=
      #recurses and matches the contents of the bracket, this part is for validation
      (?&content)
      \]
    )|
    \(
    (?=
      #anyway I added an escape character. Has to be possessive or it can create false positives. See also: lookbehind at the start.
      (?&content)
      \)
    )|
    \{
    (?=
      (?&content)
      \}
    )
  )
  (?'content'
    #this part captures the contents even though they're not consumed
    (?>[^{}[\]()\\]+|\\[{}[\]()\\]?|(?&whole))*
  )
  (?'close'[\]\)}])
))
#this is the only part that actually consumes characters. Let's move on to the next match already!
(?P=open)

?>
<?php
(?=(?'whole'(?'open'\[(?=(?&content)\])|\((?=(?&content)\))|\{(?=(?&content)\}))(?'content'(?>[^{}[\]()\\]+|(?&whole))*)(?'close'[\]\)}])))
(?P=open)
?>
