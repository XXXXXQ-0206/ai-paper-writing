# discussion corpus (55 sources)

@src https://arxiv.org/abs/1906.08237
@title XLNet: Generalized Autoregressive Pretraining for Language Understanding
@section Discussion

Comparing Eq. ( ) and ( ), we observe that both BERT and XLNet perform partial prediction, i.e., only predicting a subset of tokens in the sequence.

This is a necessary choice for BERT because if all tokens are masked, it is impossible to make any meaningful predictions.

In addition, for both BERT and XLNet, partial prediction plays a role of reducing optimization difficulty by only predicting tokens with sufficient context.

However, the independence assumption discussed in Section disables BERT to model dependency between targets.

To better understand the difference, let's consider a concrete example [New, York, is, a, city]. Suppose both BERT and XLNet select the two tokens [New, York] as the prediction targets and maximize MATH . Also suppose that XLNet samples the factorization order [is, a, city, New, York]. In this case, BERT and XLNet respectively reduce to the following objectives:

Notice that XLNet is able to capture the dependency between the pair (New, York), which is omitted by BERT.

Although in this example, BERT learns some dependency pairs such as (New, city) and (York, city), it is obvious that XLNet always learns more dependency pairs given the same target and contains "denser" effective training signals.

For more formal analysis and further discussion, please refer to Appendix .

@src https://arxiv.org/abs/1909.11942
@title ALBERT: A Lite BERT for Self-supervised Learning of Language Representations
@section Discussion

While ALBERT-xxlarge has less parameters than BERT-large and gets significantly better results, it is computationally more expensive due to its larger structure. An important next step is thus to speed up the training and inference speed of ALBERT through methods like sparse attention and block attention .

An orthogonal line of research, which could provide additional representation power, includes hard example mining and more efficient language modeling training .

Additionally, although we have convincing evidence that sentence order prediction is a more consistently-useful learning task that leads to better language representations, we hypothesize that there could be more dimensions not yet captured by the current self-supervised training losses that could create additional representation power for the resulting representations.

@src https://arxiv.org/abs/1910.10683
@title Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer
@section Discussion

fig:objectives_flow shows a flow chart of the choices made during our exploration of unsupervised objectives.

Overall, the most significant difference in performance we observed was that denoising objectives outperformed language modeling and deshuffling for pre-training.

We did not observe a remarkable difference across the many variants of the denoising objectives we explored.

However, different objectives (or parameterizations of objectives) can lead to different sequence lengths and thus different training speeds.

This implies that choosing among the denoising objectives we considered here should mainly be done according to their computational cost.

Our results also suggest that additional exploration of objectives similar to the ones we consider here may not lead to significant gains for the tasks and model we consider.

Instead, it may be fortuitous to explore entirely different ways of leveraging unlabeled data.

@src https://arxiv.org/abs/2005.11401
@title Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
@section Discussion

In this work, we presented hybrid generation models with access to parametric and non-parametric memory.

We showed that our RAG models obtain state of the art results on open-domain QA. We found that people prefer RAG's generation over purely parametric BART, finding RAG more factual and specific.

We conducted an thorough investigation of the learned retrieval component, validating its effectiveness, and we illustrated how the retrieval index can be hot-swapped to update the model without requiring any retraining.

In future work, it may be fruitful to investigate if the two components can be jointly pre-trained from scratch, either with a denoising objective similar to BART or some another objective.

Our work opens up new research directions on how parametric and non-parametric memories interact and how to most effectively combine them, showing promise in being applied to a wide variety of NLP tasks.

@src https://arxiv.org/abs/2005.11401
@title Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
@section Broader Impact

This work offers several positive societal benefits over previous work: the fact that it is more strongly grounded in real factual knowledge (in this case Wikipedia) makes it "hallucinate" less with generations that are more factual, and offers more control and interpretability. RAG could be employed in a wide variety of scenarios with direct benefit to society, for example by endowing it with a medical index and asking it open-domain questions on that topic, or by helping people be more effective at their jobs.

With these advantages also come potential downsides: Wikipedia, or any potential external knowledge source, will probably never be entirely factual and completely devoid of bias. Since RAG can be employed as a language model, similar concerns as for GPT-2 are valid here, although arguably to a lesser extent, including that it might be used to generate abuse, faked or misleading content in the news or on social media; to impersonate others; or to automate the production of spam/phishing content . Advanced language models may also lead to the automation of various jobs in the coming decades .

In order to mitigate these risks, AI systems could be employed to fight against misleading content and automated spam/phishing.

@src https://arxiv.org/abs/2005.14165
@title Language Models are Few-Shot Learners
@section Limitations

GPT-3 and our analysis of it have a number of limitations. Below we describe some of these and suggest directions for future work.

First, despite the strong quantitative and qualitative improvements of GPT-3, particularly compared to its direct predecessor GPT-2, it still has notable weaknesses in text synthesis and several NLP tasks. On text synthesis, although the overall quality is high, GPT-3 samples still sometimes repeat themselves semantically at the document level, start to lose coherence over sufficiently long passages, contradict themselves, and occasionally contain non-sequitur sentences or paragraphs. We will release a collection of 500 uncurated unconditional samples to help provide a better sense of GPT-3’s limitations and strengths at text synthesis. Within the domain of discrete language tasks, we have noticed informally that GPT-3 seems to have special difficulty with "common sense physics", despite doing well on some datasets (such as PIQA ) that test this domain. Specifically GPT-3 has difficulty with questions of the type "If I put cheese into the fridge, will it melt?". Quantitatively, GPT-3’s in-context learning performance has some notable gaps on our suite of benchmarks, as described in Section , and in particular it does little better than chance when evaluated one-shot or even few-shot on some "comparison" tasks, such as determining if two words are used the same way in a sentence, or if one sentence implies another (WIC and ANLI respectively), as well as on a subset of reading comprehension tasks. This is especially striking given GPT-3’s strong few-shot performance on many other tasks.

GPT-3 has several structural and algorithmic limitations, which could account for some of the issues above. We focused on exploring in-context learning behavior in autoregressive language models because it is straightforward to both sample and compute likelihoods with this model class. As a result our experiments do not include any bidirectional architectures or other training objectives such as denoising. This is a noticeable difference from much of the recent literature, which has documented improved fine-tuning performance when using these approaches over standard language models . Thus our design decision comes at the cost of potentially worse performance on tasks which empirically benefit from bidirectionality. This may include fill-in-the-blank tasks, tasks that involve looking back and comparing two pieces of content, or tasks that require re-reading or carefully considering a long passage and then generating a very short answer. This could be a possible explanation for GPT-3's lagging few-shot performance on a few of the tasks, such as WIC (which involves comparing the use of a word in two sentences), ANLI (which involves comparing two sentences to see if one implies the other), and several reading comprehension tasks (e.g. QuAC and RACE). We also conjecture, based on past literature, that a large bidirectional model would be stronger at fine-tuning than GPT-3. Making a bidirectional model at the scale of GPT-3, and/or trying to make bidirectional models work with few- or zero-shot learning, is a promising direction for future research, and could help achieve the "best of both worlds".

A more fundamental limitation of the general approach described in this paper – scaling up any LM-like model, whether autoregressive or bidirectional – is that it may eventually run into (or could already be running into) the limits of the pretraining objective. Our current objective weights every token equally and lacks a notion of what is most important to predict and what is less important. demonstrate benefits of customizing prediction to entities of interest. Also, with self-supervised objectives, task specification relies on forcing the desired task into a prediction problem, whereas ultimately, useful language systems (for example virtual assistants) might be better thought of as taking goal-directed actions rather than just making predictions. Finally, large pretrained language models are not grounded in other domains of experience, such as video or real-world physical interaction, and thus lack a large amount of context about the world . For all these reasons, scaling pure self-supervised prediction is likely to hit limits, and augmentation with a different approach is likely to be necessary. Promising future directions in this vein might include learning the objective function from humans , fine-tuning with reinforcement learning, or adding additional modalities such as images to provide grounding and a better model of the world .

Another limitation broadly shared by language models is poor sample efficiency during pre-training. While GPT-3 takes a step towards test-time sample efficiency closer to that of humans (one-shot or zero-shot), it still sees much more text during pre-training than a human sees in the their lifetime . Improving pre-training sample efficiency is an important direction for future work, and might come from grounding in the physical world to provide additional information, or from algorithmic improvements.

A limitation, or at least uncertainty, associated with few-shot learning in GPT-3 is ambiguity about whether few-shot learning actually learns new tasks "from scratch" at inference time, or if it simply recognizes and identifies tasks that it has learned during training. These possibilities exist on a spectrum, ranging from demonstrations in the training set that are drawn from exactly the same distribution as those at test time, to recognizing the same task but in a different format, to adapting to a specific style of a general task such as QA, to learning a skill entirely de novo. Where GPT-3 is on this spectrum may also vary from task to task. Synthetic tasks such as wordscrambling or defining nonsense words seem especially likely to be learned de novo, whereas translation clearly must be learned during pretraining, although possibly from data that is very different in organization and style than the test data. Ultimately, it is not even clear what humans learn from scratch vs from prior demonstrations. Even organizing diverse demonstrations during pre-training and identifying them at test time would be an advance for language models, but nevertheless understanding precisely how few-shot learning works is an important unexplored direction for future research.

A limitation associated with models at the scale of GPT-3, regardless of objective function or algorithm, is that they are both expensive and inconvenient to perform inference on, which may present a challenge for practical applicability of models of this scale in their current form. One possible future direction to address this is distillation of large models down to a manageable size for specific tasks. Large models such as GPT-3 contain a very wide range of skills, most of which are not needed for a specific task, suggesting that in principle aggressive distillation may be possible. Distillation is well-explored in general but has not been tried at the scale of hundred of billions parameters; new challenges and opportunities may be associated with applying it to models of this size.

Finally, GPT-3 shares some limitations common to most deep learning systems – its decisions are not easily interpretable, it is not necessarily well-calibrated in its predictions on novel inputs as observed by the much higher variance in performance than humans on standard benchmarks, and it retains the biases of the data it has been trained on. This last issue – biases in the data that may lead the model to generate stereotyped or prejudiced content – is of special concern from a societal perspective, and will be discussed along with other issues in the next section on Broader Impacts (Section ).

@src https://arxiv.org/abs/2005.14165
@title Language Models are Few-Shot Learners
@section Broader Impacts

Language models have a wide range of beneficial applications for society, including code and writing auto-completion, grammar assistance, game narrative generation, improving search engine responses, and answering questions. But they also have potentially harmful applications. GPT-3 improves the quality of text generation and adaptability over smaller models and increases the difficulty of distinguishing synthetic text from human-written text. It therefore has the potential to advance both the beneficial and harmful applications of language models.

Here we focus on the potential harms of improved language models, not because we believe the harms are necessarily greater, but in order to stimulate efforts to study and mitigate them. The broader impacts of language models like this are numerous. We focus on two primary issues: the potential for deliberate misuse of language models like GPT-3 in Section , and issues of bias, fairness, and representation within models like GPT-3 in Section . We also briefly discuss issues of energy efficiency (Section ).

@src https://arxiv.org/abs/2006.11239
@title Denoising Diffusion Probabilistic Models
@section Broader Impact

Our work on diffusion models takes on a similar scope as existing work on other types of deep generative models, such as efforts to improve the sample quality of GANs, flows, autoregressive models, and so forth. Our paper represents progress in making diffusion models a generally useful tool in this family of techniques, so it may serve to amplify any impacts that generative models have had (and will have) on the broader world.

Unfortunately, there are numerous well-known malicious uses of generative models. Sample generation techniques can be employed to produce fake images and videos of high profile figures for political purposes. While fake images were manually created long before software tools were available, generative models such as ours make the process easier. Fortunately, CNN-generated images currently have subtle flaws that allow detection , but improvements in generative models may make this more difficult.

Generative models also reflect the biases in the datasets on which they are trained. As many large datasets are collected from the internet by automated systems, it can be difficult to remove these biases, especially when the images are unlabeled. If samples from generative models trained on these datasets proliferate throughout the internet, then these biases will only be reinforced further.

On the other hand, diffusion models may be useful for data compression, which, as data becomes higher resolution and as global internet traffic increases, might be crucial to ensure accessibility of the internet to wide audiences. Our work might contribute to representation learning on unlabeled raw data for a large range of downstream tasks, from image classification to reinforcement learning, and diffusion models might also become viable for creative uses in art, photography, and music.

This work was supported by ONR PECASE and the NSF Graduate Research Fellowship under grant number DGE-1752814. Google's TensorFlow Research Cloud (TFRC) provided Cloud TPUs.

@src https://arxiv.org/abs/2006.11239
@title Denoising Diffusion Probabilistic Models
@section Discussion on related work

Our model architecture, forward process definition, and prior differ from NCSN in subtle but important ways that improve sample quality, and, notably, we directly train our sampler as a latent variable model rather than adding it after training post-hoc. In greater detail:

We use a U-Net with self-attention; NCSN uses a RefineNet with dilated convolutions.

We condition all layers on MATH by adding in the Transformer sinusoidal position embedding, rather than only in normalization layers (NCSNv1) or only at the output (v2).

