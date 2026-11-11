// Goal: Calculate and print the average of numeric scores.

function calculateAverage(scores) {
  if (scores.length === 0) {
    return 0;
  }

  let total = 0;
  for (const score of scores) {
    total += score;
  }
  return total / scores.length;
}

const scores = [70, 80, 90];
const average = calculateAverage(scores);
console.log("Average:", average;
console.log("Expected average: 80");
