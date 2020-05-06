# Hierarchical Story Generation

## Abstract

<p>Story generation involves developing a system that can write stories in a manner such that the similarity between the story written by the system is close to stories written by a human. The story generation system that we are working on generates a well-structured, coherent, and semantically correct short story. Our system sees to it that coherency is maintained between sentences as well as paragraphs alike and the plot as well as thematic ideas are carried along throughout the story. Certain characters as well as subplots are introduced as the story progresses. The generated story relies heavily on the input sentences as given by the user. The user gives a few introductory lines to the story as an input, based on which a coherent story is churned out. Keywords from the user input such as the characters and settings are extracted by the system and fed into the sequence-to-sequence model which generates the story. The user can also select a certain theme to be maintained throughout the story. The theme could be anything, for example comedy, based on which the entire mood of the story gets decided and likewise, sentences are generated to evoke a sense of light heartedness or comedy. Thus our system relies on the input provided by the user as well as the theme selected by them as a starting point to be taken into consideration while generating the story.

It must be kept in mind that stories must stick to their narrative and not deviate from its intended
idea. A basic text generation system might part ways with the main idea of a bunch of texts and
deviate off topic altogether by shifting its focus on some unimportant pieces of text. Our system
on the other hand does not deviate from the main idea of the story. We achieve this by training
our system in a hierarchical fashion. Our system first generates prompts from the user input. A
prompt is a short sentence or sentences which conveys the idea of input text. Our system sticks to
this prompt while generating the output text. Hence, by making use of a hierarchical fashion to
generate stories, our system achieves coherency and maintains the overall idea of the story
throughout the text which is generated via a sequence-to-sequence model in a hierarchical
manner.
</p>

## Our Approach

The LSTM model used is a modified version of Tensorflow's char-rnn (https://github.com/sherjilozair/char-rnn-tensorflow).

We trained this on a corpus of text containing all of <b>Sir Arthur Conan Doyle's</b> work for 100 epochs.

The input for the first paragraph must be given, following which the second paragraph uses the last complete sentence of the generated first paragraph. The story is made to follow a pre-selected theme based on customizable sentiment tokens for each paragraph.

## Usage

### To install the required libraries

```pip install -r requirements```

### To train the model

```python train.py```

Input the required prompt in the ```multipara.py``` file and run it to generate a multiple paragraph story.

Parameters in the ```train.py```, ```sample.py``` and ```multipara.py``` files may be changed as per the requirements.

## Sample Output

<b>Prompt:</b> As he walked into the street he was afraid of what might happen to him.

<b>Theme:</b> Mystery

<b>Output:</b>

<p>
As he walked into the street he was afraid of what might happen to him. That was our own danger? But I think that I broke it down upon my breast. I could only saw my hair and a sharp chuckle in the room which he is, however, unpaid, so because he might break his house, but he was an old doctor, but I know with them at the beginning of the French Museum down with seven thousand wolves all the use of insects, an quarry. A night chirrup or word, you would be glad to put up up. And what do you hesitate?" "There is only local subjects coming from the woods," said he.

There are decidedly parties at the moment this morning--a cheerful, a connoisseur as Captain William began to conclude nothing of our worthy of humours, and I observed that my horror was afar. "By my soul! they have not encouraged me ill?" I kept my girth to the house and to eat and let me be welcome to both," said he. Inscribed round in a brisker chair, and slamming his plate from the table beside him. He was dressed than that mind shown that a luckless evening, and in no muscle of anger had been lopped off from them.
</p>

## Screenshots

### Home Page


Steps:
1. Enter input prompt
2. Select theme for text generation

![alt-text](https://github.com/pumpkinman008/StoryGeneration/blob/master/screenshots/input.png "Home Page")


### Result Page


![alt-text](https://github.com/pumpkinman008/StoryGeneration/blob/master/screenshots/result.png "Result Page")

## Contributors

[Anirudh Mukherjee](https://github.com/AnirudhMukherjee) | [Keval Nagda](https://github.com/pumpkinman008) | [Milind Shah](https://github.com/mlndshh) | [Pratik Mulchandani](https://github.com/prtk1910)

## Reference
Hierarchical Neural Story Generation [https://arxiv.org/abs/1805.04833](https://arxiv.org/abs/1805.04833)