Diffusion models scale down the data with each forward process step (by a MATH factor) so that variance does not grow when adding noise, thus providing consistently scaled inputs to the neural net reverse process. NCSN omits this scaling factor.

Unlike NCSN, our forward process destroys signal ( MATH ), ensuring a close match between the prior and aggregate posterior of MATH .

Also unlike NCSN, our MATH are very small, which ensures that the forward process is reversible by a Markov chain with conditional Gaussians. Both of these factors prevent distribution shift when sampling.

Our Langevin-like sampler has coefficients (learning rate, noise scale, etc.)

derived rigorously from MATH in the forward process. Thus, our training procedure directly trains our sampler to match the data distribution after MATH steps: it trains the sampler as a latent variable model using variational inference. In contrast, NCSN's sampler coefficients are set by hand post-hoc, and their training procedure is not guaranteed to directly optimize a quality metric of their sampler.

@src https://arxiv.org/abs/2009.03300
@title Measuring Massive Multitask Language Understanding
@section Discussion

Understanding. While text is capable of conveying an enormous number of concepts about the world, many important concepts are conveyed mainly through other modalities, such as images, audio, and physical interaction . Existing large-scale NLP models, such as GPT-3, do not incorporate multimodal information, so we design our benchmark to capture a diverse array of tasks in a text-only format. However, as models gain the ability to process multimodal inputs, benchmarks should be designed to reflect this change. One such benchmark could be a "Turk Test," consisting of Amazon Mechanical Turk Human Intelligence Tasks. These are well-defined tasks that require models to interact with flexible formats and demonstrate multimodal understanding.

Internet as a Training Set. A major distinction between our benchmark and previous multitask NLP benchmarks is that we do not require large training sets. Instead, we assume that models have acquired the requisite knowledge from reading vast quantities of diverse text from the Internet. This process is typically called pretraining, but it can be thought of as training in its own right, where the downstream evaluation is demonstrating whatever knowledge we would expect a human to pick up from reading the same text.

This motivates us to propose a methodological change so that models are trained more like how humans learn.

While most previous machine learning benchmarks have models learn from a large question bank, humans primarily learn new subjects by reading books and listening to others talk about the topic. For specialized subjects such as Professional Law, massive legal corpora are available, such as the 164-volume legal encyclopedia Corpus Juris Secundum, but there are fewer than 5,000 multistate bar exam questions available. Learning the entire law exclusively through a small number of practice tests is implausible, so future models must learn more during pretraining.

For this reason we assess pretrained models in a zero-shot, few-shot, or transfer setting and we provide a dev, val, and test set for each task. The dev set is used for few-shot prompts, the val set could be used for hyperparameter tuning, and the test set is used to compute the final accuracy. Importantly, the format of our evaluation is not identical to the format in which information is acquired during pretraining. This has the benefit of obviating concerns about spurious training set annotation artifacts and is in stark contrast to the previous paradigm of identically distributed training and test sets.

This change also enables collecting a much more extensive and diverse set of tasks for evaluation.

We anticipate our methodology becoming more widespread as models improve at extracting information from diverse online sources.

Limitations. We find that current large-scale Transformers have wide room for improvement. They are notably poor at modeling human (dis)approval, as evident by the low performance on the Professional Law and Moral Scenarios tasks. For future systems to be aligned with human values, high performance on these tasks is crucial , so future research should especially aim to increase accuracy on these tasks. Models also have difficulty performing calculations, so much so that they exhibit poor performance on Elementary Mathematics and many other STEM subjects with "plug and chug" problems. Additionally, they do not match expert-level performance (90%) on any subject, so for all subjects it is subhuman. On average, models are only now starting to move beyond random-chance accuracy levels.

Addressing these shortcomings may be challenging. To illustrate this, we attempted to create a better Professional Law model by pretraining on specialized data but achieved only limited success. We collected approximately 2,000 additional Professional Law training examples. After fine-tuning a RoBERTa-base model using this custom training set, our model attained MATH test accuracy. To test the impact of additional specialized training data, we also had RoBERTa continue pretraining on approximately 1.6 million legal case summaries using Harvard’s Law Library case law corpus case.law, but after fine-tuning it only attained MATH accuracy. This suggests that while additional pretraining on relevant high quality text can help, it may not be enough to substantially increase the performance of current models.

It is unclear whether simply scaling up existing language models will solve the test. Current understanding indicates that a MATH increase in model size must be accompanied by an approximate MATH increase in data . Aside from the tremendous expense in creating multi-trillion parameter language models, data may also become a bottleneck, as there is far less written about esoteric branches of knowledge than about everyday situations.

@src https://arxiv.org/abs/2010.02502
@title Denoising Diffusion Implicit Models
@section Discussion

We have presented DDIMs – an implicit generative model trained with denoising auto-encoding / score matching objectives – from a purely variational perspective. DDIM is able to generate high-quality samples much more efficiently than existing DDPMs and NCSNs, with the ability to perform meaningful interpolations from the latent space. The non-Markovian forward process presented here seems to suggest continuous forward processes other than Gaussian (which cannot be done in the original diffusion framework, since Gaussian is the only stable distribution with finite variance). We also demonstrated a discrete case with a multinomial forward process in Appendix , and it would be interesting to investigate similar alternatives for other combinatorial structures.

Moreover, since the sampling procedure of DDIMs is similar to that of an neural ODE, it would be interesting to see if methods that decrease the discretization error in ODEs, including multi-step methods such as Adams-Bashforth , could be helpful for further improving sample quality in fewer steps . It is also relevant to investigate whether DDIMs exhibit other properties of existing implicit models .

@src https://arxiv.org/abs/2101.03961
@title Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity
@section Discussion

We pose and discuss questions about the Switch Transformer, and sparse expert models generally, where sparsity refers to weights, not on attention patterns.

Isn't Switch Transformer better due to sheer parameter count? Yes, and by design! Parameters, independent of the total FLOPs used, are a useful axis to scale neural language models. Large models have been exhaustively shown to perform better . But in this case, our model is more sample efficient and faster while using the same computational resources.

I don't have access to a supercomputer—is this still useful for me?

Though this work has focused on extremely large models, we also find that models with as few as two experts improves performance while easily fitting within memory constraints of commonly available GPUs or TPUs (details in Appendix ).

We therefore believe our techniques are useful in small-scale settings.

Do sparse models outperform dense models on the speed-accuracy Pareto curve?

Yes. Across a wide variety of different models sizes, sparse models outperform dense models per step and on wall clock time. Our controlled experiments show for a fixed amount of computation and time, sparse models outperform dense models.

I can't deploy a trillion parameter model—can we shrink these models?

We cannot fully preserve the model quality, but compression rates of 10 to 100x are achievable by distilling our sparse models into dense models while achieving MATH 30% of the quality gain of the expert model.

Why use Switch Transformer instead of a model-parallel dense model?

On a time basis, Switch Transformers can be far more efficient than dense-models with sharded parameters (Figure ).

Also, we point out that this decision is not mutually exclusive—we can, and do, use model-parallelism in Switch Transformers, increasing the FLOPs per token, but incurring the slowdown of conventional model-parallelism.

Why aren't sparse models widely used already?

The motivation to try sparse models has been stymied by the massive success of scaling dense models (the success of which is partially driven by co-adaptation with deep learning hardware as argued in ). Further, sparse models have been subject to multiple issues including (1) model complexity, (2) training difficulties, and (3) communication costs.

Switch Transformer makes strides to alleviate these issues.

@src https://arxiv.org/abs/2101.03961
@title Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity
@section Future Work

This paper lays out a simplified architecture, improved training procedures, and a study of how sparse models scale.

However, there remain many open future directions which we briefly describe here:

A significant challenge is further improving training stability for the largest models.

While our stability techniques were effective for our Switch-Base, Switch-Large and Switch-C models (no observed instability), they were not sufficient for Switch-XXL.

We have taken early steps towards stabilizing these models, which we think may be generally useful for large models, including using regularizers for improving stability and adapted forms of gradient clipping, but this remains unsolved.

Generally we find that improved pre-training quality leads to better downstream results (Appendix ), though we sometimes encounter striking anomalies.

For instance, despite similar perplexities modeling the C4 data set, the 1.6T parameter Switch-C achieves only an 87.7 exact match score in SQuAD, which compares unfavorably to 89.6 for the smaller Switch-XXL model.

One notable difference is that the Switch-XXL model applies MATH 10x the FLOPS per token than the Switch-C model, even though it has MATH 4x less unique parameters (395B vs 1.6T).

This suggests a poorly understood dependence between fine-tuning quality, FLOPS per token and number of parameters.

Perform a comprehensive study of scaling relationships to guide the design of architectures blending data, model and expert-parallelism.

Ideally, given the specs of a hardware configuration (computation, memory, communication) one could more rapidly design an optimal model.

And, vice versa, this may also help in the design of future hardware.

Our work falls within the family of adaptive computation algorithms.

Our approach always used identical, homogeneous experts, but future designs (facilitated by more flexible infrastructure) could support heterogeneous experts.

This would enable more flexible adaptation by routing to larger experts when more computation is desired—perhaps for harder examples.

Investigating expert layers outside the FFN layer of the Transformer.

We find preliminary evidence that this similarly can improve model quality.

In Appendix , we report quality improvement adding these inside Self-Attention layers, where our layer replaces the weight matrices which produce Q, K, V.

However, due to training instabilities with the bfloat16 format, we instead leave this as an area for future work.

Examining Switch Transformer in new and across different modalities. We have thus far only considered language, but we believe that model sparsity can similarly provide advantages in new modalities, as well as multi-modal networks.

This list could easily be extended, but we hope this gives a flavor for the types of challenges that we are thinking about and what we suspect are promising future directions.

@src https://arxiv.org/abs/2103.00020
@title Learning Transferable Visual Models From Natural Language Supervision
@section Limitations

There are still many limitations to CLIP. While several of these are discussed as part of analysis in various sections, we summarize and collect them here.

On datasets with training splits, the performance of zero-shot CLIP is on average competitive with the simple supervised baseline of a linear classifier on top of ResNet-50 features. On most of these datasets, the performance of this baseline is now well below the overall state of the art. Significant work is still needed to improve the task learning and transfer capabilities of CLIP. While scaling has so far steadily improved performance and suggests a route for continued improvement, we estimate around a 1000x increase in compute is required for zero-shot CLIP to reach overall state-of-the-art performance. This is infeasible to train with current hardware. Further research into improving upon the computational and data efficiency of CLIP will be necessary.

Analysis in Section found that CLIP's zero-shot performance is still quite weak on several kinds of tasks. When compared to task-specific models, the performance of CLIP is poor on several types of fine-grained classification such as differentiating models of cars, species of flowers, and variants of aircraft. CLIP also struggles with more abstract and systematic tasks such as counting the number of objects in an image. Finally for novel tasks which are unlikely to be included in CLIP's pre-training dataset, such as classifying the distance to the nearest car in a photo, CLIP's performance can be near random. We are confident that there are still many, many, tasks where CLIP's zero-shot performance is near chance level.

While zero-shot CLIP generalizes well to many natural image distributions as investigated in Section , we've observed that zero-shot CLIP still generalizes poorly to data that is truly out-of-distribution for it. An illustrative example occurs for the task of OCR as reported in Appendix . CLIP learns a high quality semantic OCR representation that performs well on digitally rendered text, which is common in its pre-training dataset, as evidenced by performance on Rendered SST2. However, CLIP only achieves 88% accuracy on the handwritten digits of MNIST. An embarrassingly simple baseline of logistic regression on raw pixels outperforms zero-shot CLIP. Both semantic and near-duplicate nearest-neighbor retrieval verify that there are almost no images that resemble MNIST digits in our pre-training dataset. This suggests CLIP does little to address the underlying problem of brittle generalization of deep learning models. Instead CLIP tries to circumvent the problem and hopes that by training on such a large and varied dataset that all data will be effectively in-distribution. This is a naive assumption that, as MNIST demonstrates, is easy to violate.

Although CLIP can flexibly generate zero-shot classifiers for a wide variety of tasks and datasets, CLIP is still limited to choosing from only those concepts in a given zero-shot classifier. This is a significant restriction compared to a truly flexible approach like image captioning which could generate novel outputs. Unfortunately, as described in Section we found the computational efficiency of the image caption baseline we tried to be much lower than CLIP. A simple idea worth trying is joint training of a contrastive and generative objective with the hope of combining the efficiency of CLIP with the flexibility of a caption model. As another alternative, search could be performed at inference time over many natural language explanations of a given image, similar to approach proposed in Learning with Latent Language .

CLIP also does not address the poor data efficiency of deep learning. Instead CLIP compensates by using a source of supervision that can be scaled to hundreds of millions of training examples. If every image seen during training of a CLIP model was presented at a rate of one per second, it would take 405 years to iterate through the 12.8 billion images seen over 32 training epochs. Combining CLIP with self-supervision and self-training methods is a promising direction given their demonstrated ability to improve data efficiency over standard supervised learning.

