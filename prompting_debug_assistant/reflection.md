# Reflection on AI-Assisted Debugging

## Introduction

In this project, I used ChatGPT to investigate six intentionally buggy programs written in Python, JavaScript, and C. I asked the AI to identify each issue, explain its cause, and suggest a fix. I kept the original snippets, saved corrected versions separately, and checked the results with automated tests. The validation script reported 28 passing checks across the six fixes. This process helped me evaluate AI as a debugging assistant rather than simply accepting its answers.

## AI Strengths

The easiest problems were the JavaScript syntax error in `bug3.js` and the missing dictionary key in `bug2.py`. In `bug3.js`, the missing closing parenthesis stopped the program from running; fixing the `console.log` statement was straightforward. In `bug2.py`, the `KeyError: 'price'` clearly pointed to a dictionary access that needed a key check. AI explained both problems quickly and suggested small changes without rewriting unrelated code.

It also handled the discount calculation in `bug4.js` well. The script ran but returned the discount amount rather than the final price. AI connected the faulty expression to the intended behavior and changed `price * discountRate` to `price * (1 - discountRate)`. That explanation was more helpful than receiving corrected code alone.

## AI Weaknesses and Trust

The harder cases required more careful interpretation. In `bug5.c`, `sizeof(numbers)` inside a function measured a pointer rather than the original array. Understanding why the solution needed a separate element count was more demanding than spotting a syntax error. `bug1.py` was also subtle: changing the slice to `items[-n:]` seems correct, but fails when `n` is zero. The fix needed an explicit zero case. In `bug6.c`, comparing C strings using `==` appeared plausible but compared addresses instead of contents.

I would describe my trust in the AI as **conditional**. Its suggestions were useful starting points, not proof of correctness. The final fixes worked in our documented tests, but passing those tests cannot guarantee that every possible input is handled.

## Human Role

Human judgment was needed to decide what each function was supposed to do and to choose meaningful test cases. I checked normal inputs and boundaries such as zero-length requests, empty collections, invalid discounts, and case-sensitive usernames. For C, strict compiler flags helped catch warning-level problems. No extra manual code changes were required beyond the suggested fixes, but designing and checking the tests still required independent judgment.

## Conclusion

AI made the debugging process more efficient by suggesting likely causes and explaining unfamiliar language behavior. However, execution and verification mattered more than confident explanations. My main lesson is to use AI to generate hypotheses, then reproduce the bug, test the correction, and document the evidence before trusting it in a real project.
