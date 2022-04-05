#!/usr/bin/node

const process = require('process');

const arguments = process.argv;

if (arguments.length < 3) {
  console.log('Select task number to execute');
} else {

  const task = parseInt(arguments[2]);
  console.log('About to execute task number: ' + task);
  switch (task) {
    case 0:
      const Rectangle = require('./0-rectangle');
      const r1 = new Rectangle();
      console.log(r1);
      console.log(r1.constructor);
      break;
    case 1:
      const Rectangle2 = require('./1-rectangle');
      const r2 = new Rectangle2(2, 3);
      console.log(r2);
      console.log(r2.width);
      console.log(r2.height);
      const r3 = new Rectangle2(2, -3);
      console.log(r3);
      console.log(r3.width);
      console.log(r3.height);
      const r4 = new Rectangle2(2);
      console.log(r4);
      console.log(r4.width);
      console.log(r4.height);
      break;
    case 2:
      const Rectangle3 = require('./2-rectangle');
      const r5 = new Rectangle3(2, 3);
      console.log(r5);
      console.log(r5.width);
      console.log(r5.height);
      const r6 = new Rectangle3(2, -3);
      console.log(r6);
      console.log(r6.width);
      console.log(r6.height);
      const r7 = new Rectangle3(2);
      console.log(r7);
      console.log(r7.width);
      console.log(r7.height);
      const r8 = new Rectangle3(2, 0);
      console.log(r8);
      console.log(r8.width);
      console.log(r8.height);
      break;
    case 3:
      const Rectangle4 = require('./3-rectangle');
      const r9 = new Rectangle4(2, 3);
      r9.print();
      const r10 = new Rectangle4(10, 5);
      r10.print();
      break;
    case 4:
      const Rectangle5 = require('./4-rectangle');
      const r11 = new Rectangle5(2, 3);
      console.log('Normal:');
      r11.print();
      console.log('Double:');
      r11.double();
      r11.print();
      console.log('Rotate:');
      r11.rotate();
      r11.print();
      break;
    case 5:
      const Square = require('./5-square');
      const s1 = new Square(4);
      s1.print();
      s1.double();
      s1.print();
      break;
    case 6:
      const Square2 = require('./6-square');
      const s2 = new Square2(4);
      s2.charPrint();
      s2.charPrint('C');
      break;
    case 7:
      const nbOccurences = require('./7-occurrences').nbOccurences;
      console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
      console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
      console.log(nbOccurences(["S", 12, "c", "S", "School", 8], "S"));     
      break;
    case 8:
      const esrever = require('./8-esrever').esrever;
      console.log(esrever([1, 2, 3, 4, 5]));
      console.log(esrever(["School", 89, { id: 12 }, "String"]));
      break;
    case 9:
      const logMe = require('./9-logme').logMe;
      logMe("Hello");
      logMe("Best");
      logMe("School");
      break;
    case 10:
      const converter = require('./10-converter').converter;
      let myConverter = converter(10);
      console.log(myConverter(2));
      console.log(myConverter(12));
      console.log(myConverter(89));
      myConverter = converter(16);
      console.log(myConverter(2));
      console.log(myConverter(12));
      console.log(myConverter(89));
      break;
    default:
      console.log("error::Default case selected ... ");
  }
}