Our methodology has several significant limitations. Despite our focus on zero-shot transfer, we repeatedly queried performance on full validation sets to guide the development of CLIP. These validation sets often have thousands of examples, which is unrealistic for true zero-shot scenarios. Similar concerns have been raised in the field of semi-supervised learning . Another potential issue is our selection of evaluation datasets. While we have reported results on 's 12 dataset evaluation suite as a standardized collection, our main results use a somewhat haphazardly assembled collection of 27 datasets that is undeniably co-adapted with the development and capabilities of CLIP. Creating a new benchmark of tasks designed explicitly to evaluate broad zero-shot transfer capabilities, rather than re-using existing supervised datasets, would help address these issues.

CLIP is trained on text paired with images on the internet. These image-text pairs are unfiltered and uncurated and result in CLIP models learning many social biases. This has been previously demonstrated for image caption models . We refer readers to Section for detailed analysis and quantification of these behaviors for CLIP as well as discussion of potential mitigation strategies.

While we have emphasized throughout this work that specifying image classifiers through natural language is a flexible and general interface, it has its own limitations. Many complex tasks and visual concepts can be difficult to specify just through text. Actual training examples are undeniably useful but CLIP does not optimize for few-shot performance directly. In our work, we fall back to fitting linear classifiers on top of CLIP's features. This results in a counter-intuitive drop in performance when transitioning from a zero-shot to a few-shot setting. As discussed in Section , this is notably different from human performance which shows a large increase from a zero to a one shot setting. Future work is needed to develop methods that combine CLIP's strong zero-shot performance with efficient few-shot learning.

@src https://arxiv.org/abs/2103.00020
@title Learning Transferable Visual Models From Natural Language Supervision
@section Broader Impacts

CLIP has a wide range of capabilities due to its ability to carry out arbitrary image classification tasks. One can give it images of cats and dogs and ask it to classify cats, or give it images taken in a department store and ask it to classify shoplifters–a task with significant social implications and for which AI may be unfit. Like any image classification system, CLIP's performance and fitness for purpose need to be evaluated, and its broader impacts analyzed in context. CLIP also introduces a capability that will magnify and alter such issues: CLIP makes it possible to easily create your own classes for categorization (to 'roll your own classifier') without a need for re-training. This capability introduces challenges similar to those found in characterizing other, large-scale generative models like GPT-3 ; models that exhibit non-trivial zero-shot (or few-shot) generalization can have a vast range of capabilities, many of which are made clear only after testing for them.

Our studies of CLIP in a zero-shot setting show that the model displays significant promise for widely-applicable tasks like image retrieval or search. For example, it can find relevant images in a database given text, or relevant text given an image. Further, the relative ease of steering CLIP toward bespoke applications with little or no additional data or training could unlock a variety of novel applications that are hard for us to envision today, as has occurred with large language models over the past few years.

In addition to the more than 30 datasets studied in earlier sections of this paper, we evaluate CLIP's performance on the FairFace benchmark and undertake exploratory bias probes. We then characterize the model's performance in a downstream task, surveillance, and discuss its usefulness as compared with other available systems. Many of CLIP’s capabilities are omni-use in nature (e.g. OCR can be used to make scanned documents searchable, to power screen reading technologies, or to read license plates). Several of the capabilities measured, from action recognition, object classification, and geo-localization, to facial emotion recognition, can be used in surveillance. Given its social implications, we address this domain of use specifically in the Surveillance section.

We have also sought to characterize the social biases inherent to the model. Our bias tests represent our initial efforts to probe aspects of how the model responds in different scenarios, and are by nature limited in scope. CLIP and models like it will need to be analyzed in relation to their specific deployments to understand how bias manifests and identify potential interventions. Further community exploration will be required to develop broader, more contextual, and more robust testing schemes so that AI developers can better characterize biases in general purpose computer vision models.

@src https://arxiv.org/abs/2103.00020
@title Learning Transferable Visual Models From Natural Language Supervision
@section Future Work

This preliminary analysis is intended to illustrate some of the challenges that general purpose computer vision models pose and to give a glimpse into their biases and impacts. We hope that this work motivates future research on the characterization of the capabilities, shortcomings, and biases of such models, and we are excited to engage with the research community on such questions.

