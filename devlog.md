# Development Log

### 8th August 2026

- Today I plan to start the development of the quadtree in code. 
- Initially, I planned for the quadtree to be made of nodes as objects, but looking at the amount of particles that will be simulated and the low performance when particles were initially objects I've decided to implement the quadtree first using structure of arrays.
- That way, instead of having multiple pieces of data scattered across memory, jumping between them, you now have fixed array blocks that you move to. Similar to what I did for particles, I'm going to put the properties of the nodes in arrays and represent the nodes by index. 
- For example, index zero of any array would point to a property of the root node, the first node.

### 13th August 2026
- Much progress not been made since I wanted to make sure this project met the rubric for assessment. It is a school project after all. 
- Either way, after some research and testing, two things have been discovered. 
- Number one, at this current stage, I seem to be hitting limitations with my simulator at 2,000 bodies running at a max of 20 fps which is not close to to my 30 fps goal nor my body count. While it does run smoothly and much better than with objects, which started slowing down from 200 to 500, if I remember correctly.
- Second I have found I can adjust my loops because acceleration goes for both weight according to Newton's third law. If I apply the same but opposite acceleration to the other body while running for the current one, I could cut my total loops in half and only have to go through all possible combinations. With that, I can potentially handle double the amount of bodies I can currently handle
- This is what I plan to implement now to see how it goes while readjusting my schedule