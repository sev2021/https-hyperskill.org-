<h2>CRAZY PYTHON LOOPS</h2>
<em>HTML works</em>
<p>
  How to hest for-in lopps? <br />
  It is not simle...
  Imagine you have sub-list like that:
  
  text = [("abc","def"),("ghi","ijk"),("lmn","opr")]
  
  text<br />
  >>[tuple<br />
  >>>>[string<br />
  >>>>>>[letter<br />
  
  Loop to iterate inside text:<br />
  for <b>tuple</b> in text   # this will return list of tuples<br />
  <br />
  We have tuples, now we want to iterete inside them:<br />
  for tuple in text + for string in tuple   # this will return list of strings<br />
  <br />
  We have now tuples and strings, now we want to iterete inside strings:<br />
  for tuple in text + for string in tuple + for letter in string  # this will return list of letters<br />
  <br />
  Now as we iterated throu text, tuples, strings and letters we can mark we

</p>