We believe one good step forward is community exploration to further characterize the capabilities of models like CLIP and - crucially - identify application areas where they have promising performance and areas where they may have reduced performance (A model could be unfit for use due to inadequate performance or due to the inappropriateness of AI use in the application area itself. . This process of characterization can help researchers increase the likelihood models are used beneficially by:

Identifying potentially beneficial downstream uses of models early in the research process, enabling other researchers to think about applications.

Surfacing tasks with significant sensitivity and a large set of societal stakeholders, which may call for intervention by policymakers.

Better characterizing biases in models, alerting other researchers to areas of concern and areas for interventions.

Creating suites of tests to evaluate systems like CLIP on, so we can better characterize model capabilities earlier in the development cycle.

Identifying potential failure modes and areas for further work.

We plan to contribute to this work, and hope this analysis provides some motivating examples for subsequent research.

@src https://arxiv.org/abs/2105.05233
@title Diffusion Models Beat GANs on Image Synthesis
@section Limitations and Future Work

While we believe diffusion models are an extremely promising direction for generative modeling, they are still slower than GANs at sampling time due to the use of multiple denoising steps (and therefore forward passes). One promising work in this direction is from ddimdistill , who explore a way to distill the DDIM sampling process into a single step model. The samples from the single step model are not yet competitive with GANs, but are much better than previous single-step likelihood-based models. Future work in this direction might be able to completely close the sampling speed gap between diffusion models and GANs without sacrificing image quality.

Our proposed classifier guidance technique is currently limited to labeled datasets, and we have provided no effective strategy for trading off diversity for fidelity on unlabeled datasets. In the future, our method could be extended to unlabeled data by clustering samples to produce synthetic labels unlabeledgan or by training discriminative models to predict when samples are in the true data distribution or from the sampling distribution.

The effectiveness of classifier guidance demonstrates that we can obtain powerful generative models from the gradients of a classification function. This could be used to condition pre-trained models in a plethora of ways, for example by conditioning an image generator with a text caption using a noisy version of CLIP clip , similar to recent methods that guide GANs using text prompts clipglass,styleclip,bigsleep . It also suggests that large unlabeled datasets could be leveraged in the future to pre-train powerful diffusion models that can later be improved by using a classifier with desirable properties.

@src https://arxiv.org/abs/2112.10741
@title GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models
@section Limitations

While our model can often compose disparate concepts in complex ways, it sometimes fails to capture certain prompts which describe highly unusual objects or scenarios. In Figure , we provide some examples of these failure cases.

Our unoptimized model takes 15 seconds to sample one image on a single A100 GPU. This is much slower than sampling for related GAN methods, which produce images in a single forward pass and are thus more favorable for use in real-time applications.

@src https://arxiv.org/abs/2112.10752
@title High-Resolution Image Synthesis with Latent Diffusion Models
@section Limitations & Societal Impact

While LDMs significantly reduce computational requirements compared to pixel-based approaches,

their sequential sampling process is still slower than that of GANs.

Moreover, the use of LDMs can be questionable when high precision is required:

although the loss of image quality is very small in our MATH autoencoding models (see Fig. ),

their reconstruction capability can become a bottleneck for tasks that require fine-grained accuracy in pixel space.

We assume that our superresolution models (Sec. ) are already somewhat limited in this respect.

Generative models for media like imagery are a double-edged sword: On the one hand, they enable various creative applications,

and in particular approaches like ours that reduce the cost of training and inference have the potential

to facilitate access to this technology and democratize its exploration.

On the other hand, it also means that it becomes easier to create and disseminate manipulated data or spread misinformation and spam.

In particular, the deliberate manipulation of images ("deep fakes") is a common problem in this context,

and women in particular are disproportionately affected by it .

Generative models can also reveal their training data ,

which is of great concern when the data contain sensitive or personal information

and were collected without explicit consent.

However, the extent to which this also applies to DMs of images is not yet fully understood.

Finally, deep learning modules tend to reproduce or exacerbate biases that are already present in the data .

While diffusion models achieve better coverage of the data distribution than GAN-based approaches,

the extent to which our two-stage approach that combines adversarial training and a likelihood-based objective

misrepresents the data remains an important research question.

For a more general, detailed discussion of the ethical considerations of deep generative models, see .

@src https://arxiv.org/abs/2201.03545
@title A ConvNet for the 2020s
@section Limitations

We demonstrate ConvNeXt, a pure ConvNet model, can perform as good as a hierarchical vision Transformer on image classification, object detection, instance and semantic segmentation tasks. While our goal is to offer a broad range of evaluation tasks, we recognize computer vision applications are even more diverse. ConvNeXt may be more suited for certain tasks, while Transformers may be more flexible for others. A case in point is multi-modal learning, in which a cross-attention module may be preferable for modeling feature interactions across many modalities. Additionally, Transformers may be more flexible when used for tasks requiring discretized, sparse, or structured outputs. We believe the architecture choice should meet the needs of the task at hand while striving for simplicity.

@src https://arxiv.org/abs/2201.03545
@title A ConvNet for the 2020s
@section Societal Impact

In the 2020s, research on visual representation learning began to place enormous demands on computing resources. While larger models and datasets improve performance across the board, they also introduce a slew of challenges. ViT, Swin, and ConvNeXt all perform best with their huge model variants. Investigating those model designs inevitably results in an increase in carbon emissions. One important direction, and a motivation for our paper, is to strive for simplicity — with more sophisticated modules, the network's design space expands enormously, obscuring critical components that contribute to the performance difference. Additionally, large models and datasets present issues in terms of model robustness and fairness.

Further investigation on the robustness behavior of ConvNeXt vs. Transformer will be an interesting research direction. In terms of data, our findings indicate that ConvNeXt models benefit from pre-training on large-scale datasets. While our method makes use of the publicly available ImageNet-22K dataset, individuals may wish to acquire their own data for pre-training. A more circumspect and responsible approach to data selection is required to avoid potential concerns with data biases.

@src https://arxiv.org/abs/2201.11903
@title Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
@section Discussion

We have explored chain-of-thought prompting as a simple mechanism for eliciting multi-step reasoning behavior in large language models.

We first saw that chain-of-thought prompting improves performance by a large margin on arithmetic reasoning, yielding improvements that are much stronger than ablations and robust to different annotators, exemplars, and language models ( sec:arithmetic-reasoning ).

Next, experiments on commonsense reasoning underscored how the linguistic nature of chain-of-thought reasoning makes it generally applicable ( sec:commonsense-reasoning ).

Finally, we showed that for symbolic reasoning, chain-of-thought prompting facilitates OOD generalization to longer sequence lengths ( sec:symbolic-reasoning ).

In all experiments, chain-of-thought reasoning is elicited simply by prompting an off-the-shelf language model.

No language models were finetuned in the process of writing this paper.

The emergence of chain-of-thought reasoning as a result of model scale has been a prevailing theme .

For many reasoning tasks where standard prompting has a flat scaling curve, chain-of-thought prompting leads to dramatically increasing scaling curves.

Chain-of-thought prompting appears to expand the set of tasks that large language models can perform successfully—in other words, our work underscores that standard prompting only provides a lower bound on the capabilities of large language models.

This observation likely raises more questions than it answers—for instance, how much more can we expect reasoning ability to improve with a further increase in model scale?

What other prompting methods might expand the range of tasks that language models can solve?

As for limitations, we first qualify that although chain of thought emulates the thought processes of human reasoners, this does not answer whether the neural network is actually "reasoning," which we leave as an open question.

Second, although the cost of manually augmenting exemplars with chains of thought is minimal in the few-shot setting, such annotation costs could be prohibitive for finetuning (though this could potentially be surmounted with synthetic data generation, or zero-shot generalization).

Third, there is no guarantee of correct reasoning paths, which can lead to both correct and incorrect answers; improving factual generations of language models is an open direction for future work .

Finally, the emergence of chain-of-thought reasoning only at large model scales makes it costly to serve in real-world applications; further research could explore how to induce reasoning in smaller models.

@src https://arxiv.org/abs/2203.02155
@title Training language models to follow instructions with human feedback
@section Limitations

Methodology. The behavior of our InstructGPT models is determined in part by the human feedback obtained from our contractors. Some of the labeling tasks rely on value judgments that may be impacted by the identity of our contractors, their beliefs, cultural backgrounds, and personal history. We hired about 40 contractors, guided by their performance on a screening test meant to judge how well they could identify and respond to sensitive prompts, and their agreement rate with researchers on a labeling task with detailed instructions (see Appendix ). We kept our team of contractors small because this facilitates high-bandwidth communication with a smaller set of contractors who are doing the task full-time. However, this group is clearly not representative of the full spectrum of people who will use and be affected by our deployed models. As a simple example, our labelers are primarily English-speaking and our data consists almost entirely of English instructions.

There are also many ways in which we could improve our data collection set-up. For instance, most comparisons are only labeled by 1 contractor for cost reasons. Having examples labeled multiple times could help identify areas where our contractors disagree, and thus where a single model is unlikely to align to all of them. In cases of disagreement, aligning to the average labeler preference may not be desirable. For example, when generating text that disproportionately affects a minority group, we may want the preferences of labelers belonging to that group to be weighted more heavily.

Models. Our models are neither fully aligned nor fully safe; they still generate toxic or biased outputs, make up facts, and generate sexual and violent content without explicit prompting. They can also fail to generate reasonable outputs on some inputs; we show some examples of this in Figure .

Perhaps the greatest limitation of our models is that, in most cases, they follow the user's instruction, even if that could lead to harm in the real world. For example, when given a prompt instructing the models to be maximally biased, InstructGPT generates more toxic outputs than equivalently-sized GPT-3 models. We discuss potential mitigations in the following sections.

@src https://arxiv.org/abs/2203.02155
@title Training language models to follow instructions with human feedback
@section Broader impacts

This work is motivated by our aim to increase the positive impact of large language models by training them to do what a given set of humans want them to do. By default, language models optimize the next word prediction objective, which is only a proxy for what we want these models to do. Our results indicate that our techniques hold promise for making language models more helpful, truthful, and harmless. In the longer term, alignment failures could lead to more severe consequences, particularly if these models are deployed in safety-critical situations. We expect that as model scaling continues, greater care has to be taken to ensure that they are aligned with human intentions .

However, making language models better at following user intentions also makes them easier to misuse. It may be easier to use these models to generate convincing misinformation, or hateful or abusive content.

Alignment techniques are not a panacea for resolving safety issues associated with large language models; rather, they should be used as one tool in a broader safety ecosystem. Aside from intentional misuse, there are many domains where large language models should be deployed only with great care, or not at all. Examples include high-stakes domains such as medical diagnoses, classifying people based on protected characteristics, determining eligibility for credit, employment, or housing, generating political advertisements, and law enforcement. If these models are open-sourced, it becomes challenging to limit harmful applications in these and other domains without proper regulation. On the other hand, if large language model access is restricted to a few organizations with the resources required to train them, this excludes most people from access to cutting-edge ML technology. Another option is for an organization to own the end-to-end infrastructure of model deployment, and make it accessible via an API. This allows for the implementation of safety protocols like use case restriction (only allowing the model to be used for certain applications), monitoring for misuse and revoking access to those who misuse the system, and rate limiting to prevent the generation of large-scale misinformation. However, this can come at the cost of reduced transparency and increased centralization of power because it requires the API provider to make decisions on where to draw the line on each of these questions.

Finally, as discussed in Section , the question of who these models are aligned to is extremely important, and will significantly affect whether the net impact of these models is positive or negative.

@src https://arxiv.org/abs/2204.14198
@title Flamingo: a Visual Language Model for Few-Shot Learning
@section Discussion

Limitations. First, our models build on pretrained LMs, and as a side effect, directly inherit their weaknesses.

For example, LM priors are generally helpful, but may play a role in occasional hallucinations and ungrounded guesses.

Furthermore, LMs generalise poorly to sequences longer than the training ones.

They also suffer from poor sample efficiency during training.

Addressing these issues can accelerate progress in the field and enhance the abilities of VLMs like Flamingo.

Second, the classification performance of lags behind that of state-of-the-art contrastive models .

These models directly optimize for text-image retrieval, of which classification is a special case.

In contrast, our models handle a wider range of tasks, such as open-ended ones.

A unified approach to achieve the best of both worlds is an important research direction.

Third, in-context learning has significant advantages over gradient-based few-shot learning methods, but also suffers from drawbacks depending on the characteristics of the application at hand.

We demonstrate the effectiveness of in-context learning when access is limited to only a few dozen examples.

In-context learning also enables simple deployment, requiring only inference,

generally with no hyperparameter tuning needed.

However, in-context learning is known to be highly sensitive to various aspects of the demonstrations ,

and its inference compute cost and absolute performance scale poorly with the number of shots beyond this low-data regime.

There may be opportunities to combine few-shot learning methods to leverage their complementary benefits.

We discuss the limitations of our work in more depth in Appendix sec:limitations .

In terms of societal impacts, offers a number of benefits while carrying some risks.

Its ability to rapidly adapt to a broad range of tasks have the potential to enable non-expert users to obtain

performance in data-starved regimes, lowering the barriers to both beneficial and malicious applications.

is exposed to the same risks as large language models, such as outputting offensive language, propagating social biases and stereotypes, as well as leaking private information .

Its ability to additionally handle visual inputs poses specific risks such as gender and racial biases relating to the contents of the input images, similar to a number of visual recognition systems .

We refer the reader to Appendix sec:broader_impact for a more extensive discussion of the societal impacts of our work, both positive and negative;

as well as mitigation strategies and early investigations of risks relating to racial or gender bias and toxic outputs.

Finally we note that, following prior work focusing on language models ,

the few-shot capabilities of could be useful for mitigating such risks.

We proposed Flamingo, a general-purpose family of models that can be applied to image and video tasks with minimal task-specific training data.

explored interactive abilities of such as "chatting" with the model, demonstrating flexibility beyond traditional vision

Our results suggest that connecting pre-trained large language models with powerful visual models is an important step towards general-purpose visual understanding.

Acknowledgments and Disclosure of Funding.

We would like to thank many colleagues for useful discussions, suggestions, feedback, and advice, including:

@src https://arxiv.org/abs/2204.14198
@title Flamingo: a Visual Language Model for Few-Shot Learning
@section Limitations, failure cases and opportunities

Here, we describe some limitations and failure cases of our models, as well as opportunities for further improving our models and extending their abilities.

Although our visual language models have important advantages over contrastive models (e.g., few-shot learning and open-ended generation capabilities), their performance lags behind that of contrastive models on classification tasks.

We believe this is because the contrastive training objective directly optimizes for text-image retrieval,

and in practice, the evaluation procedure for classification can be thought of as a special case of image-to-text retrieval .

This is not the case for the language modeling objective we use to train our visual language models

and this may contribute to the observed performance gap on classification tasks.

In particular, have shown that language models suffer from various biases arising from the training data distribution, the set of samples used in the prompt, and their order.

They also show that such issues can be mitigated with calibration techniques,

provided one can assume a certain prior distribution (e.g., uniform) over the label space.

This assumption doesn't hold in general, and further research is needed to develop techniques to address these issues in the few-shot setting.

More generally, seeking objectives, architectures, or evaluation procedures that could bridge the gap between these two classes of models is a promising research direction.

Legacies of language models. Our models build on powerful pretrained causal language models, and as a side effect, directly inherit their weaknesses.

For instance, causal modeling of the conditioning inputs is strictly less expressive than bidirectional modeling.

In this direction, recent work has shown that non-causal masked language modeling adaptation followed by multitask fine-tuning can efficiently improve the zero-shot performance of causal decoder-only language models.

Furthermore, transformer-based language models tend to generalize poorly to test sequences significantly longer than the training ones .

In settings where the expected text output is too long, the ability of the models to leverage enough shots for few-shot learning can be affected.

For instance, for the VisDial dataset , a single shot consists of an image followed by a long dialogue composed of 21 different sentences.

A sequence of 32 VisDial shots is thus composed of at least MATH sentences, which in practice means that the prompt length ranges from MATH to MATH tokens.

This is significantly longer than the maximum sequence length ( MATH ) our LMs have been trained on .

To this end, we have capped our reported results on VisDial at 16 shots.

On another note, while our ablations demonstrate the importance of the language model priors inherited from frozen language models, we suspect that they may play a role in occasional hallucinations and ungrounded guesses observed in open-ended dialogue settings. We provide and analyze examples of such behaviours in Figure .

Finally, language modeling suffers from poor sample efficiency during pretraining .

Mitigating this issue has the potential to greatly accelerate progress in the field,

by improving turnaround of large-scale training runs and in turn increasing the feasibility of more systematic exploration of design decisions at larger scales.

Further discussion on typical weaknesses observed for large LMs can be found in .

Trade-offs of few-shot learning methods.

In the paper, we use in-context learning as our "go-to" few-shot learning method (see Section sec:adapt-vlm ).

This method has notable advantages over gradient-based approaches such as fine-tuning.

Indeed, in-context learning requires almost no hyperparameter tuning, works reasonably well in the very low data regime (dozens of examples), and only requires inference, simplifying deployment.

In contrast, gradient-based approaches require carefully tuned design choices to avoid overfitting (either by proper learning rate schedule or architecture design ) and often need more data (thousands) to work well.

This motivated our focus on in-context learning;

however, this approach also has drawbacks we discuss next.

The compute cost of in-context learning with transformer models scales linearly with the number of shots if one can reuse the few-shot prompt for multiple query samples (by caching the keys and values) and quadratically otherwise.

In contrast, gradient-based few-shot learning approaches have constant complexity with respect to the number of shots during inference.

In-context learning has also been shown to be disconcertingly sensitive to various aspects of the demonstrations, such as the order of the samples or their format.

When using in-context learning, performance plateaus rapidly as the number of few-shot samples increases beyond 32.

This proves a striking contrast with typical gradient-based methods, for which the amount of correctly paired training data is a critical factor for performance.

We note that RICES (Retrieval In-Context Example Selection described in Appendix ) effectively mitigates this issue for classification tasks (Appendix ), but still faces similar issues beyond a small number of example per class.

Recent work on understanding what makes in-context learning effective sheds some light on a possible explanation for why more shots do not always help .

In more detail, raise the question of whether in-context learning actually "learns" new tasks at inference time based on the provided input-output mappings, or simply recognizes and identifies tasks learned during training. On this question, the findings of suggest that the latter is the key driver of performance across diverse settings, and refer it as task location.

Similarly, show that the mapping from input to output generally has limited impact on few-shot performance, as opposed to specifying the overall format of the examples.

In line with these findings, we also observe non-trivial zero-shot performance using prompt without any images, hence also highlighting that the format of the task matters significantly.

Intuitively, a handful of samples may often be enough to perform task location well, but the model may generally not be able to leverage further samples at inference time to refine its behaviour.

In summary, there is no "golden" few-shot method that would work well in all scenarios.

In particular, the best choice of few-shot learning approach strongly depends on characteristics of the application, an important one being the number of annotated samples.

On this point, in our work, we demonstrate that in-context learning is highly effective in the data-starved regime (32 samples or fewer).

There may be opportunities to combine different methods to leverage their complementary benefits, in particular when targeting less data-constrained data regimes (e.g., hundreds of samples).

Extending the visual and text interface.

Natural language is a powerful and versatile input/output interface to provide descriptions of visual tasks to the model and generate outputs or estimate conditional likelihoods over possible outputs.

However, it may be a cumbersome interface for tasks that involve conditioning on or predicting more structured outputs such as bounding boxes (or their temporal and spatio-temporal counterparts); as well as making spatially (or temporally and spatio-temporally) dense predictions.

Furthermore, some vision tasks, such as predicting optical flow, involve predicting in continuous space, which is not something our model is designed to handle out of the box.

Finally, one may consider additional modalities besides vision that may be complementary, such as audio.

All of these directions have the potential to extend the range of tasks that our models can handle; and even improve performance on the ones we focus on, thanks to synergies between the corresponding abilities.

Scaling laws for vision-language models.

In this work, we scale up to 80B parameters and provide some initial insights on their scaling behaviour across evaluation benchmarks, summarized in Figure fig:results .

In the language space, an important line of work has focused on establishing scaling laws for language models .

In the vision domain, take a step in this direction.

Similar efforts have yet to be made for vision-language models, including contrastive models, as well as visual language models such as the ones we propose.

While language modeling scaling law research has focused on perplexity as the golden metric, we speculate that it may be more directly useful for our purposes

to establish such trends in terms of aggregate downstream evaluation task performance.

@src https://arxiv.org/abs/2205.11916
@title Large Language Models are Zero-Shot Reasoners
@section Discussion and Related Work

Several studies have shown that pre-trained models usually are not good at reasoning , but its ability can be substantially increased by making them produce step-by-step reasoning, either by fine-tuning or few-shot prompting (See tab:related_work for summary of related work).

Unlike most prior work, we focus on zero-shot prompting and

show that a single fixed trigger prompt substantially increases the zero-shot reasoning ability of LLMs across a variety of tasks requiring complex multi-hop thinking ( tab:main_results ), especially when the model is scaled up ( fig:model_size ).

It also generates reasonable and understandable across diverse tasks ( appx:further_experiment ), even when the final prediction is wrong ( appx:error_analysis ).

Similar to our work, demonstrate a prompt, "Let's solve this problem by splitting it into steps", would facilitate the multi-step reasoning in a simple arithmetic problem. However, they treated it as a task-specific example and did not evaluate quantitatively on diverse reasoning tasks against baselines.

propose to decompose a commonsense question into a series of information seeking question, such as "what is the definition of [X]". It does not require demonstrations but requires substantial manual prompt engineering per each reasoning task.

Our results strongly suggest that LLMs are decent zero-shot reasoners, while prior work often emphasize only few-shot learning and task-specific in-context learning, e.g. no zero-shot baselines were reported.

Our method does not require time-consuming fine-tuning or expensive sample engineering, and can be combined with any pre-trained LLM, serving as the strongest zero-shot baseline for all reasoning tasks.

Zero-shot Abilities of LLMs =-1 show that LLMs have excellent zero-shot abilities in many system-1 tasks, including reading comprehension, translation, and summarization.

show that such zero-shot abilities of LLMs can be increased by explicitly fine-tuning models to follow instructions.

Although these work focus on the zero-shot performances of LLMs, we focus on many system-2 tasks beyond system-1 tasks, considered a grand challenge for LLMs given flat scaling curves.

In addition, is orthogonal to instruction tuning; it increases zero-shot performance for Instruct GPT3, vanilla GPT3, and PaLM (See fig:model_size ).

From Narrow (task-specific) to Broad (multi-task) Prompting

Most prompts are task-specific. While few-shot prompts are naturally so due to task-specific in-context samples , majority of zero-shot prompts have also focused on per-task engineering (of templates) . Borrowing terminologies from which builds on hierarchical models of intelligence , these prompts are arguably eliciting "narrow generalization" or task-specific skills from LLMs. On the other hand, our method is a multi-task prompt and elicits "broad generalization" or broad cognitive abilities in LLMs, such as logical reasoning or system-2 itself. We hope our work can serve as a reference for accelerating not just logical reasoning research with LLMs, but also discovery of other broad cognitive capabilities within LLMs.

A limitation of the work is the lack of public information on the details of training datasets used for LLMs, e.g. 001 vs 002 for GPT models, original GPT3 vs InstructGPT , and data for PaLM models . However, big performance increases from to in all recent large models (InstructGPT 001 or 002, Original GPT3, and PaLM) and consistent improvements in both arithmetic and non-arithmetic tasks suggest that the models are unlikely simply memorizing, but instead capturing a task-agnostic multi-step reasoning capability for generic problem solving. While most results are based on InstructGPT since it is the best performing open-access LLM, key results are reproduced on PaLM, and dataset details in InstructGPT (Appendix A, B, and F in ) also confirm that it is not specially engineered for multi-step reasoning.

Our work is based on prompting methods for large language models. LLMs have been trained on large corpora from various sources on the web

and have shown to capture and amplify biases found in the training data. Prompting is a method that looks to take advantage of the patterns captured by language models conducive to various tasks, and therefore it has the same shortcomings. This being said, our approach is a more direct way to probe complex reasoning inside pre-trained LLMs, removing the confounding factor of in-context learning in prior few-shot approaches, and can lead to more unbiased study of biases in LLMs.

@src https://arxiv.org/abs/2205.14135
@title FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness
@section Limitations and Future Directions

We discuss limitations of our approach and future directions. Related work is given in sec:related_work .

Compiling to CUDA. Our current approach to building IO-aware implementations of attention requires writing a new CUDA kernel for each new attention implementation.

This requires writing the attention algorithm in a considerably lower-level language than PyTorch, and requires significant engineering effort.

Implementations may also not be transferrable across GPU architectures.

These limitations suggest the need for a method that supports writing attention

algorithms in a high-level language (e.g., PyTorch), and compiling to IO-aware implementations in CUDA—similar to efforts such as Halide in image processing .

We believe that the IO-aware approach can extend beyond attention.

Attention is the most memory-intensive computation in Transformers, but every layer in a deep network touches GPU HBM.

We hope our work inspires IO-aware implementations of additional modules.

We discuss these potential extensions in sec:extension_details .

Our IO-aware implementation of attention is optimal within constants for computing attention on a single GPU.

However, the attention computation may be parallelizable across multiple GPUs .

Using multiple GPUs adds an additional layer to IO analysis—accounting for data transfer between GPUs.

We hope our work inspires future work in this direction.

As Transformer-based foundation models grow in size and data, our work seeks to understand how to train these large models more efficiently.

This may allow a general community with limited access to computational resources to train and understand those foundation models.

Our method is applicable to all Transformer-based models, which have a variety of applications, both positive and negative. For example, language modeling may make it easier to spread misinformation, while image classification models may make automatic surveillance easier.

Alleviating these risks requires addressing application-specific issues such as privacy, bias, and discrimination.

@src https://arxiv.org/abs/2209.14988
@title DreamFusion: Text-to-3D using 2D Diffusion
@section Discussion

We have presented , an effective technique for text-to-3D synthesis for a wide range of text prompts.

works by transferring scalable, high-quality 2D image diffusion models to the 3D domain through our use of a novel approach and a novel NeRF-like rendering engine. does not require 3D or multi-view training data, and uses only a pre-trained 2D diffusion model (trained on only 2D images) to perform 3D synthesis.

Though produces compelling results and outperforms prior work on this task, it still has several limitations.

is not a perfect loss function when applied to image sampling, and often produces oversaturated and oversmoothed results relative to ancestral sampling.

While dynamic thresholding partially ameliorates this issue when applying to images, it did not resolve this issue in a NeRF context.

Additionally, 2D image samples produced using tend to lack diversity compared to ancestral sampling, and our 3D results exhibit few differences across random seeds.

This may be fundamental to our use of reverse KL divergence, which has been previously noted to have mode-seeking properties in the context of variational inference and probability density distillation.

uses the MATH Imagen model, and as such our 3D synthesized models tend to lack fine details. Using a higher-resolution diffusion model and a bigger NeRF would presumably address this, but synthesis would become impractically slow. Hopefully improvements in the efficiency of diffusion and neural rendering will enable tractable 3D synthesis at high resolution in the future.

The problem of 3D reconstruction from 2D observations is widely understood to be highly ill-posed, and this ambiguity has consequences in the context of 3D synthesis. Fundamentally, our task is hard for the same reason that inverse rendering is hard: there exist many possible 3D worlds that result in identical 2D images.

The optimization landscape of our task is therefore highly non-convex, and many of the details of this work are designed specifically to sidestep these local minima. But despite our best efforts we still sometimes observe local minima, such as 3D reconstructions where all scene content is "painted" onto a single flat surface. Though the techniques presented in this work are effective, this task of "lifting" 2D observations into a 3D world is inherently ambiguous, and may benefit from more robust 3D priors.

@src https://arxiv.org/abs/2210.08402
@title LAION-5B: An open large-scale dataset for training next generation image-text models
@section Technical Limitations

The large scale of current image-text datasets makes it infeasible to thoroughly investigate all aspects of a dataset in a single publication.

Hence we now outline some potential technical limitations specifically affecting LAION-5B.

These potential limitations are starting points for future work on analyzing and improving image-text datasets.

Data Overlap. Our experiments in Section show that models trained on LAION-5B achieve good performance on a variety of downstream tasks.

However, the LAION-5B training set may overlap with some of the downstream test sets if these test sets are also included in Common Crawl.

If overlap is present, it may lead to incorrectly large test set accuracies that overstate the true generalization capabilities of models trained on LAION-5B.

Overall, we do not consider potential test set overlap to be a serious threat for the validity of results obtained with LAION-5B.

OpenAI encountered the same question in the context of their pre-training dataset for CLIP and found only few examples of substantial performance difference due to data overlap on downstream target datasets .

Some datasets such as ObjectNet are likely not contained in Common Crawl because ObjectNet was not assembled from web images.

Instead, the authors of ObjectNet tasked MTurk workers to take new pictures in their own homes.

Nevertheless, measuring the degree of overlap between LAION-5B and popular computer vision benchmarks is an important question for future work, which will include further de-duplication efforts.

described the shortcomings of alt-text and noted that alt-text is not necessarily a good description of the corresponding image.

For instance, the alt-text may be search engine optimization (SEO) spam, an incoherent list of keywords, or overly corrupted otherwise. In such cases, the language in the text annotations may become less informative or entirely useless for training.

For ImageNet zero-shot classification, BASIC has demonstrated strong results when turning 5 billion of the 6.6 billion captions into the form of CLASS_1 and CLASS_2 and

... and CLASS_K, by using an internal multi-label classification dataset (JFT-3B). Thus, image captions formed by just concatenating class names may also serve as meaningful alternative of otherwise corrupted text. Such a finding adds a possibility of employing generated together with existing natural language captions for training contrastive image-language models with strong zero-shot performance.

CLIP allows the curation and collection of this dataset to be low-cost and scalable. Such an automated process reduces dramatically necessity for the human control which would be otherwise intractable for such large scale collection. However, through curating with CLIP, we also incur its flaws and model biases. For additional discussion of CLIP filtering related to safety and ethics, see Appendix Sec. .

Filtering by a small scale CLIP ViT-B/32 may leave more image-text pairs with weak or no semantic connection in the dataset while also accidentally removing some high quality image-text pairs than filtering with stronger, larger scale models that were not available in the time of our experiments. The larger CLIP ViT-L/14 model may create a less noisy version of LAION datasets than what was possible with smaller scale CLIP ViT-B/32. We hypothesize that filtering Common Crawl with a CLIP ViT-L model will further increase the quality of our dataset. It is subject to our future work to create a CLIP ViT L/14 filtered version of LAION-400M and LAION-5B to test how this affects model training and downstream transfer performance.

@src https://arxiv.org/abs/2210.08402
@title LAION-5B: An open large-scale dataset for training next generation image-text models
@section Safety and Ethical Discussion

Recent developments in large-scale models, such as GPT-3 , CLIP , ALIGN , GLIDE , and DALLE-2 have potential for far-reaching impact on society, both positive and negative, when deployed in applications such as image classification and generation, recommendation systems, or search engines.

Besides model parameter scaling, the advances made so far also rely on the underlying large-scale datasets.

Recent research described many potential negative societal implications that may arise due to careless use of vision-language models, e.g., the models perform worse for certain groups of users or reproduce discriminatory behavior.

Unfortunately, only a minority of these models are publicly released, most of them are only accessible by an "input to output" interface. Importantly, the underlying large-scale datasets are also not often publicly available.

While open-source efforts exist to re-implement model architectures and training, the closed nature of large-scale datasets used for model training makes any proper systematic investigation of model training and model behavior very hard or even impossible. Studying full training, comparison of different model architectures and progress in large-scale multi-modal learning becomes restricted to those institutions that were able to obtain their closed large-scale datasets. It also results in safety issues of creating and using such models, as broad research community does not get to test both model and the dataset used for its training for causes underlying undesired behaviours.

LAION-5B as an open large-scale dataset provides here not only a chance to make progress in careful studies of the trained models' capabilities and replication but also to investigate how uncurated large-scale datasets impact various model biases and under which circumstances their usage may result in undesired safety issues. Such research can help to design automated ways to curate and create datasets from uncurated ones that alleviate the bias and safety issues. To this end, LAION also created a number of tools to aid researchers and other users in large-scale data handling and exploration. One such a tool uses pre-computed image embeddings to enable search of images guided either by text or image input via an easily and publically accessible web interface (CLIP retrieval tool (https://knn5.laion.ai https://knn5.laion.ai , see Appendix Sec. ). LAION made also source code for the tool and routines necessary to build an own version of it publicly available (https://github.com/rom1504/clip-retrieval https://github.com/rom1504/clip-retrieval (see Appendix Sec , , for more details).

After the release of LAION-400M, several groups (e.g., ) already used such tools and investigated potential problems arising from an unfiltered dataset. Motivated by these findings, with LAION-5B, we introduced an improved inappropriate content tagging (cf. Sec. )

as well as a watermark filter, which can improve the safety and quality of the text-to-image models trained on the dataset.

Such development indicates that this dataset acts as a starting point, and is not the final endpoint, for creating further improved datasets to train models for various tasks. In our opinion, this process is not supposed to be a non-transparent closed-door avenue. It should be approached by broad research community, resulting in open and transparent datasets and procedures for model training. Towards meeting this challenge, the large-scale public image-text dataset of over 5.8 billion pairs and further annotations introduced here provides diversity that can be a starting point for ensuring balance and for selecting safe, curated subsets for corresponding target applications. We encourage everybody to participate in this exciting and important future journey.

In the current form, we consider this dataset a research artefact and strongly advocate academic use-only and advise careful investigation of downstream model biases (Appendix Sec. ). Additionally, we encourage users to use the described tools and to transparently explore and, subsequently, report further not yet detected content and model behaviour to our dataset repository (https://github.com/laion-ai/laion5b-bias https://github.com/laion-ai/laion5b-bias , and help to further advance existing approaches for data curation using the real-world large dataset introduced here.

Privacy. We comment on privacy issues arising from Common Crawl as source of links in LAION-5B and measures undertaken to handle those in the Appendix Sec.

@src https://arxiv.org/abs/2301.12597
@title BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models
@section Limitation

Recent LLMs can perform in-context learning given few-shot examples.

our experiments with BLIP-2 do not observe an improved VQA performance when providing the LLM with in-context VQA examples.

We attribute the lack of in-context learning capability to our pre-training dataset,

which only contains a single image-text pair per sample.

The LLMs cannot learn from it the correlation among multiple image-text pairs in a single sequence.

The same observation is also reported in the Flamingo paper,

which uses a close-sourced interleaved image and text dataset (M3W) with multiple image-text pairs per sequence.

We aim to create a similar dataset in future work.

BLIP-2's image-to-text generation could have unsatisfactory results due to various reasons including inaccurate knowledge from the LLM,

activating the incorrect reasoning path,

or not having up-to-date information about new image content (see Figure ).

such as outputting offensive language, propagating social bias, or leaking private information.

Remediation approaches include using instructions to guide model's generation or training on a filtered dataset with harmful content removed.

@src https://arxiv.org/abs/2304.07193
@title DINOv2: Learning Robust Visual Features without Supervision
@section Future work and Discussion

In this work, we present DINOv2, a new series of image encoders pretrained on large curated data with no supervision.

This is the first SSL work on image data that leads to visual features that close the performance gap with (weakly) supervised alternatives across a wide range of benchmarks and without the need for finetuning.

We can attribute the strong performance of the DINOv2 family of models to several factors:

i) an improved training recipe with better hyperparameters and regularization (Table ),

ii) a larger model scale with improved results regardless of the data used for training (Fig. ),

