# Hymn Generator based on RNN

This Hymn Generator will be able to generate new hymn based on classical hymns. 


## Requirements for the Generator

* The trained Generator should be able to 'predict' future notes.
* The Generator should be able to decide if the generated hymn has 'ended'.
* The Generator should be able to make several possible output sequences with given input (for user collaboration and/or cherry picking)
* The generated hymn should have similar musical style compared to the classical hymns.
* The generated hymn should not plagiarize (copy paste) existing hymns.
* The RNN (or possibly using other AI structures) model should be under 10 MB. (In order to upload it to GitHub) 


## To Do list

* Read DeepBach paper.
* Find other research paper if needed.
* Preprocess an example hymn into a proper format which could be used in training. (characters, numbers, etc)
* Make simple RNN with PyTorch.
* Train model with single hymn and check if the model can memorize the hymn.
* Decide which part of the hymn should be preprocessed into training data. (only notes? chords? lyrics? harmonies? class? etc?)
* Figure out how to preprocess the entire hymn book.
* Preprocess hymn book data. 
* Make another simple model (possibly resembling DeepBach).
* Train model.
* Iterate process to improve results.
* Try to explain the whole process to my wife or someone who has little background in engineering.
* Find out how to know if the Generator is plagiarizing.
* Generate new hymn with starting input with the well known "Amazing grace how sweet ..." part.
* Make a demo for GitHub, and update ReadMe so others could also generate new hymns.


### Related Links
* [DeepBach Paper](https://arxiv.org/pdf/1612.01010.pdf)
* [YouTube Video, GOTO 2017 • Composing Bach Chorales Using Deep Learning • Feynman Liang](https://www.youtube.com/watch?v=yu3DZuxxV7c)
* [Liang, Feynman. Bachbot. GitHub](https://github.com/feynmanliang/bachbot)

### Current To do List
* Download a bunch of hymn midi files
* find a way to change midi file to csv file
* write code to preprocess csv file (for NN input)
* train RNN
* find a way to turn csv into midi file
* play midi file (for checking)
