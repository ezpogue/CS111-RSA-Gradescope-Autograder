# NOTE: This file MUST be named test_SOMETHING, i.e. not SOMETHING_test
# And the functions in it must start with test_SOMETHING not SOMETHING_test
# if you want them to be run as tests (via auto-discovery)

import unittest
import pytest
from gradescope_utils.autograder_utils.decorators import weight,visibility
import subprocess as subprocess
import os
import shutil

class TestAssignment(unittest.TestCase):
  #Test cases must begin with "test"
  #The @weight decorator indicates the number of points this test is worth
  #For documentation of this and other decorators, see:
  # https://github.com/gradescope/gradescope-utils/tree/master/gradescope_utils/autograder_utils 
  maxDiff = None
  #REPLACE THESE TESTS WITH YOUR OWN TESTS

  @weight(1)
  def test_1(self): #23 55 5 *ABCD* ^EFGH^
    cmd = "printf '%s\n' '23 55' '13' '43 15 51 13 17 43 36 30 14 10 11 23 30' | ./solution"
    self.compareOutput(cmd)

  @weight(1)
  def test_2(self):#5 55 5 *ABCD* ^EFGH^
    cmd = "printf '%s\n' '5 55' '13' '32 45 21 32 43 32 1 10 34 10 11 12 10' | ./solution"
    self.compareOutput(cmd)

  @visibility("after_published")
  @weight(1)
  def test_3(self):#5 1369 5 *If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.*
    cmd = "printf '%s\n' '5 1369' '118' '242 294 63 623 647 182 947 647 1291 182 623 1281 947 623 348 947 520 623 931 182 1291 294 182 1194 182 623 520 1043 387 520 623 204 387 520 1043 182 204 387 520 294 379 674 623 294 674 623 674 294 204 647 1291 182 1159 623 294 520 623 294 674 623 947 348 1291 791 623 931 182 379 387 548 674 182 623 520 1043 182 791 623 1281 947 623 348 947 520 623 716 182 387 1291 294 250 182 623 1043 947 418 623 379 947 204 647 1291 294 379 387 520 182 1281 623 1291 294 63 182 623 294 674 1052 242' | ./solution"
    self.compareOutput(cmd)
 
  @visibility("after_published")
  @weight(1)
  def test_4(self):#12 253 5 *be yourself, everyone else is already taken*
    cmd = "printf '%s\n' '12 253' '45' '78 190 147 169 236 119 163 231 23 147 223 243 220 169 147 49 147 231 236 119 225 147 169 147 223 23 147 169 59 23 169 179 223 231 147 179 31 236 169 70 179 192 147 225 78' | ./solution"
    self.compareOutput(cmd)

  @visibility("after_published")
  @weight(1)
  def test_5(self): #270 611 5 *be yourself, everyone else is already taken*
    cmd = "printf '%s\n' '270 611' '45' '441 25 521 259 144 350 222 222 534 521 118 183 545 259 521 247 521 222 144 350 285 521 259 521 118 534 521 259 533 534 259 103 118 222 521 103 220 144 259 64 103 441 521 285 441' | ./solution"
    self.compareOutput(cmd)

  @visibility("after_published")
  @weight(1)
  def test_6(self): #47 1633 5 *in a room full of top software designers, if two agree on the same thing, that^s a majority.*
    cmd = "printf '%s\n' '47 1633' '94' '1465 1093 841 305 309 305 1333 1500 1500 1486 305 586 767 1589 1589 305 1500 586 305 438 1500 456 305 690 1500 586 438 1352 309 1333 959 305 144 959 690 1093 388 841 959 1333 690 908 305 1093 586 305 438 1352 1500 305 309 388 1333 959 959 305 1500 841 305 438 348 959 305 690 309 1486 959 305 438 348 1093 841 388 908 305 438 348 309 438 1107 690 305 309 305 1486 309 1295 1500 1333 1093 438 1389 181 1465' | ./solution"
    self.compareOutput(cmd)

  @visibility("after_published")
  @weight(1)
  def test_7(self): #2397 5353 5 *in a room full of top software designers, if two agree on the same thing, that^s a majority.*
    cmd = "printf '%s\n' '4001 2731 3298 5176 2807 5176 2774 3490 3490 1630 5176 3646 4986 395 395 5176 3490 3646 5176 3667 3490 178 5176 447 3490 3646 3667 1860 2807 2774 3558 5176 332 3558 447 2731 4012 3298 3558 2774 447 4327 5176 2731 3646 5176 3667 1860 3490 5176 2807 4012 2774 3558 3558 5176 3490 3298 5176 3667 3177 3558 5176 447 2807 1630 3558 5176 3667 3177 2731 3298 4012 4327 5176 3667 3177 2807 3667 2426 447 5176 2807 5176 1630 2807 3743 3490 2774 2731 3667 1050 2552 4001' | ./solution"
    self.compareOutput(cmd)

  @visibility("after_published")
  @weight(1)
  def test_8(self): #7 77 5 *ABCD* ^EFGH^
    cmd = "printf '%s\n' '7 77' '13' '32 47 41 28 57 32 59 7 37 10 11 12 7' | ./solution"
    self.compareOutput(cmd)

  @visibility("after_published")
  @weight(1)
  def test_9(self): #3 1633 5 *in a room full of top software designers, if two agree on the same thing, that^s a majority.*
    cmd = "printf '%s\n' '3 1633' '94' '108 564 933 397 125 397 850 327 327 14 397 1000 928 830 830 397 327 1000 397 760 327 1468 397 736 327 1000 760 87 125 850 729 397 512 729 736 564 1331 933 729 850 736 11 397 564 1000 397 760 87 327 397 125 1331 850 729 729 397 327 933 397 760 95 729 397 736 125 14 729 397 760 95 564 933 1331 11 397 760 95 125 760 417 736 397 125 397 14 125 1111 327 850 564 760 1527 112 108' | ./solution"
    self.compareOutput(cmd)

  @visibility("after_published")
  @weight(1)
  def test_10(self): #5 1501 5 *We live in a society exquisitely dependent on science and technology, in which hardly anyone knows anything about science and technology.*
    cmd = "printf '%s\n' '5 1501' '139' '1078 848 510 578 878 546 961 510 578 546 1310 578 123 578 55 950 296 546 510 1320 1485 578 510 1403 1381 119 546 55 546 1320 510 878 1485 578 1247 510 1369 510 1310 1247 510 1310 1320 578 950 1310 578 55 296 546 510 1310 296 510 578 123 1310 1247 578 1320 510 296 1167 1310 950 878 950 444 1485 1321 578 546 1310 578 848 1167 546 296 1167 578 1167 123 699 1247 878 1485 578 123 1310 1485 950 1310 510 578 1370 1310 950 848 55 578 123 1310 1485 1320 1167 546 1310 444 578 123 271 950 119 1320 578 55 296 546 510 1310 296 510 578 123 1310 1247 578 1320 510 296 1167 1310 950 878 950 444 1485 154 1078' | ./solution"
    self.compareOutput(cmd)

  @visibility("after_published")
  @weight(1)
  def test_11(self): #5 7663 5 *EAT A LIVE FROG FIRST THING IN THE MORNING AND NOTHING WORSE WILL HAPPEN TO YOU THE REST OF THE DAY.*
    cmd = "printf '%s\n' '5 7663' '102' '5818 5408 3125 767 183 3125 183 6408 3469 3726 5408 183 381 4096 950 128 183 381 3469 4096 7086 767 183 767 3616 3469 4470 128 183 3469 4470 183 767 3616 5408 183 2202 950 4096 4470 3469 4470 128 183 3125 4470 2116 183 4470 950 767 3616 3469 4470 128 183 3771 950 4096 7086 5408 183 3771 3469 6408 6408 183 3616 3125 4529 4529 5408 4470 183 767 950 183 4961 950 2963 183 767 3616 5408 183 4096 5408 7086 767 183 950 381 183 767 3616 5408 183 2116 3125 4961 1497 5818' | ./solution"
    self.compareOutput(cmd)

  @visibility("after_published")
  @weight(1)
  def test_12(self): #7 7387 5 *But if the arrow is straight And the point is slick, It can pierce through dust no matter how thick. So I^ll make my stand And remain as I am And bid farewell and not give a damn.*
    cmd = "printf '%s\n' '7 7387' '181' '1695 6617 6875 1316 5930 3339 5389 5930 1316 4858 3580 5930 4255 4372 4372 417 6627 5930 3339 2020 5930 2020 1316 4372 4255 3339 265 4858 1316 5930 4255 246 6631 5930 1316 4858 3580 5930 2801 417 3339 246 1316 5930 3339 2020 5930 2020 6650 3339 3586 5452 3369 5930 3339 1316 5930 3586 4255 246 5930 2801 3339 3580 4372 3586 3580 5930 1316 4858 4372 417 6875 265 4858 5930 6631 6875 2020 1316 5930 246 417 5930 5597 4255 1316 1316 3580 4372 5930 4858 417 6627 5930 1316 4858 3339 3586 5452 7264 5930 2020 417 5930 3339 4275 6650 6650 5930 5597 4255 5452 3580 5930 5597 5067 5930 2020 1316 4255 246 6631 5930 4255 246 6631 5930 4372 3580 5597 4255 3339 246 5930 4255 2020 5930 3339 5930 4255 5597 5930 4255 246 6631 5930 6617 3339 6631 5930 5389 4255 4372 3580 6627 3580 6650 6650 5930 4255 246 6631 5930 246 417 1316 5930 265 3339 6333 3580 5930 4255 5930 6631 4255 5597 246 7264 1695' | ./solution"
    self.compareOutput(cmd)

  @visibility("after_published")
  @weight(1)
  def test_13(self): #5 901 5 *If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.*
    cmd = "printf '%s\n' '5 901' '118' '291 81 890 777 549 484 151 549 713 484 777 332 151 777 171 151 487 777 568 484 713 81 484 790 484 777 487 156 422 487 777 782 422 487 156 484 782 422 487 81 589 500 777 81 500 777 500 81 782 549 713 484 458 777 81 487 777 81 500 777 151 171 713 785 777 568 484 589 422 587 500 484 777 487 156 484 785 777 332 151 777 171 151 487 777 813 484 422 713 81 30 484 777 156 151 482 777 589 151 782 549 713 81 589 422 487 484 332 777 713 81 890 484 777 81 500 697 291' | ./solution"
    self.compareOutput(cmd)

  @visibility("after_published")
  @weight(1)
  def test_14(self): #20 20 5 hello
    cmd = "printf '%s\n' '20 20' '5' '16 1 16 16 1' | ./solution"
    self.compareOutput(cmd)

  @visibility("after_published")  
  @weight(1)
  def test_15(self): #7 1600 5 hello
    cmd = "printf '%s\n' '7 1600' '5' '1408 569 256 256 1339' | ./solution"
    self.compareOutput(cmd)

  #DO NOT EDIT BELOW THIS LINE
  def outputDirectory(self):
    return "../reference-output"

  def outputFileName(self, output_source):
    return "%s/%s.%s" % (self.outputDirectory(), self._testMethodName, output_source)

  def compareOutput(self, command, stdout = True, stderr = False, extra_outfiles = []):
    if (hasattr(self, "reference") and self.reference):
      with open(self.outputFileName('out'), 'w') as out, \
      open(self.outputFileName('err'),'w') as err:
        output = subprocess.run(command, stdout=out, stderr=err, shell=True)
        for f in extra_outfiles:
          shutil.move(f, self.outputDirectory())

    else:
      output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
      if (stdout):
        student_out = output.stdout.decode()
        with open(self.outputFileName('out'), 'r') as ref_outfile:
          self.assertEqual(student_out, ref_outfile.read())

      if (stderr):
        student_err = output.stderr.decode()
        with open(self.outputFileName('err'), 'r') as ref_outfile:
          self.assertEqual(student_err, ref_outfile.read())

      for f in extra_outfiles:
        self.assertTrue(os.path.exists(f), "File %s does not exist." % f)
        with open(f, 'r') as student_file, \
        open(self.outputDirectory() + "/" + f,'r') as ref_file:
          self.assertEqual(ref_file.read(), student_file.read())