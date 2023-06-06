If you are already familiar with online interviews and coding practice websites, you would for sure, love this easy Python feature.

Read this completely for a better understanding!

For example, I ask you to print a list of values. You would do that using a for loop in no time.

li = [10, 20, 30, 40, 50]

for i in li:
    print(i)

Output:

10
20
30
40
50

But now, I ask if you can print the values in the same line with a space between each element. You would still make that look easy by using the end argument within print().

li = [10, 20, 30, 40, 50]

for i in li:
    print(i, end=' ')

Output:

10 20 30 40 50 

The Problem

Now, here is the exact problem. The output when seen looks like what I asked for. But when you select the output, an annoying space pops out of nowhere.

And that is because the last loop prints 50 and then adds a space after it with the use of the end argument. Though the end argument helped us in printing space in between, this side effect of putting a white space at the last is not what we wanted.

Especially, when it comes to online interview questions and coding platforms, they expect us to get the exact output as given. Even an extra space would result in the website not accepting our solution.
Don’t Do This

To fix this, if you think of printing each element through indexing, that would absolutely not work!

Why? Because coding platforms have hidden test cases that may receive a varying number of values.

Here is an example.

Question

Get a list of integers as input in the given format and print the values
in the given format:

Input:
10 20 30

Output:
10 20 30

Hidden Test Case:

Input:
10 20

Output:
10 20

li = list(map(int, input().split()))
print(li[0], li[1], li[2])

Input:
10 20 30

Output:
10 20 30

For the hidden test case, there are only two values in the list. So li[2] would display an IndexError for the same program. This clearly shows that using indexing manually won’t work here!

Input:
10 20

Output:
IndexError: list index out of range

The Solution

How do you fix this? Well, that is where this hidden gem comes in. Have you ever tried using an asterisk (*) prefixed to a list (or any iterable) inside a print() function.

That is exactly what a lot of coders are missing!

You would have an idea about arbitrary arguments (*args) which is often learned with user-defined functions.

But using it inside a print function would pass each element in the list (or any iterable) as a separate value, and print them with a space between, as you do manually using a comma.

And what is more interesting is, you could have any number of values in the list (arbitrary values, as the name suggests).

Here is the correct code.

li = list(map(int, input().split()))
print(*li)

Input:
10 20 30

Output:
10 20 30

Input:
10 20

Output:
10 20

Other Use Cases

This would work for any iterable. Here are some examples given using a string and the range() class.

Example 01

s = 'medium'
print(*s)

Output:

m e d i u m

Example 02

print(*range(1, 6))
print(*range(4, 8))

Output:

1 2 3 4 5
4 5 6 7

Conclusion

Did you already know this? Was this feature new and interesting to you? Let me know in the comments.
