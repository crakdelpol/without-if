# Without-if


Solve this challenges without if statement. You can use what language do you want.

## Challenge one

We have an array of integers and we want to count how many of these integers are odd.

Example:

```
const arrayOfIntegers = [1, 4, 5, 9, 0, -1, 5];
```
Example of solution with If
```
let counter = 0;
arrayOfIntegers.forEach((integer) => {
  const remainder = Math.abs(integer % 2);
  if (remainder === 1) {
    counter++;
  }
});
console.log(counter); //5
```

## challenge two

Write a function that takes a date object argument (like new Date()) and returns the string “weekend” or “weekday”.

Example of solution with If
```
const weekendOrWeekday = (inputDate) => {
  const day = inputDate.getDay();
  if (day === 0 || day === 6) {
    return 'weekend';
  } 
  
  return 'weekday';
  // Or, for ternary fans:
  // return (day === 0 || day === 6) ? 'weekend' : 'weekday';
};
console.log(weekendOrWeekday(new Date()));
```