iv) the distillation process that makes smaller models benefit from the performance of the strongest ViT-g model (Fig. ).

A few properties emerge from these models, such as an understanding of object parts and scene geometry regardless of the image domains.

We expect that more of these properties will emerge at larger scales of models and data, akin to instruction emergence in large language models, and plan to continue scaling along these axes.

This paper also demonstrates that these visual features are compatible with classifiers as simple as linear layers - meaning the underlying information is readily available.

In future work, we plan to leverage this ability to train a a language-enabled AI system that can process visual features as if they were word tokens, and extract the required information to ground the system.

@src https://arxiv.org/abs/2304.08485
@title Visual Instruction Tuning
@section Broader Impact

The broader impact of , a general-purpose visual assistant, has potential benefits and risks associated with its deployment and release. Some considerations are unique to due to its visual nature, while others share similarities with existing instruction-following LLMs ( Alpaca, Vicuna, ). As is built upon LLaMA, Vicuna, and CLIP, it inherits some of the issues associated with LLMs and vision encoders. In the following, we outline both the risks and mitigation strategies in place for the release of this model.

To minimize potential misuse and harmful consequences, we employ two precautionary measures for : (1) OpenAI Filter API for user input text to prevent harmful or inappropriate text instructions from being processed by the model, and (2) NSFW Filter for uploaded user images to detect and block Not Safe For Work (NSFW) content or any other potentially harmful image inputs.

