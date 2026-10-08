# related-work corpus (49 sources)

@src https://arxiv.org/abs/1706.03762
@title Attention Is All You Need
@section Background

The goal of reducing sequential computation also forms the foundation of the Extended Neural GPU , ByteNet and ConvS2S , all of which use convolutional neural networks as basic building block, computing hidden representations in parallel for all input and output positions. In these models, the number of operations required to relate signals from two arbitrary input or output positions grows in the distance between positions, linearly for ConvS2S and logarithmically for ByteNet. This makes it more difficult to learn dependencies between distant positions . In the Transformer this is reduced to a constant number of operations, albeit at the cost of reduced effective resolution due to averaging attention-weighted positions, an effect we counteract with Multi-Head Attention as described in section .

Self-attention, sometimes called intra-attention is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence. Self-attention has been used successfully in a variety of tasks including reading comprehension, abstractive summarization, textual entailment and learning task-independent sentence representations .

End-to-end memory networks are based on a recurrent attention mechanism instead of sequence-aligned recurrence and have been shown to perform well on simple-language question answering and language modeling tasks .

To the best of our knowledge, however, the Transformer is the first transduction model relying entirely on self-attention to compute representations of its input and output without using sequence-aligned RNNs or convolution.

In the following sections, we will describe the Transformer, motivate self-attention and discuss its advantages over models such as and .

@src https://arxiv.org/abs/1804.07461
@title GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding
@section Related Work

used a multi-task model with a shared sentence understanding component to jointly learn POS tagging, chunking, named entity recognition, and semantic role labeling.

More recent work has explored using labels from core NLP tasks to supervise training of lower levels of deep neural networks and

automatically learning cross-task sharing mechanisms for multi-task learning .

Beyond multi-task learning, much work in developing general NLU systems has focused on sentence-to-vector encoders , leveraging unlabeled data

, labeled data , and combinations of these .

In this line of work, a standard evaluation practice has emerged, recently codified as SentEval .

Like GLUE, SentEval relies on a set of existing classification tasks involving either one or two sentences as inputs. Unlike GLUE, SentEval only evaluates sentence-to-vector encoders, making it well-suited for evaluating models on tasks involving sentences in isolation.

However, cross-sentence contextualization and alignment are instrumental in achieving state-of-the-art performance on tasks such as machine translation , question answering , and natural language inference .

GLUE is designed to facilitate the development of these methods: It is model-agnostic, allowing for any kind of representation or contextualization, including models that use no explicit vector or symbolic representations for sentences whatsoever.

GLUE also diverges from SentEval in the selection of evaluation tasks that are included in the suite. Many of the SentEval tasks are closely related to sentiment analysis, such as MR , SST , CR , and SUBJ . Other tasks are so close to being solved that evaluation on them is relatively uninformative, such as MPQA and TREC question classification . In GLUE, we attempt to construct a benchmark that is both diverse and difficult.

introduce decaNLP, which also scores NLP systems based on their performance on multiple datasets. Their benchmark recasts the ten evaluation tasks as question answering, converting tasks like summarization and text-to-SQL semantic parsing into question answering using automatic transformations. That benchmark lacks the leaderboard and error analysis toolkit of GLUE, but more importantly, we see it as pursuing a more ambitious but less immediately practical goal: While GLUE rewards methods that yield good performance on a circumscribed set of tasks using methods like those that are currently used for those tasks, their benchmark rewards systems that make progress toward their goal of unifying all of NLU under the rubric of question answering.

@src https://arxiv.org/abs/1906.08237
@title XLNet: Generalized Autoregressive Pretraining for Language Understanding
@section Background

In this section, we first review and compare the conventional AR language modeling and BERT for language pretraining.

Given a text sequence MATH , AR language modeling performs pretraining by maximizing the likelihood under the forward autoregressive factorization:

where MATH is a context representation produced by neural models, such as RNNs or Transformers, and MATH denotes the embedding of MATH .

In comparison, BERT is based on denoising auto-encoding.

Specifically, for a text sequence MATH , BERT first constructs a corrupted version MATH by randomly setting a portion (e.g. 15%) of tokens in MATH to a special symbol .

Let the masked tokens be MATH . The training objective is to reconstruct MATH from MATH :

where MATH indicates MATH is masked, and MATH is a Transformer that maps a length- MATH text sequence MATH into a sequence of hidden vectors MATH .

The pros and cons of the two pretraining objectives are compared in the following aspects:

itemize [leftmargin=*,topsep=0em,itemsep=0em]

As emphasized by the MATH sign in Eq. ( ), BERT factorizes the joint conditional probability MATH based on an independence assumption that all masked tokens MATH are separately reconstructed.

In comparison, the AR language modeling objective factorizes MATH using the product rule that holds universally without such an independence assumption.

The input to BERT contains artificial symbols like that never occur in downstream tasks, which creates a pretrain-finetune discrepancy.

Replacing with original tokens as in does not solve the problem

because original tokens can be only used with a small probability — otherwise Eq. ( ) will be trivial to optimize.

In comparison, AR language modeling does not rely on any input corruption and does not suffer from this issue.

Context dependency: The AR representation MATH is only conditioned on the tokens up to position MATH (i.e. tokens to the left), while the BERT representation MATH has access to the contextual information on both sides.

As a result, the BERT objective allows the model to be pretrained to better capture bidirectional context.

@src https://arxiv.org/abs/1907.11692
@title RoBERTa: A Robustly Optimized BERT Pretraining Approach
@section Related Work

Pretraining methods have been designed with different training objectives, including language modeling , machine translation , and masked language modeling . Many recent papers have used a basic recipe of finetuning models for each end task , and pretraining with some variant of a masked language model objective. However, newer methods have improved performance by multi-task fine tuning , incorporating entity embeddings , span prediction , and multiple variants of autoregressive pretraining . Performance is also typically improved by training bigger models on more data . Our goal was to replicate, simplify, and better tune the training of BERT, as a reference point for better understanding the relative performance of all of these methods.

@src https://arxiv.org/abs/1910.13461
@title BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension
@section Related Work

Early methods for pretraining were based on language models. GPT only models leftward context, which is problematic for some tasks. ELMo concatenates left-only and right-only representations, but does not pre-train interactions between these features.

demonstrated that very large language models can act as unsupervised multitask models.

BERT introduced masked language modelling, which allows pre-training to learn interactions between left and right context words.

Recent work has shown that very strong performance can be achieved by training for longer , by tying parameters across layers , and by masking spans instead of words .

Predictions are not made auto-regressively, reducing the effectiveness of BERT for generation tasks.

UniLM fine-tunes BERT with an ensemble of masks, some of which allow only leftward context. Like BART, this allows UniLM to be used for both generative and discriminative tasks. A difference is that UniLM predictions are conditionally independent, whereas BART's are autoregressive. BART reduces the mismatch between pre-training and generation tasks, because the decoder is always trained on uncorrupted context.

MASS is perhaps the most similar model to BART. An input sequence where a contiguous span of tokens is masked is mapped to a sequence consisting of the missing tokens. MASS is less effective for discriminative tasks, because disjoint sets of tokens are fed into the encoder and decoder.

XL-Net extends BERT by predicting masked tokens auto-regressively in a permuted order. This objective allows predictions to condition on both left and right context. In contrast, the BART decoder works left-to-right during pre-training, matching the setting during generation.

Several papers have explored using pre-trained representations to improve machine translation. The largest improvements have come from pre-training on both source and target languages , but this requires pre-training on all languages of interest. Other work has shown that encoders can be improved using pre-trained representations , but gains in decoders are more limited. We show how BART can be used to improve machine translation decoders.

@src https://arxiv.org/abs/2003.10555
@title ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators
@section Related Work

Self-supervised learning has been used to learn word representations and more recently contextual representations of words though objectives such as language modeling .

BERT pre-trains a large Transformer at the masked-language modeling

There have been numerous extensions to BERT.

For example, MASS and UniLM extend BERT to generation tasks by adding auto-regressive generative training objectives.

ERNIE and SpanBERT mask out contiguous sequences of token for improved span representations.

This idea may be complementary to ELECTRA; we think it would be interesting to make ELECTRA's generator auto-regressive and add a "replaced span detection" task.

Instead of masking out input tokens, XLNet masks attention weights such that the input sequence is auto-regressively generated in a random order. However, this method suffers from the same inefficiencies as BERT because XLNet only generates 15% of the input tokens in this way.

Like ELECTRA, XLNet may alleviate BERT's pretrain-finetune discrepancy by not requiring MATH tokens, although this isn't entirely clear because XLNet uses two "streams" of attention during pre-training but only one for fine-tuning.

Recently, models such as TinyBERT and MobileBERT show that BERT can effectively be distilled down to a smaller model.

In contrast, we focus more on pre-training speed rather than inference speed, so we train ELECTRA-Small from scratch.

Generative Adversarial Networks GANs are effective at generating high-quality synthetic data.

propose using the discriminator of a GAN in downstream tasks, which is similar to our method.

GANs have been applied to text data , although state-of-the-art approaches still lag behind standard maximum-likelihood training .

Although we do not use adversarial learning, our generator is particularly reminiscent of MaskGAN , which trains the generator to fill in tokens deleted from the input.

Broadly, contrastive learning methods distinguish observed data points from fictitious negative samples.

They have been applied to many modalities including text , images , and video data.

Common approaches learn embedding spaces where related data points are similar or models that rank real data points over negative samples .

ELECTRA is particularly related to Noise-Contrastive Estimation (NCE) , which also trains a binary classifier to distinguish real and fake data points.

Word2Vec , one of the earliest pre-training methods for NLP, uses contrastive learning.

In fact, ELECTRA can be viewed as a massively scaled-up version of Continuous Bag-of-Words (CBOW) with Negative Sampling.

CBOW also predicts an input token given surrounding context and negative sampling rephrases the learning task as a binary classification task on whether the input token comes from the data or proposal distribution.

However, CBOW uses a bag-of-vectors encoder rather than a transformer and a simple proposal distribution derived from unigram token frequencies instead of a learned generator.

@src https://arxiv.org/abs/2005.11401
@title Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
@section Related Work

Prior work has shown that retrieval improves performance across a variety of NLP tasks when considered in isolation.

Such tasks include open-domain question answering , fact checking , fact completion , long-form question answering , Wikipedia article generation , dialogue , translation , and language modeling .

Our work unifies previous successes in incorporating retrieval into individual tasks, showing that a single retrieval-based architecture is capable of achieving strong performance across several tasks.

Prior work on general-purpose architectures for NLP tasks has shown great success without the use of retrieval.

A single, pre-trained language model has been shown to achieve strong performance on various classification tasks in the GLUE benchmarks after fine-tuning .

GPT-2 later showed that a single, left-to-right, pre-trained language model could achieve strong performance across both discriminative and generative tasks.

For further improvement, BART and T5 propose a single, pre-trained encoder-decoder model that leverages bi-directional attention to achieve stronger performance on discriminative and generative tasks.

Our work aims to expand the space of possible tasks with a single, unified architecture, by learning a retrieval module to augment pre-trained, generative language models.

There is significant work on learning to retrieve documents in information retrieval, more recently with pre-trained, neural language models similar to ours.

Some work optimizes the retrieval module to aid in a specific, downstream task such as question answering, using search , reinforcement learning , or a latent variable approach as in our work.

These successes leverage different retrieval-based architectures and optimization techniques to achieve strong performance on a single task, while we show that a single retrieval-based architecture can be fine-tuned for strong performance on a variety of tasks.

Our document index can be seen as a large external memory for neural networks to attend to, analogous to memory networks .

Concurrent work learns to retrieve a trained embedding for each entity in the input, rather than to retrieve raw text as in our work.

Other work improves the ability of dialog models to generate factual text by attending over fact embeddings . A key feature of our memory is that it is comprised of raw text rather distributed representations, which makes the memory both (i) human-readable, lending a form of interpretability to our model, and (ii) human-writable, enabling us to dynamically update the model's memory by editing the document index. This approach has also been used in knowledge-intensive dialog, where generators have been conditioned on retrieved text directly, albeit obtained via TF-IDF rather than end-to-end learnt retrieval .

Retrieve-and-Edit approaches Our method shares some similarities with retrieve-and-edit style approaches, where a similar training input-output pair is retrieved for a given input, and then edited to provide a final output. These approaches have proved successful in a number of domains including Machine Translation and Semantic Parsing . Our approach does have several differences, including less of emphasis on lightly editing a retrieved item, but on aggregating content from several pieces of retrieved content, as well as learning latent retrieval, and retrieving evidence documents rather than related training pairs. This said, RAG techniques may work well in these settings, and could represent promising future work.

@src https://arxiv.org/abs/2005.14165
@title Language Models are Few-Shot Learners
@section Related Work

Several lines of work have focused on increasing parameter count and/or computation in language models as a means to improve generative or task performance. An early work scaled LSTM based language models to over a billion parameters . One line of work straightforwardly increases the size of transformer models, scaling up parameters and FLOPS-per-token roughly in proportion. Work in this vein has successively increased model size: 213 million parameters in the original paper, 300 million parameters , 1.5 billion parameters , 8 billion parameters , 11 billion parameters , and most recently 17 billion parameters . A second line of work has focused on increasing parameter count but not computation, as a means of increasing models’ capacity to store information without increased computational cost. These approaches rely on the conditional computation framework and specifically, the mixture-of-experts method has been used to produce 100 billion parameter models and more recently 50 billion parameter translation models , though only a small fraction of the parameters are actually used on each forward pass. A third approach increases computation without increasing parameters; examples of this approach include adaptive computation time and the universal transformer . Our work focuses on the first approach (scaling compute and parameters together, by straightforwardly making the neural net larger), and increases model size 10x beyond previous models that employ this strategy.

