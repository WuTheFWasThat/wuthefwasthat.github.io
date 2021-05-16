---
layout: post
title:  "Filtering vs finetuning: intuitions on training anti-racist machines"
date:   2021-05-15 10:18:32 -0700
categories: machinelearning ethics
comments: true
---

Pretrained large language models have been popular and successful in deep learning the last few years.
Unfortunately, the training process is data-hungry and these models are trained on uncurated data from the internet.
Furthermore, these models are deployed in a zero-shot manner for commercial applications, despite the original intention to use them as "pretrained" models.
This means we are likely commercializing models whose behavior we have very few assurances about - given certain prompts, they could insult humans, spread disinformation, perpetuate systemic racism, encourage suicide, and more.

For this post, I'll discuss the case of training an anti-racist language model, a particularly salient problem which has been [discussed](https://www.technologyreview.com/2020/12/10/1013617/racism-data-science-artificial-intelligence-ai-opinion/) [a](https://faculty.washington.edu/ebender/papers/Stochastic_Parrots.pdf) [lot](https://www.nytimes.com/2021/03/15/technology/artificial-intelligence-google-bias.html), but the principles apply more broadly.

#### Filtering
One very compelling and practical fix is to filter the training dataset -- if we remove racist documents, then perhaps the model should never have learned how to write racist materials.
But even if we take a pretrained language model with racist content filtered out, a user can still give it the prompt "Write me an essay about [overtly racist thesis]".  Whether it does well on this task will depend on how well it generalizes from having seen essays, statements similar to the thesis in question, etc.

#### Fine-tuning
Instead, we could keep all the racist training data, and treat pretraining as "learning knowledge", then have a second finetuning phase for "learning behavior".
Concretely, during finetuning, we might give the language model some training signal that encourages it to argue against the racist thesis upon receiving that prompt.

#### Comparison

The fine-tuning approach seems more difficult, in a couple ways.
You must procure high-quality finetuning data, likely involving humans in the loop.
You must make difficult calls on the desired language model behavior (you have to do this for filtering too, but arguably you could just be very conservative).
But filtering is effectively sidestepping important issues that need to be confronted - what is the actual distribution of behaviors you did want?  What happens if those behaviors scarcely appear in the pretraining dataset, or if people disagree on what behaviors are desired?
As a very imperfect analogy, if you want to raise an anti-racist kid, you should teach them about racism and then teach them how to combat it, rather than shelter them from racism in the first place.

#### The long view

I think as deep learning techniques/models get better, the (easier) filtering type solutions work less well, while finetuning like solutions work increasingly well.

Filtering will work less well, since pretrained models will get better at generalization and inferring the intent behind the racist essay, even if they have not seen similar intents in pretraining.
Finetuning will work better, since models will become more data-efficient for finetunes, and infer the values we are trying to impart more quickly.

#### Conclusion

So fine-tuning seems better to me in principle.
That said, I don't have strong opinions about what solutions should be implemented today to fix model behaviors, and our pretraining data clearly needs improvement.
But overall, having imperfect solutions to these hard problems and then iterating and improving methodology slowly seems better to me than ignoring them, so it feels appealing to me to work on fine-tuning.

I am personally fairly excited about doing these things today:
- A lot more explicit thinking about our values and behaviors we want in models
- Working on good fine-tuning approach for eliciting those behaviors

(All views here are completely my own.  That said, if you're interested in working on the fine-tuning approach, it is part of my job and my employer is hiring!