Similar to LLMs, might generate outputs that aren't grounded in facts or input data. This raises concerns about inferences made, especially in critical applications ( medical).

Bias can be transferred from the base models to , both from the vision encoder (CLIP) and the language decoder (LLaMA/Vicuna). This may lead to biased outcomes or unfair representations of diverse content.

Though energy consumption is not a primary concern for due to a smaller pretraining dataset (see details in Sec. ), it may become a concern when scaling up the pretraining dataset or increasing the model size, e.g., to a larger LLaMA version like the 65B model.

Assessing the performance of is challenging as it involves both language and visual tasks. Our evaluation benchmark covers several aspects, including accuracy, concept coverage, reasoning ability, and creativity. However, additional aspects need consideration, such as the degree of visual content hallucination and fine-grained understanding of visual content. While text-only GPT-4 based multimodal evaluation is consistent and accurate in our study, its robustness in different situations and capability to evaluate other unexplored aspects are subjects for future work.

Despite these risks, we believe that the benefits of releasing to the research community outweigh the potential harm. It allows for ongoing investigation and improvement of the model and engages the community in developing better mitigation strategies to address these concerns. Moreover, the release of can spur the development of new applications and research directions, ultimately contributing to the progress and responsible deployment of foundation models in vision-language tasks.

@src https://arxiv.org/abs/2304.10592
@title MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models
@section Limitation analysis

As MiniGPT-4 is built upon LLMs, it inherits LLM's limitations like hallucinating nonexistent knowledge. An example in Fig. shows that MiniGPT-4 incorrectly identifies the presence of white tablecloths in the image, despite their absence. Here, we use the metric MATH to gauge the hallucination rate of the generation, with the two distinct prompts to control the model generation length: MiniGPT-4 (long): Please describe this image as detailed as possible. MiniGPT-4 (short): Please describe the image shortly and precisely, in less than 20 words.

Results in Tab. show that longer captions tend to have higher hallucination rates. For example, MiniGPT-4 (long) generates captions averaging 175 words with a higher hallucination rate, while MiniGPT-4 (short) averages 28.8 words with a lower rate. BLIP-2, averaging 6.5 words, hallucinates less but covers fewer objects as seen in Tab. .

Hallucination in detailed image descriptions is still an unresolved issue. Using Reinforcement Learning with AI feadback with hallucination detection modules may be a potential solution.

Spatial Information Understanding MiniGPT-4's visual perception remains limited. It may struggle to differentiate spatial localization. For example, MiniGPT-4 in Fig. fails to identify the location of the windows.

This limitation may stem from a lack of aligned image-text data designed for spatial information understanding. Training on such datasets like RefCOCO or Visual Genome could potentially alleviate this issue.

@src https://arxiv.org/abs/2304.10592
@title MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models
@section Discussion

How does MiniGPT-4 obtain these advanced abilities?

Many of the advanced vision-language capabilities demonstrated by GPT-4 can be understood as compositional skills rooted in two foundational skills: image understanding and language generation.

Take the task of image-based poem writing as an example. Advanced LLMs like ChatGPT and Vicuna can already craft poems based on users' instructions.

If they acquire the ability to understand images, compositionally generalizing to the task of image-based poem writing even without having image-poem pairs in their training data is possible.

In the first pretraining stage, MiniGPT-4 learns to understand images by modeling the correlation between images and short image descriptions from image caption datasets.

However, the language style in these image caption datasets differs from that of modern LLMs' generation, which leads to distorted language generation and hinders successful compositional generalization.

Therefore, we introduce a second-stage finetuning to restore the language generation ability.

MiniGPT-4 after the two-stage training successfully generalizes to many advanced compositional vision-language abilities like website coding from drafts or meme interpretation, verifies our assumption.

Future research might delve deeper into the mechanism of compositional generalization and seek ways to enhance them. We hope our work, as an early exploration of these vision-based LLM capabilities, will spur further investigations in this domain.

@src https://arxiv.org/abs/2305.10601
@title Tree of Thoughts: Deliberate Problem Solving with Large Language Models
@section Discussion

Deliberate search such as ToT might not be necessary for many existing tasks that GPT-4 already excels at (see Appendix ), and as an initial step this work only explores three relatively simple tasks that challenges GPT-4 (see Appendix for some GPT-3.5 experiment results) and calls of better search and planning abilities incorporated with LMs. However, as we begin to deploy LMs for more real-world decision making applications (e.g.\,coding, data analysis, robotics, etc.), more complex tasks could emerge and present new opportunities to study these research questions. Also, search methods like ToT requires more resources (e.g.\,GPT-4 API cost) than sampling methods in order to improve task performances, but the modular flexibility of ToT allows users to customize such performance-cost tradeoffs, and ongoing open-source efforts should readily reduce such costs in the near future. More details about cost and efficiency are in Appendix . Lastly, this work focuses on using an off-the-shelf LM, and fine-tuning LMs using a ToT-style high-level counterfactual decision making (e.g.\,deliberating over potential choices for the next paragraph, instead of predicting the next token) might present opportunities to enhance the problem-solving capabilities of LMs.

Conclusion. The associative "System 1" of LMs can be beneficially augmented by a "System 2" based on searching a tree of possible paths to the solution to a problem. The Tree of Thoughts framework provides a way to translate classical insights about problem-solving into actionable methods for contemporary LMs. At the same time, LMs address a weakness of these classical methods, providing a way to solve complex problems that are not easily formalized, such as creative writing. We see this intersection of LMs with classical approaches to AI as an exciting direction.

@src https://arxiv.org/abs/2305.10601
@title Tree of Thoughts: Deliberate Problem Solving with Large Language Models
@section Broader Impact

ToT is a framework that empowers LMs to more autonomously and intelligently make decisions and solve problems. While current tasks are limited to reasoning and search problems, future applications involving interaction with external environments or humans could bring potential danger, e.g.\,facilitating harmful uses of LMs. On the other hand, ToT also improves the interpretability of model decisions and the opportunity for human alignment, as the resulting representations are readable, high-level language reasoning instead of implicit, low-level token values.

@src https://arxiv.org/abs/2305.14314
@title QLoRA: Efficient Finetuning of Quantized LLMs
@section Limitations and Discussion

We have shown evidence that our method, , can replicate 16-bit full finetuning performance with a 4-bit base model and Low-rank Adapters (LoRA). Despite this evidence, we did not establish that can match full 16-bit finetuning performance at 33B and 65B scales. Due to the immense resource costs, we leave this study to future work.

Another limitation is the evaluation of instruction finetuning models. While we provide evaluations on MMLU, the Vicuna benchmark, and the OA benchmark, we did not evaluate on other benchmarks such as BigBench, RAFT, and HELM, and it is not ensured that our evaluations generalize to these benchmarks. On the other hand, we perform a very broad study on MMLU and develop new methods for evaluating chatbots.

From the evidence presented, it appears that the performance of these benchmarks likely depends how similar the finetuning data is to the benchmark dataset. For example, FLAN v2 is similar to MMLU, but dissimilar to chatbot benchmarks and vice versa for the Chip2 dataset and both models score accordingly on the MMLU and Vicuna benchmarks. This highlights that not only better benchmarks and evaluation is needed, but that one needs to be careful about what one is evaluating in the first place. Do we want to create models that do well on classroom highschool and colleague knowledge or do we want to do well on chatbot conversation ability? Maybe something else? Because it is always easier to evaluate on an existing benchmark compared to creating a new one, certain benchmarks can steer the community towards a certain direction. We should ensure as a community that the benchmarks measure what we care about.

While we provide a detailed evaluation for general chatbot performance, another limitation is that we only do a limited responsible AI evaluation of . We evaluate the likelihood of -65B to generate a socially biased sequence of tokens compared to other models in Table . We see that the average score in -65B is much lower than other raw pretrained models. As such, it seems that finetuning on the OASST1 dataset reduces the bias of the LLaMA base model. While these results are encouraging, it is unclear if does also well when assessed on other types of biases. We leave further evaluation of analyzing biases in and similar chatbots to future work.

An additional limitation is that we did not evaluate different bit-precisions, such as using 3-bit base models, or different adapter methods. Besides LoRA, there is also a wide variety Parameter Efficient FineTuning (PEFT) methods that have been shown to work well. However, it is unclear if these methods scale to large models. We used LoRA as many results established its robustness but other adapters might yield better performance. Since finetuning after quantization seems to recover most of the information that is lost during quantization this might enable much more aggressive quantization. For example, 3-bit GPTQ quantization of the basemodel with LoRA might also yield 16-bit full finetuning performance after finetuning.

@src https://arxiv.org/abs/2305.14314
@title QLoRA: Efficient Finetuning of Quantized LLMs
@section Broader Impacts

Our finetuning method is the first method that enables the finetuning of 33B parameter models on a single consumer GPU and 65B parameter models on a single professional GPU, while not degrading performance relative to a full finetuning baseline. We have demonstrated that our best 33B model trained on the Open Assistant dataset can rival ChatGPT on the Vicuna benchmark. Since instruction finetuning is an essential tool to transform raw pretrained LLMs into ChatGPT-like chatbots, we believe that our method will make finetuning widespread and common in particular for the researchers that have the least resources, a big win for the accessibility of state of the art NLP technology. can be seen as an equalizing factor that helps to close the resource gap between large corporations and small teams with consumer GPUs.

Another potential source of impact is deployment to mobile phones. We believe our method might enable the critical milestone of enabling the finetuning of LLMs on phones and other low resource settings. While 7B models were shown to be able to be run on phones before, is the first method that would enable the finetuning of such models. We estimate that with an iPhone 12 Plus, can finetune 3 million tokens per night while the phone is charging. While finetuned 7B models do not reach the quality of ChatGPT, we believe that the quality is good enough to enable novel applications that have not been possible before due to privacy or LLM quality issues. can help enable privacy-preserving usage of LLMs, where users can own and manage their own data and models, while simultaneously making LLMs easier to deploy.

However, finetuning is a dual-use technology that can be abused to cause harm. Widespread use of LLMs has known dangers , but we believe that equalizing access to a technology that is quickly becoming ubiquitous will allow for better more independent analysis than keeping the power of LLMs in the hands of large corporations that do not release models or source code for auditing.

All in all, we believe that will have a broadly positive impact making the finetuning of high quality LLMs much more widely and easily accessible.

@src https://arxiv.org/abs/2305.18290
@title Direct Preference Optimization: Your Language Model is Secretly a Reward Model
@section Discussion

Learning from preferences is a powerful, scalable framework for training capable, aligned language models. We have introduced DPO, a simple training paradigm for training language models from preferences without reinforcement learning. Rather than coercing the preference learning problem into a standard RL setting in order to use off-the-shelf RL algorithms, DPO identifies a mapping between language model policies and reward functions that enables training a language model to satisfy human preferences directly, with a simple cross-entropy loss, without reinforcement learning or loss of generality. With virtually no tuning of hyperparameters, DPO performs similarly or better than existing RLHF algorithms, including those based on PPO; DPO thus meaningfully reduces the barrier to training more language models from human preferences.