Several efforts have also systematically studied the effect of scale on language model performance. , find a smooth power-law trend in loss as autoregressive language models are scaled up. This work suggests that this trend largely continues as models continue to scale up (although a slight bending of the curve can perhaps be detected in Figure ), and we also find relatively smooth increases in many (though not all) downstream tasks across 3 orders of magnitude of scaling.

Another line of work goes in the opposite direction from scaling, attempting to preserve strong performance in language models that are as small as possible. This approach includes ALBERT as well as general and task-specific approaches to distillation of language models. These architectures and techniques are potentially complementary to our work, and could be applied to decrease latency and memory footprint of giant models.

As fine-tuned language models have neared human performance on many standard benchmark tasks, considerable effort has been devoted to constructing more difficult or open-ended tasks, including question answering , reading comprehension , and adversarially constructed datasets designed to be difficult for existing language models . In this work we test our models on many of these datasets.

Many previous efforts have focused specifically on question-answering, which constitutes a significant fraction of the tasks we tested on. Recent efforts include , which fine-tuned an 11 billion parameter language model, and , which focused on attending over a large corpus of data at test time. Our work differs in focusing on in-context learning but could be combined in the future with those of .

Metalearning in language models has been utilized in , though with much more limited results and no systematic study. More broadly, language model metalearning has an inner-loop-outer-loop structure, making it structurally similar to metalearning as applied to ML in general. Here there is an extensive literature, including matching networks , RL2 , learning to optimize and MAML . Our approach of stuffing the model’s context with previous examples is most structurally similar to RL2 and also resembles , in that an inner loop of adaptation takes place through computation in the model’s activations across timesteps, without updating the weights, while an outer loop (in this case just language model pre-training) updates the weights, and implicitly learns the ability to adapt to or at least recognize tasks defined at inference-time. Few-shot auto-regressive density estimation was explored in and studied low-resource NMT as a few-shot learning problem.

While the mechanism of our few-shot approach is different, prior work has also explored ways of using pre-trained language models in combination with gradient descent to perform few-shot learning . Another sub-field with similar goals is semi-supervised learning where approaches such as UDA also explore methods of fine-tuning when very little labeled data is available.

Giving multi-task models instructions in natural language was first formalized in a supervised setting with and utilized for some tasks (such as summarizing) in a language model with . The notion of presenting tasks in natural language was also explored in the text-to-text transformer , although there it was applied for multi-task fine-tuning rather than for in-context learning without weight updates.

Another approach to increasing generality and transfer-learning capability in language models is multi-task learning , which fine-tunes on a mixture of downstream tasks together, rather than separately updating the weights for each one. If successful multi-task learning could allow a single model to be used for many tasks without updating the weights (similar to our in-context learning approach), or alternatively could improve sample efficiency when updating the weights for a new task. Multi-task learning has shown some promising initial results and multi-stage fine-tuning has recently become a standardized part of SOTA results on some datasets and pushed the boundaries on certain tasks , but is still limited by the need to manually curate collections of datasets and set up training curricula. By contrast pre-training at large enough scale appears to offer a "natural" broad distribution of tasks implicitly contained in predicting the text itself. One direction for future work might be attempting to generate a broader set of explicit tasks for multi-task learning, for example through procedural generation , human interaction , or active learning .

Algorithmic innovation in language models over the last two years has been enormous, including denoising-based bidirectionality , prefixLM and encoder-decoder architectures , random permutations during training , architectures that improve the efficiency of sampling , improvements in data and training procedures , and efficiency increases in the embedding parameters . Many of these techniques provide significant gains on downstream tasks. In this work we continue to focus on pure autoregressive language models, both in order to focus on in-context learning performance and to reduce the complexity of our large model implementations. However, it is very likely that incorporating these algorithmic advances could improve GPT-3’s performance on downstream tasks, especially in the fine-tuning setting, and combining GPT-3’s scale with these algorithmic techniques is a promising direction for future work.

@src https://arxiv.org/abs/2006.11239
@title Denoising Diffusion Probabilistic Models
@section Background

Diffusion models are latent variable models of the form MATH , where MATH are latents of the same dimensionality as the data MATH . The joint distribution MATH is called the reverse process, and it is defined as a Markov chain with learned Gaussian transitions starting at MATH :

What distinguishes diffusion models from other types of latent variable models is that the approximate posterior MATH , called the forward process or diffusion process, is fixed to a Markov chain that gradually adds Gaussian noise to the data according to a variance schedule MATH :

Training is performed by optimizing the usual variational bound on negative log likelihood:

The forward process variances MATH can be learned by reparameterization or held constant as hyperparameters, and

expressiveness of the reverse process is ensured in part by the choice of Gaussian conditionals in MATH , because both processes have the same functional form when MATH are small .

A notable property of the forward process is that it admits sampling MATH at an arbitrary timestep MATH in closed form: using the notation MATH and MATH , we have

Efficient training is therefore possible by optimizing random terms of MATH with stochastic gradient descent.

Further improvements come from variance reduction by rewriting MATH eq:vb_original as:

(See sec:extended_derivations for details. The labels on the terms are used in sec:main .) eq:vb uses KL divergence to directly compare MATH against forward process posteriors, which are tractable when conditioned on MATH :

Consequently, all KL divergences in eq:vb are comparisons between Gaussians, so they can be calculated in a Rao-Blackwellized fashion with closed form expressions instead of high variance Monte Carlo estimates.

@src https://arxiv.org/abs/2006.11239
@title Denoising Diffusion Probabilistic Models
@section Related Work

While diffusion models might resemble flows and VAEs , diffusion models are designed so that MATH has no parameters and the top-level latent MATH has nearly zero mutual information with the data MATH .

Our MATH -prediction reverse process parameterization establishes a connection between diffusion models and denoising score matching over multiple noise levels with annealed Langevin dynamics for sampling . Diffusion models, however, admit straightforward log likelihood evaluation, and the training procedure explicitly trains the Langevin dynamics sampler using variational inference (see sec:extended_related_work for details).

The connection also has the reverse implication that a certain weighted form of denoising score matching is the same as variational inference to train a Langevin-like sampler. Other methods for learning transition operators of Markov chains include infusion training , variational walkback , generative stochastic networks , and others .

By the known connection between score matching and energy-based modeling, our work could have implications for other recent work on energy-based models . Our rate-distortion curves are computed over time in one evaluation of the variational bound, reminiscent of how rate-distortion curves can be computed over distortion penalties in one run of annealed importance sampling . Our progressive decoding argument can be seen in convolutional DRAW and related models and may also lead to more general designs for subscale orderings or sampling strategies for autoregressive models .

@src https://arxiv.org/abs/2009.03300
@title Measuring Massive Multitask Language Understanding
@section Related Work

The dominant paradigm in NLP is to pretrain large models on massive text corpora including educational books and websites. In the process, these models are exposed to information about a wide range of topics.

found that recent models learn enough information from pretraining that they can serve as knowledge bases.

However, no prior work has comprehensively measured the knowledge models have across many real-world domains.

Until recently, researchers primarily used fine-tuned models on downstream tasks . However, larger pretrained models like GPT-3 have made it possible to achieve competitive performance without fine-tuning by using few-shot learning, which removes the need for a large fine-tuning set. With the advent of strong zero-shot and few-shot learning, it is now possible to curate a diverse set of tasks for evaluation and remove the possibility of models on "spurious cues" in a dataset to achieve high performance.

Many recent benchmarks aim to assess a model's general world knowledge and basic reasoning ability by testing its "commonsense." A number of commonsense benchmarks have been proposed in the past year, but recent models are already nearing human-level performance on several of these, including HellaSwag , Physical IQA , and CosmosQA . By design, these datasets assess abilities that almost every child has. In contrast, we include harder specialized subjects that people must study to learn.

Some researchers have suggested that the future of NLP evaluation should focus on Natural Language Generation (NLG) , an idea that reaches back to the Turing Test . However, NLG is notoriously difficult to evaluate and lacks a standard metric . Consequently, we instead create a simple-to-evaluate test that measures classification accuracy on multiple choice questions.

While several question answering benchmarks exist, they are comparatively limited in scope. Most either cover easy topics like grade school subjects for which models can already achieve strong performance , or are focused on linguistic understanding in the form of reading comprehension . In contrast, we include a wide range of difficult subjects that go far beyond linguistic understanding.

@src https://arxiv.org/abs/2010.02502
@title Denoising Diffusion Implicit Models
@section Background

Given samples from a data distribution MATH , we are interested in learning a model distribution MATH that approximates MATH and is easy to sample from.

Denoising diffusion probabilistic models (DDPMs, ) are latent variable models of the form

where MATH are latent variables in the same sample space as MATH (denoted as MATH ). The parameters MATH are learned to fit the data distribution MATH by maximizing a variational lower bound:

where MATH is some inference distribution over the latent variables.

Unlike typical latent variable models (such as the variational autoencoder ), DDPMs are learned with a fixed (rather than trainable) inference procedure MATH ,

and latent variables are relatively high dimensional.

For example, considered the following Markov chain with Gaussian transitions

where the covariance matrix is ensured to have positive terms on its diagonal.

This is called the forward process due to the autoregressive nature of the sampling procedure (from MATH to MATH ). We call the latent variable model MATH , which is a Markov chain that samples from MATH to MATH , the generative process, since it approximates the intractable reverse process MATH . Intuitively, the forward process progressively adds noise to the observation MATH , whereas the generative process progressively denoises a noisy observation ( fig:diffusion , left).

A special property of the forward process is that

so we can express MATH as a linear combination of MATH and a noise variable MATH :

When we set MATH sufficiently close to MATH , MATH converges to a standard Gaussian for all MATH , so it is natural to set MATH .

