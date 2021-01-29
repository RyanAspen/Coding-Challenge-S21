# ACM Research Coding Challenge (Spring 2021)

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge-S21`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Submit your solution by filling out this [form](https://acmutd.typeform.com/to/uqAJNXUe).

## Question One

Genome analysis is the identification of genomic features such as gene expression or DNA sequences in an individual's genetic makeup. A genbank file (.gb) format contains information about an individual's DNA sequence. The following dataset in `Genome.gb` contains a complete genome sequence of Tomato Curly Stunt Virus. 

**With this file, create a circular genome map and output it as a JPG/PNG/JPEG format.** We're not looking for any complex maps, just be sure to highlight the features and their labels.

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

## My Explanation

First, I did some research as to what circular genome maps or genbank file are, as I had never heard either term before. After that, the vast majority of the time that I spent for this project was on finding the best tools to create the circular genome map. For at least a few days, I was stuck on a module called nxviz, which can be used to create Circos plots. After some issues with installation, I found that the module does not easily plot the kind of diagrams that I wanted to get. I eventually found a module called GenomeDiagram on Github along with a nice tutorial on TutorialPoint (https://www.tutorialspoint.com/biopython/biopython_genome_analysis.htm). There was not much to do after this, as the tutorial fit very well with what I wanted to accompish. I just had to make a few modifications to work with the specific genbank file provided. I then added some comments to make my code extra clear.