Limitations & Future Work. Our results raise several important questions for future work. How does the DPO policy generalize out of distribution, compared with learning from an explicit reward function? Our initial results suggest that DPO policies can generalize similarly to PPO-based models, but more comprehensive study is needed. For example, can training with self-labeling from the DPO policy similarly make effective use of unlabeled prompts? On another front, how does reward over-optimization manifest in the direct preference optimization setting, and is the slight decrease in performance in Figure -right an instance of it? Additionally, while we evaluate models up to 6B parameters, exploration of scaling DPO to state-of-the-art models orders of magnitude larger is an exciting direction for future work. Regarding evaluations, we find that the win rates computed by GPT-4 are impacted by the prompt; future work may study the best way to elicit high-quality judgments from automated systems. Finally, many possible applications of DPO exist beyond training language models from human preferences, including training generative models in other modalities.

@src https://arxiv.org/abs/2307.01952
@title SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis
@section Future Work

This report presents a preliminary analysis of improvements to the foundation model for text-to-image synthesis. While we achieve significant improvements in synthesized image quality, prompt adherence and composition, in the following, we discuss a few aspects for which we believe the model may be improved further:

Single stage: Currently, we generate the best samples from using a two-stage approach with an additional refinement model. This results in having to load two large models into memory, hampering accessibility and sampling speed. Future work should investigate ways to provide a single stage of equal or better quality.

Text synthesis: While the scale and the larger text encoder (OpenCLIP ViT-bigG ) help to improve the text rendering capabilities over previous versions of , incorporating byte-level tokenizers or simply scaling the model to larger sizes may further improve text synthesis.

Architecture: During the exploration stage of this work, we briefly experimented with transformer-based architectures such as UViT and DiT , but found no immediate benefit. We remain, however, optimistic that a careful hyperparameter study will eventually enable scaling to much larger transformer-dominated architectures.

Distillation: While our improvements over the original model are significant, they come at the price of increased inference cost (both in VRAM and sampling speed). Future work will thus focus on decreasing the compute needed for inference, and increased sampling speed, for example through guidance- , knowledge- and progressive distillation .

Our model is trained in the discrete-time formulation of , and requires offset-noise for aesthetically pleasing results. The EDM-framework of is a promising candidate for future model training, as its formulation in continuous time allows for increased sampling flexibility and does not require noise-schedule corrections.

@src https://arxiv.org/abs/2307.01952
@title SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis
@section Limitations

While our model has demonstrated impressive capabilities in generating realistic images and synthesizing complex scenes, it is important to acknowledge its inherent limitations. Understanding these limitations is crucial for further improvements and ensuring responsible use of the technology.

Firstly, the model may encounter challenges when synthesizing intricate structures, such as human hands (see fig:failure_cases , top left). Although it has been trained on a diverse range of data, the complexity of human anatomy poses a difficulty in achieving accurate representations consistently. This limitation suggests the need for further scaling and training techniques specifically targeting the synthesis of fine-grained details. A reason for this occurring might be that hands and similar objects appear with very high variance in photographs and it is hard for the model to extract the knowledge of the real 3D shape and physical limitations in that case.

Secondly, while the model achieves a remarkable level of realism in its generated images, it is important to note that it does not attain perfect photorealism. Certain nuances, such as subtle lighting effects or minute texture variations, may still be absent or less faithfully represented in the generated images. This limitation implies that caution should be exercised when relying solely on model-generated visuals for applications that require a high degree of visual fidelity.

Furthermore, the model's training process heavily relies on large-scale datasets,

which can inadvertently introduce social and racial biases. As a result, the model may inadvertently exacerbate these biases when generating images or inferring visual attributes.

In certain cases where samples contain multiple objects or subjects, the model may exhibit a phenomenon known as "concept bleeding".

This issue manifests as the unintended merging or overlap of distinct visual elements.

For instance, in fig:comp_old_model_app , an orange sunglass is observed, which indicates an instance of concept bleeding from the orange sweater.

Another case of this can be seen in fig:comparetoif , the penguin is supposed to have a "blue hat" and "red gloves", but is instead generated with blue gloves and a red hat.

Recognizing and addressing such occurrences is essential for refining the model's ability to accurately separate and represent individual objects within complex scenes.

The root cause of this may lie in the used pretrained text-encoders: firstly, they are trained to compress all information into a single token, so they may fail at binding only the right attributes and objects, mitigate this issue by explicitly encoding word relationships into the encoding. Secondly, the contrastive loss may also contribute to this, since negative examples with a different binding are needed within the same batch .

Additionally, while our model represents a significant advancement over previous iterations of , it still encounters difficulties when rendering long, legible text. Occasionally, the generated text may contain random characters or exhibit inconsistencies, as illustrated in fig:comparetoif .

Overcoming this limitation requires further investigation and development of techniques that enhance the model's text generation capabilities, particularly for extended textual content — see for example the work of , who propose to enhance text rendering capabilities via character-level text tokenizers. Alternatively, scaling the model does further improve text synthesis .

In conclusion, our model exhibits notable strengths in image synthesis, but it is not exempt from certain limitations. The challenges associated with synthesizing intricate structures, achieving perfect photorealism, further addressing biases, mitigating concept bleeding, and improving text rendering highlight avenues for future research and optimization.

@src https://arxiv.org/abs/2307.08691
@title FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning
@section Discussion and Future Directions

is 2 MATH faster than , which means that we can train models

with 16k longer context for the same price as previously training a 8k context

We are excited about how this can be used to understand long books and reports,

high resolution images, audio and video.

will also speed up training, finetuning, and inference of

In the near future, we plan to collaborate with researchers and engineers to

make FlashAttention widely applicable in different kinds of devices (e.g., H100

GPUs, AMD GPUs), as well as new data types such as FP8.

As an immediate next step, we plan to optimize FlashAttention-2 for H100 GPUs to

use new hardware features (TMA, 4th-gen Tensor Cores, fp8).

Combining the low-level optimizations in FlashAttention-2 with high-level

algorithmic changes (e.g., local, dilated, block-sparse attention) could allow

us to train AI models with much longer context.

We are also excited to work with compiler researchers to make these optimization

@src https://arxiv.org/abs/2307.15818
@title RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control
@section Limitations

Even though exhibits promising generalization properties, there are multiple limitations of this approach. First, although we show that including web-scale pretraining via VLMs boosts generalization over semantic and visual concepts, the robot does not acquire any ability to perform new motions by virtue of including this additional experience. The model's physical skills are still limited to the distribution of skills seen in the robot data (see Appendix ), but it learns to deploy those skills in new ways.

We believe this is a result of the dataset not being varied enough along the axes of skills. An exciting direction for future work is to study how new skills could be acquired through new data collection paradigms such as videos of humans.

