More human than human
=====================

This is a version of Voight-Kampff test. It has a set of 10 questions with four responses to choose from.

After each response a set of variables should be typed in manually:

- Respiration (measured in BPM, normally around 12-16 breaths per minute)
- Heart rate (normally around 60 to 100 beats per minute)
- Blushing level (categorical, 6 possible levels)
- Pupillary dilation (current pupil size, 2 to 8 mm)

After ten questions and variable measurements, the test prints out a strict binary decision
whether a responding subject is a human or a replicant.

How the test works?
-------------------

Different answers have different primary scores, and after the needed physical
measurements (the results are checked to be abnormal, extremely low or extremely high)
and taken the primary score in consideration the responding subject is given the score
for the step. Alltogether step scores are calculated and the final decision is made.