are modeled as Gaussians with trainable mean functions and fixed variances, the objective in can be simplified to (Please refer to Appendix for details. :

where MATH is a set of MATH functions, each MATH (indexed by MATH ) is a function with trainable parameters MATH , and MATH is a vector of positive coefficients in the objective that depends on MATH .

In , the objective with MATH is optimized instead to maximize generation performance of the trained model; this is also the same objective used in noise conditional score networks based on score matching .

From a trained model, MATH is sampled by first sampling MATH from the prior MATH , and then sampling MATH from the generative processes iteratively.

The length MATH of the forward process is an important hyperparameter in DDPMs.

From a variational perspective, a large MATH allows the reverse process to be close to a Gaussian , so that the generative process modeled with Gaussian conditional distributions becomes a good approximation; this motivates the choice of large MATH values, such as MATH in .

However, as all MATH iterations have to be performed sequentially, instead of in parallel, to obtain a sample MATH , sampling from DDPMs is much slower than sampling from other deep generative models, which makes them impractical for tasks where compute is limited and latency is critical.

@src https://arxiv.org/abs/2010.02502
@title Denoising Diffusion Implicit Models
@section Related Work

Our work is based on a large family of existing methods on learning generative models as transition operators of Markov chains . Among them, denoising diffusion probabilistic models (DDPMs, ) and noise conditional score networks (NCSN, ) have recently achieved high sample quality comparable to GANs . DDPMs optimize a variational lower bound to the log-likelihood, whereas NCSNs optimize the score matching objective over a nonparametric Parzen density estimator of the data .

Despite their different motivations, DDPMs and NCSNs are closely related. Both use a denoising autoencoder objective for many noise levels, and both use a procedure similar to Langevin dynamics to produce samples . Since Langevin dynamics is a discretization of a gradient flow ,

both DDPM and NCSN require many steps to achieve good sample quality.

This aligns with the observation that DDPM and existing NCSN methods have trouble generating high-quality samples in a few iterations.

DDIM, on the other hand, is an implicit generative model where samples are uniquely determined from the latent variables. Hence, DDIM has certain properties that resemble GANs and invertible flows , such as the ability to produce semantically meaningful interpolations. We derive DDIM from a purely variational perspective, where the restrictions of Langevin dynamics are not relevant; this could partially explain why we are able to observe superior sample quality compared to DDPM under fewer iterations.

The sampling procedure of DDIM is also reminiscent of neural networks with continuous depth , since the samples it produces from the same latent variable have similar high-level visual features, regardless of the specific sample trajectory.

@src https://arxiv.org/abs/2010.11929
@title An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale
@section Related Work

Transformers were proposed by for machine translation, and have since become the state of the art method in many NLP tasks. Large Transformer-based models are often pre-trained on large corpora and then fine-tuned for the task at hand: BERT uses a denoising self-supervised pre-training task, while the GPT line of work uses language modeling as its pre-training task .

Naive application of self-attention to images would require that each pixel attends to every other pixel. With quadratic cost in the number of pixels, this does not scale to realistic input sizes.

Thus, to apply Transformers in the context of image processing, several approximations have been tried in the past.

applied the self-attention only in local neighborhoods for each query pixel instead of globally.

Such local multi-head dot-product self attention blocks can completely replace convolutions .

In a different line of work, Sparse Transformers employ scalable approximations to global self-attention in order to be applicable to images.

An alternative way to scale attention is to apply it in blocks of varying sizes , in the extreme case only along individual axes .

Many of these specialized attention architectures demonstrate promising results on computer vision tasks, but require complex engineering to be implemented efficiently on hardware accelerators.

Most related to ours is the model of , which extracts patches of size MATH from the input image and applies full self-attention on top. This model is very similar to ViT, but our work goes further to demonstrate that large scale pre-training makes vanilla transformers competitive with (or even better than) state-of-the-art CNNs. Moreover, use a small patch size of MATH pixels, which makes the model applicable only to small-resolution images, while we handle medium-resolution images as well.

There has also been a lot of interest in combining convolutional neural networks (CNNs) with forms of self-attention, e.g. by augmenting feature maps for image classification or by further processing the output of a CNN using self-attention, e.g. for object detection , video processing , image classification , unsupervised object discovery , or unified text-vision tasks .

Another recent related model is image GPT (iGPT) , which applies Transformers to image pixels after reducing image resolution and color space. The model is trained in an unsupervised fashion as a generative model, and the resulting representation can then be fine-tuned or probed linearly for classification performance, achieving a maximal accuracy of 72% on .

Our work adds to the increasing collection of papers that explore image recognition at larger scales than the standard dataset.

The use of additional data sources allows to achieve state-of-the-art results on standard benchmarks .

Moreover, study how CNN performance scales with dataset size, and perform an empirical exploration of CNN transfer learning from large scale datasets such as ImageNet-21k and JFT-300M.

We focus on these two latter datasets as well, but train Transformers instead of ResNet-based models used in prior works.

@src https://arxiv.org/abs/2101.03961
@title Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity
@section Related Work

The importance of scale in neural networks is widely recognized and several approaches have been proposed.

Recent works have scaled models to billions of parameters through using model parallelism (e.g. splitting weights and tensors across multiple cores) .

Alternatively, propose using pipeline based model parallelism, where different layers are split across devices and micro-batches are pipelined to the different layers.

Finally, Product Key networks were proposed to scale up the capacity of neural networks by doing a lookup for learnable embeddings based on the incoming token representations to a given layer.

Our work studies a specific model in a class of methods that do conditional computation, where computation decisions are made dynamically based on the input.

proposed adaptively selecting weights based on certain bit patterns occuring in the model hidden-states.

built stacked expert layers with dense matrix multiplications and ReLU activations and showed promising results on jittered MNIST and monotone speech.

In computer vision manually route tokens based on semantic classes during upstream pre-training and then select the relevant experts to be used according to the downstream task.

Mixture of Experts (MoE), in the context of modern deep learning architectures, was proven effective in .

That work added an MoE layer which was stacked between LSTM layers, and tokens were separately routed to combinations of experts.

This resulted in state-of-the-art results in language modeling and machine translation benchmarks.

The MoE layer was reintroduced into the Transformer architecture by the Mesh Tensorflow library where MoE layers were introduced as a substitute of the FFN layers, however, there were no accompanying NLP results.

More recently, through advances in machine learning infrastructure, GShard , which extended the XLA compiler, used the MoE Transformer to dramatically improve machine translation across 100 languages.

Finally chooses a different deterministic MoE strategy to split the model parameters into non-overlapping groups of languages.

Sparsity along the sequence length dimension ( MATH ) in the Transformer attention patterns has been a successful technique to reduce the attention complexity from MATH . This has enabled learning longer sequences than previously possible. This version of the Switch Transformer does not employ attention sparsity, but these techniques are complimentary, and, as future work, these could be combined to potentially improve learning on tasks requiring long contexts.

@src https://arxiv.org/abs/2103.00020
@title Learning Transferable Visual Models From Natural Language Supervision
@section Related Work

Any model that leverages written, spoken, signed or any other form of human language as part of its training signal is arguably using natural language as a source of supervision. This is an admittedly extremely broad area and covers most work in the field of distributional semantics including topic models , word, sentence, and paragraph vectors , and language models . It also includes much of the broader field of NLP that deals with predicting or modeling sequences of natural language in some way. Work in NLP intentionally leveraging natural language supervision in the form of explanations, feedback, instructions, and advice for tasks such as classification (as opposed to the commonly used representation of supervision as a set of arbitrarily encoded discrete category labels) has been explored in many creative and advanced ways. Dialog based learning develops techniques to learn from interactive natural language feedback in dialog. Several papers have leveraged semantic parsing to convert natural language explanations into features or additional training labels . More recently, ExpBERT uses feature representations produced by conditioning a deep contextual language model on natural language explanations and descriptions of relations to improve performance on the task of relation extraction.

CLIP is an example of using natural language as a training signal for learning about a domain other than language. In this context, the earliest use of the term natural language supervision that we are aware of is the work of which showed that natural language descriptions could be used along side other sources of supervision to improve performance on the task of video event understanding. However, as mentioned in the introduction and approach section, methods of leveraging natural language descriptions in computer vision well predate the use of this specific term, especially for image retrieval and object classification . Other early work leveraged tags (but not natural language) associated with images for the task of semantic segmentation . More recently, and demonstrated using natural language descriptions and explanations to improve fine-grained visual classification of birds. Others have investigated how grounded language can be used to improve visual representations and classifiers on the ShapeWorld dataset . Finally, techniques which combine natural language with reinforcement learning environments have demonstrated exciting emergent behaviors such as systematically accomplishing zero-shot tasks .

CLIP's pre-training task optimizes for text-image retrieval. This areas of research dates back to the mid-90s with the previously mentioned as representative of early work. While initial efforts focused primarily on predictive objectives over time research shifted towards learning joint multi-modal embedding spaces with techniques like kernel Canonical Correlation Analysis and various ranking objectives . Over time work explored many combinations of training objective, transfer, and more expressive models and steadily improved performance .

Other work has leveraged natural language supervision for domains other than images. explores large scale representation learning by training a system to pair descriptive text with videos instead of images. Several works have explored using dense spoken natural language supervision for videos . When considered together with CLIP, these works suggest that large scale natural language supervision is a promising way to learn high quality perceptual systems for many domains. extended this line of work to an additional modality by adding raw audio as an additional supervision source and demonstrated benefits from combining all three sources of supervision.

As part of our work on CLIP we also construct a new dataset of image-text pairs. Modern work on image-text retrieval has relied on a set of crowd-sourced sentence level image caption evaluation datasets like Pascal1K , Flickr8K , and Flickr30K . However, these datasets are still relatively small and limit achievable performance. Several methods have been proposed to create larger datasets automatically with as a notable early example. In the deep learning era, demonstrated an additional set of (image, text) pairs collected from the internet could improve retrieval performance and several new automatically constructed datasets such as Conceptual Captions , LAIT , and OCR-CC have been created. However, these datasets still use significantly more aggressive filtering or are designed for a specific task such as OCR and as a result are still much smaller than WIT with between 1 and 10 million training examples.

A related idea to CLIP is webly supervised learning. This line of work queries image search engines to build image datasets by querying for terms and uses the queries as the labels for the returned images . Classifiers trained on these large but noisily labeled datasets can be competitive with those trained on smaller carefully labeled datasets. These image-query pairs are also often used to improve performance on standard datasets as additional training data . CLIP also uses search queries as part of its dataset creation process. However CLIP only uses full text sequences co-occuring with images as supervision rather than just the queries, which are often only a single word or short n-gram. We also restrict this step in CLIP to text only querying for sub-string matches while most webly supervised work uses standard image search engines which have their own complex retrieval and filtering pipelines that often involve computer vision systems. Of this line of work, Learning Everything about Anything:

Webly-Supervised Visual Concept Learning has a notably similar ambition and goal as CLIP.

Finally, CLIP is related to a recent burst of activity on learning joint models of vision and language . This line of work focuses on richly connecting vision and language in order to solve complex downstream tasks such as visual question answering, visual commonsense reasoning, or multimodal entailment. These approaches leverage impressively engineered models which combine 3 (or more) pre-trained subsystems, typically an image feature model, a region proposal / object detection model, and a pre-trained masked language model such as BERT. These systems are then jointly fine-tuned via various training objectives on image-text pairs and applied to the aforementioned tasks and achieve impressive results. CLIP is instead focused on learning visual models from scratch via natural language supervision and does not densely connect the two domains with a joint attention model. The only interaction in a CLIP model between the image and text domain is a single dot product in a learned joint embedding space. We are excited to see CLIP hybridized with this line of work.

@src https://arxiv.org/abs/2103.14030
@title Swin Transformer: Hierarchical Vision Transformer using Shifted Windows
@section Related Work

CNN and variants CNNs serve as the standard network model throughout computer vision. While the CNN has existed for several decades , it was not until the introduction of AlexNet that the CNN took off and became mainstream. Since then, deeper and more effective convolutional neural architectures have been proposed to further propel the deep learning wave in computer vision, e.g., VGG , GoogleNet , ResNet , DenseNet , HRNet , and EfficientNet . In addition to these architectural advances, there has also been much work on improving individual convolution layers, such as depth-wise convolution and deformable convolution . While the CNN and its variants are still the primary backbone architectures for computer vision applications, we highlight the strong potential of Transformer-like architectures for unified modeling between vision and language. Our work achieves strong performance on several basic visual recognition tasks, and we hope it will contribute to a modeling shift.

Self-attention based backbone architectures Also inspired by the success of self-attention layers and Transformer architectures in the NLP field, some works employ self-attention layers to replace some or all of the spatial convolution layers in the popular ResNet . In these works, the self-attention is computed within a local window of each pixel to expedite optimization , and they achieve slightly better accuracy/FLOPs trade-offs than the counterpart ResNet architecture. However, their costly memory access causes their actual latency to be significantly larger than that of the convolutional networks . Instead of using sliding windows, we propose to shift windows between consecutive layers, which allows for a more efficient implementation in general hardware.

Self-attention/Transformers to complement CNNs Another line of work is to augment a standard CNN architecture with self-attention layers or Transformers. The self-attention layers can complement backbones or head networks by providing the capability to encode distant dependencies or heterogeneous interactions. More recently, the encoder-decoder design in Transformer has been applied for the object detection and instance segmentation tasks . Our work explores the adaptation of Transformers for basic visual feature extraction and is complementary to these works.

Transformer based vision backbones Most related to our work is the Vision Transformer (ViT) and its follow-ups . The pioneering work of ViT directly applies a Transformer architecture on non-overlapping medium-sized image patches for image classification. It achieves an impressive speed-accuracy trade-off on image classification compared to convolutional networks. While ViT requires large-scale training datasets (i.e., JFT-300M) to perform well, DeiT introduces several training strategies that allow ViT to also be effective using the smaller ImageNet-1K dataset. The results of ViT on image classification are encouraging, but its architecture is unsuitable for use as a general-purpose backbone network on dense vision tasks or when the input image resolution is high, due to its low-resolution feature maps and the quadratic increase in complexity with image size. There are a few works applying ViT models to the dense vision tasks of object detection and semantic segmentation by direct upsampling or deconvolution but with relatively lower performance . Concurrent to our work are some that modify the ViT architecture for better image classification. Empirically, we find our Swin Transformer architecture to achieve the best speed-accuracy trade-off among these methods on image classification, even though our work focuses on general-purpose performance rather than specifically on classification. Another concurrent work explores a similar line of thinking to build multi-resolution feature maps on Transformers. Its complexity is still quadratic to image size, while ours is linear and also operates locally which has proven beneficial in modeling the high correlation in visual signals . Our approach is both efficient and effective, achieving state-of-the-art accuracy on both COCO object detection and ADE20K semantic segmentation.

@src https://arxiv.org/abs/2105.05233
@title Diffusion Models Beat GANs on Image Synthesis
@section Background

In this section, we provide a brief overview of diffusion models. For a more detailed mathematical description, we refer the reader to Appendix .

On a high level, diffusion models sample from a distribution by reversing a gradual noising process. In particular, sampling starts with noise MATH and produces gradually less-noisy samples MATH until reaching a final sample MATH . Each timestep MATH corresponds to a certain noise level, and MATH can be thought of as a mixture of a signal MATH with some noise MATH where the signal to noise ratio is determined by the timestep MATH . For the remainder of this paper, we assume that the noise MATH is drawn from a diagonal Gaussian distribution, which works well for natural images and simplifies various derivations.

A diffusion model learns to produce a slightly more "denoised" MATH from MATH . ddpm parameterize this model as a function MATH which predicts the noise component of a noisy sample MATH . To train these models, each sample in a minibatch is produced by randomly drawing a data sample MATH , a timestep MATH , and noise MATH , which together give rise to a noised sample MATH (Equation ).

The training objective is then MATH , i.e. a simple mean-squared error loss between the true noise and the predicted noise (Equation ).

It is not immediately obvious how to sample from a noise predictor MATH . Recall that diffusion sampling proceeds by repeatedly predicting MATH from MATH , starting from MATH . ddpm show that, under reasonable assumptions, we can model the distribution MATH of MATH given MATH as a diagonal Gaussian MATH ,

where the mean MATH can be calculated as a function of MATH (Equation ).

The variance MATH of this Gaussian distribution can be fixed to a known constant ddpm or learned with a separate neural network head improved ,

and both approaches yield high-quality samples when the total number of diffusion steps MATH is large enough.

ddpm observe that the simple mean-sqaured error objective, MATH , works better in practice than the actual variational lower bound MATH that can be derived from interpreting the denoising diffusion model as a VAE. They also note that training with this objective and using their corresponding sampling procedure is equivalent to the denoising score matching model from improvedscore , who use Langevin dynamics to sample from a denoising model trained with multiple noise levels to produce high quality image samples. We often use "diffusion models" as shorthand to refer to both classes of models.

@src https://arxiv.org/abs/2105.05233
@title Diffusion Models Beat GANs on Image Synthesis
@section Related Work

Score based generative models were introduced by scorematching as a way of modeling a data distribution using its gradients, and then sampling using Langevin dynamics langevin . ddpm found a connection between this method and diffusion models dickstein , and achieved excellent sample quality by leveraging this connection. After this breakthrough work, many works followed up with more promising results: diffwave and wavegrad demonstrated that diffusion models work well for audio; adversarial found that a GAN-like setup could improve samples from these models; sde explored ways to leverage techniques from stochastic differential equations to improve the sample quality obtained by score-based models; ddim and improved proposed methods to improve sampling speed; improved and sr3 demonstrated promising results on the difficult ImageNet generation task using upsampling diffusion models. Also related to diffusion models, and following the work of dickstein , variationalwalkback described a technique for learning a model with learned iterative generation steps, and found that it could achieve good image samples when trained with a likelihood objective.

One missing element from previous work on diffusion models is a way to trade off diversity for fidelity. Other generative techniques provide natural levers for this trade-off. biggan introduced the truncation trick for GANs, wherein the latent vector is sampled from a truncated normal distribution. They found that increasing truncation naturally led to a decrease in diversity but an increase in fidelity. More recently, vqvae2 proposed to use classifier rejection sampling to filter out bad samples from an autoregressive likelihood-based model, and found that this technique improved FID. Most likelihood-based models also allow for low-temperature sampling temperature , which provides a natural way to emphasize modes of the data distribution (see Appendix ).

Other likelihood-based models have been shown to produce high-fidelity image samples. VQ-VAE vqvae and VQ-VAE-2 vqvae2 are autoregressive models trained on top of quantized latent codes, greatly reducing the computational resources required to train these models on large images. These models produce diverse and high quality images, but still fall short of GANs without expensive rejection sampling and special metrics to compensate for blurriness. DCTransformer dctransformer is a related method which relies on a more intelligent compression scheme. VAEs are another promising class of likelihood-based models, and recent methods such as NVAE nvae and VDVAE vdvae have successfully been applied to difficult image generation domains. Energy-based models are another class of likelihood-based models with a rich history temperature,helmholtz,contrastive . Sampling from the EBM distribution is challenging, and genconv demonstrate that Langevin dynamics can be used to sample coherent images from these models. yilunenergy further improve upon this approach, obtaining high quality images. More recently, diffusionebm incorporate diffusion steps into an energy-based model, and find that doing so improves image samples from these models.

Other works have controlled generative models with a pre-trained classifier. For example, an emerging body of work clipglass,styleclip,bigsleep aims to optimize GAN latent spaces for text prompts using pre-trained CLIP clip models. More similar to our work, sde uses a classifier to generate class-conditional CIFAR-10 images with a diffusion model. In some cases, classifiers can act as stand-alone generative models. For example, robustgeneration demonstrate that a robust image classifier can be used as a stand-alone generative model, and jem train a model which is jointly a classifier and an energy-based model.

@src https://arxiv.org/abs/2106.09685
@title LoRA: Low-Rank Adaptation of Large Language Models
@section Related Works

Transformer is a sequence-to-sequence architecture that makes heavy use of self-attention.

applied it to autoregressive language modeling by using a stack of Transformer decoders.

Since then, Transformer-based language models have dominated NLP, achieving the state-of-the-art in many tasks.

A new paradigm emerged with BERT and GPT-2 – both are large Transformer language models trained on a large amount of text – where fine-tuning on task-specific data after pre-training on general domain data provides a significant performance gain compared to training on task-specific data directly.

Training larger Transformers generally results in better performance and remains an active research direction.

GPT-3 is the largest single Transformer language model trained to-date with 175B parameters.

While GPT-3 175B can adapt its behavior with just a few additional training examples, the result depends heavily on the input prompt .

This necessitates an empirical art of composing and formatting the prompt to maximize a model's performance on a desired task, which is known as prompt engineering or prompt hacking.

Fine-tuning retrains a model pre-trained on general domains to a specific task .

Variants of it include learning just a subset of the parameters , yet practitioners often retrain all of them to maximize the downstream performance.

However, the enormity of GPT-3 175B makes it challenging to perform fine-tuning in the usual way due to the large checkpoint it produces and the high hardware barrier to entry since it has the same memory footprint as pre-training.

Many have proposed inserting adapter layers between existing layers in a neural network .

Our method uses a similar bottleneck structure to impose a low-rank constraint on the weight updates.

The key functional difference is that our learned weights can be merged with the main weights during inference, thus not introducing any latency, which is not the case for the adapter layers ( sec:existing_solutions_no_good ).

A comtenporary extension of adapter is compacter , which essentially parametrizes the adapter layers using Kronecker products with some predetermined weight sharing scheme.

Similarly, combining LoRA with other tensor product-based methods could potentially improve its parameter efficiency, which we leave to future work.

More recently, many proposed optimizing the input word embeddings in lieu of fine-tuning, akin to a continuous and differentiable generalization of prompt engineering .

We include comparisons with in our experiment section.

However, this line of works can only scale up by using more special tokens in the prompt, which take up available sequence length for task tokens when positional embeddings are learned.

Low-Rank Structures in Deep Learning Low-rank structure is very common in machine learning.

A lot of machine learning problems have certain intrinsic low-rank structure .

Moreover, it is known that for many deep learning tasks, especially those with a heavily over-parametrized neural network, the learned neural network will enjoy low-rank properties after training .

Some prior works even explicitly impose the low-rank constraint when training the original neural network ; however, to the best of our knowledge, none of these works considers low-rank update to a frozen model for adaptation to downstream tasks.

In theory literature, it is known that neural networks outperform other classical learning methods, including the corresponding (finite-width) neural tangent kernels when the underlying concept class has certain low-rank structure .

Another theoretical result in suggests that low-rank adaptations can be useful for adversarial training.

In sum, we believe that our proposed low-rank adaptation update is well-motivated by the literature.

@src https://arxiv.org/abs/2112.10741
@title GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models
@section Related Work

Many works have approached the problem of text-conditional image generation. train GANs with text-conditioning using publicly available image captioning datasets. synthesize images conditioned on text by building on the approach of , wherein an autoregressive generative model is trained on top of discrete latent codes. Concurrently with our work, train text-conditional discrete diffusion models on top of discrete latent codes, finding that the resulting system can produce competitive image samples.

Several works have explored image inpainting with diffusion models. finds that diffusion models can not only inpaint regions of an image, but can do so conditioned on a rough sketch (or set of colors) for the image. finds that, when trained directly on the inpainting task, diffusion models can smoothly inpaint regions of an image without edge artifacts.

CLIP has previously been used to guide image generation. use CLIP to guide GAN generation towards text prompts. The online AI-generated art community has produced promising early results using unnoised CLIP-guided diffusion . edits images using text prompts by fine-tuning a diffusion model to target a CLIP loss while reconstructing the original image's DDIM latent. trains GAN models conditioned on perturbed CLIP image embeddings, resulting in a model which can condition images on CLIP text embeddings. None of these works explore noised CLIP models, and often rely on data augmentations and perceptual losses as a result.

Several works have explored text-based image editing. propose a dual attention mechanism for using text embeddings to inpaint missing regions of an image. propose a method for editing images of faces using feature vectors grounded in text. pair CLIP with state-of-the-art GAN models to inpaint images using text targets. Concurrently with our work, use CLIP-guided diffusion to inpaint regions of images conditioned on text.

@src https://arxiv.org/abs/2112.10752
@title High-Resolution Image Synthesis with Latent Diffusion Models
@section Related Work

The high dimensional nature of images presents distinct challenges to generative modeling.

allow for efficient sampling of high resolution images with good perceptual quality , but are difficult to optimize and struggle to capture the full data distribution

In contrast, likelihood-based methods emphasize good density estimation which renders optimization more well-behaved.

and flow-based models enable efficient synthesis of high resolution images , but sample quality is not on par with GANs.

While autoregressive models (ARM) achieve strong performance in density

estimation, computationally demanding architectures

and a sequential sampling process limit them to low resolution images.

Because pixel based representations of images contain barely

perceptible, high-frequency details , maximum-likelihood training spends a

disproportionate amount of capacity on modeling them, resulting in

use ARMs to model a compressed latent image space instead of raw pixels.

Recently, Diffusion Probabilistic Models (DM) , have achieved state-of-the-art results in density estimation as well as in sample quality . The generative power of these models stems from a natural fit to the inductive biases of image-like data when their underlying neural backbone is implemented as a UNet .

The best synthesis quality is usually achieved when a reweighted objective

is used for training. In this case, the DM corresponds to a lossy compressor and allow to trade image quality for compression capabilities.

Evaluating and optimizing these models in pixel space, however, has the downside of low inference speed and very high training costs.

While the former can be partially adressed by advanced sampling strategies and hierarchical approaches , training on high-resolution image data always requires to calculate expensive gradients.

We adress both drawbacks with our proposed LDMs, which

work on a compressed latent space of lower dimensionality.

This renders training computationally cheaper and speeds up inference with

almost no reduction in synthesis quality (see

To mitigate the shortcomings of individual generative approaches, a lot of research has gone into combining the strengths of different methods into more efficient and performant models via a two stage approach. VQ-VAEs use autoregressive models to learn an expressive prior over a discretized latent space.

extend this approach to text-to-image generation by learning a joint distributation over discretized image and text representations.

More generally, uses conditionally invertible networks to provide a generic transfer between latent spaces of diverse domains.

Different from VQ-VAEs, VQGANs employ a first stage with an adversarial and perceptual objective to scale autoregressive transformers to larger images.

However, the high compression rates required for feasible ARM training, which introduces billions of trainable parameters , limit the overall performance of such approaches and less compression comes at the price of high computational cost .

Our work prevents such trade-offs, as our proposed LDMs scale more gently to higher dimensional latent spaces due to their convolutional backbone.

Thus, we are free to choose the level of compression which optimally mediates between learning a powerful first stage, without leaving too much perceptual compression up to the generative diffusion model while guaranteeing high-fidelity reconstructions (see Fig. ).

While approaches to jointly or separately

learn an encoding/decoding model together with a score-based prior exist,

the former still require a difficult weighting between reconstruction and generative capabilities and are outperformed by our approach (Sec. ), and the latter focus on highly structured images such as human faces.

@src https://arxiv.org/abs/2201.03545
@title A ConvNet for the 2020s
@section Related Work

In both the pre- and post-ViT eras, the hybrid model combining convolutions and self-attentions has been actively studied.

Prior to ViT, the focus was on augmenting a ConvNet with self-attention/non-local modules to capture long-range dependencies.

The original ViT first studied a hybrid configuration, and a large body of follow-up works focused on reintroducing convolutional priors to ViT, either in an explicit or implicit fashion.

Recent convolution-based approaches. Han et al. show that local Transformer attention is equivalent to inhomogeneous dynamic depthwise conv. The MSA block in Swin is then replaced with a dynamic or regular depthwise convolution, achieving comparable performance to Swin. A concurrent work ConvMixer demonstrates that, in small-scale settings, depthwise convolution can be used as a promising mixing strategy. ConvMixer uses a smaller patch size to achieve the best results, making the throughput much lower than other baselines. GFNet adopts Fast Fourier Transform (FFT) for token mixing. FFT is also a form of convolution, but with a global kernel size and circular padding. Unlike many recent Transformer or ConvNet designs, one primary goal of our study is to provide an in-depth look at the process of modernizing a standard ResNet and achieving state-of-the-art performance.

@src https://arxiv.org/abs/2201.11903
@title Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
@section Related Work

This work is inspired by many research areas, which we detail in an extended related work section ( sec:extended-related-work ). Here we describe two directions and associated papers that are perhaps most relevant.

The first relevant direction is using intermediate steps to solve reasoning problems. pioneer the idea of using natural language rationales to solve math word problems through a series of intermediate steps. Their work is a remarkable contrast to the literature using formal languages to reason . extend by creating a larger dataset and using it to finetune a pretrained language model rather than training a model from scratch. In the domain of program synthesis, leverage language models to predict the final outputs of Python programs via first line-to-line predicting the intermediate computational results, and show that their step-by-step prediction method performs better than directly predicting the final outputs.

Naturally, this paper also relates closely to the large body of recent work on prompting.

Since the popularization of few-shot prompting as given by , several general approaches have improved the prompting ability of models, such as automatically learning prompts or giving models instructions describing a task .

Whereas these approaches improve or augment the input part of the prompt (e.g., instructions that are prepended to inputs), our work takes the orthogonal direction of augmenting the outputs of language models with a chain of thought.

@src https://arxiv.org/abs/2203.02155
@title Training language models to follow instructions with human feedback
@section Related work

Research on alignment and learning from human feedback. We build on previous techniques to align models with human intentions, particularly reinforcement learning from human feedback (RLHF). Originally developed for training simple robots in simulated environments and Atari games , it has recently been applied to fine-tuning language models to summarize text . This work is in turn influenced by similar work using human feedback as a reward in domains such as dialogue , translation , semantic parsing , story generation , review generation , and evidence extraction . use written human feedback to augment prompts and improve the performance of GPT-3. There has also been work on aligning agents in text-based environments using RL with a normative prior . Our work can be seen as a direct application of RLHF to aligning language models on a broad distribution of language tasks.

The question of what it means for language models to be aligned has also received attention recently . catalog behavioral issues in LMs that result from misalignment, including producing harmful content and gaming misspecified objectives. In concurrent work, propose language assistants as a testbed for alignment research, study some simple baselines, and their scaling properties.

Training language models to follow instructions. Our work is also related to research on cross-task generalization in language models, where LMs are fine-tuned on a broad range of public NLP datasets (usually prefixed with an appropriate instruction) and evaluated on a different set of NLP tasks. There has been a range of work in this domain , which differ in training and evaluation data, formatting of instructions, size of pretrained models, and other experimental details. A consistent finding across studies is that fine-tuning LMs on a range of NLP tasks, with instructions, improves their downstream performance on held-out tasks, both in the zero-shot and few-shot settings.

There is also a related line of work on instruction following for navigation, where models are trained to follow natural language instructions to navigate in a simulated environment .

Evaluating the harms of language models. A goal of modifying the behavior of language models is to mitigate the harms of these models when they're deployed in the real world. These risks have been extensively documented . Language models can produce biased outputs , leak private data , generate misinformation , and be used maliciously; for a thorough review we direct the reader to . Deploying language models in specific domains gives rise to new risks and challenges, for example in dialog systems . There is a nascent but growing field that aims to build benchmarks to concretely evaluate these harms, particularly around toxicity , stereotypes , and social bias . Making significant progress on these problems is hard since well-intentioned interventions on LM behavior can have side-effects ; for instance, efforts to reduce the toxicity of LMs can reduce their ability to model text from under-represented groups, due to prejudicial correlations in the training data .

Modifying the behavior of language models to mitigate harms. There are many ways to change the generation behavior of language models. fine-tune LMs on a small, value-targeted dataset, which improves the models' ability to adhere to these values on a question answering task. filter the pretraining dataset by removing documents on which a language model has a high conditional likelihood of generating a set of researcher-written trigger phrases. When trained on this filtered dataset, their LMs generate less harmful text, at the cost of a slight decrease in language modeling performance. use a variety of approaches to improve the safety of chatbots, including data filtering, blocking certain words or n-grams during generation, safety-specific control tokens , and human-in-the-loop data collection . Other approaches for mitigating the generated bias by LMs use word embedding regularization , data augmentation , null space projection to make the distribution over sensitive tokens more uniform , different objective functions , or causal mediation analysis . There is also work on steering the generation of language models using a second (usually smaller) language model , and variants of this idea have been applied to reducing language model toxicity .

@src https://arxiv.org/abs/2203.11171
@title Self-Consistency Improves Chain of Thought Reasoning in Language Models
@section Related work

Language models are known to struggle in Type 2 tasks, such as arithmetic, logical and commonsense reasoning .

Previous work has primarily focused on specialized approaches for improving reasoning .

Compared to prior work, self-consistency is applicable to a wide range of reasoning tasks without any additional supervision or fine-tuning, while still substantially improving the performance of the chain-of-thought prompting approach proposed in .

Sampling and re-ranking in language models.

Multiple decoding strategies for language models have been proposed in the literature, e.g., temperature sampling , top- MATH sampling , nucleus sampling , minimum Bayes risk decoding , and typical decoding .

Other work has sought to explicitly promote diversity in the decoding process .

Re-ranking is another common approach to improve generation quality in language models .

collect additional human annotations to train a re-ranker for response filtering.

train a "verifier" to re-rank generated solutions, which substantially improves the solve rate on math tasks compared to just fine-tuning the language model.

improve the consistency of factual knowledge extraction by extending pre-training with an additional consistency loss.

All these methods require either training an additional re-ranker or collecting additional human annotation, while self-consistency requires no additional training, fine-tuning, nor extra data collection.

Some previous work has considered task-specific approaches for identifying reasoning paths, such as constructing semantic graphs , learning an RNN to retrieve reasoning paths over the Wikipedia graph , fine-tuning with human annotated reasoning paths on math problems , or training an extractor with heuristic-based pseudo reasoning paths

More recently, the importance of diversity in the reasoning processes has been noticed, but only leveraged via task-specific training, either through an additional QA model over extracted reasoning paths , or by the introduction of latent variables in a commonsense knowledge graph .

Compared to these approaches, self-consistency is far simpler and requires no additional training. The approach we propose simply couples the generation of reasoning paths and a final answer by sampling from the decoder, using aggregation to recover the most consistent answer without additional modules.

Some prior work has shown that language models can suffer from inconsistency in conversation ,

use "consistency" to refer to generating an infinite-length sequence in recurrent language models.

improve the logical consistency of samples from a System 1 model by adding a System 2-inspired logical reasoning module.

In this paper we focus on a slightly different notion of "consistency", i.e., utilizing answer consistency among diverse reasoning paths to improve accuracy.

@src https://arxiv.org/abs/2204.14198
@title Flamingo: a Visual Language Model for Few-Shot Learning
@section Related work

Language modelling and few-shot adaptation.

Language modelling has recently made substantial progress following the introduction of Transformers .

The paradigm of first pretraining on a vast amount of data followed by an adaptation on a downstream task has become standard .

In this work, we build on the 70B Chinchilla language model as the base LM for .

Numerous works have explored techniques to adapt language models to novel tasks using a few examples.

These include adding small adapter modules , fine-tuning a small part of the LM , showing in-context examples in the prompt , or optimizing the prompt through gradient descent.

In this paper, we take inspiration from the in-context few-shot learning technique instead of more involved few-shot learning approaches based on metric learning or meta-learning .

These LM breakthroughs have been influential for vision-language modelling.

In particular, BERT inspired a large body of vision-language work .

We differ from these approaches as do not require fine-tuning on new tasks.

Another family of vision-language models is based on contrastive learning .

differs from contrastive models as it can generate text,

although we build and rely upon them for our vision encoder.

Similar to our work are VLMs able to generate text in an autoregressive manner .

Concurrent works also propose to formulate numerous vision tasks as text generation problems.

Building on top of powerful pretrained language models has been explored in several recent works.

One recent line of work proposes to freeze the pretrained LM weights to prevent catastrophic forgetting .

We follow this idea by freezing the Chinchilla LM layers and adding learnable layers within the frozen LM.

We differ from prior work by introducing the first LM that can ingest arbitrarily interleaved images, videos, and text.

Web-scale vision and language training datasets.

Manually annotated vision and language datasets are costly to obtain and thus relatively small (10k-100k) in scale .

To alleviate this lack of data, numerous works automatically scrape readily available paired vision-text data.

In addition to such paired data, we show the importance of also training on entire multimodal webpages containing interleaved images and text as a single sequence.

Concurrent work CM3 proposes to generate HTML markup from pages, while we simplify the text prediction task by only generating plain text.

We emphasize few-shot learning and vision tasks while CM3 primarily evaluates on language-only benchmarks in a zero-shot or fine-tuned setup.

@src https://arxiv.org/abs/2205.11487
@title Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding
@section Related Work

Diffusion models have seen wide success in image generation , outperforming GANs in fidelity and diversity, without training instability and mode collapse issues .

Autoregressive models , GANs , VQ-VAE Transformer-based methods , and diffusion models have seen remarkable progress in text-to-image , including the concurrent DALL-E 2 , which uses a diffusion prior on CLIP text latents and cascaded diffusion models to generate high resolution MATH images; we believe is much simpler, as does not need to learn a latent prior, yet achieves better results in both MS-COCO FID and human evaluation on .

GLIDE also uses cascaded diffusion models for text-to-image, but we use large pretrained frozen language models, which we found to be instrumental to both image fidelity and image-text alignment.

XMC-GAN also uses BERT as a text encoder, but we scale to much larger text encoders and demonstrate the effectiveness thereof.

The use of cascaded models is also popular throughout the literature and has been used with success in diffusion models to generate high resolution images .

@src https://arxiv.org/abs/2205.11487
@title Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding
@section Background

Diffusion models are latent variable models with latents MATH that obey a forward process MATH starting at data MATH . This forward process is a Gaussian process that satisfies the Markovian structure:

where MATH , MATH , and MATH specify a differentiable noise schedule whose log signal-to-noise-ratio,

i.e., MATH , decreases with MATH until MATH .

For generation, the diffusion model is learned to reverse this forward process.

Learning to reverse the forward process can be reduced to learning to denoise MATH into an estimate MATH for all MATH , where MATH is an optional conditioning signal (such as text embeddings or a low resolution image) drawn from the dataset jointly with MATH . This is accomplished training MATH using a weighted squared error loss

where MATH , MATH , and MATH . This reduction of generation to denoising is justified as optimizing a weighted variational lower bound on the data log likelihood under the diffusion model, or as a form of denoising score matching . We use the MATH -prediction parameterization, defined as MATH , and we impose a squared error loss on MATH in MATH space with MATH sampled according to a cosine schedule . This corresponds to a particular weighting MATH and leads to a scaled score estimate MATH , where MATH is the true density of MATH given MATH under the forward process starting at MATH . Related model designs include the work of .

To sample from the diffusion model, we start at MATH and use the discrete time ancestral sampler and DDIM for certain models. DDIM follows the deterministic update rule

where MATH follow a uniformly spaced sequence from 1 to 0. The ancestral sampler arises from a reversed description of the forward process; noting that MATH , where

MATH and MATH , it follows the stochastic update rule

where MATH , and MATH controls the stochasticity of the sampler .

@src https://arxiv.org/abs/2205.11916
@title Large Language Models are Zero-Shot Reasoners
@section Background

We briefly review the two core preliminary concepts that form the basis of this work: the advent of large language models (LLMs) and prompting, and (CoT) prompting for multi-step reasoning.

A language model (LM), is a model that looks to estimate the probability distribution over text. Recently, scaling improvements through larger model sizes (from a few million to hundreds of millions to hundreds of billions parameters) and larger data (e.g. webtext corpora ) have enabled pre-trained large language models (LLMs) to be incredibly adept at many downstream NLP tasks. Besides the classic "pre-train and fine-tune" paradigm , models scaled to 100B+ parameters exhibit properties conducive to few-shot learning , by way of in context learning, where one can use a text or template known as a prompt to strongly guide the generation to output answers for desired tasks, thus beginning an era of "pre-train and prompt" . In work, we call such prompts with explicit conditioning on few task examples as few-shot prompts, and other template-only prompts as zero-shot prompts.

Multi-step arithmetic and logical reasoning benchmarks have particularly challenged the scaling laws of large language models . Chain of thought (CoT) prompting , an instance of few-shot prompting, proposed a simple solution by modifying the answers in few-shot examples to step-by-step answers, and achieved significant boosts in performance across these difficult benchmarks, especially when combined with very large language models like PaLM . The top row of fig_overview_1 shows standard few-shot prompting against (few-shot) CoT prompting. Notably, few-shot learning was taken as a given for tackling such difficult tasks, and the zero-shot baseline performances were not even reported in the original work . To differentiate it from our method, we call as in this work.

@src https://arxiv.org/abs/2205.14135
@title FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness
@section Related Work

The broad concept of optimizing for reading and writing to fast/slow memory has a long history in computer science and has been known by many names.

We draw the most direct connection to the literature of analyzing I/O complexity in this work , but concepts of memory hierarchies are fundamental and has appeared in many forms, from the working set model , to data locality , to the Roofline model of arithmetic intensity , to analyses of scalability , to standard textbook treatments of computer architecture .

We hope that this work encourages the community to adopt these ideas in more parts of the deep learning stack.

Efficient ML Models with Structured Matrices.

Matrix multiply is the core computational bottleneck of most machine learning

To reduce the computational complexity, there have been numerous approaches to

learn over a more efficient set of matrices.

These matrices are called structured matrices, which have subquadratic

( MATH for dimension MATH ) number of parameters and runtime.

Most common examples of structured matrices are sparse and low-rank matrices,

along with fast transforms commonly encountered in signal processing (Fourier,

Chebyshev, sine/cosine, orthogonal polynomials).

There have been several more general classes of structured matrices proposed in

The butterfly pattern we use for our block-sparse attention is motivated by the

products have been shown to be able to express any structured matrices with

However, even though structured matrices are efficient in theory, they have not

seen wide adoption since it is hard to translate their efficiency to wall-clock

speedup since dense unconstrained matrix multiply has very optimize

implementation, a phenomenon known as the hardware

to make butterfly matrices more hardware-friendly.

Our block-sparse can be seen as a step towards making sparse model

Sparse models have seen success in compressing models for inference (pruning) by

suggests that there are a set of small sub-networks derived from a larger dense

network that performs as well as the original dense network.

Out block-sparse can also be seen as a fixed lottery ticket in the

context of attention: we fix the sparsity pattern to be the butterfly pattern

through training, and observe that it performs almost as well as the (dense)

Transformer-based models have become the most widely-used architecture in

natural language processing and computer

However, one of their computational bottlenecks is that their time and memory

scales quadratic in the sequence length.

There are numerous approaches to overcome this bottleneck, including

approximation with hashing (i.e., sparse) such as

One can even combine sparse and low-rank approximation for better accuracy

Other approaches include compressing along the sequence dimension to attend to

One can also attend over the states from previous sequences to help lengthen the

context (e.g., Transformer-XL and Compressive

We recommend the survey for more details.

There are several lines of work on developing other modules instead of attention

to model longer context. HiPPO and its extensions, most

history on a polynomial basis, allowing accurate reconstruction of the history

They combine the strengths of CNNs (efficient training), RNNs (efficient

inference), and continuous models (robust to change in sampling rates).

and FLASH are other attempts at replacing attention

in the context of image classification and language modeling.

@src https://arxiv.org/abs/2210.03629
@title ReAct: Synergizing Reasoning and Acting in Language Models
@section Related Work

Perhaps the most well-known work of using LLMs for reasoning is Chain-of-Thought (CoT) , which reveals the ability of LLMs to formulate their own "thinking procedure" for problem solving. Several follow-up works have since been performed, including least-to-most prompting for solving complicated tasks , zero-shot-CoT , and reasoning with self-consistency . Recently, systematically studied the formulation and structure of CoT, and observed that the presence of symbols, patterns and texts is crucial to the effectiveness of CoT.

Other work has also been extended to more sophisticated reasoning architecture beyond simple prompting. For example Selection-Inference divides the reasoning process into two steps of "selection" and "inference". STaR bootstraps the reasoning process by finetuning the model on correct rationales generated by the model itself. Faithful reasoning decomposes multi-step reasoning into three steps, each performed by a dedicated LM respectively. Similar approaches like Scratchpad , which finetunes a LM on intermediate computation steps, also demonstrate improvement on multi-step computation problems.

In contrast to these methods, performs more than just isolated, fixed reasoning, and integrates model actions and their corresponding observations into a coherent stream of inputs for the model to reason more accurately and tackle tasks beyond reasoning (e.g.\,interactive decision making).

The strong capability of LLMs has enabled them to perform tasks beyond language generation, and it is becoming more popular to take advantage of LLMs as a policy model for decision making, especially in interactive environments. WebGPT

uses an LM to interact with web browsers, navigate through web pages, and infer answers to complicated questions from ELI5 . In comparison to , WebGPT does not explicitly model the thinking and reasoning procedure, instead rely on expensive human feedback for reinforcement learning.

In conversation modeling, chatbots like BlenderBot and Sparrow and task-oriented dialogue systems like SimpleTOD also train LMs to make decision about API calls. Unlike , they do not explicitly consider the reasoning procedure either, and also relies on expensive datasets and human feedback collections for policy learning. In contrast, learns a policy in a much cheaper way, since the decision making process only requires language description of the reasoning procedure. (Human feedback can also be incorporated in a complementary manner but we leave it for future work.

LLMS have also been increasingly employed in interactive and embodied environments for planning and decision making. Perhaps most relevant to in this respect are SayCan and Inner Monologue , which use LLMs for robotic action planning and decision making. In SayCan, LLMs were prompted to directly predict possible actions a robot can take, which is then reranked by an affordance model grounded on the visual environments for final prediction. Inner Monologue made further improvements by adding the eponymous "inner monologue", which is implemented as injected feedback from the environment. To our knowledge, Inner Monologue is the first work that demonstrates such a closed-loop system, which builds on. However, we argue that Inner Monologue does not truly comprise of inner thoughts — this is elaborated in Section .

We also note that leveraging language as semantically-rich inputs in the process of interactive decision making has been shown to be successful under other settings . It is becoming more evident that with the help of LLMs, language as a fundamental cognitive mechanism will play a critical role in interaction and decision making. What is more, progress in LLMs has also inspired the development of versatile and generalist agents like .

@src https://arxiv.org/abs/2210.08402
@title LAION-5B: An open large-scale dataset for training next generation image-text models
@section Related Work

Vision-Language Models. made a large step forward in multimodal learning for image-text data with their CLIP (Contrastive Language–Image Pre-training) model.

The authors proposed a contrastive learning scheme to embed both images and text into a shared representation space, which enabled unparalleled performance in zero-shot image classification.

Moreover, CLIP made large progress on multiple challenging distribution shifts .

After CLIP's initial success, ALIGN and BASIC improved contrastive multimodal learning by increasing the training set size and the batch size used for training .

LiT also increased training scale and experimented with a combination of pre-trained image representations and contrastive fine-tuning to connect frozen image representations to text .

Flamingo introduced the first large vision-language model with in-context learning .

Other papers have combined contrastive losses with image captioning to further improve performance .

Beyond image classification and retrieval, the community later adapted CLIP to further vision tasks such as object navigation and visual question answering .

Another direction that has recently seen large progress in multimodal learning is text-guided image generation .

Specifically, DALL-E demonstrated diverse image generation capabilities for text prompts combining multiple concepts .

GLIDE, DALL-E 2, Imagen, Parti, and Stable Diffusion then improved visual fidelity and text-prompt correspondence .

Image-Text Datasets. Earlier dataset creation efforts such as MS-COCO and Visual Genome curated image and region labels through human annotation .

While this resulted in high-quality labels, it also limited the scale of the datasets to only 330K and 5M examples, respectively.

The web-harvested YFCC-100M dataset is substantially larger with about 99 million images and one million videos from Flickr, but only contains the user-generated metadata without additional annotations collected specifically for training computer vision models .

As a result, the text associated with an image sometimes has little to no correspondence with the actual image content.

To address this shortcoming of web-harvested image-text data, the Conceptual Captions dataset (CC3M) started with images and alt-text collected from the web, but then performed additional data cleaning procedures .

To increase the size of the dataset, researchers later relaxed the filtering protocol to arrive at the subsequent CC12M dataset .

Building datasets from alt-text continued with ALT200M and ALIGN , which increased the dataset size up to 1.8 billion image-text pairs.

In contrast to relying on alt-text, RedCaps used the captions provided by Reddit users to collect higher quality captions .

Datasets with non-English image-text pairs are less common.

As a result, researchers translated English captioning datasets to other languages such as Farsi, Korean, and Japanese .

To the best of our knowledge, the largest multilingual dataset before LAION-5B has around 36 million samples from Wikipedia Image Text .

With the release of LAION-5B, researchers now have access to roughly two orders of magnitude more multilingual samples, which provides new opportunities for research on low-resource languages and multilingual models.

Scaling Behavior. Improving model performance by increasing data scale has been a theme in machine learning since at least the ImageNet dataset .

In the following decade, computer vision benefited from growth in model, data, and compute scale, in addition to advances in both convolutional and transformer architectures .

Industrial research labs assembled large internal datasets such as Instagram-1B, JFT300M, and JFT3B to support image pre-training .

Natural language processing (NLP) demonstrated the beneficial effect of model, data, and compute scale on generalization through large language models such as GPT-3 and associated experiments on scaling behavior .

Community efforts like the The Pile and BigScience ROOTS made large text datasets more accessible.

@src https://arxiv.org/abs/2212.06817
@title RT-1: Robotics Transformer for Real-World Control at Scale
@section Related Work

A number of recent works have proposed Transformer-based policies for robotic control. As in RT-1, several works use language commands processed with Transformers as a robust framework for specifying and generalizing to new tasks .

Our work takes the application of Transformers a step further and treats the mapping of language and vision observations to robot actions as a sequence modelling problem, using a Transformer to learn this mapping. This idea is directly inspired by successes in game-playing as well as simulated robot navigation , locomotion , and manipulation environments. We note that several of these works go beyond only text conditioning and use Transformers to also generalize across robot morphologies (e.g., ) and other modalities for task specifications (e.g., ). These extensions are promising future directions for RT-1.

Beyond Transformer-based policies, the focus of our work is on generalizable and robust real-world robotic manipulation at scale.

Existing works on real-world Transformer-based robotic manipulation focus on efficiently learning tasks from a set of demonstrations per task . Behavior Transformer and Gato advocate for training a single model on large-scale robotic and non-robotic datasets. However, these works are limited in their real-world robotic tasks; e.g., Gato learns effectively a single task (colored block stacking) without evaluating generalization to new tasks or a variety of real-world settings. On the technical side, our work examines how Transformer-based policies can be built so as to combine high capacity and generalization with the computational efficiency necessary for real-time control.

While the use of high-capacity Transformer models to learn robotic control policies is a fairly recent innovation, robotics has a long history of multi-task and language-conditioned learning, and RT-1 builds on these foundations.

A significant body of work deals with learning policies and predictive models for robotic grasping , with the aim of generalizing to new objects.

Prior works have sought to address robotic language understanding through pipelined approaches that combine language parsing, vision, and robotic control and with end-to-end approaches .

Multi-task robotic learning has also been approached from the perspective of learning to reach goals , as well as learning policies that can perform tasks in a discrete set or some other parameterized form .

A number of prior works in robotics have also focused on collecting datasets containing demonstrations or trials that illustrate a variety of different tasks .

Our work adds further evidence in support of the power of multi-task, language-conditioned robotic learning, presenting experimental results at a larger scale and with a greater variety of behaviors, objects, and scenes and proposing new architectures and design choices that enable robotic learning at a significantly larger scale.

@src https://arxiv.org/abs/2304.07193
@title DINOv2: Learning Robust Visual Features without Supervision
@section Related Work

A first family of self-supervised methods focuses on pretext tasks built from the image, i.e., extracting a signal from the image to be predicted from the rest of the image.

This idea has become prevalent with the work of , where they train by predicting the context of a given patch.

Many other pretext tasks were introduced based on, for example, re-colorizing images , predicting transformations , inpainting or patch re-ordering .

Recently, the emergence of patch-based architectures, like ViTs, has led to a revisit of inpainting for pre-training , potentially in feature space .

Of particular interest, show that a masked auto-encoder (MAE) learns features that provide substantial improvements when finetuned on downstream tasks.

This property of MAEs has been further validated on video , audio , and across other modalities .

However, their features require supervised finetuning, while our features perform well out of the box.

Discriminative self-supervised learning.

The second line of work, closer to ours, is using discriminative signals between images or groups of images to learn features.

This family of methods has roots in early deep learning work but became popular with the emergence of instance classification methods .

Several improvements were made based either on instance-level objectives or clustering .

These methods provide performant frozen features on standard benchmarks like ImageNet , but they are hard to scale to larger model sizes .

In this work, we revisit the training of these approaches in the context of large pretraining datasets and models.

In particular, we build on top of that we find particularly suited for scaling.

A growing body of work has focused on the scaling abilities of self-supervised learning in terms of data and model size .

Most of these works use large quantities of uncurated data to train models without supervision.

They show evidence that discriminative methods scale with data, but because of the poor quality of the pretraining data, most of the results are obtained by finetuning the features.

Of particular interest, have also shown that these methods benefit from scaling in model size given enough pretrained data.

This line of work questions the ability of self-supervised methods to work on any data while we focus on producing the best pretrained encoders.

Our dataset construction borrows from the image retrieval community .

In particular, the use of retrieval to augment the training set has been studied in the context of semi-supervised learning .

Similarly, others have used hashtags or other metadata or pretrained vision encoders to filter uncurated datasets.

Unlike these works, we use no pretrained encoders, metadata nor supervision to filter images and leverage visual similarity between images.

Our approach is inspired by text curation pipelines , where a language model is trained on Wikipedia to score texts extracted from an uncurated source.

@src https://arxiv.org/abs/2304.08485
@title Visual Instruction Tuning
@section Related Work

Multimodal Instruction-following Agents.

In computer vision, existing works that build instruction-following agents can be broadly categorized into two classes:

MATH End-to-end trained models, which are separately explored for each specific research topic. For example, the vision-language navigation task and Habitat require the embodied AI agent to follow natural language instructions and take a sequence of actions to complete goals in visual environments. In the image editing domain, given an input image and a written instruction that tells the agent what to do, InstructPix2Pix edits images by following the human instructions.

MATH A system that coordinates various models via LangChain / LLMs , such as

Visual ChatGPT , X-GPT , MM-REACT , VisProg , and ViperGPT . While sharing the same goal in building instruction-following agents, we focus on developing an end-to-end trained language-vision multimodal model for multiple tasks.

Instruction Tuning. In the natural language processing (NLP) community, to enable LLMs such as GPT-3 , T5 , PaLM , and OPT to follow natural language instructions

and complete real-world tasks, researchers have explored methods for LLM instruction-tuning , leading to instruction-tuned counterparts such as InstructGPT /ChatGPT , FLAN-T5 , FLAN-PaLM , and OPT-IML , respectively.

It turns out that this simple approach can effectively improve the zero- and few-shot generalization abilities of LLMs. It is thus natural to borrow the idea from NLP to computer vision. More broadly, the teacher-student distillation ideas with foundation models have been studied in other topics such as image classification . Flamingo can be viewed as the GPT-3 moment in the multimodal domain, due to its strong performance on zero-shot task transfer and in-context-learning. Other LMMs trained on image-text pairs include BLIP-2 , FROMAGe , and KOSMOS-1 .

Based on the recent "best" open-source LLM LLaMA, OpenFlamingo and LLaMA-Adapter are open-source efforts that enable LLaMA to use image inputs, paving the way to build open-source multimodal LLMs.

While these models present promising task transfer generalization performance, they are not explicitly tuned with vision-language instruction data, and their performance in multimodal tasks usually falls short compared to language-only tasks.

In this paper, we aim to fill this gap and study its effectiveness. Finally, note that visual instruction tuning is different from visual prompt tuning : the former aims to improve the model's instruction-following abilities, while the latter aims to improve the parameter-efficiency in model adaptation.

@src https://arxiv.org/abs/2304.10592
@title MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models
@section Related Works

Large language models have experienced tremendous success in recent years due to the scaling up of training data and an increase in the number of parameters. Early models, such as BERT , GPT-2 , and T5 , laid the foundation for this progress. Subsequently, GPT-3 , with a massive scale of 175 billion parameters, was introduced, demonstrating significant breakthroughs across numerous language benchmarks. This development inspired the creation of various other large language models, including Megatron-Turing NLG , Chinchilla , PaLM , OPT , BLOOM , and LLaMA , among others. Wei et al. further discovered several emergent abilities, which appear exclusively in large models. The emergence of these abilities underscores the importance of scaling up in the development of large language models. Moreover, by aligning the pre-trained large language model GPT-3 with human intent, instructions and human feedback, InstructGPT and ChatGPT enable conversational interactions with humans and can answer a wide range of diverse and complex questions. More recently, several open-sourced models, such as Alpaca and Vicuna , have been developed based on LLaMA and also exhibit similar performance.

Leveraging Pre-trained LLMs in Vision-Language Tasks.

In recent years, the trend of using autoregressive language models as decoders in vision-language tasks has gained significant traction . This approach takes advantage of cross-modal transfer, allowing knowledge to be shared between language and multimodal domains. Pioneering studies like VisualGPT and Frozen have demonstrated the benefits of employing a pre-trained language model as a vision-language model decoder. Flamingo was then developed to align a pre-trained vision encoder and language model using gated cross-attention, and was trained on billions of image-text pairs, showcasing impressive in-context few-shot learning capabilities. Following that, BLIP-2 was introduced, employing a Flan-T5 with a Q-Former to efficiently align visual features with the language model. Most recently, PaLM-E , featuring 562 billion parameters, has been developed to integrate real-world continuous sensor modalities into an LLM, thereby establishing a connection between real-world perceptions and human languages. GPT-4 has also been recently released, showcasing more powerful visual understanding and reasoning abilities after pre-training on a vast collection of aligned image-text data.

LLMs, such as ChatGPT, have proven to be powerful tools in enhancing the performance of vision-language tasks by collaborating with other specialized models. For instance, Visual ChatGPT and MM-REACT showcase how ChatGPT can act as a coordinator, integrating with diverse visual foundation models and facilitating their collaboration to tackle more complex challenges. ChatCaptioner treats ChatGPT as a questioner, prompting diverse questions for BLIP-2 to answer. Through multi-round conversations, ChatGPT extracts visual information from BLIP-2 and effectively summarizes the image content. Video ChatCaptioner extends this approach, applying it to video spatiotemporal understanding. ViperGPT demonstrates the potential of combining an LLM with different vision models to address complex visual queries programmatically. In contrast, MiniGPT-4 directly aligns visual information with the language model to accomplish diverse vision-language tasks without the usage of external vision models.

@src https://arxiv.org/abs/2305.10601
@title Tree of Thoughts: Deliberate Problem Solving with Large Language Models
@section Background

We first formalize some existing methods that use large language models for problem-solving, which our approach is inspired by and later compared with.

We use MATH to denote a pre-trained LM with parameters MATH , and lowercase letters MATH to denote a language sequence , i.e.\, MATH where each MATH is a token, so that MATH . We use uppercase letters MATH to denote a collection of language sequences.

Input-output (IO) prompting is the most common way to turn a problem input MATH into output MATH with LM: MATH , where MATH wraps input MATH with task instructions and/or few-shot input-output examples. For simplicity, let us denote MATH , so that IO prompting can be formulated as MATH .

Chain-of-thought (CoT) prompting was proposed to address cases where the mapping of input MATH to output MATH is non-trivial (e.g.\,when MATH is a math question and MATH is the final numerical answer). The key idea is to introduce a chain of thoughts MATH to bridge MATH and MATH , where each MATH is a coherent language sequence that serves as a meaningful intermediate step toward problem solving (e.g.\, MATH could be an intermediate equation for math QA). To solve problems with CoT, each thought MATH is sampled sequentially, then the output MATH . In practice, MATH is sampled as a continuous language sequence, and the decomposition of thoughts (e.g.\,is each MATH a phrase, a sentence, or a paragraph) is left ambiguous.

Self-consistency with CoT (CoT-SC) is an ensemble approach that samples MATH i.i.d.\,chains of thought: MATH , then returns the most frequent output: MATH . CoT-SC improves upon CoT, because there are generally different thought processes for the same problem (e.g.\,different ways to prove the same theorem), and the output decision can be more faithful by exploring a richer set of thoughts. However, within each chain there is no local exploration of different thought steps, and the "most frequent" heuristic only applies when the output space is limited (e.g.\,multi-choice QA).

@src https://arxiv.org/abs/2305.10601
@title Tree of Thoughts: Deliberate Problem Solving with Large Language Models
@section Related Work

Planning and decision making. Smart planning and decision making are critical to achieving predefined goals. As they are trained on vast amount of world knowledge and human examples,

LMs are known to have already absorbed rich commonsense that makes it possible to propose reasonable plans conditioned on problem setting and environmental states . Our proposed ToT approach extends existing planning formulations by considering multiple potentially feasible plans simultaneously at each problem-solving step, and proceeding with the most promising ones. The integration between thought sampling and value feedback organically integrates planning and decision-making mechanisms, enabling effective search inside a solution tree. On the other hand, traditional decision-making procedures usually require training dedicated reward and policy models as in reinforcement learning (for example CHAI ), whereas we use the LM itself to provide the value estimates for decision making.

RAP is a concurrent work that treats language model reasoning as planning with its internal world model, and proposes a MCTS-based method similar to ToT. However, its tasks are simpler than ours, and its framework lacks the modularity to incorporate different tree search algorithms.

Self-reflection. Using LLMs to assess the viability of their own predictions is becoming an increasingly important procedure in problem solving. introduced the "self-reflection" mechanism, in which LMs provide feedback to their generation candidates. improves LMs code generation accuracy by injecting feedback messages generated by the LM itself based on its code execution results. Similarly, also introduces "critic" or review steps over the actions and states, deciding the next action to take in solving computer operation tasks. Another recent work very relevant to ours is "self-eval guided decoding" . Similar to our method, self-eval decoding also follows a tree-search procedure with leaves sampled from stochastic beam search decoding, which are then evaluated by LLM itself with carefully prepared self-eval prompts. Their approach however, uses the PAL formulation which represents thoughts as codes, which makes it difficult to tackle challenging tasks like creative writing which we consider in this paper. Our Tree-of-Thought formulation is thus more versatile and handles challenging tasks on which GPT-4 only achieves very low accuracy with standard prompts.

Program-guided LLM generation. Our proposal is also related to recent advancements that organize LM's behavior with systematic procedures or symbolic program guidance. For example, embeds LMs in an algorithmic search procedure to help solve problems like question answering step-by-step, in which the search trees are expanded by relevant paragraphs that might provide answers. This approach however differs from ours in that trees are expanded by sampling external paragraphs instead of the LM's own thoughts, and there is no reflection or voting steps. Another approach, LLM+P , goes one step further and delegates the actual planning process to a classical planner.

Classical search methods. Last but not least, our approach can be treated as a modern rendition of classical search methods for problem solving. For example it can be considered as a heuristic search algorithm like A* , in which the heuristic at each search node is provided by the LM's self-assessment. From this perspective, our method is also related to NeuroLogic A*esque decoding , which is inspired by A* search but introduces look-ahead heuristics that are efficient for LMs to improve the beam-search or top-k sampling decoding. This method however is constrained to sentence generation tasks, whereas our framework are designed for complex, multi-step problem solving guarded by value feedback.

@src https://arxiv.org/abs/2305.14314
@title QLoRA: Efficient Finetuning of Quantized LLMs
@section Background

Block-wise k-bit Quantization Quantization is the process of discretizing an input from a representation that holds more information to a representation with less information. It often means taking a data type with more bits and converting it to fewer bits, for example from 32-bit floats to 8-bit Integers. To ensure that the entire range of the low-bit data type is used, the input data type is commonly rescaled into the target data type range through normalization by the absolute maximum of the input elements, which are usually structured as a tensor. For example, quantizing a 32-bit Floating Point (FP32) tensor into a Int8 tensor with range MATH :

where MATH is the quantization constant or quantization scale . Dequantization is the inverse:

The problem with this approach is that if a large magnitude value (i.e., an outlier) occurs in the input tensor, then the quantization bins—certain bit combinations—are not utilized well with few or no numbers quantized in some bins. To prevent the outlier issue, a common approach is to chunk the input tensor into blocks that are independently quantized, each with their own quantization constant MATH . This can be formalized as follows: We chunk the input tensor MATH into MATH contiguous blocks of size MATH by flattening the input tensor and slicing the linear segment into MATH blocks. We quantize these blocks independently with Equation 1 to create a quantized tensor and MATH quantization constants MATH .

Low-rank Adapters Low-rank Adapter (LoRA) finetuning is a method that reduces memory requirements by using a small set of trainable parameters, often termed adapters, while not updating the full model parameters which remain fixed. Gradients during stochastic gradient descent are passed through the fixed pretrained model weights to the adapter, which is updated to optimize the loss function. LoRA augments a linear projection through an additional factorized projection. Given a projection MATH with MATH , MATH LoRA computes:

where MATH and MATH , and MATH is a scalar.

Memory Requirement of Parameter-Efficient Finetuning

One important point of discussion is the memory requirement of LoRA during training both in terms of the number and size of adapters used. Since the memory footprint of LoRA is so minimal, we can use more adapters to improve performance without significantly increasing the total memory used.

While LoRA was designed as a Parameter Efficient Finetuning (PEFT) method, most of the memory footprint for LLM finetuning comes from activation gradients and not from the learned LoRA parameters.

For a 7B LLaMA model trained on FLAN v2 with a batch size of 1, with LoRA weights equivalent to commonly used 0.2% of the original model weights , the LoRA input gradients have a memory footprint of 567 MB while the LoRA parameters take up only 26 MB. With gradient checkpointing , the input gradients reduce to an average of 18 MB per sequence making them more memory intensive than all LoRA weights combined. In comparison, the 4-bit base model consumes 5,048 MB of memory.

This highlights that gradient checkpointing is important but also that aggressively reducing the amount of LoRA parameter yields only minor memory benefits. This means we can use more adapters without significantly increasing the overall training memory footprint (see Appendix for a detailed breakdown).

As discussed later, this is crucial for recovering full 16-bit precision performance.

@src https://arxiv.org/abs/2305.14314
@title QLoRA: Efficient Finetuning of Quantized LLMs
@section Related Work

Quantization of Large Language Models Quantization of LLMs has largely focused on quantization for inference time.

Major approaches for preserving 16-bit LLM quality focus on managing outlier features (e.g., SmoothQuant and LLM.int8() ) while others use more sophisticated grouping methods . Lossy quantization approaches study the trade-offs for regular rounding or how to optimize rounding decisions to improve quantization precision . Besides our work, SwitchBack layers is the only work that studies backpropagation through quantized weights at a scale beyond 1B parameters.

Finetuning with Adapters While we use Low-rank Adapters (LoRA), many other Parameter Efficient FineTuning (PEFT) methods have been proposed such as prompt tuning , tuning the embedding layer inputs , tuning hidden states (IA MATH ) , adding full layers , tuning biases , learning a mask over weights based on Fisher information , and a combination of approaches . In our work, we show that LoRA adapters are able to reach full 16-bit finetuning performance. We leave it to future work to explore the tradeoffs of other PEFT approaches.

Instruction Finetuning To help a pretrained LLM follow the instructions provided in a prompt, instruction finetuning uses input-output pairs of various data sources to finetune a pretrained LLM to generate the output given the input as a prompt. Approaches and datasets include MetaICL , MetaTuning , InstructGPT , FLAN , PromptSource , Super-NaturalInstructions , Self-instruct , UnnaturalInstructions , OPT-IML , UnifiedSKG , OIG/Chip2 , Alpaca , Vicuna , Koala , and Self-instruct-GPT-4 .

Chatbots Many instruction following models are structured as dialogue-based chatbots, often using Reinforcement Learning from Human Feedback (RLHF) or generating data from an existing model to train with AI model feedback (RLAIF) . Approaches and datasets include Anthropic-HH , Open Assistant , LaMDA , and Sparrow .

We do not use reinforcement learning, but our best model, Guanaco, is finetuned on multi-turn chat interactions from the Open Assistant dataset which was designed to be used for RLHF training . For the evaluation of chatbots approaches that use GPT-4 instead of costly human annotation have been developed . We improve on such approaches with a focus on an evaluation setup that is more reliable.

@src https://arxiv.org/abs/2305.18290
@title Direct Preference Optimization: Your Language Model is Secretly a Reward Model
@section Related Work

Self-supervised language models of increasing scale learn to complete some tasks zero-shot or with few-shot prompts . However, their performance on downstream tasks and alignment with user intent can be significantly improved by fine-tuning on datasets of instructions and human-written completions . This 'instruction-tuning' procedure

enables LLMs to generalize to instructions outside of the instruction-tuning set and generally increase their usability . Despite the success of instruction tuning, relative human judgments of response quality are often easier to collect than expert demonstrations, and thus subsequent works have fine-tuned LLMs with datasets of human preferences, improving proficiency in translation , summarization , story-telling , and instruction-following . These methods first optimize a neural network reward function for compatibility with the dataset of preferences under a preference model such as the Bradley-Terry model , then fine-tune a language model to maximize the given reward using reinforcement learning algorithms, commonly REINFORCE , proximal policy optimization (PPO; ), or variants . A closely-related line of work leverages LLMs fine-tuned for instruction following with human feedback to generate additional synthetic preference data for targeted attributes such as safety or harmlessness , using only weak supervision from humans in the form of a text rubric for the LLM's annotations. These methods represent a convergence of two bodies of work: one body of work on training language models with reinforcement learning for a variety of objectives and another body of work on general methods for learning from human preferences .

Despite the appeal of using relative human preferences, fine-tuning large language models with reinforcement learning remains a major practical challenge; this work provides a theoretically-justified approach to optimizing relative preferences without RL.

Outside of the context of language, learning policies from preferences has been studied in both bandit and reinforcement learning settings, and several approaches have been proposed. Contextual bandit learning using preferences or rankings of actions, rather than rewards, is known as a contextual dueling bandit (CDB; ). In the absence of absolute rewards, theoretical analysis of CDBs substitutes the notion of an optimal policy with a von Neumann winner, a policy whose expected win rate against any other policy is at least 50% . However, in the CDB setting, preference labels are given online, while in learning from human preferences, we typically learn from a fixed batch of offline preference-annotated action pairs . Similarly, preference-based RL (PbRL) learns from binary preferences generated by an unknown 'scoring' function rather than rewards . Various algorithms for PbRL exist, including methods that can reuse off-policy preference data, but generally involve first explicitly estimating the latent scoring function (i.e. the reward model) and subsequently optimizing it . We instead present a single stage policy learning approach that directly optimizes a policy to satisfy preferences.

@src https://arxiv.org/abs/2307.15818
@title RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control
@section Related Work

There are several categories of Vision-Language Models (VLMs) , with perhaps two most relevant: (1) representation-learning models, e.g. CLIP , which learn common embeddings for both modalities, and (2) visual language models of the form MATH which learn to take vision and language as input and provide free-form text.

Both categories have been used to provide pretraining for a wide variety of applied to downstream applications such as object classification , detection , and segmentation .

In this work, we focus on the latter category .

These models are generally trained on many different tasks, such as image captioning, vision-question answering (VQA), and general language tasks on multiple datasets at the same time.

While prior works study VLMs for a wide range of problems and settings including in robotics, our focus is on how the capabilities of VLMs

can be extended to robotics closed-loop control by endowing them with the ability to predict robot actions, thus leveraging the knowledge already present in VLMs to enable new levels of generalization.

Generalization in robot learning. Developing robotic controllers that can broadly succeed in a variety of scenarios is a long-standing goal in robotics research . A promising approach for enabling generalization in robotic manipulation is by learning from large and diverse datasets . By doing so, prior methods have demonstrated how robots can generalize to novel object instances , to tasks involving novel combinations of objects and skills , to new goals or language instructions , to tasks with novel semantic object categories , and to unseen environments . Unlike most of these prior works, we aim to develop and study a single model that can generalize to unseen conditions along all of these axes. A key ingredient of our approach is to leverage pre-trained models that have been exposed to data that is much broader than the data seen by the robot.

Pre-training for robotic manipulation. Pre-training has a long history in robotic learning. Most works focus on pre-trained visual representations that can be used to initialize the encoder of the robot's camera observations, either via supervised ImageNet classification , data augmentation or objectives that are tailored towards robotic control . Other works have incorporated pre-trained language models, often either as an instruction encoder or for high-level planning . Rather than using pre-training vision models or pre-trained language models, we specifically consider the use of pre-trained vision-language models (VLMs), which provide rich, grounded knowledge about the world. Prior works have studied the use of VLMs for robotics , and form part of the inspiration for this work. These prior approaches use VLMs for visual state representations , for identifying objects , for high-level planning , or for providing supervision or success detection . While CLIPort and MOO integrate pre-trained VLMs into end-to-end visuomotor manipulation policies, both incorporate significant structure into the policy that limits their applicability. Notably, our work does not rely on a restricted 2D action space and does not require a calibrated camera.

Moreover, a critical distinction is that, unlike these works, we leverage VLMs that generate language, and the unified output space of our formulation enables model weights to be entirely shared across language and action tasks, without introducing action-only model layer components.

@src https://arxiv.org/abs/2310.06770
@title SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
@section Related Work

Several recent works for evaluating LMs have either proposed a collection of mutually distinct tasks spanning across multiple domains or turned to the web as an interactive setting featuring tasks that require multiple steps to solve .

There are several drawbacks with such a "potpourri" style setup.

First, each task tends to narrowly focus on one or a few skills, resulting in challenges that are typically too simple, pigeonhole the model into a reduced role, and do not provide models with the bandwidth to exercise their versatility or potentially demonstrate new abilities .

Consequently, a model's performance on such task conglomerations may not yield actionable, deep insights regarding its capabilities and how to improve them .

addresses these shortcomings, as our work demonstrates that it is significantly challenging, presents a wide range of possibilities for improving LMs to solve this task, and is easy to refresh over time with new task instances, each of which introduce novel, nuanced, and practical challenges.

HumanEval is the current standard in a long-standing pursuit of synthesizing code from natural language descriptions .

In the past year, subsequent benchmarks have sought to augment HumanEval with extensions to different languages , variations in edit scope , similar but novel code completion tasks , and more testing .

Simultaneously, separate works have sought to introduce new coding paradigms or design library-specific problems .

Instead of partitioning problems into siloed datasets and curtailing them for simplicity's sake, 's collection procedure transforms the source code with minimal post-processing, preserving a much broader set of challenges grounded in real-world software engineering beyond closed form completion, such as patch generation, reasoning over long contexts, navigating a codebase directory, and capturing dependency-based relationships across modules.

To overcome traditional program analysis techniques that may not scale or incorporate natural language, one direction of current software engineering research is to use neural networks, including LMs, to automate real-world software development processes .

Use cases include automating commit generation , PR review , bug localization , testing , and program repair .

Most relevant to are works that have sought to apply LMs towards automated program repair , guiding code editing with commits .

However, none of the existing datasets present code context at the scale of .

Moreover, can be easily extended to new programming languages and repositories, and it provides a significantly more realistic and challenging arena to carry out experiments towards augmenting LMs with software engineering tools and practices.

@src https://arxiv.org/abs/2310.11511
@title Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection
@section Related Work

Retrieval-Augmented Generation (RAG) augments the input space of LMs with retrieved text passages , leading to large improvements in knowledge-intensive tasks after fine-tuning or used with off-the-shelf LMs .

A more recent work instruction-tunes an LM with a fixed number of retrieved passages prepended to input, or pre-train a retriever and LM jointly, followed by few-shot fine-tuning on task datasets .

While prior work often retrieves only once at the beginning, propose to

adaptively retrieve passages for generation on top of a proprietary LLM or train an LM to generate API calls for named entities.

Yet, the improved task performance of such approaches often comes at the expense of runtime efficiency , robustness to irrelevant context , and lack of attributions .

We introduce a method to train an arbitrary LM to learn to use retrieval on-demand for diverse instruction-following queries and introduce controlled generation guided by reflections tokens to further improve generation quality and attributions.

A few concurrent works (All work is arXived within a week of this preprint. on RAG propose new training or prompting strategies to improve widely-adopted RAG approaches.

fine-tune both the retriever and LM on instruction-tuning datasets in two steps.

While we also train our model on diverse instruction-following datasets, enables retrieval on demand and selection of the best possible model output via fine-grained self-reflection, making it widely applicable and more robust and controllable.

use a natural language inference model and use a summarization model to filter out or compress retrieved passages before using them to prompt the LM to generate the output.

processes passages in parallel and filters out irrelevant ones through self-reflection, without relying on external models at inference. Moreover, our self-reflection mechanism also evaluates other aspects of the model output quality including factuality.

LATS prompt off-the-shelf LMs to search for relevant information for question answering tasks and to generate with tree search, guided by LM-generated value scores.

While their value function simply indicates an overall score of each generation, trains to an arbitrary LM to learn to generate fine-grained self-reflection and customizable inference.

Training LLMs with reinforcement learning (e.g., Proximal Policy Optimization or PPO; ) from human feedback (RLHF) has proven effective in aligning LLMs with human preferences .

introduce fine-grained RLHF with multiple reward models.

Though our work also studies fine-grained critique on retrieval and generation, we train our target LM on task examples augmented with reflection tokens from a critic

model offline, with a far lower training cost compared to RLHF. In addition, reflection tokens in enable controllable generation at inference, while RLHF focuses on human preference alignment during training.

Other works use general control tokens to guide LM generation , while uses reflection tokens to decide the need for retrieval and to self-evaluate generation quality.

propose a self-evaluation-guided decoding framework, but they focus only on reasoning tasks with one evaluation dimension (reasoning path consistency) and without retrieval.

Recent work on LLM refinement prompts a model to generate task output, natural language feedback and refined task output iteratively, but at the cost of inference efficiency.

@src https://arxiv.org/abs/2402.13753
@title LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens
@section Related Works

In addition to methods based on position interpolation, this section discusses related works of other approaches.

-based approaches use an external memory module to memorize long past context and retrieval modules for related documents fetching at inference . These designs typically need explicit modifications on the LLM architectures. Our work, in contrast, is more lightweight, with minor positional embedding modifications. We can also handle more long context tasks beyond retrieval, such as long document summarization and few-shot learning.

-based context window extensions. Beyond positional embedding interpolation, some research achieves input context extension using the original LLM context window length by manipulating attention mechanisms . The key idea is to mitigate the attention explosion issue caused by new positions using novel attention masks.

These efforts and positional interpolation methods are complementary.

-tuning based approaches focus on how to effectively fine-tune pre-trained LLMs with modified position embeddings for longer context. Works like Code LLaMA , LLaMA2 Long and ScaledRoPE choose a very large base value for RoPE and fine-tune on the target length. Our method offers flexibility for various target lengths and can achieve beyond 2M length. More recently, as fine-tuning for long context lengths (i.e., over 128k) demands substantial GPU resources, LongLoRA and PoSE are proposed to mitigate this overhead.

Our method is orthogonal to these efficient fine-tuning works.

@src https://arxiv.org/abs/2408.00714
@title SAM 2: Segment Anything in Images and Videos
@section Related work

Image segmentation. Segment Anything introduces a promptable image segmentation task where the goal is to output a valid segmentation mask given an input prompt such as a bounding box or a point that refers to the object of interest. SAM trained on the SA-1B dataset allows for zero-shot segmentation which enabled its adoption to a wide range of applications. Recent work has extended SAM, e.g., by introducing a High-Quality output token to train on fine-grained masks , or improve SAM's efficiency . More broadly, SAM is used in a wide range of applications, including medical imaging , remote sensing , motion segmentation , and camouflaged object detection .

Interactive Video Object Segmentation (iVOS). Interactive video object segmentation has emerged as a crucial task to efficiently obtain object segmentations in videos (masklets) with user guidance, often in the form of scribbles, clicks, or bounding boxes. A few early approaches deploy graph-based optimization to guide the segmentation annotation process. More recent approaches often adopt a modular design, converting user inputs into a mask representation on a single frame and then propagating it to other frames.

Click-based input is easier to collect for interactive video segmentation.

Recent works have used a combination of SAM on images with video trackers based on masks or points . However, these approaches have limitations: the tracker may not work for all objects, SAM may not perform well on video frames, and there is no mechanism to interactively refine a model's mistakes, other than re-annotating using SAM in each frame and restarting the tracking from there.

Our work shares a similar goal to these works to segment objects across videos interactively, and we build a strong unified model that directly takes prompts for interactive video segmentation, along with a large and diverse dataset in pursuit of solving this goal.

Video Object Segmentation (VOS). The VOS task begins with an object mask as input in the first frame, which must be accurately tracked throughout the video . The task is referred to as "semi-supervised VOS" since the input mask can be seen as supervision signal of the object which is available only in the first frame. This task has drawn significant attention due to its relevance in applications, including video editing or robotics.

Early deep learning based approaches have often used online fine-tuning on the first video frame or on all frames to adapt the model to the target object.

Faster inference has been achieved with offline-trained models, conditioned either only on the first frame , or also integrating the previous frame . This multi-conditioning has been extended to all frames with RNNs and transformers .

Semi-supervised VOS can be seen as a special case of our Promptable Visual Segmentation (PVS) task, with only a mask prompt in the first video frame. Notably, annotating the required high-quality object mask in the first frame in VOS is practically challenging and time-consuming for inference.

Video segmentation datasets. Many datasets have been proposed to support the VOS task. Early VOS datasets , such as DAVIS , include high-quality annotations but their size limits deep-learning based approaches. YouTube-VOS is the first large-scale dataset for VOS. As algorithms became better and benchmark performance started to saturate, researchers have looked at increasing the difficulty of the VOS task by specifically focusing on occlusions , long videos , extreme transformations , object diversity or scene diversity .

We find that current video segmentation datasets lack sufficient coverage to achieve the capability of "segmenting anything in videos". Their annotations typically cover entire objects (not parts) and datasets are often centered around specific object classes, such as people, vehicles, and animals. In comparison to these datasets, our released SA-V dataset not only focuses on whole objects but also extensively covers object parts and contains over an order of magnitude more masks.

@src https://arxiv.org/abs/2408.06072
@title CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer
@section Related works

Generating videos has been explored through various types of generative models, such as Generative Adversarial Networks (GANs) , autoregressive methods , and non-autoregressive methods . Diffusion models have recently gained significant attention, achieving remarkable results in both image generation and video generation . However, the limited compression ratio and simple training strategy often restrict the generation to low-resolution short-duration videos (2-3 seconds), requiring multiple super-resolution and frame interpolation models to be cascaded for a generation. This leads to generated videos with limited semantic information and minimal motion.

Video VAEs To increase the compression ratio of videos and reduce computation costs, a common approach is to encode the video into a latent space using a Variational Autoencoder(VAE), which is also widely used in image generation. Early video models usually directly use image VAE for generation. However, modeling only the space dimension can result in jittery videos. SVD tries to finetune the image VAE decoder to solve the jittering issue. However, this approach cannot take advantage of the temporal redundancy in videos and still cannot achieve an optimal compression rate. Recently, some video models try to use 3D VAE for temporal compression, but small latent channels still result in blurry and jittery videos.

@src https://arxiv.org/abs/2410.18072
@title WorldSimBench: Towards Video Generation Models as World Simulators
@section Related Work

Predictive models are capable of generating process representations that map the current state to future states by incorporating current state representations and control over future trends.

, built on LLMs and MLLMs , generate future predictions in the text modality by accepting current state representations and text instructions.

These models have demonstrated impressive performance in high-level planning tasks for embodied agents .

Similarly, image generation models as can produce future goal images, showcasing strong capabilities during the decision-making phase of embodied agents.

, based on video generation models , have made some progress in embodied control.

However, due to limitations in data or models, the generated videos often lack essential physical representations and logical consistency, restricting their applicability to fixed scenarios and single tasks.

With the advancement of diffusion transformer and the extensive utilization of large-scale internet video datasets , certain models, also known as World Simulators, have achieved more precise representations of physical laws and 3D environments.

Evaluation of Predictive Models. With the advancement of predictive models, research has also expanded to evaluate the capabilities of models at different stages.

conducted text-level and task completion evaluations for at the MATH stage.

performed score-based evaluations from an aesthetic perspective for at the MATH stage.

also assessed the aesthetic quality of videos generated by at the MATH stage.

We take the first step in evaluating World Simulators through an embodied perspective.