Second, although we showed we could run large VLA models in real time, the computation cost of these models is high, and as these methods are applied to settings that demand high-frequency control, real-time inference may become a major bottleneck. An exciting direction for future research is to explore quantization and distillation techniques that might enable such models to run at higher rates or on lower-cost hardware. This is also connected to another current limitation in that there are only a small number of generally available VLM models that can be used to create . We hope that more open-sourced models will become available (e.g. https://llava-vl.github.io/) and the proprietary ones will open up their fine-tuning APIs, which is a sufficient requirement to build models.

@src https://arxiv.org/abs/2310.06770
@title SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
@section Discussion

task instances are all in Python; we hope to apply 's task instance collection procedure to expand its coverage to more programming languages and domains.

Second, our experiments aim to establish a baseline of the simplest and most straight-forward approaches for this task; we do not intend to constrain future methodologies to the same type of approach and encourage future work to investigate different methods (e.g., agent-based approaches, tool augmented LMs).

Lastly, while this work evaluates models using execution-based code testing, relying solely on this method is insufficient to guarantee reliable performance of model generations, as we find automated code generations from LMs can frequently be less comprehensive, efficient, or readable compared to human-written solutions.

The complexity of real-world software development processes extends far beyond just code completion.

By drawing on the open-source collaborative pipeline, creates a faithful mirror of real world coding environments.

This more realistic environment encourages creative solutions that can have immediate applicability in open-source software development.

We hope that this benchmark and our other contributions can serve as valuable assets in the future development of LMs that are more practical, intelligent, and autonomous.

@src https://arxiv.org/abs/2310.06770
@title SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
@section Societal Impact

As reasoning on code has emerged as a foundational skill underlying many LM's capability, a potential future of machine-automated software engineering raises many important questions and has important potential ramifications with regards to AI Safety .

It is important to address questions on how to ensure AI-generated code is faithful to human intents and what guardrails might be in place when human objectives are misinterpreted by code agents that then carry out the task.

To observe such problems in a controlled setting and manifest their solutions, we hope might serve as a testbed for designing safe, robust measures

towards aligned, verifiable, and safe AI-driven software engineering.

In this section, we provide five additional qualitative analyses of generations from both Claude 2 and generations (Oracle retrieval setting) following the style of Section .

Claude 2 qualitative studies can be found in Tables and .

Tables , , and are task instances that Claude 2 did not address correctly.

qualitative studies are covered across Tables , , , , .

For Tables , , and , we present task instances solved correctly by 13b.

In Table and , we present two task instances where 13b does not address the issue correctly, pointing out a subset of the reasoning and generation skills that models may not be adept at enough to accomplish the task at hand.

The observations we make across these sections corroborate with the points stated in the main paper, which is that models tend to struggle with multi-line and multi-file changes, are more adept when the required fix is relatively short, and need help with understanding the codebase in an efficient manner.

@src https://arxiv.org/abs/2310.11511
@title Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection
@section Ethical Concerns

This work aims to improve the factuality of LLM outputs, the lack of which continues to cause numerous real-world problems (e.g., spread of misinformation and provision of incorrect and dangerous advice). While our method shows significant improvements in terms of performance, factuality, and citation accuracy, it can still generate outputs that are not fully supported by the citations.

We hope that explicit self-reflection and fine-grained attribution may help users verify factual errors in the model outputs.

@src https://arxiv.org/abs/2403.07974
@title LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code
@section Limitations

code generation scenario currently hosts over MATH instances from problems released between May and February.

To account for contamination in , we only perform evaluations on problems released after the model cutoff date.

This leads to only MATH problems used in our final evaluations which might add noise due to problem set samples.

We currently estimate MATH performance variations in code generation due to this issue (measured by bootstrapping MATH sized problem sets from the MATH sized dataset).

Other scenarios, i.e. self-repair, code execution, and test output prediction comprise MATH , MATH , and MATH problems would have similar performance variations.

We thus recommend exercising proper judgement when comparing models with small performance differences.

Note that has MATH problems and would also struggle with similar issues.

This issue is also exacerbated for newer models, with more recent cutoff dates, as they might only have access to a smaller evaluation set.

We propose two solutions addressing this issue as we evolve .

First, we will use other competition platforms for problem collection, allowing larger number of recent problems to be added to the benchmark.

In addition, we also hope supplement this with an unreleased private test set constructed specifically for model evaluation.

These problems will use a similar flavor to current problems and will be used when models are submitted for evaluation to the platform.

This would reduce the reliance on public accessible problems and provide a more robust evaluation of the models while providing community public access to similar problems, similar to strategies employed by popular platforms like Kaggle .

currently only focuses on which might not provide enough signal about model capabilities in other languages.

However, since we collected problem statements and serialized tests, adding new programming languages would be straightforward once appropriate evaluation engines are used.

Recent works have identified huge performance variances that can be caused due to insufficient prompt.

Here, we either do not tune prompts across models or make minor adjustments based on the system prompts and delimiter tokens.

This can lead to performance variance in our results.

Our findings and model comparison orders generalize across scenarios

and mostly match the performance trends observed on making this a less prominient issue.

This issue can be particularly observed open models on the code execution scenario with prompting.

Interestingly, often the open models perform even worse in comparsion to the direct code execution baseline.

Note that we used same prompts for the closed models all of which show noticable improvement from .

While the used prompts might be sub-optimal, this highlights how open-models perform worse against the closed models at performing chain-of-thought.

Programming is a vast domain and occurs in various forms such as programming puzzles, competition programming, and real-world software development.

Different domains might have individual requirements, constraints, challenges, and difficulty levels.

currently focuses on competition problems sourced from three platforms.

This might not be representative of the "most general" notion of programming capabilities.

Particularly, real-world usage of is drawn upon open-ended and unconstrained problems rasied by users.

We therefore recommend using as a starting point for evaluating and

further using domain-specific evaluations to measure and compare in specific settings as required.

@src https://arxiv.org/abs/2408.00714
@title SAM 2: Segment Anything in Images and Videos
@section Limitations

SAM 2 demonstrates strong performance in both static image and video domains, yet it encounters difficulties in certain scenarios. The model may fail to segment objects across shot changes and can lose track of or confuse objects in crowded scenes, after long occlusions or in extended videos. To alleviate this issue, we designed the ability to prompt SAM 2 in any frame: if the model loses the object or makes an error, refinement clicks on additional frames can quickly recover the correct prediction in most cases. SAM 2 also struggles with accurately tracking objects with very thin or fine details especially when they are fast-moving. Another challenging scenario occurs when there are nearby objects with similar appearance (e.g., multiple identical juggling balls). Incorporating more explicit motion modeling into SAM 2 could mitigate errors in such cases.

While SAM 2 can track multiple objects in a video simultaneously, SAM 2 processes each object separately, utilizing only shared per-frame embeddings without inter-object communication. While this approach is simple, incorporating shared object-level contextual information could aid in improving efficiency.

Our data engine relies on human annotators to verify masklet quality and select frames that require correction. Future developments could include automating this process to enhance efficiency.

@src https://arxiv.org/abs/2410.18072
@title WorldSimBench: Towards Video Generation Models as World Simulators
@section Design Features and Discussions

In this section, we discuss the Design features and corresponding observations we draw from our comprehensive evaluation experiments. More details can be found in the Supplementary Material.

Human Prefrence with Feedback. Given the complexity and diversity in the representation of physical rules in videos, even a specific dimension may manifest in various ways (for example, both illogical and discontinuous object motion fall under trajectory-related issues). This makes it challenging to evaluate using score-based models or a single fixed set of evaluation criteria. addresses this challenge effectively by employing a human preference scoring mechanism and a fine-grained feedback system.

Fig. illustrates the evaluation results of , more detail analyze could be found in Sup. .

In , most models struggle with Embodied Interaction, particularly in generating plausible object deformations, , block shattering, due to the complexity of physical rules.

In , the variation between models is minimal, with high-performing models excelling across all dimensions. The simpler instructions, like moving forward or turning, lead to high Instruction Alignment, but many generated videos suffer from poor 3D depth (Perspectivity) and fail to depict realistic embodied elements like pedestrians and vehicles, affecting the overall Aesthetic.

In , models perform uniformly well in static scene depiction, excelling in Perspectivity and Foreground/Background Consistency. However, they struggle with Instruction Alignment, often generating aimless actions. Despite this, the lack of unreasonable trajectories results in relatively high Trajectory scores, though robotic manipulation remains a significant challenge for current models.

Close-loop Interactive Evaluation. Given the dynamic nature and real-time requirements of interactive environments, evaluating World Simulators through static benchmarks often fails to capture the full spectrum of their capabilities. Close-loop Interactive Evaluation addresses this by enabling continuous feedback and adaptation, ensuring that the model's predictions and actions evolve in response to the changing environment, thus providing a more accurate and realistic assessment of its performance.

Fig. presents the evaluation results, showing significant variation in the performance of video generation models across different tasks. In the , video generation models conditioned on the first frame have a significantly lower success rate compared to those without image conditioning. This suggests that models with image conditioning struggle to generate physical laws and 3D scene representations accurately.

Tasks like travel, requiring high-quality trajectories and 3D representation, show the greatest variation in model performance, while simpler tasks like collecting wood see similar performance across models, indicating effective handling of minimal background variation. In the , models with better trajectory(Open-Sora-Plan) generation perform better.

In the , where background variation is minimal, models perform similarly on simple tasks, but as complexity increases, more robust models achieve higher success rates. Despite some success across scenarios, video generation models still need significant improvements in generating physically consistent content to be reliable for training agents or guiding actions.

Alignment of Physical Rules and Actions. Ensuring that World Simulators adhere to physical laws while generating predictions is crucial for practical application. The alignment of physical rules and actions is essential as it guarantees that the model's outputs are not only visually plausible but also executable in real-world scenarios. This approach allows for the seamless integration of predicted actions with their physical environment, ensuring reliability and effectiveness in real-world tasks.

Based on our experimental findings, we observe that most conclusions from the and evaluations are consistent. Specifically, the visual quality across most dimensions aligns with the results from the closed-loop experiments. , Dynamicrafter, which performs well in trajectory generation in , also excels in trajectory-focused scenarios like and . However, in other cases—such as the , which requires more frequent interactions, and long-sequence tasks (4, 5) in —Dynamicrafter underperforms compared to Open-Sora-Plan. This differs from the results, likely because these tasks demand stable, high-quality video generation for guidance, where Open-Sora-Plan shows higher robustness. Therefore, a comprehensive evaluation of video generation models requires a combination of and assessments to provide the most fair and accurate judgment.

Finally, based on the overall and results, we conclude that current video generation models still fail to effectively capture many physical rules, indicating significant improvements are needed before they can function as true World Simulators.

@src https://arxiv.org/abs/2410.18072
@title WorldSimBench: Towards Video Generation Models as World Simulators
@section - In this section, we provide additional details about - that are not covered in the main paper due to space limitations.

Minecraft has emerged as a popular open-world environment for developing generalist embodied agents due to its diverse tasks (e.g., survival, harvesting, crafting, combat, and creative tasks), varied environments, and interactive mobs, all of which require generalized agent capabilities.

Previous works have primarily focused on exploring the capabilities of LLMs or MLLMs as at the MATH stage.

However, no prior research has conducted closed-loop evaluations of World Simulators at the MATH stage within Minecraft.

To address this gap, we leverage the Steve-1 pipeline to assess the performance of Video Generation Models as World Simulators in .

@src https://arxiv.org/abs/2412.08821
@title Large Concept Models: Language Modeling in a Sentence Representation Space
@section Limitations

In this section we discuss the possible limitations of the presented Large Concept Modeling approach.

The choice and design of the embedding space plays a crucial role in the modeling approach.

The embedding space was chosen for its good multilingual and multimodal representations, as well as the availability of a massively multilingual decoder, which achieves excellent results in both translation and auto-encoding. However, the model was trained on very specific training data, namely bitext machine translation data containing rather short sentences. This has several consequences:

is trained to sustain a local geometry (sentences with very similar meanings are geometrically close) with no special guarantees for sentences that are only loosely related.

Yet, predicting next sentences distribution requires the space to operate well globally.

auto-encodes surprisingly well texts containing links, references, or merely numbers or code data.

Yet, such texts tend to be fragile, highlighting a distribution mismatch between the training data and commonly used pre-training text corpora.

Therefore, the accurate prediction of the sentences containing such a content (non-negligible in pre-training data) will be hard for any based model. For instance, the factuality of fragile generated sentences may easily be compromised.

Using a frozen encoder represents some interesting trade-offs.

Any frozen encoder which is learned in a different data context, and with no a-priori strong connection to modeling, may be suboptimal compared to encoders that are learned in an end-to-end fashion (with the loss coming from the decoder).

At the same time, learning an encoder within end-to-end training can be challenging and the resulting space is not guaranteed to result in good semantic representations shared across languages and modalities.

Training the concept representation and the end-to-end would also be less data and compute efficient since all modeling data should be multilingual and -modal, bearing the risk of modality competition.

In this work, the definition of concepts is interpreted at sentence level. However, the manifold of possible next sentences is very wide, attributing a proper probability to each of such sentences is much harder (even with a modeling within the latent space) that to the discrete set of tokens.

In NLP, we encounter sentences of variable length. Combinatorial complexity of possible next sentences grows exponentially with the maximum character length.

The choice of granularity for is not trivial as long sentences (>120 characters) could reasonably be considered as several concepts.

However, any finer splitting of such sentences does not necessary separate well these concepts. This shows the limitation of a fixed size embedding representation for one sentence. Text splitting (such as sentence splitting) or one-to-many mapping of a sentence into several embeddings is a major future direction of research.

Each document in a training corpus typically contains a sequence of unique sentences or a little number of repetitions. This data sparsity effect manifests as well at large corpora level: the large majority of sentences are merely unique. In principle, this issue can be addressed with higher-level semantic embedding representations. These higher-level representations come with trade-off between requirement of lossless data encoding (think of named-entities or numbers, critical in many language modeling tasks) and good level of abstraction to enable reasoning capabilities. Compared to a monolingual auto-encoder which would simply compress input sentences, offers semantic representations with good auto-encoding quality but still certainly sacrificing generalization capacities.

This generalization issue can be partially mitigated by splitting or encoding input text as new conceptual units which are more commonly shared across source documents. This is in the spirit of stemming or lemmatization techniques studied in NLP for words.

That being said, building such conceptual units that are also language and modality agnostic is a challenging task. Such shared multilingual and multimodal conceptual units are also key for generalization across languages and across modalities. To maximize cross-lingual and cross-modal transfers, should be exposed to a richer variety of multilingual and multi-modal data.

Diffusion modeling has proven to be very efficient in generative modeling of continuous data like images or speech. As previously stated, sentences in the space, despite being represented as continuous vectors, remain discrete combinatorial objects. This makes diffusion modeling struggle on the text modality (either at word or sentence embedding level).

The contrastive nature of cross-entropy loss based on softmax outputs which is used for next token prediction plays a critical role for many downstream task where higher accuracy is required (e.g. MCQ tasks, code or math generation).

On the opposite, continuous diffusion modeling does not allow to integrate such a contrastive objective.

The could be a way to address the discrete nature of text while modeling on coarse-to-fine semantic units shared across languages and modalities. The limited performance of the approaches presented in this paper may be explained by the fact that space was not trained to be efficiently quantizable, yielding a significant number of codebooks and a large amount of units per codebook. Therefore, the current quantization suffers from the exponentially increasing number of RVQ units combinations which does not solve the data sparsity/uniqueness issue discussed earlier.

This indicates once again the importance of developing a new representation space, either continuous or discrete, for the .

@src https://arxiv.org/abs/2412.13663
@title Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference
@section Downstream Results and Discussion

Aggregated results for all evaluations are presented in Table . For BEIR and GLUE, the two common evaluation suites, we follow existing practice in reporting the average results. Detailed results are provided in Appendix .

In terms of downstream performance, ModernBERT is the strongest overall model at both the base and large model sizes. ModernBERT represents a Pareto improvement on all tasks over the original BERT and RoBERTA models, with better performance on every evaluation category.

Short-Context Retrieval On BEIR, both variants of ModernBERT outperform existing encoders in both the DPR and ColBERT settings, including the recent GTE-en-MLM and NomicBERT models designed to serve as better backbones for retrieval .

While ModernBERT-base only narrowly edges out GTE-en-MLM-base on DPR evaluations, ModernBERT-large increases its lead despite having comparatively fewer parameters at 395M to GTE-en-MLM-large's 435M.

Long-Context Retrieval - Single Vector In the DPR setting, ModernBERT achieves impressive performance on MLDR, a long-context text retrieval task. However, these results also highlight an interesting phenomenon: without long-context finetuning ModernBERT outperforms both shorter-context models and the long-context NomicBERT but performs noticeably worse than GTE-en-MLM. The performance gap narrows considerably when evaluated in-domain, with both models performing similarly. This suggests that ModernBERT can effectively process long context sequences as a dense encoder but may require more adapted tuning. We plan to explore multiple potential explanations for this phenomenon in future work, including the impact of local attention or GTE-en-MLM having spent a larger part of its pretraining compute budget on longer sequence lengths .

Long-Context Retrieval - Multi-Vector In the ColBERT setting, long-context models (GTE-en-MLM, NomicBERT, and ModernBERT) all outperform short-context models by at least 40 NDCG@10 points without requiring any specific finetuning. These results confirm the findings of , who showed that ColBERT models are particularly well-suited to long-context retrieval tasks. Among the long-context models, ModernBERT outperforms other long-context models, with at least a 9 NDCG@10 point lead on both model sizes. We theorize that these sizable gains could be explained by our long pretraining ensuring few, if any, tokens are under-trained, as well as a potentially synergistic effect of local attention with ColBERT-style retrieval, but leave further exploration of this phenomenon to future work.

Natural Language Understanding Both ModernBERT models demonstrate exceptional NLU results, as measured by GLUE. ModernBERT-base surpasses all existing base models, including DeBERTaV3-base, becoming the first MLM-trained model to do so. This is surprising, as DeBERTaV3 was trained with the Replaced-Token-Detection objective, which was previously thought to yield stronger downstream NLU performance . ModernBERT-large is the second-best large encoder on GLUE, almost matching DeBERTaV3-large with one-tenth fewer parameters while processing tokens in half the time (see Section ).

Code On programming tasks, in both code-to-text (CodeSearchNet) and longer-context hybrid settings (StackQA), ModernBERT outperforms all other models. This result was expected, as it is the only evaluated encoder to be trained on a data mixture including programming data. These results, combined with ModernBERT's strong showings on other tasks, indicates that ModernBERT has improved understanding of code at no detriment to its ability to process natural text.

@src https://arxiv.org/abs/2412.13663
@title Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference
@section Limitations

Language This study focuses exclusively on the English language, and trains on a very large number of tokens. As such, a major limitation of our work is that it is not directly applicable to other languages, and potentially even less-so to lower resources languages.

Biases Our model is trained largely on web data, as a result, all of its representations are subject to the biases present in such data.

Harmful Content Generation The MLM objective gives the model some ability to generate text by suggesting a given token to replace the [MASK] token , which could result in the generation of harmful content. However, ModernBERT is not, primarily, a generative model, and as such, has not been trained to and therefore cannot generate longer sequences of text. As a result, it is considerably less likely to be at risk of generating harmful content of any kind.

Given the strong results of DeBERTav3 on classification tasks but weak ones on retrieval, it seems that a training leveraging both MLM and RTD might be better suited to achieve best results on classification. Extending our work to RTD is thus a promising line of research.

Besides the architectural modifications, a key aspect of our studies is data scaling. However, other scaling axes, notably in terms of model parameters are left unexplored.
