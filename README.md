<h2>CRAZY PYTHON LOOPS</h2>
<i>HTML works</i>
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
  <b>for <i>tuple</i> in text</b>   # this will return list of tuples<br />
  <br />
  We have tuples, now we want to iterete inside them:<br />
  <b>for tuple in text + for <i>string</i> in tuple</b>   # this will return list of strings<br />
  <br />
  We have now tuples and strings, now we want to iterete inside strings:<br />
  <b>for tuple in text + for string in tuple + for <i>letter</i> in string</b>  # this will return list of letters<br />
  <br />
  Now as we iterated throu text, tuples, strings and letters we can mark we
  <b><i>letter</i> for tuple in text + for string in tuple + for <i>letter</i> in string</b>
  DONE!
</p>
