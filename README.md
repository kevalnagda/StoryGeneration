# StoryGeneration

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

## Reference
[Hierarchical Neural Story Generation](https://arxiv.org/abs/1805.04833)
