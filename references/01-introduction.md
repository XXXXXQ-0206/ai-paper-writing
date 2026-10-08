# introduction corpus (68 sources)

@src https://arxiv.org/abs/1706.03762
@title Attention Is All You Need
@section Introduction

Provided proper attribution is provided, Google hereby grants permission to reproduce the tables and figures in this paper solely for use in journalistic or scholarly works.

The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.

Recurrent neural networks, long short-term memory and gated recurrent neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction problems such as language modeling and machine translation . Numerous efforts have since continued to push the boundaries of recurrent language models and encoder-decoder architectures .

Recurrent models typically factor computation along the symbol positions of the input and output sequences. Aligning the positions to steps in computation time, they generate a sequence of hidden states MATH , as a function of the previous hidden state MATH and the input for position MATH . This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples.

Recent work has achieved significant improvements in computational efficiency through factorization tricks and conditional computation , while also improving model performance in case of the latter. The fundamental constraint of sequential computation, however, remains.

Attention mechanisms have become an integral part of compelling sequence modeling and transduction models in various tasks, allowing modeling of dependencies without regard to their distance in the input or output sequences . In all but a few cases , however, such attention mechanisms are used in conjunction with a recurrent network.

In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output. The Transformer allows for significantly more parallelization and can reach a new state of the art in translation quality after being trained for as little as twelve hours on eight P100 GPUs.

@src https://arxiv.org/abs/1804.07461
@title GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding
@section Introduction

For natural language understanding (NLU) technology to be maximally useful, it must be able to process language in a way that is not exclusive to a single task, genre, or dataset.

In pursuit of this objective, we introduce the General Language Understanding Evaluation (GLUE) benchmark, a collection of tools for evaluating the performance of models across a diverse set of existing NLU tasks.

By including tasks with limited training data, GLUE is designed to favor and encourage models that share general linguistic knowledge across tasks.

GLUE also includes a hand-crafted diagnostic test suite that enables detailed linguistic analysis of models.

We evaluate baselines based on current methods for transfer and representation learning and find that multi-task training on all tasks performs better than training a separate model per task. However, the low absolute performance of our best model indicates the need for improved general NLU systems.

The human ability to understand language is general, flexible, and robust.

In contrast, most NLU models above the word level are designed for a specific task and struggle with out-of-domain data.

If we aspire to develop models with understanding beyond the detection of superficial correspondences between inputs and outputs,

then it is critical to develop a more unified model that can learn to execute a range of different linguistic tasks in different domains.

To facilitate research in this direction, we present the General Language Understanding Evaluation

benchmark: a collection of NLU tasks including question answering, sentiment analysis, and textual entailment, and an associated online platform for model evaluation, comparison, and analysis.

GLUE does not place any constraints on model architecture beyond the ability to process single-sentence and sentence-pair inputs and to make corresponding predictions.

For some GLUE tasks, training data is plentiful, but for others it is limited or fails to match the genre of the test set. GLUE therefore favors models that can learn to represent linguistic knowledge in a way that facilitates sample-efficient learning and effective knowledge-transfer across tasks.

None of the datasets in GLUE were created from scratch for the benchmark; we rely on preexisting datasets because they have been implicitly agreed upon by the NLP community as challenging and interesting.

Four of the datasets feature privately-held test data, which will be used to ensure that the benchmark is used fairly. (To evaluate on the private test data, users of the benchmark must submit to gluebenchmark.com gluebenchmark.com

To understand the types of knowledge learned by models and to encourage linguistic-meaningful solution strategies, GLUE also includes a set of hand-crafted analysis examples for probing trained models.

This dataset is designed to highlight common challenges, such as the use of world knowledge and logical operators, that we expect models must handle to robustly solve the tasks.

To better understand the challenged posed by GLUE, we conduct experiments with simple baselines and state-of-the-art sentence representation models.

We find that unified multi-task trained models slightly outperform comparable models trained on each task separately.

Our best multi-task model makes use of ELMo ,

a recently proposed pre-training technique.

However, this model still achieves a fairly low absolute score.

Analysis with our diagnostic dataset reveals that our baseline models deal well with strong lexical signals but struggle with deeper logical structure.

In summary, we offer: (i) A suite of nine sentence or sentence-pair NLU tasks, built on established annotated datasets and selected to cover a diverse range of text genres, dataset sizes, and degrees of difficulty. (ii) An online evaluation platform and leaderboard, based primarily on privately-held test data. The platform is model-agnostic, and can evaluate any method capable of producing results on all nine tasks. (iii) An expert-constructed diagnostic evaluation dataset. (iv) Baseline results for several major existing approaches to sentence representation learning.

@src https://arxiv.org/abs/1810.04805
@title BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
@section Introduction

We introduce a new language representation model called , which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models , is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task-specific architecture modifications.

is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement) and SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement).

Language model pre-training has been shown to be effective for improving many natural language processing tasks . These include sentence-level tasks such as natural language inference and paraphrasing , which aim to predict the relationships between sentences by analyzing them holistically, as well as token-level tasks such as named entity recognition and question answering, where models are required to produce fine-grained output at the token level .

There are two existing strategies for applying pre-trained language representations to downstream tasks: feature-based and fine-tuning . The feature-based approach, such as ELMo , uses task-specific architectures that include the pre-trained representations as additional features. The fine-tuning approach, such as the Generative Pre-trained Transformer (OpenAI GPT) , introduces minimal task-specific parameters, and is trained on the downstream tasks by simply fine-tuning all pre-trained parameters. The two approaches share the same objective function during pre-training, where they use unidirectional language models to learn general language representations.

We argue that current techniques restrict the power of the pre-trained representations, especially for the fine-tuning approaches. The major limitation is that standard language models are unidirectional, and this limits the choice of architectures that can be used during pre-training. For example, in OpenAI GPT, the authors use a left-to-right architecture, where every token can only attend to previous tokens in the self-attention layers of the Transformer . Such restrictions are sub-optimal for sentence-level tasks, and could be very harmful when applying fine-tuning based approaches to token-level tasks such as question answering, where it is crucial to incorporate context from both directions.

In this paper, we improve the fine-tuning based approaches by proposing : Bidirectional Encoder Representations from Transformers. alleviates the previously mentioned unidirectionality constraint by using a "masked language model" (MLM) pre-training objective, inspired by the Cloze task . The masked language model randomly masks some of the tokens from the input, and the objective is to predict the original vocabulary id of the masked word based only on its context. Unlike left-to-right language model pre-training, the MLM objective enables the representation to fuse the left and the right context, which allows us to pre-train a deep bidirectional Transformer. In addition to the masked language model, we also use a "next sentence prediction" task that jointly pre-trains text-pair representations. The contributions of our paper are as follows:

We demonstrate the importance of bidirectional pre-training for language representations. Unlike , which uses unidirectional language models for pre-training, uses masked language models to enable pre-trained deep bidirectional representations. This is also in contrast to , which uses a shallow concatenation of independently trained left-to-right and right-to-left LMs.

We show that pre-trained representations reduce the need for many heavily-engineered task-specific architectures. is the first fine-tuning based representation model that achieves state-of-the-art performance on a large suite of sentence-level and token-level tasks, outperforming many task-specific architectures.

advances the state of the art for eleven NLP tasks.

The code and pre-trained models are available at https://github.com/google-research/bert.

@src https://arxiv.org/abs/1906.08237
@title XLNet: Generalized Autoregressive Pretraining for Language Understanding
@section Introduction

Equal contribution. Order determined by swapping the one in .

With the capability of modeling bidirectional contexts, denoising autoencoding based pretraining like BERT achieves better performance than pretraining approaches based on autoregressive language modeling.

However, relying on corrupting the input with masks, BERT neglects dependency between the masked positions and suffers from a pretrain-finetune discrepancy.

In light of these pros and cons, we propose XLNet, a generalized autoregressive pretraining method that (1) enables learning bidirectional contexts by maximizing the expected likelihood over all permutations of the factorization order and (2) overcomes the limitations of BERT thanks to its autoregressive formulation.

Furthermore, XLNet integrates ideas from Transformer-XL, the state-of-the-art autoregressive model, into pretraining.

Empirically, under comparable experiment settings, XLNet outperforms BERT on 20 tasks, often by a large margin, including question answering, natural language inference, sentiment analysis, and document ranking. (Pretrained models and code are available at https://github.com/zihangdai/xlnet .

Unsupervised representation learning has been highly successful in the domain of natural language processing .

Typically, these methods first pretrain neural networks on large-scale unlabeled text corpora, and then finetune the models or representations on downstream tasks.

Under this shared high-level idea, different unsupervised pretraining objectives have been explored in literature.

Among them, autoregressive (AR) language modeling and autoencoding (AE) have been the two most successful pretraining objectives.

AR language modeling seeks to estimate the probability distribution of a text corpus with an autoregressive model .

Specifically, given a text sequence MATH , AR language modeling factorizes the likelihood into a forward product MATH or a backward one MATH .

A parametric model (e.g. a neural network) is trained to model each conditional distribution.

Since an AR language model is only trained to encode a uni-directional context (either forward or backward), it is not effective at modeling deep bidirectional contexts.

On the contrary, downstream language understanding tasks often require bidirectional context information. This results in a gap between AR language modeling and effective pretraining.

In comparison, AE based pretraining does not perform explicit density estimation but instead aims to reconstruct the original data from corrupted input.

A notable example is BERT , which has been the state-of-the-art pretraining approach.

Given the input token sequence, a certain portion of tokens are replaced by a special symbol [MASK], and the model is trained to recover the original tokens from the corrupted version.

Since density estimation is not part of the objective, BERT is allowed to utilize bidirectional contexts for reconstruction.

As an immediate benefit, this closes the aforementioned bidirectional information gap in AR language modeling, leading to improved performance.

However, the artificial symbols like [MASK] used by BERT during pretraining are absent from real data at finetuning time, resulting in a pretrain-finetune discrepancy.

Moreover, since the predicted tokens are masked in the input, BERT is not able to model the joint probability using the product rule as in AR language modeling. In other words, BERT assumes the predicted tokens are independent of each other given the unmasked tokens, which is oversimplified as high-order, long-range dependency is prevalent in natural language .

Faced with the pros and cons of existing language pretraining objectives, in this work, we propose XLNet, a generalized autoregressive method that leverages the best of both AR language modeling and AE while avoiding their limitations.

itemize [leftmargin=*,topsep=0em,itemsep=0em,parsep=0.2em]

Firstly, instead of using a fixed forward or backward factorization order as in conventional AR models, XLNet maximizes the expected log likelihood of a sequence w.r.t. all possible permutations of the factorization order.

Thanks to the permutation operation, the context for each position can consist of tokens from both left and right.

In expectation, each position learns to utilize contextual information from all positions, i.e., capturing bidirectional context.

Secondly, as a generalized AR language model, XLNet does not rely on data corruption.

Hence, XLNet does not suffer from the pretrain-finetune discrepancy that BERT is subject to.

Meanwhile, the autoregressive objective also provides a natural way to use the product rule for factorizing the joint probability of the predicted tokens, eliminating the independence assumption made in BERT.

In addition to a novel pretraining objective, XLNet improves architectural designs for pretraining.

itemize [leftmargin=*,topsep=0em,itemsep=0em,parsep=0.2em]

Inspired by the latest advancements in AR language modeling, XLNet integrates the segment recurrence mechanism and relative encoding scheme of Transformer-XL into pretraining, which empirically improves the performance especially for tasks involving a longer text sequence.

Naively applying a Transformer(-XL) architecture to permutation-based language modeling does not work because the factorization order is arbitrary and the target is ambiguous. As a solution, we propose to reparameterize the Transformer(-XL) network to remove the ambiguity.

Empirically, under comparable experiment setting, XLNet consistently outperforms BERT on a wide spectrum of problems including GLUE language understanding tasks, reading comprehension tasks like SQuAD and RACE, text classification tasks such as Yelp and IMDB, and the ClueWeb09-B document ranking task.

Related Work The idea of permutation-based AR modeling has been explored in , but there are several key differences.

Firstly, previous models aim to improve density estimation by baking an "orderless" inductive bias into the model while XLNet is motivated by enabling AR language models to learn bidirectional contexts.

Technically, to construct a valid target-aware prediction distribution, XLNet incorporates the target position into the hidden state via two-stream attention while previous permutation-based AR models relied on implicit position awareness inherent to their MLP architectures.

Finally, for both orderless NADE and XLNet, we would like to emphasize that "orderless" does not mean that the input sequence can be randomly permuted but that the model allows for different factorization orders of the distribution.

Another related idea is to perform autoregressive denoising in the context of text generation , which only considers a fixed order though.

@src https://arxiv.org/abs/1907.11692
@title RoBERTa: A Robustly Optimized BERT Pretraining Approach
@section Introduction

Language model pretraining has led to significant performance gains but careful comparison between different approaches is challenging.

Training is computationally expensive, often done on private datasets of different sizes, and, as we will show, hyperparameter choices have significant impact on the final results.

We present a replication study of BERT pretraining that carefully measures the impact of many key hyperparameters and training data size. We find that BERT was significantly undertrained, and can match or exceed the performance of every model published after it. Our best model achieves state-of-the-art results on GLUE, RACE and SQuAD.

These results highlight the importance of previously overlooked design choices, and raise questions about the source of recently reported improvements. We release our models and code. (Our models and code are available at:

Self-training methods such as ELMo , GPT , BERT , XLM , and XLNet have brought significant performance gains, but it can be challenging to determine which aspects of the methods contribute the most.

Training is computationally expensive, limiting the amount of tuning that can be done, and is often done with private training data of varying sizes, limiting our ability to measure the effects of the modeling advances.

We present a replication study of BERT pretraining , which includes a careful evaluation of the effects of hyperparmeter tuning and training set size.

We find that BERT was significantly undertrained and propose an improved recipe for training BERT models, which we call , that can match or exceed the performance of all of the post-BERT methods.

Our modifications are simple, they include: (1) training the model longer, with bigger batches, over more data; (2) removing the next sentence prediction objective; (3) training on longer sequences; and (4) dynamically changing the masking pattern applied to the training data. We also collect a large new dataset (CC-News) of comparable size to other privately used datasets, to better control for training set size effects.

When controlling for training data, our improved training procedure improves upon the published BERT results on both GLUE and SQuAD.

When trained for longer over additional data, our model achieves a score of 88.5 on the public GLUE leaderboard, matching the 88.4 reported by yang2019xlnet .

Our model establishes a new state-of-the-art on 4/9 of the GLUE tasks: MNLI, QNLI, RTE and STS-B.

We also match state-of-the-art results on SQuAD and RACE.

Overall, we re-establish that BERT's masked language model training objective is competitive with other recently proposed training objectives such as perturbed autoregressive language modeling . (It is possible that these other methods could also improve with more tuning. We leave this exploration to future work.

In summary, the contributions of this paper are: (1) We present a set of important BERT design choices and training strategies and introduce alternatives that lead to better downstream task performance; (2) We use a novel dataset, CC-News, and confirm that using more data for pretraining further improves performance on downstream tasks; (3) Our training improvements show that masked language model pretraining, under the right design choices, is competitive with all other recently published methods. We release our model, pretraining and fine-tuning code implemented in PyTorch .

@src https://arxiv.org/abs/1909.11942
@title ALBERT: A Lite BERT for Self-supervised Learning of Language Representations
@section Introduction

Increasing model size when pretraining natural language representations often results in improved performance on downstream tasks. However, at some point further model increases become harder due to GPU/TPU memory limitations and longer training times. To address these problems, we present two parameter-reduction techniques to lower memory consumption and increase the training speed of BERT . Comprehensive empirical evidence shows that our proposed methods lead to models that scale much better compared to the original BERT. We also use a self-supervised loss that focuses on modeling inter-sentence coherence, and show it consistently helps downstream tasks with multi-sentence inputs. As a result, our best model establishes new state-of-the-art results on the GLUE, RACE, and benchmarks while having fewer parameters compared to BERT-large. The code and the pretrained models are available at https://github.com/google-research/ALBERT.

Full network pre-training has led to a series of breakthroughs in language representation learning. Many nontrivial NLP tasks, including those that have limited training data, have greatly benefited from these pre-trained models. One of the most compelling signs of these breakthroughs is the evolution of machine performance on a reading comprehension task designed for middle and high-school English exams in China, the RACE test : the paper that originally describes the task and formulates the modeling challenge reports then state-of-the-art machine accuracy at MATH ; the latest published result reports their model performance at MATH ; the work we present here pushes it even higher to MATH , a stunning MATH improvement that is mainly attributable to our current ability to build high-performance pretrained language representations.

Evidence from these improvements reveals that a large network is of crucial importance for achieving state-of-the-art performance . It has become common practice to pre-train large models and distill them down to smaller ones for real applications. Given the importance of model size, we ask: Is having better NLP models as easy as having larger models?

An obstacle to answering this question is the memory limitations of available hardware.

Given that current state-of-the-art models often have hundreds of millions or even billions of parameters, it is easy to hit these limitations as we try to scale our models.

Training speed can also be significantly hampered in distributed training, as the communication overhead is directly proportional to the number of parameters in the model.

Existing solutions to the aforementioned problems include model parallelization and clever memory management .

These solutions address the memory limitation problem, but not the communication overhead.

In this paper, we address all of the aforementioned problems, by designing A Lite BERT (ALBERT) architecture that has significantly fewer parameters than a traditional BERT architecture.

ALBERT incorporates two parameter reduction techniques that lift the major obstacles in scaling pre-trained models.

The first one is a factorized embedding parameterization.

By decomposing the large vocabulary embedding matrix into two small matrices, we separate the size of the hidden layers from the size of vocabulary embedding.

This separation makes it easier to grow the hidden size without significantly increasing the parameter size of the vocabulary embeddings.

The second technique is cross-layer parameter sharing.

This technique prevents the parameter from growing with the depth of the network.

Both techniques significantly reduce the number of parameters for BERT without seriously hurting performance, thus improving parameter-efficiency.

An ALBERT configuration similar to BERT-large has 18x fewer parameters and can be trained about 1.7x faster.

The parameter reduction techniques also act as a form of regularization that stabilizes the training and helps with generalization.

To further improve the performance of ALBERT, we also introduce a self-supervised loss for sentence-order prediction (SOP). SOP primary focuses on inter-sentence coherence and is designed to address the ineffectiveness of the next sentence prediction (NSP) loss proposed in the original .

As a result of these design decisions, we are able to scale up to much larger ALBERT configurations that still have fewer parameters than BERT-large but achieve significantly better performance.

We establish new state-of-the-art results on the well-known GLUE, SQuAD, and RACE benchmarks for natural language understanding.

Specifically, we push the RACE accuracy to MATH , the GLUE benchmark to 89.4, and the F1 score of SQuAD 2.0 to 92.2.

@src https://arxiv.org/abs/1910.10683
@title Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer
@section Introduction

Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer

Colin Raffel Equal contribution. A description of each author's contribution is available in sec:contributions . Correspondence to craffel@gmail.com. craffel@gmail.com

Katherine Lee MATH katherinelee@google.com

Transfer learning, where a model is first pre-trained on a data-rich task before being fine-tuned on a downstream task, has emerged as a powerful technique in natural language processing (NLP).

The effectiveness of transfer learning has given rise to a diversity of approaches, methodology, and practice.

In this paper, we explore the landscape of transfer learning techniques for NLP by introducing a unified framework that converts all text-based language problems into a text-to-text format.

Our systematic study compares pre-training objectives, architectures, unlabeled data sets, transfer approaches, and other factors on dozens of language understanding tasks.

By combining the insights from our exploration with scale and our new "Colossal Clean Crawled Corpus", we achieve state-of-the-art results on many benchmarks covering summarization, question answering, text classification, and more.

To facilitate future work on transfer learning for NLP, we release our data set, pre-trained models, and code. ( https://github.com/google-research/text-to-text-transfer-transformer

transfer learning, natural language processing, multi-task learning, attention-based models, deep learning

Training a machine learning model to perform natural language processing (NLP) tasks often requires that the model can process text in a way that is amenable to downstream learning.

This can be loosely viewed as developing general-purpose knowledge that allows the model to "understand" text.

This knowledge can range from low-level (e.g.\ the spelling or meaning of words) to high-level (e.g.\ that a tuba is too large to fit in most backpacks).

In modern machine learning practice, providing this knowledge is rarely done explicitly; instead, it is often learned as part of an auxiliary task.

For example, a historically common approach is to use word vectors to map word identities to a continuous representation where, ideally, similar words map to similar vectors.

These vectors are often learned through an objective that, for example, encourages co-occurring words to be positioned nearby in the continuous space .

Recently, it has become increasingly common to pre-train the entire model on a data-rich task.

Ideally, this pre-training causes the model to develop general-purpose abilities and knowledge that can then be transferred to downstream tasks.

In applications of transfer learning to computer vision , pre-training is typically done via supervised learning on a large labeled data set like ImageNet .

In contrast, modern techniques for transfer learning in NLP often pre-train using unsupervised learning on unlabeled data.

This approach has recently been used to obtain state-of-the-art results in many of the most common NLP benchmarks .

Beyond its empirical strength, unsupervised pre-training for NLP is particularly attractive because unlabeled text data is available en masse thanks to the Internet—for example, the Common Crawl project (http://commoncrawl.org produces about 20TB of text data extracted from web pages each month.

This is a natural fit for neural networks, which have been shown to exhibit remarkable scalability, i.e.\ it is often possible to achieve better performance simply by training a larger model on a larger data set .

This synergy has resulted in a great deal of recent work developing transfer learning methodology for NLP, which has produced a wide landscape of pre-training objectives , unlabeled data sets , benchmarks , fine-tuning methods , and more.

The rapid rate of progress and diversity of techniques in this burgeoning field can make it difficult to compare different algorithms, tease apart the effects of new contributions, and understand the space of existing methods for transfer learning.

Motivated by a need for more rigorous understanding, we leverage a unified approach to transfer learning that allows us to systematically study different approaches and push the current limits of the field.

The basic idea underlying our work is to treat every text processing problem as a "text-to-text" problem, i.e.\ taking text as input and producing new text as output.

This approach is inspired by previous unifying frameworks for NLP tasks, including casting all text problems as question answering , language modeling , or span extraction tasks.

Crucially, the text-to-text framework allows us to directly apply the same model, objective, training procedure, and decoding process to every task we consider.

We leverage this flexibility by evaluating performance on a wide variety of English-based NLP problems, including question answering, document summarization, and sentiment classification, to name a few.

With this unified approach, we can compare the effectiveness of different transfer learning objectives, unlabeled data sets, and other factors, while exploring the limits of transfer learning for NLP by scaling up models and data sets beyond what has previously been considered.

We emphasize that our goal is not to propose new methods but instead to provide a comprehensive perspective on where the field stands.

As such, our work primarily comprises a survey, exploration, and empirical comparison of existing techniques.

We also explore the limits of current approaches by scaling up the insights from our systematic study (training models up to MATH billion parameters) to obtain state-of-the-art results in many of the tasks we consider.

In order to perform experiments at this scale, we introduce the "Colossal Clean Crawled Corpus" (C4), a data set consisting of hundreds of gigabytes of clean English text scraped from the web.

Recognizing that the main utility of transfer learning is the possibility of leveraging pre-trained models in data-scarce settings, we release our code, data sets, and pre-trained models. fn:oss

The remainder of the paper is structured as follows:

In the following section, we discuss our base model and its implementation, our procedure for formulating every text processing problem as a text-to-text task, and the suite of tasks we consider.

In sec:experiments , we present a large set of experiments that explore the field of transfer learning for NLP.

At the end of the section ( sec:together ), we combine insights from our systematic study to obtain state-of-the-art results on a wide variety of benchmarks.

Finally, we provide a summary of our results and wrap up with a look towards the future in sec:conclusion .

@src https://arxiv.org/abs/1910.13461
@title BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension
@section Introduction

We present BART, a denoising autoencoder for pretraining sequence-to-sequence models. BART is trained by (1) corrupting text with an arbitrary noising function, and (2) learning a model to reconstruct the original text. It uses a standard Tranformer-based neural machine translation architecture which, despite its simplicity, can be seen as generalizing BERT (due to the bidirectional encoder), GPT (with the left-to-right decoder), and many other more recent pretraining schemes. We evaluate a number of noising approaches, finding the best performance by both randomly shuffling the order of the original sentences and using a novel in-filling scheme, where spans of text are replaced with a single mask token. BART is particularly effective when fine tuned for text generation but also works well for comprehension tasks. It matches the performance of RoBERTa with comparable training resources on GLUE and SQuAD, achieves new state-of-the-art results on a range of abstractive dialogue, question answering, and summarization tasks, with gains of up to 6 ROUGE. BART also provides a 1.1 BLEU increase over a back-translation system for machine translation, with only target language pretraining. We also report ablation experiments that replicate other pretraining schemes within the BART framework, to better measure which factors most influence end-task performance.

Self-supervised methods have achieved remarkable success in a wide range of NLP tasks .

The most successful approaches have been variants of masked language models, which are denoising autoencoders that are trained to reconstruct text where a random subset of the words has been masked out. Recent work has shown gains by improving the distribution of masked tokens , the order in which masked tokens are predicted , and the available context for replacing masked tokens . However, these methods typically focus on particular types of end tasks (e.g. span prediction, generation, etc.), limiting their applicability.

In this paper, we present BART, which pre-trains a model combining Bidirectional and Auto-Regressive Transformers. BART is a denoising autoencoder built with a sequence-to-sequence model that is applicable to a very wide range of end tasks. Pretraining has two stages (1) text is corrupted with an arbitrary noising function, and (2) a sequence-to-sequence model is learned to reconstruct the original text. BART uses a standard Tranformer-based neural machine translation architecture which, despite its simplicity, can be seen as generalizing BERT (due to the bidirectional encoder), GPT (with the left-to-right decoder), and many other more recent pretraining schemes (see Figure ).

A key advantage of this setup is the noising flexibility; arbitrary transformations can be applied to the original text, including changing its length. We evaluate a number of noising approaches, finding the best performance by both randomly shuffling the order of the original sentences and using a novel in-filling scheme, where arbitrary length spans of text (including zero length) are replaced with a single mask token. This approach generalizes the original word masking and next sentence prediction objectives in BERT by forcing the model to reason more about overall sentence length and make longer range transformations to the input.

BART is particularly effective when fine tuned for text generation but also works well for comprehension tasks. It matches the performance of RoBERTa with comparable training resources on GLUE and SQuAD , and achieves new state-of-the-art results on a range of abstractive dialogue, question answering, and summarization tasks. For example, it improves performance by 6 ROUGE over previous work on XSum .

BART also opens up new ways of thinking about fine tuning. We present a new scheme for machine translation where a BART model is stacked above a few additional transformer layers. These layers are trained to essentially translate the foreign language to noised English, by propagation through BART, thereby using BART as a pre-trained target-side language model. This approach improves performance over a strong back-translation MT baseline by 1.1 BLEU on the WMT Romanian-English benchmark.

To better understand these effects, we also report an ablation analysis that replicates other recently proposed training objectives. This study allows us to carefully control for a number of factors, including data and optimization parameters, which have been shown to be as important for overall performance as the selection of training objectives . We find that BART exhibits the most consistently strong performance across the full range of tasks we consider.

@src https://arxiv.org/abs/2003.10555
@title ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators
@section Introduction

Masked language modeling (MLM) pre-training methods such as BERT corrupt the input by replacing some tokens with [MASK] and then train a model to reconstruct the original tokens.

While they produce good results when transferred to downstream NLP tasks, they generally require large amounts of compute to be effective.

As an alternative, we propose a more sample-efficient pre-training task called replaced token detection.

Instead of masking the input, our approach corrupts it by replacing some tokens with plausible alternatives sampled from a small generator network.

Then, instead of training a model that predicts the original identities of the corrupted tokens, we train a discriminative model that predicts whether each token in the corrupted input was replaced by a generator sample or not.

Thorough experiments demonstrate this new pre-training task is more efficient than MLM because the task is defined over all input tokens rather than just the small subset that was masked out.

As a result, the contextual representations learned by our approach substantially outperform the ones learned by BERT given the same model size, data, and compute.

The gains are particularly strong for small models; for example, we train a model on one GPU for 4 days that outperforms GPT (trained using 30x more compute) on the GLUE natural language understanding benchmark.

Our approach also works well at scale, where it performs comparably to RoBERTa and XLNet while using less than 1/4 of their compute and outperforms them when using the same amount of compute.

Current state-of-the-art representation learning methods for language can be viewed as learning denoising autoencoders .

They select a small subset of the unlabeled input sequence (typically 15%), mask the identities of those tokens (e.g., BERT; ) or attention to those tokens (e.g., XLNet; ), and then train the network to recover the original input.

While more effective than conventional language-model pre-training due to learning bidirectional representations, these masked language modeling (MLM) approaches incur a substantial compute cost because the network only learns from 15% of the tokens per example.

As an alternative, we propose replaced token detection, a pre-training task in which the model learns to distinguish real input tokens from plausible but synthetically generated replacements.

Instead of masking, our method corrupts the input by replacing some tokens with samples from a proposal distribution, which is typically the output of a small masked language model.

This corruption procedure solves a mismatch in BERT (although not in XLNet) where the network sees artificial MATH tokens during pre-training but not when being fine-tuned on downstream tasks.

We then pre-train the network as a discriminator that predicts for every token whether it is an original or a replacement.

In contrast, MLM trains the network as a generator that predicts the original identities of the corrupted tokens.

A key advantage of our discriminative task is that the model learns from all input tokens instead of just the small masked-out subset, making it more computationally efficient.

Although our approach is reminiscent of training the discriminator of a GAN, our method is not adversarial in that the generator producing corrupted tokens is trained with maximum likelihood due to the difficulty of applying GANs to text .

We call our approach ELECTRA (Code and pre-trained weights will be released at https://github.com/google-research/electra for "Efficiently Learning an Encoder that Classifies Token Replacements Accurately."

As in prior work, we apply it to pre-train Transformer text encoders that can be fine-tuned on downstream tasks.

Through a series of ablations, we show that learning from all input positions causes ELECTRA to train much faster than BERT.

We also show ELECTRA achieves higher accuracy on downstream tasks when fully trained.

Most current pre-training methods require large amounts of compute to be effective, raising concerns about their cost and accessibility.

Since pre-training with more compute almost always results in better downstream accuracies, we argue an important consideration for pre-training methods should be compute efficiency as well as absolute downstream performance.

From this viewpoint, we train ELECTRA models of various sizes and evaluate their downstream performance vs.\ their compute requirement.

In particular, we run experiments on the GLUE natural language understanding benchmark and SQuAD question answering benchmark .

ELECTRA substantially outperforms MLM-based methods such as BERT and XLNet given the same model size, data, and compute (see Figure ).

For example, we build an ELECTRA-Small model that can be trained on 1 GPU in 4 days. (It has 1/20th the parameters and requires 1/135th the pre-training compute of BERT-Large.

ELECTRA-Small outperforms a comparably small BERT model by 5 points on GLUE, and even outperforms the much larger GPT model .

Our approach also works well at large scale, where we train an ELECTRA-Large model that performs comparably to RoBERTa and XLNet , despite having fewer parameters and using 1/4 of the compute for training.

Training ELECTRA-Large further results in an even stronger model that outperforms ALBERT on GLUE and sets a new state-of-the-art for SQuAD 2.0.

Taken together, our results indicate that the discriminative task of distinguishing real data from challenging negative samples is more compute-efficient and parameter-efficient than existing generative approaches for

@src https://arxiv.org/abs/2005.11401
@title Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
@section Introduction

Large pre-trained language models have been shown to store factual knowledge in their parameters, and achieve state-of-the-art results when fine-tuned on downstream NLP tasks.

However, their ability to access and precisely manipulate knowledge is still limited, and hence on knowledge-intensive tasks, their performance lags behind task-specific architectures.

Additionally, providing provenance for their decisions and updating their world knowledge remain open research problems.

Pre-trained models with a differentiable access mechanism to explicit non-parametric memory

have so far been only investigated for extractive downstream tasks.

We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG) — models which combine pre-trained parametric and non-parametric memory for language generation.

We introduce RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever.

We compare two RAG formulations, one which conditions on the same retrieved passages across the whole generated sequence, and another which can use different passages per token.

We fine-tune and evaluate our models on a wide range of knowledge-intensive NLP tasks and set the state of the art on three open domain QA tasks, outperforming parametric seq2seq models and task-specific retrieve-and-extract architectures.

For language generation tasks, we find that RAG models generate more specific, diverse and factual language than a state-of-the-art parametric-only seq2seq baseline.

Pre-trained neural language models have been shown to learn a substantial amount of in-depth knowledge from data .

They can do so without any access to an external memory, as a parameterized implicit knowledge base .

While this development is exciting, such models do have downsides:

They cannot easily expand or revise their memory, can't straightforwardly provide insight into their predictions, and may produce "hallucinations" .

Hybrid models that combine parametric memory with non-parametric (i.e., retrieval-based) memories can address some of these issues because knowledge

can be directly revised and expanded, and accessed knowledge can be inspected and interpreted.

REALM and ORQA , two recently introduced models that combine masked language models with a differentiable retriever, have shown promising results, but have only explored open-domain extractive question answering.

Here, we bring hybrid parametric and non-parametric memory to the "workhorse of NLP," i.e. sequence-to-sequence (seq2seq) models.

We endow pre-trained, parametric-memory generation models with a non-parametric memory through a general-purpose fine-tuning approach which we refer to as retrieval-augmented generation (RAG).

We build RAG models where the parametric memory is a pre-trained seq2seq transformer, and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever. We combine these components in a probabilistic model trained end-to-end (Fig. ). The retriever (Dense Passage Retriever , henceforth DPR) provides latent documents conditioned on the input, and the seq2seq model (BART ) then conditions on these latent documents together with the input to generate the output.

We marginalize the latent documents with a top-K approximation, either on a per-output basis (assuming the same document is responsible for all tokens) or a per-token basis (where different documents are responsible for different tokens). Like T5 or BART, RAG can be fine-tuned on any seq2seq task, whereby both the generator and retriever are jointly learned.

There has been extensive previous work proposing architectures to enrich systems with non-parametric memory which are trained from scratch for specific tasks, e.g. memory networks , stack-augmented networks and memory layers . In contrast, we explore a setting where both parametric and non-parametric memory components are pre-trained and pre-loaded with extensive knowledge. Crucially, by using pre-trained access mechanisms, the ability to access knowledge is present without additional training.

Our results highlight the benefits of combining parametric and non-parametric memory with generation for knowledge-intensive tasks—tasks that humans could not reasonably be expected to perform without access to an external knowledge source.

Our RAG models achieve state-of-the-art results on open Natural Questions , WebQuestions and CuratedTrec and strongly outperform recent approaches that use specialised pre-training objectives on TriviaQA . Despite these being extractive tasks, we find that unconstrained generation outperforms previous extractive approaches. For knowledge-intensive generation, we experiment with MS-MARCO and Jeopardy question generation, and we find that our models generate responses that are more factual, specific, and diverse than a BART baseline. For FEVER fact verification, we achieve results within 4.3% of state-of-the-art pipeline models which use strong retrieval supervision.

Finally, we demonstrate that the non-parametric memory can be replaced

to update the models' knowledge as the world changes. (Code to run experiments with RAG has been open-sourced as part of the HuggingFace Transformers Library and can be found at https://github.com/huggingface/transformers/blob/master/examples/rag/. An interactive demo of RAG models can be found at https://huggingface.co/rag/

@src https://arxiv.org/abs/2005.12872
@title End-to-End Object Detection with Transformers
@section Introduction

End-to-End Object Detection with Transformers

End-to-End Object Detection with Transformers

Nicolas Carion Equal contribution Francisco Massa 1 Gabriel Synnaeve Nicolas Usunier Alexander Kirillov Sergey Zagoruyko

We present a new method that views object detection as a direct set prediction problem. Our approach streamlines the detection pipeline, effectively removing the need for many hand-designed components like a non-maximum suppression procedure or anchor generation that explicitly encode our prior knowledge about the task. The main ingredients of the new framework, called DEtection TRansformer or , are a set-based global loss that forces unique predictions

and a transformer encoder-decoder architecture. Given a fixed small set of learned object queries, reasons about the relations of the objects and the global image context to directly output the final set of predictions in parallel.

The new model is conceptually simple and does not require a specialized library, unlike many other modern detectors.

demonstrates accuracy and run-time performance on par with the

well-established and highly-optimized Faster R-CNN baseline on the challenging

Moreover, can be easily generalized to produce panoptic segmentation in a unified manner. We show that it significantly outperforms competitive baselines.

Training code and pretrained models are available at https://github.com/facebookresearch/detr.

The goal of object detection is to predict a set of bounding boxes and category labels for each object of interest.

Modern detectors address this set prediction task in an indirect way, by defining surrogate regression and classification problems on a large set of proposals , anchors , or window centers .

Their performances are significantly influenced by postprocessing steps to collapse near-duplicate predictions, by the design of the anchor sets and by the heuristics that assign target boxes to anchors .

To simplify these pipelines, we propose a direct set prediction approach to bypass the surrogate tasks.

This end-to-end philosophy has led to significant advances in complex structured prediction tasks such as machine translation or speech recognition, but not yet in object detection: previous attempts either add other forms of prior knowledge, or have not proven to be competitive with strong baselines on challenging benchmarks. This paper aims to bridge this gap.

We streamline the training pipeline by viewing object detection as a direct set prediction problem. We adopt an encoder-decoder architecture based on transformers , a popular architecture for sequence prediction. The self-attention mechanisms of transformers, which explicitly model all pairwise interactions between elements in a sequence, make these architectures particularly suitable for specific constraints of set prediction such as removing duplicate predictions.

Our DEtection TRansformer ( , see Figure ) predicts all objects at once, and is trained end-to-end with a set loss function which performs bipartite matching between predicted and ground-truth objects.

simplifies the detection pipeline by dropping multiple hand-designed components that encode prior knowledge, like spatial anchors or non-maximal suppression.

Unlike most existing detection methods, doesn't require any customized layers, and thus can be reproduced easily in any framework that contains standard CNN and transformer classes. (In our work we use standard implementations of Transformers and ResNet backbones from standard deep learning libraries. .

Compared to most previous work on direct set prediction, the main features of are the conjunction of the bipartite matching loss and transformers with (non-autoregressive) parallel decoding . In contrast, previous work focused on autoregressive decoding with RNNs . Our matching loss function uniquely assigns a prediction to a ground truth object, and is invariant to a permutation of predicted objects, so we can emit them in parallel.

We evaluate on one of the most popular object detection datasets, COCO , against a very competitive Faster R-CNN baseline . Faster R-CNN has undergone many design iterations and its performance was greatly improved since the original publication. Our experiments show that our new model

achieves comparable performances. More precisely, demonstrates significantly better performance on large objects, a result likely enabled by the non-local computations of the transformer. It obtains, however, lower performances on small objects. We expect that future work will improve this aspect in the same way the development of FPN did for Faster R-CNN.

Training settings for differ from standard object detectors in multiple ways. The new model requires extra-long training schedule and benefits from auxiliary decoding losses in the transformer.

We thoroughly explore what components are crucial for the demonstrated performance.

The design ethos of easily extend to more complex tasks. In our

experiments, we show that a simple segmentation head trained on top of a

pre-trained outperfoms competitive baselines on Panoptic Segmentation , a challenging pixel-level recognition task that has recently gained popularity.

@src https://arxiv.org/abs/2005.14165
@title Language Models are Few-Shot Learners
@section Introduction

Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task. While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples. By contrast, humans can generally perform a new language task from only a few examples or from simple instructions – something which current NLP systems still largely struggle to do. Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches. Specifically, we train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in the few-shot setting. For all tasks, GPT-3 is applied without any gradient updates or fine-tuning, with tasks and few-shot demonstrations specified purely via text interaction with the model. GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic. At the same time, we also identify some datasets where GPT-3's few-shot learning still struggles, as well as some datasets where GPT-3 faces methodological issues related to training on large web corpora. Finally, we find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans. We discuss broader societal impacts of this finding and of GPT-3 in general.

Recent years have featured a trend towards pre-trained language representations in NLP systems, applied in increasingly flexible and task-agnostic ways for downstream transfer. First, single-layer representations were learned using word vectors and fed to task-specific architectures, then RNNs with multiple layers of representations and contextual state were used to form stronger representations (though still applied to task-specific architectures), and more recently pre-trained recurrent or transformer language models have been directly fine-tuned, entirely removing the need for task-specific architectures .

This last paradigm has led to substantial progress on many challenging NLP tasks such as reading comprehension, question answering, textual entailment, and many others, and has continued to advance based on new architectures and algorithms . However, a major limitation to this approach is that while the architecture is task-agnostic, there is still a need for task-specific datasets and task-specific fine-tuning: to achieve strong performance on a desired task typically requires fine-tuning on a dataset of thousands to hundreds of thousands of examples specific to that task. Removing this limitation would be desirable, for several reasons.

First, from a practical perspective, the need for a large dataset of labeled examples for every new task limits the applicability of language models. There exists a very wide range of possible useful language tasks, encompassing anything from correcting grammar, to generating examples of an abstract concept, to critiquing a short story. For many of these tasks it is difficult to collect a large supervised training dataset, especially when the process must be repeated for every new task.

Second, the potential to exploit spurious correlations in training data fundamentally grows with the expressiveness of the model and the narrowness of the training distribution. This can create problems for the pre-training plus fine-tuning paradigm, where models are designed to be large to absorb information during pre-training, but are then fine-tuned on very narrow task distributions. For instance observe that larger models do not necessarily generalize better out-of-distribution. There is evidence that suggests that the generalization achieved under this paradigm can be poor because the model is overly specific to the training distribution and does not generalize well outside it . Thus, the performance of fine-tuned models on specific benchmarks, even when it is nominally at human-level, may exaggerate actual performance on the underlying task .

Third, humans do not require large supervised datasets to learn most language tasks – a brief directive in natural language (e.g. "please tell me if this sentence describes something happy or something sad") or at most a tiny number of demonstrations (e.g. "here are two examples of people acting brave; please give a third example of bravery") is often sufficient to enable a human to perform a new task to at least a reasonable degree of competence. Aside from pointing to a conceptual limitation in our current NLP techniques, this adaptability has practical advantages – it allows humans to seamlessly mix together or switch between many tasks and skills, for example performing addition during a lengthy dialogue. To be broadly useful, we would someday like our NLP systems to have this same fluidity and generality.

One potential route towards addressing these issues is meta-learning (In the context of language models this has sometimes been called "zero-shot transfer", but this term is potentially ambiguous: the method is "zero-shot" in the sense that no gradient updates are performed, but it often involves providing inference-time demonstrations to the model, so is not truly learning from zero examples. To avoid this confusion, we use the term "meta-learning" to capture the inner-loop / outer-loop structure of the general method, and the term "in context-learning" to refer to the inner loop of meta-learning. We further specialize the description to "zero-shot", "one-shot", or "few-shot" depending on how many demonstrations are provided at inference time. These terms are intended to remain agnostic on the question of whether the model learns new tasks from scratch at inference time or simply recognizes patterns seen during training – this is an important issue which we discuss later in the paper, but "meta-learning" is intended to encompass both possibilities, and simply describes the inner-outer loop structure. – which in the context of language models means the model develops a broad set of skills and pattern recognition abilities at training time, and then uses those abilities at inference time to rapidly adapt to or recognize the desired task (illustrated in Figure ). Recent work attempts to do this via what we call "in-context learning", using the text input of a pretrained language model as a form of task specification: the model is conditioned on a natural language instruction and/or a few demonstrations of the task and is then expected to complete further instances of the task simply by predicting what comes next.

While it has shown some initial promise, this approach still achieves results far inferior to fine-tuning – for example achieves only 4% on Natural Questions, and even its 55 F1 CoQa result is now more than 35 points behind the state of the art. Meta-learning clearly requires substantial improvement in order to be viable as a practical method of solving language tasks.

Another recent trend in language modeling may offer a way forward. In recent years the capacity of transformer language models has increased substantially, from 100 million parameters , to 300 million parameters , to 1.5 billion parameters , to 8 billion parameters , 11 billion parameters , and finally 17 billion parameters . Each increase has brought improvements in text synthesis and/or downstream NLP tasks, and there is evidence suggesting that log loss, which correlates well with many downstream tasks, follows a smooth trend of improvement with scale . Since in-context learning involves absorbing many skills and tasks within the parameters of the model, it is plausible that in-context learning abilities might show similarly strong gains with scale.

In this paper, we test this hypothesis by training a 175 billion parameter autoregressive language model, which we call GPT-3, and measuring its in-context learning abilities. Specifically, we evaluate GPT-3 on over two dozen NLP datasets, as well as several novel tasks designed to test rapid adaptation to tasks unlikely to be directly contained in the training set. For each task, we evaluate GPT-3 under 3 conditions: (a) "few-shot learning", or in-context learning where we allow as many demonstrations as will fit into the model’s context window (typically 10 to 100), (b) "one-shot learning", where we allow only one demonstration, and (c) "zero-shot" learning, where no demonstrations are allowed and only an instruction in natural language is given to the model. GPT-3 could also in principle be evaluated in the traditional fine-tuning setting, but we leave this to future work.

Figure illustrates the conditions we study, and shows few-shot learning of a simple task requiring the model to remove extraneous symbols from a word. Model performance improves with the addition of a natural language task description, and with the number of examples in the model's context, MATH . Few-shot learning also improves dramatically with model size. Though the results in this case are particularly striking, the general trends with both model size and number of examples in-context hold for most tasks we study. We emphasize that these "learning" curves involve no gradient updates or fine-tuning, just increasing numbers of demonstrations given as conditioning.

Broadly, on NLP tasks GPT-3 achieves promising results in the zero-shot and one-shot settings, and in the the few-shot setting is sometimes competitive with or even occasionally surpasses state-of-the-art (despite state-of-the-art being held by fine-tuned models). For example, GPT-3 achieves 81.5 F1 on CoQA in the zero-shot setting, 84.0 F1 on CoQA in the one-shot setting, 85.0 F1 in the few-shot setting. Similarly, GPT-3 achieves 64.3% accuracy on TriviaQA in the zero-shot setting, 68.0% in the one-shot setting, and 71.2% in the few-shot setting, the last of which is state-of-the-art relative to fine-tuned models operating in the same closed-book setting.

GPT-3 also displays one-shot and few-shot proficiency at tasks designed to test rapid adaption or on-the-fly reasoning, which include unscrambling words, performing arithmetic, and using novel words in a sentence after seeing them defined only once. We also show that in the few-shot setting, GPT-3 can generate synthetic news articles which human evaluators have difficulty distinguishing from human-generated articles.

At the same time, we also find some tasks on which few-shot performance struggles, even at the scale of GPT-3. This includes natural language inference tasks like the ANLI dataset, and some reading comprehension datasets like RACE or QuAC. By presenting a broad characterization of GPT-3's strengths and weaknesses, including these limitations, we hope to stimulate study of few-shot learning in language models and draw attention to where progress is most needed.

A heuristic sense of the overall results can be seen in Figure , which aggregates the various tasks (though it should not be seen as a rigorous or meaningful benchmark in itself).

We also undertake a systematic study of "data contamination" – a growing problem when training high capacity models on datasets such as Common Crawl, which can potentially include content from test datasets simply because such content often exists on the web. In this paper we develop systematic tools to measure data contamination and quantify its distorting effects. Although we find that data contamination has a minimal effect on GPT-3's performance on most datasets, we do identify a few datasets where it could be inflating results, and we either do not report results on these datasets or we note them with an asterisk, depending on the severity.

In addition to all the above, we also train a series of smaller models (ranging from 125 million parameters to 13 billion parameters) in order to compare their performance to GPT-3 in the zero, one and few-shot settings. Broadly, for most tasks we find relatively smooth scaling with model capacity in all three settings; one notable pattern is that the gap between zero-, one-, and few-shot performance often grows with model capacity, perhaps suggesting that larger models are more proficient meta-learners.

Finally, given the broad spectrum of capabilities displayed by GPT-3, we discuss concerns about bias, fairness, and broader societal impacts, and attempt a preliminary analysis of GPT-3's characteristics in this regard.

The remainder of this paper is organized as follows. In Section , we describe our approach and methods for training GPT-3 and evaluating it. Section presents results on the full range of tasks in the zero-, one- and few-shot settings. Section addresses questions of data contamination (train-test overlap). Section discusses limitations of GPT-3. Section discusses broader impacts. Section reviews related work and Section concludes.

@src https://arxiv.org/abs/2006.11239
@title Denoising Diffusion Probabilistic Models
@section Introduction

We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics. Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score matching with Langevin dynamics, and our models naturally admit a progressive lossy decompression scheme that can be interpreted as a generalization of autoregressive decoding. On the unconditional CIFAR10 dataset, we obtain an Inception score of 9.46 and a state-of-the-art FID score of 3.17. On 256x256 LSUN, we obtain sample quality similar to ProgressiveGAN. Our implementation is available at https://github.com/hojonathanho/diffusion.

Deep generative models of all kinds have recently exhibited high quality samples in a wide variety of data modalities. Generative adversarial networks (GANs), autoregressive models, flows, and variational autoencoders (VAEs) have synthesized striking image and audio samples , and there have been remarkable advances in energy-based modeling and score matching that have produced images comparable to those of GANs .

This paper presents progress in diffusion probabilistic models . A diffusion probabilistic model (which we will call a "diffusion model" for brevity) is a parameterized Markov chain trained using variational inference to produce samples matching the data after finite time. Transitions of this chain are learned to reverse a diffusion process, which is a Markov chain that gradually adds noise to the data in the opposite direction of sampling until signal is destroyed.

When the diffusion consists of small amounts of Gaussian noise, it is sufficient to set the sampling chain transitions to conditional Gaussians too, allowing for a particularly simple neural network parameterization.

Diffusion models are straightforward to define and efficient to train, but to the best of our knowledge, there has been no demonstration that they are capable of generating high quality samples. We show that diffusion models actually are capable of generating high quality samples, sometimes better than the published results on other types of generative models ( sec:experiments ).

In addition, we show that a certain parameterization of diffusion models reveals an equivalence with denoising score matching over multiple noise levels during training and with annealed Langevin dynamics during sampling ( sec:revproc_dsm_diffusion_connection ) .

We obtained our best sample quality results using this parameterization ( sec:loss_ablation ), so we consider this equivalence to be one of our primary contributions.

Despite their sample quality, our models do not have competitive log likelihoods compared to other likelihood-based models (our models do, however, have log likelihoods better than the large estimates annealed importance sampling has been reported to produce for energy based models and score matching ).

We find that the majority of our models' lossless codelengths are consumed to describe imperceptible image details ( sec:coding ). We present a more refined analysis of this phenomenon in the language of lossy compression, and we show that the sampling procedure of diffusion models is a type of progressive decoding that resembles autoregressive decoding along a bit ordering that vastly generalizes what is normally possible with autoregressive models.

@src https://arxiv.org/abs/2009.03300
@title Measuring Massive Multitask Language Understanding
@section Introduction

We propose a new test to measure a text model's multitask accuracy. The test covers 57 tasks including elementary mathematics, US history, computer science, law, and more. To attain high accuracy on this test, models must possess extensive world knowledge and problem solving ability. We find that while most recent models have near random-chance accuracy, the very largest GPT-3 model improves over random chance by almost 20 percentage points on average. However, on every one of the 57 tasks, the best models still need substantial improvements before they can reach expert-level accuracy. Models also have lopsided performance and frequently do not know when they are wrong. Worse, they still have near-random accuracy on some socially important subjects such as morality and law. By comprehensively evaluating the breadth and depth of a model's academic and professional understanding, our test can be used to analyze models across many tasks and to identify important shortcomings.

Natural Language Processing (NLP) models have achieved superhuman performance on a number of recently proposed benchmarks.

However, these models are still well below human level performance for language understanding as a whole, suggesting a disconnect between our benchmarks and the actual capabilities of these models.

The General Language Understanding Evaluation benchmark (GLUE) was introduced in 2018 to evaluate performance on a wide range of NLP tasks, and top models achieved superhuman performance within a year. To address the shortcomings of GLUE, researchers designed the SuperGLUE benchmark with more difficult tasks . About a year since the release of SuperGLUE, performance is again essentially human-level . While these benchmarks evaluate linguistic skills more than overall language understanding, an array of commonsense benchmarks have been proposed to measure basic reasoning and everyday knowledge .

However, these recent benchmarks have similarly seen rapid progress . Overall, the near human-level performance on these benchmarks suggests that they are not capturing important facets of language understanding.

Transformer models have driven this recent progress by pretraining on massive text corpora, including all of Wikipedia, thousands of books, and numerous websites. These models consequently see extensive information about specialized topics, most of which is not assessed by existing NLP benchmarks.

It consequently remains an open question just how capable current language models are at learning and applying knowledge from many domains.

To bridge the gap between the wide-ranging knowledge that models see during pretraining and the existing measures of success,

we introduce a new benchmark for assessing models across a diverse set of subjects that humans learn.

We design the benchmark to measure knowledge acquired during pretraining by evaluating models exclusively in zero-shot and few-shot settings. This makes the benchmark more challenging and more similar to how we evaluate humans.

The benchmark covers MATH subjects across STEM, the humanities, the social sciences, and more. It ranges in difficulty from an elementary level to an advanced professional level, and it tests both world knowledge and problem solving ability.

Subjects range from traditional areas, such as mathematics and history, to more specialized areas like law and ethics .

The granularity and breadth of the subjects makes the benchmark ideal for identifying a model's blind spots.

We find that meaningful progress on our benchmark has only become possible in recent months. In particular, few-shot models up to MATH billion parameters achieve random chance performance of MATH accuracy, but the MATH billion parameter GPT-3 model reaches a much higher MATH accuracy (see fig:juxtaposition ).

On the other hand, unlike human professionals GPT-3 does not excel at any single subject.

Instead, we find that performance is lopsided, with GPT-3 having almost MATH accuracy for its best subject but near-random performance for several other subjects.

Our results indicate that while recent advances have been impressive, state-of-the-art models still struggle at learning and applying knowledge from pretraining.

The tasks with near-random accuracy include calculation-heavy subjects such as physics and mathematics and subjects related to human values such as law and morality.

This second weakness is particularly concerning because it will be important for future models to have a strong understanding of what is legal and what is ethical. Worryingly, we also find that GPT-3 does not have an accurate sense of what it does or does not know since its average confidence can be up to MATH off from its actual accuracy.

We comprehensively evaluate the breadth and depth of a model's text understanding by covering numerous topics that humans are incentivized to learn.

Since our test consists in MATH tasks, it can be used to analyze aggregate properties of models across tasks and to track important shortcomings.

The test and code is available at https://github.com/hendrycks/test github.com/hendrycks/test .

@src https://arxiv.org/abs/2010.02502
@title Denoising Diffusion Implicit Models
@section Introduction

Denoising diffusion probabilistic models (DDPMs) have achieved high quality image generation without adversarial training, yet they require simulating a Markov chain for many steps in order to produce a sample. To accelerate sampling, we present denoising diffusion implicit models (DDIMs), a more efficient class of iterative implicit probabilistic models with the same training procedure as DDPMs. In DDPMs, the generative process is defined as the reverse of a particular Markovian diffusion process. We generalize DDPMs via a class of non-Markovian diffusion processes that lead to the same training objective. These non-Markovian processes can correspond to generative processes that are deterministic, giving rise to implicit models that produce high quality samples much faster. We empirically demonstrate that DDIMs can produce high quality samples MATH to MATH faster in terms of wall-clock time compared to DDPMs, allow us to trade off computation for sample quality, perform semantically meaningful image interpolation directly in the latent space, and reconstruct observations with very low error.

Deep generative models have demonstrated the ability to produce high quality samples in many domains . In terms of image generation, generative adversarial networks (GANs, ) currently exhibits higher sample quality than likelihood-based methods such as variational autoencoders , autoregressive models and normalizing flows . However, GANs require very specific choices in optimization and architectures in order to stabilize training , and could fail to cover modes of the data distribution .

Recent works on iterative generative models , such as denoising diffusion probabilistic models (DDPM, ) and noise conditional score networks (NCSN, )

have demonstrated the ability to produce samples comparable to that of GANs, without having to perform adversarial training. To achieve this, many denoising autoencoding models are trained to denoise samples corrupted by various levels of Gaussian noise. Samples are then produced by a Markov chain which, starting from white noise, progressively denoises it into an image. This generative Markov Chain process is either based on Langevin dynamics or obtained by reversing a forward diffusion process that progressively turns an image into noise .

A critical drawback of these models is that they require many iterations to produce a high quality sample. For DDPMs, this is because that the generative process (from noise to data) approximates the reverse of the forward diffusion process (from data to noise), which could have thousands of steps; iterating over all the steps is required to produce a single sample, which is much slower compared to GANs, which only needs one pass through a network.

For example, it takes around 20 hours to sample 50k images of size MATH from a DDPM, but less than a minute to do so from https://github.com/ajbrock/BigGAN-PyTorch a GAN on a Nvidia 2080 Ti GPU. This becomes more problematic for larger images as sampling 50k images of size MATH could take nearly MATH hours on the same GPU.

To close this efficiency gap between DDPMs and GANs,

we present denoising diffusion implicit models (DDIMs). DDIMs are implicit probabilistic models and are closely related to DDPMs, in the sense that they are trained with the same objective function.

we generalize the forward diffusion process used by DDPMs, which is Markovian, to non-Markovian ones, for which we are still able to design suitable reverse generative Markov chains.

We show that the resulting variational training objectives have a shared surrogate objective, which is exactly the objective used to train DDPM.

Therefore, we can freely choose from a large family of generative models using the same neural network simply by choosing a different, non-Markovian diffusion process (Section ) and the corresponding reverse generative Markov Chain.

In particular, we are able to use non-Markovian diffusion processes which lead to "short" generative Markov chains (Section ) that can be simulated in a small number of steps.

This can massively increase sample efficiency only at a minor cost in sample quality.

In Section , we demonstrate several empirical benefits of DDIMs over DDPMs. First, DDIMs have superior sample generation quality compared to DDPMs, when we accelerate sampling by MATH to MATH using our proposed method.

Second, DDIM samples have the following "consistency" property, which does not hold for DDPMs: if we start with the same initial latent variable and generate several samples with Markov chains of various lengths, these samples would have similar high-level features.

Third, because of "consistency" in DDIMs,

we can perform semantically meaningful image interpolation by manipulating the initial latent variable in DDIMs, unlike DDPMs which interpolates near the image space due to the stochastic generative process.

@src https://arxiv.org/abs/2010.11929
@title An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale
@section Introduction

While the Transformer architecture has become the de-facto standard for natural language processing tasks, its applications to computer vision remain limited.

In vision, attention is either applied in conjunction with convolutional networks, or used to replace certain components of convolutional networks while keeping their overall structure in place.

We show that this reliance on CNNs is not necessary and a pure transformer applied directly to sequences of image patches can perform very well on image classification tasks.

When pre-trained on large amounts of data and transferred to multiple mid-sized or small image recognition benchmarks ( , CIFAR-100, VTAB, etc.), ( ) attains excellent results compared to state-of-the-art convolutional networks while requiring substantially fewer computational resources to train. (Fine-tuning code and pre-trained models are available at https://github.com/google-research/vision_transformer

Self-attention-based architectures, in particular Transformers , have become the model of choice in natural language processing (NLP).

The dominant approach is to pre-train on a large text corpus and then fine-tune on a smaller task-specific dataset .

Thanks to Transformers' computational efficiency and scalability, it has become possible to train models of unprecedented size, with over 100B parameters .

With the models and datasets growing, there is still no sign of saturating performance.

In computer vision, however, convolutional architectures remain dominant .

Inspired by NLP successes, multiple works try combining CNN-like architectures with self-attention , some replacing the convolutions entirely .

The latter models, while theoretically efficient, have not yet been scaled effectively on modern hardware accelerators due to the use of specialized attention patterns.

Therefore, in large-scale image recognition, classic ResNet-like architectures are still state of the art .

Inspired by the Transformer scaling successes in NLP, we experiment with applying a standard Transformer directly to images, with the fewest possible modifications.

To do so, we split an image into patches and provide the sequence of linear embeddings of these patches as an input to a Transformer.

Image patches are treated the same way as tokens (words) in an NLP application.

We train the model on image classification in supervised fashion.

When trained on mid-sized datasets such as without strong regularization, these models yield modest accuracies of a few percentage points below ResNets of comparable size.

This seemingly discouraging outcome may be expected: Transformers lack some of the inductive biases inherent to CNNs, such as translation equivariance and locality, and therefore do not generalize well when trained on insufficient amounts of data.

However, the picture changes if the models are trained on larger datasets (14M-300M images).

We find that large scale training trumps inductive bias.

Our ( ) attains excellent results when pre-trained at sufficient scale and transferred to tasks with fewer datapoints.

When pre-trained on the public ImageNet-21k dataset or the in-house JFT-300M dataset, approaches or beats state of the art on multiple image recognition benchmarks.

In particular, the best model reaches the accuracy of MATH on , MATH on -ReaL, MATH on CIFAR-100, and MATH on the VTAB suite of 19 tasks.

@src https://arxiv.org/abs/2011.13456
@title Score-Based Generative Modeling through Stochastic Differential Equations
@section Introduction

Creating noise from data is easy; creating data from noise is generative modeling. We present a stochastic differential equation (SDE) that smoothly transforms a complex data distribution to a known prior distribution by slowly injecting noise, and a corresponding reverse-time SDE that transforms the prior distribution back into the data distribution by slowly removing the noise.

Crucially, the reverse-time SDE depends only on the time-dependent gradient field ( , score) of the perturbed data distribution. By leveraging advances in score-based generative modeling, we can accurately estimate these scores with neural networks, and use numerical SDE solvers to generate samples. We show that this framework encapsulates previous approaches in score-based generative modeling and diffusion probabilistic modeling, allowing for new sampling procedures and new modeling capabilities. In particular, we introduce a predictor-corrector framework to correct errors in the evolution of the discretized reverse-time SDE. We also derive an equivalent neural ODE that samples from the same distribution as the SDE, but additionally enables exact likelihood computation, and improved sampling efficiency. In addition, we provide a new way to solve inverse problems with score-based models,

as demonstrated with experiments on class-conditional generation, image inpainting, and colorization. Combined with multiple architectural improvements, we achieve record-breaking performance for unconditional image generation on CIFAR-10 with an Inception score of 9.89 and FID of 2.20, a competitive likelihood of 2.99 bits/dim, and demonstrate high fidelity generation of MATH images for the first time from a score-based generative model.

Two successful classes of probabilistic generative models involve sequentially corrupting training data with slowly increasing noise, and then learning to reverse this corruption in order to form a generative model of the data.

Score matching with Langevin dynamics (SMLD)

estimates the score ( , the gradient of the log probability density with respect to data) at each noise scale, and then uses Langevin dynamics to sample from a sequence of decreasing noise scales during generation.

Denoising diffusion probabilistic modeling (DDPM) trains a sequence of probabilistic models to reverse each step of the noise corruption,

using knowledge of the functional form of the reverse distributions to make training tractable.

For continuous state spaces, the DDPM training objective implicitly computes

We therefore refer to these two model classes together as score-based generative models.

Score-based generative models, and related techniques , have proven effective at generation of images , audio , graphs , and shapes . To enable new sampling methods and further extend the capabilities of score-based generative models, we propose a unified framework that generalizes previous approaches through the lens of stochastic differential equations (SDEs).

Solving a reverse-time SDE yields a score-based generative model. Transforming data to a simple noise distribution can be accomplished with a continuous-time SDE. This SDE can be reversed if we know the score of the distribution at each intermediate time step, MATH .

Specifically, instead of perturbing data with a finite number of noise distributions, we consider a continuum of distributions that evolve over time according to a diffusion process. This process progressively diffuses a data point into random noise, and is given by a prescribed SDE that does not depend on the data and has no trainable parameters.

By reversing this process, we can smoothly mold random noise into data for sample generation. Crucially, this reverse process satisfies a reverse-time SDE , which can be derived from the forward SDE given the score of the marginal probability densities as a function of time. We can therefore approximate the reverse-time SDE by training a time-dependent neural network to estimate the scores, and then produce samples using numerical SDE solvers. Our key idea is summarized in fig:teaser .

Our proposed framework has several theoretical and practical contributions:

Flexible sampling and likelihood computation: We can employ any general-purpose SDE solver to integrate the reverse-time SDE for sampling. In addition, we propose two special methods not viable for general SDEs: (i) Predictor-Corrector (PC) samplers that combine numerical SDE solvers with score-based MCMC approaches, such as Langevin MCMC and HMC ; and (ii) deterministic samplers based on the probability flow ordinary differential equation (ODE). The former unifies and improves over existing sampling methods for score-based models. The latter allows for fast adaptive sampling via black-box ODE solvers, flexible data manipulation via latent codes, a uniquely identifiable encoding, and notably, exact likelihood computation.

Controllable generation: We can modulate the generation process by conditioning on information not available during training, because the conditional reverse-time SDE can be efficiently estimated from unconditional scores. This enables applications such as class-conditional generation, image inpainting, colorization and other inverse problems, all achievable using a single unconditional score-based model without re-training.

Unified framework: Our framework provides a unified way to explore and tune various SDEs for improving score-based generative models.

The methods of SMLD and DDPM can be amalgamated into our framework as discretizations of two separate SDEs.

Although DDPM was recently reported to achieve higher sample quality than SMLD , we show that with better architectures and new sampling algorithms allowed by our framework, the latter can catch up—it achieves new state-of-the-art Inception score (9.89) and FID score (2.20) on CIFAR-10, as well as high-fidelity generation of MATH images for the first time from a score-based model. In addition, we propose a new SDE under our framework that achieves a likelihood value of 2.99 bits/dim on uniformly dequantized CIFAR-10 images, setting a new record on this task.

@src https://arxiv.org/abs/2101.03961
@title Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity
@section Introduction

Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity

In deep learning, models typically reuse the same parameters for all inputs.

Mixture of Experts (MoE) models defy this and instead select different parameters for each incoming example.

The result is a sparsely-activated model—with an outrageous number of parameters—but a constant computational cost.

However, despite several notable successes of MoE, widespread adoption has been hindered by complexity, communication costs, and training instability.

We address these with the introduction of the Switch Transformer.

We simplify the MoE routing algorithm and design intuitive improved models with reduced communication and computational costs.

Our proposed training techniques mitigate the instabilities, and we show large sparse models may be trained, for the first time, with lower precision (bfloat16) formats.

We design models based off T5-Base and T5-Large to obtain up to 7x increases in pre-training speed with the same computational resources.

These improvements extend into multilingual settings where we measure gains over the mT5-Base version across all 101 languages.

Finally, we advance the current scale of language models by pre-training up to trillion parameter models on the "Colossal Clean Crawled Corpus", and achieve a 4x speedup over the T5-XXL model. (JAX code for Switch Transformer and all model checkpoints are available at https://github.com/google-research/t5x (Tensorflow code for Switch Transformer is available at https://github.com/tensorflow/mesh/blob/master/mesh_tensorflow/transformer/moe.py

mixture-of-experts, natural language processing, sparsity, large-scale machine learning, distributed computing

Large scale training has been an effective path towards flexible and powerful neural language models .

Simple architectures—backed by a generous computational budget, data set size and parameter count—surpass more complicated algorithms .

An approach followed in expands the model size of a densely-activated Transformer .

While effective, it is also extremely computationally intensive .

Inspired by the success of model scale, but seeking greater computational efficiency, we instead propose a sparsely-activated expert model: the Switch Transformer.

In our case the sparsity comes from activating a subset of the neural network weights for each incoming example.

Sparse training is an active area of research and engineering , but as of today, machine learning libraries and hardware accelerators still cater to dense matrix multiplications.

To have an efficient sparse algorithm, we start with the Mixture-of-Expert (MoE) paradigm , and simplify it to yield training stability and computational benefits.

MoE models have had notable successes in machine translation , however, widespread adoption is hindered by complexity, communication costs, and training instabilities.

We address these issues, and then go beyond translation, to find that these class of algorithms are broadly valuable in natural language.

We measure superior scaling on a diverse set of natural language tasks and across three regimes in NLP: pre-training, fine-tuning and multi-task training.

While this work focuses on scale, we also show that the Switch Transformer architecture not only excels in the domain of supercomputers, but is beneficial even with only a few computational cores.

Further, our large sparse models can be distilled into small dense versions while preserving 30% of the sparse model quality gain.

The Switch Transformer architecture, which simplifies and improves over Mixture of Experts.

Scaling properties and a benchmark against the strongly tuned T5 model where we measure 7x+ pre-training speedups while still using the same FLOPS per token. We further show the improvements hold even with limited computational resources, using as few as two experts.

Successful distillation of sparse pre-trained and specialized fine-tuned models into small dense models. We reduce the model size by up to 99% while preserving 30% of the quality gains of the large sparse teacher.

Improved pre-training and fine-tuning techniques: (1) selective precision training that enables training with lower bfloat16 precision (2) an initialization scheme that allows for scaling to a larger number of experts and (3) increased expert regularization that improves sparse model fine-tuning and multi-task training.

A measurement of the pre-training benefits on multilingual data where we find a universal improvement across all 101 languages and with 91% of languages benefiting from 4x+ speedups over the mT5 baseline .

An increase in the scale of neural language models achieved by efficiently combining data, model, and expert-parallelism to create models with up to a trillion parameters.

These models improve the pre-training speed of a strongly tuned T5-XXL baseline by 4x.

@src https://arxiv.org/abs/2102.12092
@title Zero-Shot Text-to-Image Generation
@section Introduction

Text-to-image generation has traditionally focused on finding better modeling assumptions for training on a fixed dataset. These assumptions might involve complex architectures, auxiliary losses, or side information such as object part labels or segmentation masks supplied during training. We describe a simple approach for this task based on a transformer that autoregressively models the text and image tokens as a single stream of data. With sufficient data and scale, our approach is competitive with previous domain-specific models when evaluated in a zero-shot fashion.

Modern machine learning approaches to text to image synthesis started with the work of , who showed that the DRAW generative model, when extended to condition on image captions, could also generate novel visual scenes. later demonstrated that using a generative adversarial network , rather than a recurrent variational auto-encoder, improved image fidelity. showed that this system could not only generate objects with recognizable properties, but also could zero-shot generalize to held-out categories.

Over the next few years, progress continued using a combination of methods. These include improving the generative model architecture with modifications like multi-scale generators , integrating attention and auxiliary losses , and leveraging additional sources of conditioning information beyond just text .

Separately, propose an energy-based framework for conditional image generation that obtained a large improvement in sample quality relative to contemporary methods. Their approach can incorporate pretrained discriminative models, and they show that it is capable of performing text-to-image generation when applied to a captioning model pretrained on MS-COCO.

More recently, also propose a method that involves optimizing the input to a pretrained cross-modal masked language model. While significant increases in visual fidelity have occurred as a result of the work since , samples can still suffer from severe artifacts such as object distortion, illogical object placement, or unnatural blending of foreground and background elements.

Recent advances fueled by large-scale generative models suggest a possible route for further improvements. Specifically, when compute, model size, and data are scaled carefully, autoregressive transformers have achieved impressive results in several domains such as text , images , and audio .

By comparison, text-to-image generation has typically been evaluated on relatively small datasets such as MS-COCO and CUB-200 . Could dataset size and model size be the limiting factor of current approaches? In this work, we demonstrate that training a 12-billion parameter autoregressive transformer on 250 million image-text pairs collected from the internet results in a flexible, high fidelity generative model of images controllable through natural language.

The resulting system achieves high quality image generation on the popular MS-COCO dataset zero-shot, without using any of the training labels. It is preferred over prior work trained on the dataset by human evaluators 90% of the time. We also find that it is able to perform complex tasks such as image-to-image translation at a rudimentary level. This previously required custom approaches , rather

emerging as a capability of a single, large generative model.

@src https://arxiv.org/abs/2103.00020
@title Learning Transferable Visual Models From Natural Language Supervision
@section Introduction and Motivating Work

State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories. This restricted form of supervision limits their generality and usability since additional labeled data is needed to specify any other visual concept. Learning directly from raw text about images is a promising alternative which leverages a much broader source of supervision. We demonstrate that the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn SOTA image representations from scratch on a dataset of 400 million (image, text) pairs collected from the internet. After pre-training, natural language is used to reference learned visual concepts (or describe new ones) enabling zero-shot transfer of the model to downstream tasks. We study the performance of this approach by benchmarking on over 30 different existing computer vision datasets, spanning tasks such as OCR, action recognition in videos, geo-localization, and many types of fine-grained object classification. The model transfers non-trivially to most tasks and is often competitive with a fully supervised baseline without the need for any dataset specific training. For instance, we match the accuracy of the original ResNet-50 on ImageNet zero-shot without needing to use any of the 1.28 million training examples it was trained on.

We release our code and pre-trained model weights at https://github.com/OpenAI/CLIP.

Pre-training methods which learn directly from raw text have revolutionized NLP over the last few years . Task-agnostic objectives such as autoregressive and masked language modeling have scaled across many orders of magnitude in compute, model capacity, and data, steadily improving capabilities. The development of "text-to-text" as a standardized input-output interface has enabled task-agnostic architectures to zero-shot transfer to downstream datasets removing the need for specialized output heads or dataset specific customization. Flagship systems like GPT-3 are now competitive across many tasks with bespoke models while requiring little to no dataset specific training data.

These results suggest that the aggregate supervision accessible to modern pre-training methods within web-scale collections of text surpasses that of high-quality crowd-labeled NLP datasets. However, in other fields such as computer vision it is still standard practice to pre-train models on crowd-labeled datasets such as ImageNet . Could scalable pre-training methods which learn directly from web text result in a similar breakthrough in computer vision? Prior work is encouraging.

Over 20 years ago explored improving content based image retrieval by training a model to predict the nouns and adjectives in text documents paired with images. demonstrated it was possible to learn more data efficient image representations via manifold learning in the weight space of classifiers trained to predict words in captions associated with images. explored deep representation learning by training multimodal Deep Boltzmann Machines on top of low-level image and text tag features. modernized this line of work and demonstrated that CNNs trained to predict words in image captions learn useful image representations. They converted the title, description, and hashtag metadata of images in the YFCC100M dataset into a bag-of-words multi-label classification task and showed that pre-training AlexNet to predict these labels learned representations which preformed similarly to ImageNet-based pre-training on transfer tasks. then extended this approach to predicting phrase n-grams in addition to individual words and demonstrated the ability of their system to zero-shot transfer to other image classification datasets by scoring target classes based on their dictionary of learned visual n-grams and predicting the one with the highest score. Adopting more recent architectures and pre-training approaches, VirTex , ICMLM , and ConVIRT have recently demonstrated the potential of transformer-based language modeling, masked language modeling, and contrastive objectives to learn image representations from text.

While exciting as proofs of concept, using natural language supervision for image representation learning is still rare. This is likely because demonstrated performance on common benchmarks is much lower than alternative approaches. For example, reach only 11.5% accuracy on ImageNet in a zero-shot setting. This is well below the 88.4% accuracy of the current state of the art . It is even below the 50% accuracy of classic computer vision approaches . Instead, more narrowly scoped but well-targeted uses of weak supervision have improved performance. showed that predicting ImageNet-related hashtags on Instagram images is an effective pre-training task. When fine-tuned to ImageNet these pre-trained models increased accuracy by over 5% and improved the overall state of the art at the time. and have also demonstrated large gains on a broader set of transfer benchmarks by pre-training models to predict the classes of the noisily labeled JFT-300M dataset.

This line of work represents the current pragmatic middle ground between learning from a limited amount of supervised "gold-labels" and learning from practically unlimited amounts of raw text. However, it is not without compromises. Both works carefully design, and in the process limit, their supervision to 1000 and 18291 classes respectively. Natural language is able to express, and therefore supervise, a much wider set of visual concepts through its generality. Both approaches also use static softmax classifiers to perform prediction and lack a mechanism for dynamic outputs. This severely curtails their flexibility and limits their "zero-shot" capabilities.

A crucial difference between these weakly supervised models and recent explorations of learning image representations directly from natural language is scale. While and trained their models for accelerator years on millions to billions of images, VirTex, ICMLM, and ConVIRT trained for accelerator days on one to two hundred thousand images. In this work, we close this gap and study the behaviors of image classifiers trained with natural language supervision at large scale. Enabled by the large amounts of publicly available data of this form on the internet, we create a new dataset of 400 million (image, text) pairs and demonstrate that a simplified version of ConVIRT trained from scratch, which we call CLIP, for Contrastive Language-Image Pre-training, is an efficient method of learning from natural language supervision. We study the scalability of CLIP by training a series of eight models spanning almost 2 orders of magnitude of compute and observe that transfer performance is a smoothly predictable function of compute . We find that CLIP, similar to the GPT family, learns to perform a wide set of tasks during pre-training including OCR, geo-localization, action recognition, and many others. We measure this by benchmarking the zero-shot transfer performance of CLIP on over 30 existing datasets and find it can be competitive with prior task-specific supervised models. We also confirm these findings with linear-probe representation learning analysis and show that CLIP outperforms the best publicly available ImageNet model while also being more computationally efficient. We additionally find that zero-shot CLIP models are much more robust than equivalent accuracy supervised ImageNet models which suggests that zero-shot evaluation of task-agnostic models is much more representative of a model's capability. These results have significant policy and ethical implications, which we consider in Section .

@src https://arxiv.org/abs/2103.00020
@title Learning Transferable Visual Models From Natural Language Supervision
@section Motivation

In computer vision, zero-shot learning usually refers to the study of generalizing to unseen object categories in image classification . We instead use the term in a broader sense and study generalization to unseen datasets. We motivate this as a proxy for performing unseen tasks, as aspired to in the zero-data learning paper of . While much research in the field of unsupervised learning focuses on the representation learning capabilities of machine learning systems, we motivate studying zero-shot transfer as a way of measuring the task-learning capabilities of machine learning systems. In this view, a dataset evaluates performance on a task on a specific distribution. However, many popular computer vision datasets were created by the research community primarily as benchmarks to guide the development of generic image classification methods rather than measuring performance on a specific task. While it is reasonable to say that the SVHN dataset measures the task of street number transcription on the distribution of Google Street View photos, it is unclear what "real" task the CIFAR-10 dataset measures. It is clear, however, what distribution CIFAR-10 is drawn from - TinyImages . On these kinds of datasets, zero-shot transfer is more an evaluation of CLIP's robustness to distribution shift and domain generalization rather than task generalization. Please see Section for analysis focused on this.

To our knowledge, Visual N-Grams first studied zero-shot transfer to existing image classification datasets in the manner described above. It is also the only other work we are aware of that has studied zero-shot transfer to standard image classification datasets using a generically pre-trained model and serves as the best reference point for contextualizing CLIP. Their approach learns the parameters of a dictionary of 142,806 visual n-grams (spanning 1- to 5- grams) and optimizes these n-grams using a differential version of Jelinek-Mercer smoothing to maximize the probability of all text n-grams for a given image. In order to perform zero-shot transfer, they first convert the text of each of the dataset's class names into its n-gram representation and then compute its probability according to their model, predicting the one with the highest score.

Our focus on studying zero-shot transfer as an evaluation of task learning is inspired by work demonstrating task learning in the field of NLP. To our knowledge first identified task learning as an "unexpected side-effect" when a language model trained to generate Wikipedia articles learned to reliably transliterate names between languages. While GPT-1 focused on pre-training as a transfer learning method to improve supervised fine-tuning, it also included an ablation study demonstrating that the performance of four heuristic zero-shot transfer methods improved steadily over the course of pre-training, without any supervised adaption. This analysis served as the basis for GPT-2 which focused exclusively on studying the task-learning capabilities of language models via zero-shot transfer.

@src https://arxiv.org/abs/2103.14030
@title Swin Transformer: Hierarchical Vision Transformer using Shifted Windows
@section Introduction

Swin Transformer: Hierarchical Vision Transformer using Shifted Windows

Ze Liu Equal contribution. Interns at MSRA. Contact person.

\ v-zeliu1,v-yutlin,yuecao,hanhu,v-yixwe,zhez,stevelin,bainguo\ @microsoft.com

This paper presents a new vision Transformer, called Swin Transformer, that capably serves as a general-purpose backbone for computer vision. Challenges in adapting Transformer from language to vision arise from differences between the two domains, such as large variations in the scale of visual entities and the high resolution of pixels in images compared to words in text. To address these differences, we propose a hierarchical Transformer whose representation is computed with Shifted windows. The shifted windowing scheme brings greater efficiency by limiting self-attention computation to non-overlapping local windows while also allowing for cross-window connection. This hierarchical architecture has the flexibility to model at various scales and has linear computational complexity with respect to image size.

These qualities of Swin Transformer make it compatible with a broad range of vision tasks, including image classification (87.3 top-1 accuracy on ImageNet-1K) and dense prediction tasks such as object detection (58.7 box AP and 51.1 mask AP on COCO test-dev) and semantic segmentation (53.5 mIoU on ADE20K val). Its performance surpasses the previous state-of-the-art by a large margin of +2.7 box AP and +2.6 mask AP on COCO, and +3.2 mIoU on ADE20K, demonstrating the potential of Transformer-based models as vision backbones. The hierarchical design and the shifted window approach also prove beneficial for all-MLP architectures. The code and models are publicly available at https://github.com/microsoft/Swin-Transformer.

Modeling in computer vision has long been dominated by convolutional neural networks (CNNs). Beginning with AlexNet and its revolutionary performance on the ImageNet image classification challenge, CNN architectures have evolved to become increasingly powerful through greater scale , more extensive connections , and more sophisticated forms of convolution . With CNNs serving as backbone networks for a variety of vision tasks, these architectural advances have led to performance improvements that have broadly lifted the entire field.

On the other hand, the evolution of network architectures in natural language processing (NLP) has taken a different path, where the prevalent architecture today is instead the Transformer . Designed for sequence modeling and transduction tasks, the Transformer is notable for its use of attention to model long-range dependencies in the data. Its tremendous success in the language domain has led researchers to investigate its adaptation to computer vision, where it has recently demonstrated promising results on certain tasks, specifically image classification and joint vision-language modeling .

In this paper, we seek to expand the applicability of Transformer such that it can serve as a general-purpose backbone for computer vision, as it does for NLP and as CNNs do in vision. We observe that significant challenges in transferring its high performance in the language domain to the visual domain can be explained by differences between the two modalities. One of these differences involves scale. Unlike the word tokens that serve as the basic elements of processing in language Transformers, visual elements can vary substantially in scale, a problem that receives attention in tasks such as object detection . In existing Transformer-based models , tokens are all of a fixed scale, a property unsuitable for these vision applications.

Another difference is the much higher resolution of pixels in images compared to words in passages of text. There exist many vision tasks such as semantic segmentation that require dense prediction at the pixel level, and this would be intractable for Transformer on high-resolution images, as the computational complexity of its self-attention is quadratic to image size.

To overcome these issues, we propose a general-purpose Transformer backbone, called Swin Transformer, which constructs hierarchical feature maps and has linear computational complexity to image size. As illustrated in Figure (a), Swin Transformer constructs a hierarchical representation by starting from small-sized patches (outlined in gray) and gradually merging neighboring patches in deeper Transformer layers. With these hierarchical feature maps, the Swin Transformer model can conveniently leverage advanced techniques for dense prediction such as feature pyramid networks (FPN) or U-Net . The linear computational complexity is achieved by computing self-attention locally within non-overlapping windows that partition an image (outlined in red). The number of patches in each window is fixed, and thus the complexity becomes linear to image size. These merits make Swin Transformer suitable as a general-purpose backbone for various vision tasks, in contrast to previous Transformer based architectures which produce feature maps of a single resolution and have quadratic complexity.

A key design element of Swin Transformer is its shift of the window partition between consecutive self-attention layers, as illustrated in Figure . The shifted windows bridge the windows of the preceding layer, providing connections among them that significantly enhance modeling power (see Table ). This strategy is also efficient in regards to real-world latency: all query patches within a window share the same key set (The query and key are projection vectors in a self-attention layer. , which facilitates memory access in hardware. In contrast, earlier sliding window based self-attention approaches suffer from low latency on general hardware due to different key sets for different query pixels (While there are efficient methods to implement a sliding-window based convolution layer on general hardware, thanks to its shared kernel weights across a feature map, it is difficult for a sliding-window based self-attention layer to have efficient memory access in practice. . Our experiments show that the proposed shifted window approach has much lower latency than the sliding window method, yet is similar in modeling power (see Tables and ). The shifted window approach also proves beneficial for all-MLP architectures .

The proposed Swin Transformer achieves strong performance on the recognition tasks of image classification, object detection and semantic segmentation. It outperforms the ViT / DeiT and ResNe(X)t models significantly with similar latency on the three tasks. Its 58.7 box AP and 51.1 mask AP on the COCO test-dev set surpass the previous state-of-the-art results by +2.7 box AP (Copy-paste without external data) and +2.6 mask AP (DetectoRS ). On ADE20K semantic segmentation, it obtains 53.5 mIoU on the val set, an improvement of +3.2 mIoU over the previous state-of-the-art (SETR ). It also achieves a top-1 accuracy of 87.3% on ImageNet-1K image classification.

It is our belief that a unified architecture across computer vision and natural language processing could benefit both fields, since it would facilitate joint modeling of visual and textual signals and the modeling knowledge from both domains can be more deeply shared. We hope that Swin Transformer's strong performance on various vision problems can drive this belief deeper in the community and encourage unified modeling of vision and language signals.

@src https://arxiv.org/abs/2104.14294
@title Emerging Properties in Self-Supervised Vision Transformers
@section Introduction

\ Author Guidelines for ICCV Proceedings

The ABSTRACT is to be in fully-justified italicized text, at the top

of the left-hand column, below the author and affiliation

information. Use the word "Abstract" as the title, in 12-point

Times, boldface type, centered relative to the column, initially

capitalized. The abstract is to be in 10-point, single-spaced type.

Leave two blank lines after the Abstract, then begin the main text.

Look at previous ICCV abstracts to get a feel for style and length.

Please follow the steps outlined below when submitting your manuscript to

the IEEE Computer Society Press. This style guide now has several

important modifications (for example, you are no longer warned against the

use of sticky tape to attach your artwork to the paper), so all authors

@src https://arxiv.org/abs/2105.05233
@title Diffusion Models Beat GANs on Image Synthesis
@section Introduction

We show that diffusion models can achieve image sample quality superior to the current state-of-the-art generative models. We achieve this on unconditional image synthesis by finding a better architecture through a series of ablations. For conditional image synthesis, we further improve sample quality with classifier guidance: a simple, compute-efficient method for trading off diversity for fidelity using gradients from a classifier. We achieve an FID of 2.97 on ImageNet 128 MATH 128, 4.59 on ImageNet 256 MATH 256, and 7.72 on ImageNet 512 MATH 512, and we match BigGAN-deep even with as few as 25 forward passes per sample, all while maintaining better coverage of the distribution. Finally, we find that classifier guidance combines well with upsampling diffusion models, further improving FID to 3.94 on ImageNet 256 MATH 256 and 3.85 on ImageNet 512 MATH 512. We release our code at https://github.com/openai/guided-diffusion.

Over the past few years, generative models have gained the ability to generate human-like natural language gpt3 , infinite high-quality synthetic images biggan,stylegan2,vqvae2 and highly diverse human speech and music wavenet,jukebox . These models can be used in a variety of ways, such as generating images from text prompts stackgan,dalle or learning useful feature representations bigbigan,igpt . While these models are already capable of producing realistic images and sound, there is still much room for improvement beyond the current state-of-the-art, and better generative models could have wide-ranging impacts on graphic design, games, music production, and countless other fields.

GANs gan currently hold the state-of-the-art on most image generation tasks biggan,logan,stylegan2 as measured by sample quality metrics such as FID fid , Inception Score inceptionscore and Precision precrecall . However, some of these metrics do not fully capture diversity, and it has been shown that GANs capture less diversity than state-of-the-art likelihood-based models vqvae2,improved,dctransformer . Furthermore, GANs are often difficult to train, collapsing without carefully selected hyperparameters and regularizers biggan,sngan,orthoreg .

While GANs hold the state-of-the-art, their drawbacks make them difficult to scale and apply to new domains. As a result, much work has been done to achieve GAN-like sample quality with likelihood-based models vqvae2,ddpm,dctransformer,vdvae . While these models capture more diversity and are typically easier to scale and train than GANs, they still fall short in terms of visual sample quality. Furthermore, except for VAEs, sampling from these models is slower than GANs in terms of wall-clock time.

Diffusion models are a class of likelihood-based models which have recently been shown to produce high-quality images dickstein,scorematching,ddpm while offering desirable properties such as distribution coverage, a stationary training objective, and easy scalability. These models generate samples by gradually removing noise from a signal, and their training objective can be expressed as a reweighted variational lower-bound ddpm . This class of models already holds the state-of-the-art sde on CIFAR-10 cifar10 , but still lags behind GANs on difficult generation datasets like LSUN and ImageNet. improved found that these models improve reliably with increased compute, and can produce high-quality samples even on the difficult ImageNet 256 MATH 256 dataset using an upsampling stack. However, the FID of this model is still not competitive with BigGAN-deep biggan , the current state-of-the-art on this dataset.

We hypothesize that the gap between diffusion models and GANs stems from at least two factors: first, that the model architectures used by recent GAN literature have been heavily explored and refined; second, that GANs are able to trade off diversity for fidelity, producing high quality samples but not covering the whole distribution. We aim to bring these benefits to diffusion models, first by improving model architecture and then by devising a scheme for trading off diversity for fidelity. With these improvements, we achieve a new state-of-the-art, surpassing GANs on several different metrics and datasets.

The rest of the paper is organized as follows. In Section , we give a brief background of diffusion models based on ddpm and the improvements from improved and ddim , and we describe our evaluation setup. In Section , we introduce simple architecture improvements that give a substantial boost to FID. In Section , we describe a method for using gradients from a classifier to guide a diffusion model during sampling. We find that a single hyperparameter, the scale of the classifier gradients, can be tuned to trade off diversity for fidelity, and we can increase this gradient scale factor by an order of magnitude without obtaining adversarial examples adversarialexamples .

Finally, in Section we show that models with our improved architecture achieve state-of-the-art on unconditional image synthesis tasks, and with classifier guidance achieve state-of-the-art on conditional image synthesis. When using classifier guidance, we find that we can sample with as few as 25 forward passes while maintaining FIDs comparable to BigGAN. We also compare our improved models to upsampling stacks, finding that the two approaches give complementary improvements and that combining them gives the best results on ImageNet 256 MATH 256 and 512 MATH 512.

@src https://arxiv.org/abs/2106.09685
@title LoRA: Low-Rank Adaptation of Large Language Models
@section Introduction

An important paradigm of natural language processing consists of large-scale pre-training on general domain data and adaptation to particular tasks or domains.

As we pre-train larger models, full fine-tuning, which retrains all model parameters, becomes less feasible.

Using GPT-3 175B as an example – deploying independent instances of fine-tuned models, each with 175B parameters, is prohibitively expensive.

We propose Low-Rank Adaptation, or LoRA, which freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, greatly reducing the number of trainable parameters for downstream tasks.

Compared to GPT-3 175B fine-tuned with Adam, LoRA can reduce the number of trainable parameters by 10,000 times and the GPU memory requirement by 3 times.

LoRA performs on-par or better than fine-tuning in model quality on RoBERTa, DeBERTa, GPT-2, and GPT-3, despite having fewer trainable parameters, a higher training throughput, and, unlike adapters, no additional inference latency.

We also provide an empirical investigation into rank-deficiency in language model adaptation, which sheds light on the efficacy of LoRA.

We release a package that facilitates the integration of LoRA with PyTorch models and provide our implementations and model checkpoints for RoBERTa, DeBERTa, and GPT-2 at https://github.com/microsoft/LoRA.

Compared to V1, this draft includes better baselines, experiments on GLUE, and more on adapter latency.

Many applications in natural language processing rely on adapting one large-scale, pre-trained language model to multiple downstream applications.

Such adaptation is usually done via fine-tuning, which updates all the parameters of the pre-trained model.

The major downside of fine-tuning is that the new model contains as many parameters as in the original model.

As larger models are trained every few months, this changes from a mere "inconvenience" for GPT-2 or RoBERTa large to a critical deployment challenge for GPT-3 with 175 billion trainable parameters.

(While GPT-3 175B achieves non-trivial performance with few-shot learning, fine-tuning boosts its performance significantly as shown in app:fewshot_vs_finetune .

Many sought to mitigate this by adapting only some parameters or learning external modules for new tasks.

This way, we only need to store and load a small number of task-specific parameters in addition to the pre-trained model for each task, greatly boosting the operational efficiency when deployed.

However, existing techniques often introduce inference latency by extending model depth or reduce the model's usable sequence length ( sec:existing_solutions_no_good ).

More importantly, these method often fail to match the fine-tuning baselines, posing a trade-off between efficiency and model quality.

We take inspiration from which show that the learned over-parametrized models in fact reside on a low intrinsic dimension.

We hypothesize that the change in weights during model adaptation also has a low "intrinsic rank", leading to our proposed Low-Rank Adaptation (LoRA) approach.

LoRA allows us to train some dense layers in a neural network indirectly by optimizing rank decomposition matrices of the dense layers' change during adaptation instead, while keeping the pre-trained weights frozen, as shown in fig:reparam .

Using GPT-3 175B as an example, we show that a very low rank (i.e., r in fig:reparam can be one or two) suffices even when the full rank (i.e., d) is as high as 12,288, making LoRA both storage- and compute-efficient.

itemize [topsep=6pt,itemsep=3pt,partopsep=4pt, parsep=4pt]

A pre-trained model can be shared and used to build many small LoRA modules for different tasks.

We can freeze the shared model and efficiently switch tasks by replacing the matrices MATH and MATH in fig:reparam , reducing the storage requirement and task-switching overhead significantly.

LoRA makes training more efficient and lowers the hardware barrier to entry by up to 3 times when using adaptive optimizers since we do not need to calculate the gradients or maintain the optimizer states for most parameters.

Instead, we only optimize the injected, much smaller low-rank matrices.

Our simple linear design allows us to merge the trainable matrices with the frozen weights when deployed, introducing no inference latency compared to a fully fine-tuned model, by construction.

LoRA is orthogonal to many prior methods and can be combined with many of them, such as prefix-tuning. We provide an example in app:lora_plus .

We make frequent references to the Transformer architecture and use the conventional terminologies for its dimensions.

We call the input and output dimension size of a Transformer layer MATH .

We use MATH , MATH , MATH , and MATH to refer to the query/key/value/output projection matrices in the self-attention module.

MATH or MATH refers to a pre-trained weight matrix and MATH its accumulated gradient update during adaptation.

We use MATH to denote the rank of a LoRA module.

We follow the conventions set out by and use Adam for model optimization and use a Transformer MLP feedforward dimension MATH .

@src https://arxiv.org/abs/2112.10741
@title GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models
@section Introduction

Diffusion models have recently been shown to generate high-quality synthetic images, especially when paired with a guidance technique to trade off diversity for fidelity. We explore diffusion models for the problem of text-conditional image synthesis and compare two different guidance strategies: CLIP guidance and classifier-free guidance. We find that the latter is preferred by human evaluators for both photorealism and caption similarity, and often produces photorealistic samples. Samples from a 3.5 billion parameter text-conditional diffusion model using classifier-free guidance are favored by human evaluators to those from DALL-E, even when the latter uses expensive CLIP reranking. Additionally, we find that our models can be fine-tuned to perform image inpainting, enabling powerful text-driven image editing. We train a smaller model on a filtered dataset and release the code and weights at https://github.com/openai/glide-text2im https://github.com/openai/glide-text2im .

MATH Equal contribution. Correspondence to alex@openai.com , prafulla@openai.com , aramesh@openai.com

Images, such as illustrations, paintings, and photographs, can often be easily described using text, but can require specialized skills and hours of labor to create. Therefore, a tool capable of generating realistic images from natural language can empower humans to create rich and diverse visual content with unprecedented ease. The ability to edit images using natural language further allows for iterative refinement and fine-grained control, both of which are critical for real world applications.

Recent text-conditional image models are capable of synthesizing images from free-form text prompts, and can compose unrelated objects in semantically plausible ways . However, they are not yet able to generate photorealistic images that capture all aspects of their corresponding text prompts.

On the other hand, unconditional image models can synthesize photorealistic images , sometimes with enough fidelity that humans can't distinguish them from real images . Within this line of research, diffusion models have emerged as a promising family of generative models, achieving state-of-the-art sample quality on a number of image generation benchmarks .

To achieve photorealism in the class-conditional setting, augmented diffusion models with classifier guidance, a technique which allows diffusion models to condition on a classifier's labels. The classifier is first trained on noised images, and during the diffusion sampling process, gradients from the classifier are used to guide the sample towards the label. achieved similar results without a separately trained classifier through the use of classifier-free guidance, a form of guidance that interpolates between predictions from a diffusion model with and without labels.

Motivated by the ability of guided diffusion models to generate photorealistic samples and the ability of text-to-image models to handle free-form prompts, we apply guided diffusion to the problem of text-conditional image synthesis. First, we train a 3.5 billion parameter diffusion model that uses a text encoder to condition on natural language descriptions. Next, we compare two techniques for guiding diffusion models towards text prompts: CLIP guidance and classifier-free guidance. Using human and automated evaluations, we find that classifier-free guidance yields higher-quality images.

We find that samples from our model generated with classifier-free guidance are both photorealistic and reflect a wide breadth of world knowledge. When evaluated by human judges, our samples are preferred to those from DALL-E 87% of the time when evaluated for photorealism, and 69% of the time when evaluated for caption similarity.

While our model can render a wide variety of text prompts zero-shot, it can can have difficulty producing realistic images for complex prompts. Therefore, we provide our model with editing capabilities in addition to zero-shot generation, which allows humans to iteratively improve model samples until they match more complex prompts. Specifically, we fine-tune our model to perform image inpainting, finding that it is capable of making realistic edits to existing images using natural language prompts. Edits produced by the model match the style and lighting of the surrounding context, including convincing shadows and reflections. Future applications of these models could potentially aid humans in creating compelling custom images with unprecedented speed and ease.

We observe that our resulting model can significantly reduce the effort required to produce convincing disinformation or Deepfakes. To safeguard against these use cases while aiding future research, we release a smaller diffusion model and a noised CLIP model trained on filtered datasets.

We refer to our system as , which stands for Guided Language to Image Diffusion for Generation and Editing. We refer to our small filtered model as (filtered).

@src https://arxiv.org/abs/2112.10752
@title High-Resolution Image Synthesis with Latent Diffusion Models
@section Introduction

High-Resolution Image Synthesis with Latent Diffusion Models

Robin Rombach MATH The first two authors contributed equally to this

work. Andreas Blattmann MATH MATH Dominik Lorenz MATH Patrick Esser \, runway Björn Ommer MATH

MATH https://ommer-lab.com/ Ludwig Maximilian University of Munich & IWR, Heidelberg

University, Germany runway https://runwayml.com/ Runway ML

By decomposing the image formation process into a sequential application of

denoising autoencoders, diffusion models (DMs) achieve state-of-the-art synthesis results on image data and beyond.

Additionally, their formulation allows for a guiding mechanism to control the image generation process without retraining.

However, since these models typically operate directly in pixel space, optimization of powerful DMs often consumes hundreds of GPU days and inference is expensive due to

To enable DM training on limited computational resources while retaining their quality and flexibility,

we apply them in the latent space of powerful pretrained autoencoders.

In contrast to previous work, training diffusion models on such a representation allows for the first time to reach a near-optimal point

between complexity reduction and detail preservation,

By introducing cross-attention layers into the model architecture,

we turn diffusion models into powerful and flexible

for general conditioning inputs such as text or bounding boxes and high-resolution synthesis becomes possible in a convolutional manner.

Our latent diffusion models (LDMs) achieve new state-of-the-art scores for image

inpainting and class-conditional image synthesis and highly competitive performance on various tasks, including

text-to-image synthesis, unconditional image generation and super-resolution, while

significantly reducing computational requirements compared to pixel-based DMs.

Image synthesis is one of the computer vision fields with the most spectacular recent development, but also among those with the greatest computational demands. Especially high-resolution synthesis of complex, natural scenes is presently dominated by

scaling up likelihood-based models, potentially containing billions of parameters in autoregressive (AR) transformers .

In contrast, the promising results of GANs have been revealed to be mostly confined to data with comparably limited variability as their adversarial learning procedure does not easily scale to modeling complex, multi-modal distributions.

Recently, diffusion models , which are built from a hierarchy of denoising autoencoders, have shown to achieve impressive results in image synthesis and beyond , and define the state-of-the-art in class-conditional image synthesis and super-resolution . Moreover, even unconditional DMs can readily be applied to tasks such as inpainting and colorization or stroke-based synthesis , in contrast to other types of generative models .

Being likelihood-based models, they do not exhibit mode-collapse and training

instabilities as GANs and, by heavily exploiting parameter sharing,

they can model highly complex distributions of natural images without involving

Democratizing High-Resolution Image Synthesis

DMs belong to the class of likelihood-based models, whose mode-covering behavior makes them prone to spend excessive amounts of capacity (and thus compute resources) on modeling imperceptible details of the data .

Although the reweighted variational objective

by undersampling the initial denoising steps,

DMs are still computationally demanding, since training and evaluating such a model requires repeated function evaluations (and gradient computations) in the high-dimensional space of RGB images.

As an example, training the most powerful DMs often takes hundreds of GPU days ( 150 - 1000 V100 days in )

and repeated evaluations on a noisy version of the input space render also inference expensive, so that producing 50k samples

This has two consequences for the research community and users in general:

requires massive computational resources only available to a small fraction of the field,

Secondly, evaluating an already trained model is also expensive in time and memory, since the same model architecture must

run sequentially for a large number of steps ( 25 - 1000 steps in ).

To increase the accessibility of this powerful model class and at the same time

reduce its significant resource consumption, a method is needed that

reduces the computational complexity for both training and sampling.

Reducing the computational demands of DMs without impairing their performance is, therefore, key to enhance their accessibility.

Our approach starts with the analysis of already trained diffusion models in pixel space:

Fig. shows the rate-distortion trade-off of a trained model.

As with any likelihood-based model, learning can be roughly divided into two stages: First is a perceptual compression stage which removes high-frequency details

In the second stage, the actual generative model learns the semantic and conceptual composition of the data (semantic compression).

We thus aim to first find a perceptually equivalent, but computationally more suitable space , in which we will train diffusion models for high-resolution image synthesis.

we separate training into two distinct phases: First, we train an autoencoder

which provides a lower-dimensional (and thereby efficient) representational space which is perceptually equivalent to the data space.

Importantly, and in contrast to previous work ,

rely on excessive spatial compression, as we train DMs in the learned latent space, which

exhibits better scaling properties with respect to the spatial dimensionality.

The reduced complexity also provides efficient image generation from the latent space with a single network pass.

We dub the resulting model class Latent Diffusion Models (LDMs).

advantage of this approach is that we need to train the universal

autoencoding stage only once and can therefore reuse it for multiple DM

trainings or to explore possibly completely different tasks

This enables efficient exploration of a large number of diffusion models for various image-to-image and text-to-image tasks.

For the latter, we design an architecture that connects transformers to the DM's UNet backbone

and enables arbitrary types of token-based conditioning mechanisms, see Sec. .

In sum, our work makes the following contributions:

(i) In contrast to purely transformer-based approaches , our

method scales more graceful to higher dimensional data and can thus (a) work on a compression level which provides more faithful and detailed reconstructions than previous work (see Fig. ) and (b) can be efficiently applied to high-resolution synthesis of megapixel images.

(ii) We achieve competitive performance on multiple tasks (unconditional image synthesis, inpainting, stochastic super-resolution)

and datasets while significantly lowering computational costs.

Compared to pixel-based diffusion approaches, we also significantly decrease inference costs.

(iii) We show that, in contrast to previous work which learns both an encoder/decoder architecture and a score-based prior simultaneously, our

approach does not require a delicate weighting of reconstruction and generative abilities.

This ensures extremely faithful reconstructions and requires very little regularization of the latent space.

(iv) We find that for densely conditioned tasks such as super-resolution, inpainting and semantic synthesis, our model can be applied in a

convolutional fashion and render large, consistent images of MATH px.

we design a general-purpose conditioning mechanism based on cross-attention, enabling multi-modal training.

We use it to train class-conditional, text-to-image and layout-to-image models.

(vi) Finally, we release pretrained latent diffusion and autoencoding models at which might be reusable for a various tasks besides

@src https://arxiv.org/abs/2201.03545
@title A ConvNet for the 2020s
@section Introduction

Zhuang Liu MATH Work done during an internship at Facebook AI Research. Hanzi Mao MATH Chao-Yuan Wu MATH Christoph Feichtenhofer MATH Trevor Darrell MATH Saining Xie MATH Corresponding author. [2mm]

MATH Facebook AI Research (FAIR) MATH UC Berkeley

The "Roaring 20s" of visual recognition began with the introduction of Vision Transformers (ViTs), which quickly superseded ConvNets as the state-of-the-art image classification model. A vanilla ViT, on the other hand, faces difficulties when applied to general computer vision tasks such as object detection and semantic segmentation. It is the hierarchical Transformers (e.g., Swin Transformers) that reintroduced several ConvNet priors, making Transformers practically viable as a generic vision backbone and demonstrating remarkable performance on a wide variety of vision tasks. However, the effectiveness of such hybrid approaches is still largely credited to the intrinsic superiority of Transformers, rather than the inherent inductive biases of convolutions. In this work, we reexamine the design spaces and test the limits of what a pure ConvNet can achieve. We gradually "modernize" a standard ResNet toward the design of a vision Transformer, and discover several key components that contribute to the performance difference along the way. The outcome of this exploration is a family of pure ConvNet models dubbed ConvNeXt. Constructed entirely from standard ConvNet modules, ConvNeXts compete favorably with Transformers in terms of accuracy and scalability, achieving 87.8% ImageNet top-1 accuracy and outperforming Swin Transformers on COCO detection and ADE20K segmentation, while maintaining the simplicity and efficiency of standard ConvNets.

Code: https://github.com/facebookresearch/ConvNeXt

Looking back at the 2010s, the decade was marked by the monumental progress and impact of deep learning. The primary driver was the renaissance of neural networks, particularly convolutional neural networks (ConvNets). Through the decade, the field of visual recognition successfully shifted from engineering features to designing (ConvNet) architectures. Although the invention of back-propagation-trained ConvNets dates all the way back to the 1980s , it was not until late 2012 that we saw its true potential for visual feature learning. The introduction of AlexNet precipitated the "ImageNet moment" , ushering in a new era of computer vision. The field has since evolved at a rapid speed. Representative ConvNets like VGGNet , Inceptions , ResNe(X)t , DenseNet , MobileNet , EfficientNet and RegNet focused on different aspects of accuracy, efficiency and scalability, and popularized many useful design principles.

The full dominance of ConvNets in computer vision was not a coincidence: in many application scenarios, a "sliding window" strategy is intrinsic to visual processing, particularly when working with high-resolution images. ConvNets have several built-in inductive biases that make them well-suited to a wide variety of computer vision applications. The most important one is translation equivariance, which is a desirable property for tasks like objection detection. ConvNets are also inherently efficient due to the fact that when used in a sliding-window manner, the computations are shared . For many decades, this has been the default use of ConvNets, generally on limited object categories such as digits , faces and pedestrians . Entering the 2010s, the region-based detectors further elevated ConvNets to the position of being the fundamental building block in a visual recognition system.

Around the same time, the odyssey of neural network design for natural language processing (NLP) took a very different path, as the Transformers replaced recurrent neural networks to become the dominant backbone architecture. Despite the disparity in the task of interest between language and vision domains, the two streams surprisingly converged in the year 2020, as the introduction of Vision Transformers (ViT) completely altered the landscape of network architecture design. Except for the initial "patchify" layer, which splits an image into a sequence of patches, ViT introduces no image-specific inductive bias and makes minimal changes to the original NLP Transformers. One primary focus of ViT is on the scaling behavior: with the help of larger model and dataset sizes, Transformers can outperform standard ResNets by a significant margin. Those results on image classification tasks are inspiring, but computer vision is not limited to image classification. As discussed previously, solutions to numerous computer vision tasks in the past decade depended significantly on a sliding-window, fully-convolutional paradigm. Without the ConvNet inductive biases, a vanilla ViT model faces many challenges in being adopted as a generic vision backbone. The biggest challenge is ViT's global attention design, which has a quadratic complexity with respect to the input size. This might be acceptable for ImageNet classification, but quickly becomes intractable with higher-resolution inputs.

Hierarchical Transformers employ a hybrid approach to bridge this gap. For example, the "sliding window" strategy ( attention within local windows) was reintroduced to Transformers, allowing them to behave more similarly to ConvNets. Swin Transformer is a milestone work in this direction, demonstrating for the first time that Transformers can be adopted as a generic vision backbone and achieve state-of-the-art performance across a range of computer vision tasks beyond image classification. Swin Transformer's success and rapid adoption also revealed one thing: the essence of convolution is not becoming irrelevant; rather, it remains much desired and has never faded.

Under this perspective, many of the advancements of Transformers for computer vision have been aimed at bringing back convolutions. These attempts, however, come at a cost: a naive implementation of sliding window self-attention can be expensive ; with advanced approaches such as cyclic shifting , the speed can be optimized but the system becomes more sophisticated in design.

On the other hand, it is almost ironic that a ConvNet already satisfies many of those desired properties, albeit in a straightforward, no-frills way. The only reason ConvNets appear to be losing steam is that (hierarchical) Transformers surpass them in many vision tasks, and the performance difference is usually attributed to the superior scaling behavior of Transformers, with multi-head self-attention being the key component.

Unlike ConvNets, which have progressively improved over the last decade, the adoption of Vision Transformers was a step change. In recent literature, system-level comparisons ( a Swin Transformer a ResNet) are usually adopted when comparing the two. ConvNets and hierarchical vision Transformers become different and similar at the same time: they are both equipped with similar inductive biases, but differ significantly in the training procedure and macro/micro-level architecture design.

we investigate the architectural distinctions between ConvNets and Transformers and try to identify the confounding variables when comparing the network performance.

Our research is intended to bridge the gap between the pre-ViT and post-ViT eras for ConvNets, as well as to test the limits of what a pure ConvNet can achieve.

To do this, we start with a standard ResNet ( ResNet-50) trained with an improved procedure. We gradually "modernize" the architecture to the construction of a hierarchical vision Transformer ( Swin-T). Our exploration is directed by a key question: How do design decisions in Transformers impact ConvNets' performance? We discover several key components that contribute to the performance difference along the way. As a result, we propose a family of pure ConvNets dubbed .

We evaluate s on a variety of vision tasks such as ImageNet classification , object detection/segmentation on COCO , and semantic segmentation on ADE20K . Surprisingly, s , constructed entirely from standard ConvNet modules, compete favorably with Transformers in terms of accuracy, scalability and robustness across all major benchmarks.

ConvNeXt maintains the efficiency of standard ConvNets, and the fully-convolutional nature for both training and testing makes it extremely simple to implement.

We hope the new observations and discussions can challenge some common beliefs and encourage people to rethink the importance of convolutions in computer vision.

@src https://arxiv.org/abs/2201.11903
@title Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
@section Introduction

We explore how generating a chain of thought—a series of intermediate reasoning steps—significantly improves the ability of large language models to perform complex reasoning.

In particular, we show how such reasoning abilities emerge naturally in sufficiently large language models via a simple method called chain-of-thought prompting, where a few chain of thought demonstrations are provided as exemplars in prompting.

Experiments on three large language models show that chain-of-thought prompting improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks.

For instance, prompting a PaLM 540B with just eight chain-of-thought exemplars achieves state-of-the-art accuracy on the GSM8K benchmark of math word problems, surpassing even finetuned GPT-3 with a verifier.

The NLP landscape has recently been revolutionized by language models .

Scaling up the size of language models has been shown to confer a range of benefits, such as improved performance and sample efficiency .

However, scaling up model size alone has not proved sufficient for achieving high performance on challenging tasks such as arithmetic, commonsense, and symbolic reasoning .

This work explores how the reasoning ability of large language models can be unlocked by a simple method motivated by two ideas.

First, techniques for arithmetic reasoning can benefit from generating natural language rationales that lead to the final answer.

Prior work has given models the ability to generate natural language intermediate steps by training from scratch or finetuning a pretrained model , in addition to neuro-symbolic methods that use formal languages instead of natural language .

Second, large language models offer the exciting prospect of in-context few-shot learning via prompting.

That is, instead of finetuning a separate language model checkpoint for each new task, one can simply "prompt" the model with a few input–output exemplars demonstrating the task.

Remarkably, this has been successful for a range of simple question-answering tasks .

Both of the above ideas, however, have key limitations. For rationale-augmented training and finetuning methods, it is costly to create a large set of high quality rationales, which is much more complicated than simple input–output pairs used in normal machine learning.

For the traditional few-shot prompting method used in , it works poorly on tasks that require reasoning abilities, and often does not improve substantially with increasing language model scale .

In this paper, we combine the strengths of these two ideas in a way that avoids their limitations. Specifically, we explore the ability of language models to perform few-shot prompting for reasoning tasks, given a prompt that consists of triples: MATH input, chain of thought, output MATH .

A chain of thought is a series of intermediate natural language reasoning steps that lead to the final output, and we refer to this approach as chain-of-thought prompting. An example prompt is shown in fig:pull-figure .

We present empirical evaluations on arithmetic, commonsense, and symbolic reasoning benchmarks, showing that chain-of-thought prompting outperforms standard prompting, sometimes to a striking degree.

fig:pull-bar-chart illustrates one such result—on the GSM8K benchmark of math word problems , chain-of-thought prompting with 540B outperforms standard prompting by a large margin and achieves new state-of-the-art performance.

A prompting only approach is important because it does not require a large training dataset and because a single model checkpoint can perform many tasks without loss of generality.

This work underscores how large language models can learn via a few examples with natural language data about the task (c.f. automatically learning the patterns underlying inputs and outputs via a large training dataset).

@src https://arxiv.org/abs/2201.12086
@title BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation
@section Introduction

Vision-Language Pre-training (VLP) has advanced the performance for many vision-language tasks.

most existing pre-trained models only excel in either understanding-based tasks or generation-based tasks.

performance improvement has been largely achieved by scaling up the dataset with noisy image-text pairs collected from the web,

which is a suboptimal source of supervision.

a new VLP framework which transfers flexibly to both vision-language understanding and generation tasks.

effectively utilizes the noisy web data by bootstrapping the captions, where a captioner generates synthetic captions and a filter removes the noisy ones.

We achieve state-of-the-art results on a wide range of vision-language tasks,

such as image-text retrieval (+2.7% in average recall@1), image captioning (+2.8% in CIDEr),

also demonstrates strong generalization ability when directly transferred to video-language tasks in a zero-shot manner.

Code, models, and datasets are released.

Vision-language pre-training has recently received tremendous success on various multimodal downstream tasks.

However, existing methods have two major limitations:

(1) Model perspective: most methods either adopt an encoder-based model , or an encoder-decoder model.

However, encoder-based models are less straightforward to directly transfer to text generation tasks ( image captioning), whereas encoder-decoder models have not been successfully adopted for image-text retrieval tasks.

(2) Data perspective: most state-of-the-art methods ( , CLIP , ALBEF , SimVLM ) pre-train on image-text pairs collected from the web.

Despite the performance gain obtained by scaling up the dataset,

our paper shows that the noisy web text is suboptimal for vision-language learning.

To this end, we propose : Bootstrapping Language-Image Pre-training for unified vision-language understanding and generation.

is a new VLP framework which enables a wider range of downstream tasks than existing methods.

It introduces two contributions from the model and data perspective, respectively:

(a) Multimodal mixture of Encoder-Decoder (MED):

a new model architecture for effective multi-task pre-training and flexible transfer learning.

An MED can operate either as a unimodal encoder, or an image-grounded text encoder, or an image-grounded text decoder.

The model is jointly pre-trained with three vision-language objectives: image-text contrastive learning, image-text matching, and image-conditioned language modeling.

a new dataset boostrapping method for learning from noisy image-text pairs.

We finetune a pre-trained MED into two modules: a captioner to produce synthetic captions given web images,

and a filter to remove noisy captions from both the original web texts and the synthetic texts.

We perform extensive experiments and analysis, and make the following key observations.

We show that the captioner and the filter work together to achieve substantial performance improvement on various downstream tasks by bootstrapping the captions.

We also find that more diverse captions yield larger gains.

achieves state-of-the-art performance on a wide range of vision-language tasks,

including image-text retrieval, image captioning, visual question answering, visual reasoning, and visual dialog. We also achieve state-of-the-art zero-shot performance when directly transferring our models to two video-language tasks: text-to-video retrieval and videoQA.

@src https://arxiv.org/abs/2203.02155
@title Training language models to follow instructions with human feedback
@section Introduction

Making language models bigger does not inherently make them better at following a user's intent.

For example, large language models can generate outputs that are untruthful, toxic, or simply not helpful to the user.

In other words, these models are not aligned with their users.

In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback.

Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model behavior, which we use to fine-tune GPT-3 using supervised learning.

We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback.

We call the resulting models InstructGPT.

In human evaluations on our prompt distribution, outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3 , despite having 100x fewer parameters.

Moreover, InstructGPT models show improvements in truthfulness and reductions in toxic output generation while having minimal performance regressions on public NLP datasets.

Even though InstructGPT still makes simple mistakes, our results show that fine-tuning with human feedback is a promising direction for aligning language models with human intent.

Large language models (LMs) can be "prompted" to perform a range of natural language processing (NLP) tasks, given some examples of the task as input. However, these models often express unintended behaviors such as making up facts, generating biased or toxic text, or simply not following user instructions . This is because the language modeling objective used for many recent large LMs—predicting the next token on a webpage from the internet—is different from the objective "follow the user's instructions helpfully and safely" . Thus, we say that the language modeling objective is misaligned. Averting these unintended behaviors is especially important for language models that are deployed and used in hundreds of applications.

We make progress on aligning language models by training them to act in accordance with the user's intention . This encompasses both explicit intentions such as following instructions and implicit intentions such as staying truthful, and not being biased, toxic, or otherwise harmful. Using the language of , we want language models to be helpful (they should help the user solve their task), honest (they shouldn't fabricate information or mislead the user), and harmless (they should not cause physical, psychological, or social harm to people or the environment). We elaborate on the evaluation of these criteria in Section .

We focus on fine-tuning approaches to aligning language models. Specifically, we use reinforcement learning from human feedback (RLHF; ) to fine-tune GPT-3 to follow a broad class of written instructions (see Figure ). This technique uses human preferences as a reward signal to fine-tune our models. We first hire a team of 40 contractors to label our data, based on their performance on a screening test (see Section and Appendix for more details).

We then collect a dataset of human-written demonstrations of the desired output behavior on (mostly English) prompts submitted to the OpenAI API (Specifically, we train on prompts submitted to earlier versions of the InstructGPT models on the OpenAI API Playground, which were trained only using demonstration data. We filter out prompts containing PII. and some labeler-written prompts, and use this to train our supervised learning baselines. Next, we collect a dataset of human-labeled comparisons between outputs from our models on a larger set of API prompts. We then train a reward model (RM) on this dataset to predict which model output our labelers would prefer. Finally, we use this RM as a reward function and fine-tune our supervised learning baseline to maximize this reward using the PPO algorithm . We illustrate this process in Figure . This procedure aligns the behavior of GPT-3 to the stated preferences of a specific group of people (mostly our labelers and researchers), rather than any broader notion of "human values"; we discuss this further in Section . We call the resulting models InstructGPT.

We mainly evaluate our models by having our labelers rate the quality of model outputs on our test set, consisting of prompts from held-out customers (who are not represented in the training data). We also conduct automatic evaluations on a range of public NLP datasets. We train three model sizes (1.3B, 6B, and 175B parameters), and all of our models use the GPT-3 architecture.

Labelers significantly prefer InstructGPT outputs over outputs from GPT-3. On our test set, outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having over 100x fewer parameters. These models have the same architecture, and differ only by the fact that InstructGPT is fine-tuned on our human data. This result holds true even when we add a few-shot prompt to GPT-3 to make it better at following instructions.

Outputs from our 175B InstructGPT are preferred to 175B GPT-3 outputs 85 MATH 3% of the time, and preferred 71 MATH 4% of the time to few-shot 175B GPT-3. InstructGPT models also generate more appropriate outputs according to our labelers, and more reliably follow explicit constraints in the instruction.

InstructGPT models show improvements in truthfulness over GPT-3. On the TruthfulQA benchmark, InstructGPT generates truthful and informative answers about twice as often as GPT-3. Our results are equally strong on the subset of questions that were not adversarially selected against GPT-3. On "closed-domain" tasks from our API prompt distribution, where the output should not contain information that is not present in the input (e.g.\ summarization and closed-domain QA), InstructGPT models make up information not present in the input about half as often as GPT-3 (a 21% vs. 41% hallucination rate, respectively).

InstructGPT shows small improvements in toxicity over GPT-3, but not bias. To measure toxicity, we use the RealToxicityPrompts dataset and conduct both automatic and human evaluations. InstructGPT models generate about 25% fewer toxic outputs than GPT-3 when prompted to be respectful. InstructGPT does not significantly improve over GPT-3 on the Winogender and CrowSPairs datasets.

We can minimize performance regressions on public NLP datasets by modifying our RLHF fine-tuning procedure. During RLHF fine-tuning, we observe performance regressions compared to GPT-3 on certain public NLP datasets, notably SQuAD , DROP , HellaSwag , and WMT 2015 French to English translation . This is an example of an "alignment tax" since our alignment procedure comes at the cost of lower performance on certain tasks that we may care about. We can greatly reduce the performance regressions on these datasets by mixing PPO updates with updates that increase the log likelihood of the pretraining distribution (PPO-ptx), without compromising labeler preference scores.

Our models generalize to the preferences of "held-out" labelers that did not produce any training data. To test the generalization of our models, we conduct a preliminary experiment with held-out labelers, and find that they prefer InstructGPT outputs to outputs from GPT-3 at about the same rate as our training labelers. However, more work is needed to study how these models perform on broader groups of users, and how they perform on inputs where humans disagree about the desired behavior.

Public NLP datasets are not reflective of how our language models are used.

We compare GPT-3 fine-tuned on our human preference data (i.e.\ InstructGPT) to GPT-3 fine-tuned on two different compilations of public NLP tasks: the FLAN and T0 (in particular, the T0++ variant). These datasets consist of a variety of NLP tasks, combined with natural language instructions for each task. On our API prompt distribution, our FLAN and T0 models perform slightly worse than our SFT baseline, and labelers significantly prefer InstructGPT to these models (InstructGPT has a 73.4 MATH winrate vs. our baseline, compared to 26.8 MATH and 29.8 MATH for our version of T0 and FLAN, respectively).

InstructGPT models show promising generalization to instructions outside of the RLHF fine-tuning distribution. We qualitatively probe InstructGPT's capabilities, and find that it is able to follow instructions for summarizing code, answer questions about code, and sometimes follows instructions in different languages, despite these instructions being very rare in the fine-tuning distribution. In contrast, GPT-3 can perform these tasks but requires more careful prompting, and does not usually follow instructions in these domains.

This result is exciting because it suggests that our models are able to generalize the notion of "following instructions." They retain some alignment even on tasks for which they get very little direct supervision signal.

InstructGPT still makes simple mistakes. For example, InstructGPT can still fail to follow instructions, make up facts, give long hedging answers to simple questions, or fail to detect instructions with false premises.

Overall, our results indicate that fine-tuning large language models using human preferences significantly improves their behavior on a wide range of tasks, though much work remains to be done to improve their safety and reliability.

The rest of this paper is structured as follows: We first detail related work in Section , before diving into our method and experiment details in Section , including our high-level methodology ( ), task and dataset details ( and ), human data collection ( ), how we trained our models ( ), and our evaluation procedure ( ). We then present our results in Section , divided into three parts: results on the API prompt distribution ( ), results on public NLP datasets ( ), and qualitative results ( ). Finally we give an extended discussion of our work in Section , including implications for alignment research ( ), what we are aligning to ( ), limitations ( ), open questions ( ), and broader impacts of this work ( ).

@src https://arxiv.org/abs/2203.11171
@title Self-Consistency Improves Chain of Thought Reasoning in Language Models
@section Introduction

Chain-of-thought prompting combined with pre-trained large language models has achieved encouraging results on complex reasoning tasks. In this paper, we propose a new decoding strategy, self-consistency, to replace the naive greedy decoding used in chain-of-thought prompting. It first samples a diverse set of reasoning paths instead of only taking the greedy one, and then selects the most consistent answer by marginalizing out the sampled reasoning paths. Self-consistency leverages the intuition that a complex reasoning problem typically admits multiple different ways of thinking leading to its unique correct answer. Our extensive empirical evaluation shows that self-consistency boosts the performance of chain-of-thought prompting with a striking margin on a range of popular arithmetic and commonsense reasoning benchmarks, including GSM8K (+17.9%), SVAMP (+11.0%), AQuA (+12.2%), StrategyQA (+6.4%) and ARC-challenge (+3.9%).

Although language models have demonstrated remarkable success across

their ability to demonstrate reasoning is often seen as a limitation,

which cannot be overcome solely by increasing model scale .

In an effort to address this shortcoming, have proposed chain-of-thought prompting, where a language model is prompted to generate a series of short sentences that mimic the reasoning process

a person might employ in solving a task.

For example, given the question "If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?", instead of directly responding with "5",

a language model would be prompted to respond with the entire chain-of-thought: "There are 3 cars in the parking lot already. 2 more arrive. Now there are 3 + 2 = 5 cars. The answer is 5.".

It has been observed that chain-of-thought prompting significantly improves model performance across a variety of multi-step reasoning tasks .

In this paper, we introduce a novel decoding strategy called self-consistency to replace the greedy decoding strategy used in chain-of-thought prompting , that further improves language models' reasoning performance by a significant margin.

Self-consistency leverages the intuition that complex reasoning tasks typically admit multiple reasoning paths that reach a correct answer .

The more that deliberate thinking and analysis is required for a problem , the greater the diversity of reasoning paths that can recover the answer.

fig:overview illustrates the self-consistency method with an example.

We first prompt the language model with chain-of-thought prompting,

then instead of greedily decoding the optimal reasoning path, we propose a "sample-and-marginalize" decoding procedure: we first sample from the language model's decoder to generate a diverse set of reasoning paths; each reasoning path might lead to a different final answer, so we determine the optimal answer by marginalizing out the sampled reasoning paths to find the most consistent answer in the final answer set.

Such an approach is analogous to the human experience that if multiple different ways of thinking lead to the same answer, one has greater confidence that the final answer is correct.

Compared to other decoding methods, self-consistency avoids the repetitiveness and local-optimality that plague greedy decoding, while mitigating the stochasticity of a single sampled generation.

Self-consistency is far simpler than prior approaches that either train an additional verifier or train a re-ranker given additional human annotations to improve generation quality .

Instead, self-consistency is entirely unsupervised, works off-the-shelf with pre-trained language models, requires no additional human annotation, and avoids any additional training, auxiliary models or fine-tuning.

Self-consistency also differs from a typical ensemble approach where multiple models are trained and the outputs from each model are aggregated, it acts more like a "self-ensemble" that works on top of a single language model.

We evaluate self-consistency on a wide range of arithmetic and commonsense reasoning tasks over four language models with varying scales: the public UL2-20B and GPT-3-175B , and two densely-activated decoder-only language models: LaMDA-137B and PaLM-540B .

On all four language models, self-consistency improves over chain-of-thought prompting by a striking margin across all tasks.

In particular, when used with PaLM-540B or GPT-3, self-consistency achieves new state-of-the-art levels of performance across arithmetic reasoning tasks, including GSM8K (+17.9% absolute accuracy gains), SVAMP (+11.0%), AQuA (+12.2%), and across commonsense reasoning tasks such as StrategyQA (+6.4%) and ARC-challenge (+3.9%).

In additional experiments, we show self-consistency can robustly boost performance on NLP tasks where adding a chain-of-thought might hurt performance compared to standard prompting .

We also show self-consistency significantly outperforms sample-and-rank, beam search, ensemble-based approaches, and is robust to sampling strategies and imperfect prompts.

@src https://arxiv.org/abs/2204.14198
@title Flamingo: a Visual Language Model for Few-Shot Learning
@section Introduction

Building models that can be rapidly adapted to novel tasks

using only a handful of annotated examples is an open challenge for multimodal machine learning research.

We introduce , a family of Visual Language Models (VLM) with this ability.

We propose key architectural innovations to:

(i) bridge powerful pretrained vision-only and language-only models,

(ii) handle sequences of arbitrarily interleaved visual and textual data,

and (iii) seamlessly ingest images or videos as inputs.

Thanks to their flexibility, models can be trained on large-scale multimodal web corpora containing arbitrarily interleaved text and images, which is key to endow them with in-context few-shot learning capabilities.

We perform a thorough evaluation of our models, exploring and measuring their ability to rapidly adapt to a variety of image and video tasks.

These include open-ended tasks such as visual question-answering, where the model is prompted with a question which it has to answer; captioning tasks, which evaluate the ability to describe a scene or an event;

and close-ended tasks such as multiple-choice visual question-answering.

For tasks lying anywhere on this spectrum, a single model can achieve a new state of the art with few-shot learning, simply by prompting the model with task-specific examples.

On numerous benchmarks, outperforms models fine-tuned on thousands of times more task-specific data.

boxsep=2pt,left=0pt,right=0pt,top=0pt,bottom=0pt,

boxsep=2pt,left=0pt,right=0pt,top=0pt,bottom=0pt,

boxsep=2pt,left=0pt,right=0pt,top=0pt,bottom=0pt,

boxsep=6pt,left=0pt,right=0pt,top=0pt,bottom=0pt,

boxsep=4pt,left=0pt,right=0pt,top=0pt,bottom=0pt,

boxsep=4pt,left=0pt,right=0pt,top=0pt,bottom=0pt,

boxsep=4pt,left=0pt,right=0pt,top=0pt,bottom=0pt,

boxsep=4pt,left=0pt,right=0pt,top=0pt,bottom=0pt,

teaserdialogueuserbox #1 teaserdialogueuserbox

teaserdialogueuserboxwrap #1 teaserdialogueuserboxwrap

teaserdialogueflamingoboxwrap #1 teaserdialogueflamingoboxwrap

teaserdialogueflamingobox #1 teaserdialogueflamingobox

One key aspect of intelligence is the ability to quickly learn to perform a new task given a short instruction .

While initial progress has been made towards a similar capability in computer vision,

the most widely used paradigm still consists of first pretraining on a large amount of supervised data, before fine-tuning the model on the task of interest .

However, successful fine-tuning often requires many thousands of annotated data points.

In addition, it often requires careful per-task hyperparameter tuning and is also resource intensive.

Recently, multimodal vision-language models trained with a contrastive objective have enabled zero-shot adaptation to novel tasks, without the need for fine-tuning.

However, because these models simply provide a similarity score between a text and an image, they can only address limited use cases such as classification, where a finite set of outcomes is provided beforehand.

They crucially lack the ability to generate language, which makes them less suitable to more open-ended tasks such as captioning or visual question-answering.

Others have explored visually-conditioned language generation but have not yet shown good performance in low-data regimes.

We introduce , a Visual Language Model (VLM) that sets a new state of the art in few-shot learning on a wide range of open-ended vision and language tasks, simply by being prompted with a few input/output examples, as illustrated in Figure .

Of the 16 tasks we consider, also surpasses the fine-tuned state of the art on 6 tasks, despite using orders of magnitude less task-specific training data (see Figure ).

To achieve this, Flamingo takes inspiration from recent work on large language models (LMs) which are good few-shot learners .

achieve strong performance on many tasks using only its text interface: a few examples of a task are provided to the model as a prompt, along with a query input, and the model generates a continuation to produce a predicted output for that query.

We show that the same can be done for image and video understanding tasks such as classification, captioning, or question-answering: these can be cast as text prediction problems with visual input conditioning.

The difference from a LM is that the model must be able to ingest a multimodal prompt containing images and/or videos interleaved with text.

visually-conditioned autoregressive text generation models able to ingest a sequence of text tokens interleaved with images and/or videos, and produce text as output.

leverage two complementary pre-trained and frozen models: a vision model which can "perceive" visual scenes and a large LM which performs a basic form of reasoning.

Novel architecture components are added in between these models to connect them in a way that preserves the knowledge they have accumulated during computationally intensive pre-training.

are also able to ingest high-resolution images or videos thanks to a Perceiver-based architecture that can produce a small fixed number of visual tokens per image/video, given a large and variable number of visual input features.

A crucial aspect for the performance of large LMs is that they are trained on a large amount of text data.

This training provides general-purpose generation capabilities that allows these LMs to perform well when prompted with task examples.

Similarly, we demonstrate that the way we train

the models is crucial for their final performance.

They are trained on a carefully chosen =0pt mixture of complementary large-scale multimodal data coming only from the web, without using any data annotated for machine learning purposes.

a model can be directly adapted to vision tasks via simple few-shot learning without any

In summary, our contributions are the following:

(i) We introduce the family of VLMs which can perform various multimodal tasks (such as captioning, visual dialogue, or visual question-answering) from only a few input/output examples.

Thanks to architectural innovations, the models can efficiently accept arbitrarily interleaved visual data and text as input and generate text in an open-ended manner.

(ii) We quantitatively evaluate how models can be adapted to various tasks via few-shot learning.

We notably reserve a large set of held-out benchmarks which have not been used for validation of any design decisions or hyperparameters of the approach.

We use these to estimate unbiased few-shot performance.

(iii) sets a new state of the art in few-shot learning on a wide array of 16 multimodal language and image/video understanding tasks.

On 6 of these 16 tasks, also outperforms the fine-tuned state of the art despite using only 32 task-specific examples, around 1000 times less task-specific training data than the current state of the art.

With a larger annotation budget, can also be effectively fine-tuned to set a new state of the art on five additional challenging benchmarks: VQAv2, VATEX, VizWiz, MSRVTTQA, and HatefulMemes.

@src https://arxiv.org/abs/2205.11487
@title Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding
@section Introduction

We present , a text-to-image diffusion model with an unprecedented degree of photorealism and a deep level of language understanding.

builds on the power of large transformer language models in understanding text and hinges on the strength of diffusion models in high-fidelity image generation.

Our key discovery is that generic large language models (e.g. T5), pretrained on text-only corpora, are surprisingly

effective at encoding text for image synthesis: increasing the size of the language model in boosts both sample fidelity and image-text

alignment much more than increasing the size of the image diffusion model.

achieves a new state-of-the-art FID score of on the COCO dataset, without ever training on COCO, and human raters find samples to be on par with the COCO data itself in image-text alignment.

To assess text-to-image models in greater depth, we introduce , a comprehensive and challenging benchmark for text-to-image models.

With , we compare with recent methods including VQ-GAN+CLIP, Latent Diffusion Models, GLIDE and DALL-E 2, and find that human raters prefer over other models in side-by-side comparisons, both in terms of sample quality and image-text alignment. See https://imagen.research.google/ imagen.research.google for an overview of the results.

Multimodal learning has come into prominence recently, with text-to-image synthesis and image-text contrastive learning at the forefront.

These models have transformed the research community and captured widespread public attention with creative image generation and editing applications .

To pursue this research direction further, we introduce , a text-to-image diffusion model that combines the power of transformer language models (LMs) with high-fidelity diffusion models to deliver an unprecedented degree of photorealism and a deep level of language understanding in text-to-image synthesis.

In contrast to prior work that uses only image-text data for model training , the key finding behind is that text embeddings from large LMs ,

pretrained on text-only corpora, are remarkably effective for text-to-image synthesis.

See fig:full_page_collage for select samples.

comprises a frozen T5-XXL encoder to map input text into a sequence of embeddings and a MATH image diffusion model, followed by two super-resolution diffusion models for generating MATH and MATH images (see fig:main_diagram ). All diffusion models are conditioned on the text embedding sequence and use classifier-free guidance . relies on new sampling techniques to allow usage of large guidance weights without sample quality degradation observed in prior work, resulting in images with higher fidelity and better image-text alignment than previously possible.

While conceptually simple and easy to train, yields surprisingly strong results. outperforms other methods on COCO with zero-shot FID-30K of , significantly outperforming prior work such as GLIDE (at 12.4) and the concurrent work of DALL-E 2 (at 10.4). Our zero-shot FID score is also better than state-of-the-art models trained on COCO, e.g., Make-A-Scene (at 7.6).

Additionally, human raters indicate that generated samples from are on-par in image-text alignment to the reference images on COCO captions.

We introduce , a new structured suite of text prompts for text-to-image evaluation.

enables deeper insights through a multi-dimensional evaluation of text-to-image

models, with text prompts designed to probe different semantic properties of models. These include compositionality, cardinality, spatial relations, the ability to handle complex text prompts or prompts with rare words, and they include creative prompts that push the limits of models' ability to generate highly implausible scenes well beyond the scope of the training data.

With , extensive human evaluation shows that outperforms other recent methods by a significant margin.

We further demonstrate some of the clear advantages of the use of large pre-trained language models over multi-modal embeddings such as CLIP as a text encoder for .

enumerate [noitemsep,nolistsep,leftmargin=0.5cm]

We discover that large frozen language models trained only on text data are surprisingly very effective text encoders for text-to-image generation, and that scaling the size of frozen text encoder improves sample quality significantly more than scaling the size of image diffusion model.

new diffusion sampling technique to leverage high guidance weights and generating more photorealistic and detailed images than previously possible.

We highlight several important diffusion architecture design choices and propose Efficient U-Net, a new architecture variant which is simpler, converges faster and is more memory efficient.

We achieve a new state-of-the-art COCO FID of . Human raters find to be on-par with the reference images in terms of image-text alignment.

We introduce , a new comprehensive and challenging evaluation benchmark for the text-to-image task. On human evaluation, we find to outperform all other work, including the concurrent work of DALL-E 2 .

@src https://arxiv.org/abs/2205.11916
@title Large Language Models are Zero-Shot Reasoners
@section Introduction

Pretrained large language models (LLMs) are widely used in many sub-fields of natural language processing (NLP) and generally known as excellent few-shot learners with task-specific exemplars. Notably, chain of thought (CoT) prompting, a recent technique for eliciting complex multi-step reasoning through step-by-step answer examples, achieved the state-of-the-art performances in arithmetics and symbolic reasoning, difficult system-2 tasks that do not follow the standard scaling laws for LLMs. While these successes are often attributed to LLMs' ability for few-shot learning, we show that LLMs are decent zero-shot reasoners by simply adding "Let's think step by step" before each answer. Experimental results demonstrate that our Zero-shot-CoT, using the same single prompt template, significantly outperforms zero-shot LLM performances on diverse benchmark reasoning tasks including arithmetics (MultiArith, GSM8K, AQUA-RAT, SVAMP), symbolic reasoning (Last Letter, Coin Flip), and other logical reasoning tasks (Date Understanding, Tracking Shuffled Objects), without any hand-crafted few-shot examples, e.g. increasing the accuracy on MultiArith from 17.7% to 78.7% and GSM8K from 10.4% to 40.7% with large-scale InstructGPT model (text-davinci-002), as well as similar magnitudes of improvements with another off-the-shelf large model, 540B parameter PaLM. The versatility of this single prompt across very diverse reasoning tasks hints at untapped and understudied fundamental zero-shot capabilities of LLMs, suggesting high-level, multi-task broad cognitive capabilities may be extracted by simple prompting. We hope our work not only serves as the minimal strongest zero-shot baseline for the challenging reasoning benchmarks, but also highlights the importance of carefully exploring and analyzing the enormous zero-shot knowledge hidden inside LLMs before crafting finetuning datasets or few-shot exemplars.

Scaling up the size of language models has been key ingredients of recent revolutions in natural language processing (NLP) .

The success of large language models (LLMs) is often attributed to (in-context) few-shot or zero-shot learning. It can solve various tasks by simply conditioning the models on a few examples (few-shot) or instructions describing the task (zero-shot).

The method of conditioning the language model is called "prompting" , and designing prompts either manually or automatically has become a hot topic in NLP.

In contrast to the excellent performance of LLMs in intuitive and single-step system-1 tasks with task-specific few-shot or zero-shot prompting , even language models at the scale of 100B or more parameters had struggled on system-2 tasks requiring slow and multi-step reasoning .

To address this shortcoming, have proposed prompting (CoT), which feed LLMs with the step-by-step reasoning examples rather than standard question and answer examples (see Fig. -a).

Such demonstrations facilitate models to generate a reasoning path that decomposes the complex reasoning into multiple easier steps.

Notably with CoT, the reasoning performance then satisfies the scaling laws better and jumps up with the size of the language models. For example, when combined with the 540B parameter PaLM model , prompting significantly increases the performance over standard few-shot prompting across several benchmark reasoning tasks, e.g., GSM8K (17.9% MATH 58.1%).

While the successes of CoT prompting , along those of many other task-specific prompting work , are often attributed to LLMs' ability for few-shot learning , we show that LLMs are decent zero-shot reasoners by adding a simple prompt, Let's think step by step, to facilitate step-by-step thinking before answering each question (see fig_overview_1 ).

Despite the simplicity, our successfully generates a plausible reasoning path in a zero-shot manner and reaches the correct answer in a problem where the standard zero-shot approach fails.

Importantly, our is versatile and task-agnostic, unlike most prior task-specific prompt engineering in the forms of examples (few-shot) or templates (zero-shot) :

it can facilitate step-by-step answers across various reasoning tasks, including arithmetic (MultiArith , GSM8K , AQUA-RAT , and SVAMP ), symbolic reasoning (Last letter and Coin flip), commonsense reasoning (CommonSenseQA and Strategy QA ), and other logical reasoning tasks (Date understanding and Tracking Shuffled Objects from BIG-bench ) without modifying the prompt per task.

We empirically evaluate against other prompting baselines in tab:few_shot . While our underperforms with carefully-crafted and task-specific step-by-step examples, achieves enormous score gains compared to the zero-shot baseline, e.g. from 17.7% to 78.7% on MultiArith and from 10.4% to 40.7% on GSM8K with large-scale InstructGPT model (text-davinci-002).

We also evaluate with another off-the-shelf large model, 540B parameter PaLM, showing similar magnitudes of improvements on MultiArith and GSM8K.

Importantly, with our single fixed prompt, zero-shot LLMs have a significantly better scaling curve comparable to that of the few-shot CoT baseline.

We also show that besides requiring human engineering of multi-step reasoning prompts, their performance deteriorates if prompt example question types and task question type are unmatched, suggesting high sensitivity to per-task prompt designs.

In contrast, the versatility of this single prompt across diverse reasoning tasks hints at untapped and understudied zero-shot fundamental capabilities of LLMs, such as higher-level broad cognitive capabilities like generic logical reasoning .

While the vibrant field of LLMs started out from the premise of excellent few-shot learners , we hope our work encourages more research into uncovering high-level and multi-task zero-shot capabilities hidden inside those models.

@src https://arxiv.org/abs/2205.14135
@title FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness
@section Introduction

Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length.

Approximate attention methods have attempted to address this problem by

trading off model quality to reduce the compute complexity, but often do not achieve wall-clock speedup.

We argue that a missing principle is making attention algorithms IO-aware—accounting for reads and writes between levels of GPU memory.

We propose , an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes between GPU high bandwidth memory (HBM) and GPU on-chip SRAM.

We analyze the IO complexity of , showing that it requires fewer HBM accesses than standard attention, and is optimal for a range of SRAM sizes.

We also extend to block-sparse attention, yielding an approximate attention algorithm that is faster than any existing approximate attention method.

trains Transformers faster than existing baselines: 15% end-to-end wall-clock speedup on BERT-large (seq.\ length 512) compared to the MLPerf 1.1 training speed record, 3 MATH speedup on GPT-2 (seq.\ length 1K), and 2.4 MATH speedup on long-range arena (seq.\ length 1K-4K).

and block-sparse enable longer context in Transformers, yielding higher quality models (0.7 better perplexity on GPT-2 and 6.4 points of lift on long-document classification) and entirely new capabilities: the first Transformers to achieve better-than-chance performance on the Path-X challenge (seq.\ length 16K, 61.4% accuracy) and Path-256 (seq.\ length 64K, 63.1% accuracy).

Transformer models have emerged as the most widely used architecture in applications such as natural language processing and image classification.

Transformers have grown larger and deeper , but equipping them with longer context remains difficult , since the self-attention module at their heart has time and memory complexity quadratic in sequence length.

An important question is whether making attention faster and more memory-efficient can help Transformer models address their runtime and memory challenges for long sequences.

Many approximate attention methods have aimed to reduce the compute and memory requirements of attention.

These methods range from sparse-approximation to low-rank approximation , and their combinations .

Although these methods reduce the compute requirements to linear or near-linear in sequence length, many of them do not display wall-clock speedup against standard attention and have not gained wide adoption. One main reason is that they focus on FLOP reduction (which may not correlate with wall-clock speed) and tend to ignore overheads from memory access (IO).

In this paper, we argue that a missing principle is making attention algorithms IO-aware —that is, carefully accounting for reads and writes to different levels of fast and slow memory (e.g., between fast GPU on-chip SRAM and relatively slow GPU high bandwidth memory, or HBM , Figure left).

On modern GPUs, compute speed has out-paced memory speed , and most operations in Transformers are bottlenecked by memory accesses .

IO-aware algorithms have been critical for similar memory-bound operations, when reading and writing data can account for a large portion of the runtime—such as database joins , image processing , numerical linear algebra , and more .

However, common Python interfaces to deep learning such as PyTorch and Tensorflow do not allow fine-grained control of memory access.

We propose , a new attention algorithm that computes exact attention with far fewer memory accesses.

Our main goal is to avoid reading and writing the attention matrix to and from HBM.

This requires (i) computing the softmax reduction without access to the whole input (ii) not storing the large intermediate attention matrix for the backward pass.

We apply two well-established techniques to address these challenges.

(i) We restructure the attention computation to split the input into blocks and make several passes over input blocks, thus incrementally performing the softmax reduction (also known as tiling). (ii) We store the softmax normalization factor from the forward pass to quickly recompute attention on-chip in the backward pass, which is faster than the standard approach of reading the intermediate attention matrix from HBM.

We implement in CUDA to achieve fine-grained control over memory access and fuse all the attention operations into one GPU kernel.

Even with the increased FLOPs due to recomputation, our algorithm both runs faster (up to 7.6x on GPT-2 , Figure right) and uses less memory—linear in sequence length—than standard attention, thanks to the massively reduced amount of HBM access.

We analyze the IO complexity of , proving that it requires MATH HBM accesses where MATH is the head dimension and MATH is the size of SRAM, as compared to MATH of standard attention.

For typical values of MATH and MATH , requires many times fewer HBM accesses compared to standard attention (up to 9 MATH fewer, as shown in fig:micros ).

Moreover, we provide a lower bound, showing that no exact attention algorithm can asymptotically improve on the number of HBM accesses over all SRAM sizes.

useful primitive for realizing the potential of approximate attention algorithms by overcoming their issues with memory access overhead.

As a proof of concept, we implement block-sparse , a sparse attention algorithm that is 2-4 MATH faster than even , scaling up to sequence length of 64k.

We prove that block-sparse has better IO complexity than by a factor proportional to the sparsity ratio.

We discuss further extensions to other operations (attention on multi-GPU, kernel regression, block-sparse matrix multiply) in sec:discussion .

We open-source to make it easier to build on this primitive. ( code is available at https://github.com/HazyResearch/flash-attention

We empirically validate that speeds up model training and improves model quality by modeling longer context. We also benchmark the runtime and memory footprint of and block-sparse compared to prior attention implementations.

itemize [itemsep=0.1pt,topsep=0pt,leftmargin=*]

Faster Model Training. trains Transformer models faster in wall-clock time. We train BERT-large (seq.\ length 512) 15% faster than the training speed record in MLPerf 1.1 , GPT2 (seq.\ length 1K) 3 MATH faster than baseline implementations from HuggingFace and Megatron-LM , and long-range arena (seq.\ length 1K-4K) 2.4 MATH faster than baselines.

Higher Quality Models. scales Transformers to longer sequences, which improves their quality and enables new capabilities.

We observe a 0.7 improvement in perplexity on GPT-2 and 6.4 points of lift from modeling longer sequences on long-document classification .

enables the first Transformer that can achieve better-than-chance performance on the Path-X challenge, solely from using a longer sequence length (16K).

Block-sparse enables a Transformer to scale to even longer sequences (64K), resulting in the first model that can achieve better-than-chance performance on Path-256.

Benchmarking Attention. is up to 3 MATH faster than the standard attention implementation across common sequence lengths from 128 to 2K and scales up to 64K.

Up to sequence length of 512, is both faster and more memory-efficient than any existing attention method, whereas for sequence length beyond 1K, some approximate attention methods (e.g., Linformer) start to become faster.

On the other hand, block-sparse is faster than all existing approximate attention methods that we know of.

@src https://arxiv.org/abs/2209.14988
@title DreamFusion: Text-to-3D using 2D Diffusion
@section Introduction

Recent breakthroughs in text-to-image synthesis have been driven by diffusion models trained on billions of image-text pairs. Adapting this approach to 3D synthesis would require large-scale datasets of labeled 3D data and efficient architectures for denoising 3D data, neither of which currently exist. In this work, we circumvent these limitations by using a pretrained 2D text-to-image diffusion model to perform text-to-3D synthesis. We introduce a loss based on probability density distillation that enables the use of a 2D diffusion model as a prior for optimization of a parametric image generator. Using this loss in a DeepDream-like procedure, we optimize a randomly-initialized 3D model (a Neural Radiance Field, or NeRF) via gradient descent such that its 2D renderings from random angles achieve a low loss. The resulting 3D model of the given text can be viewed from any angle, relit by arbitrary illumination, or composited into any 3D environment. Our approach requires no 3D training data and no modifications to the image diffusion model, demonstrating the effectiveness of image diffusion models as priors. See for a more immersive view into our 3D results.

Generative image models conditioned on text now support high-fidelity, diverse and controllable image synthesis . These quality improvements have come from large aligned image-text datasets and scalable generative model architectures. Diffusion models are particularly effective at learning high-quality image generators with a stable and scalable denoising objective . Applying diffusion models to other modalities has been successful, but requires large amounts of modality-specific training data . In this work, we develop techniques to transfer pretrained 2D image-text diffusion models to 3D object synthesis, without any 3D data (see Figure ). Though 2D image generation is widely applicable, simulators and digital media like video games and movies demand thousands of detailed 3D assets to populate rich interactive environments. 3D assets are currently designed by hand in modeling software like Blender and Maya3D, a process requiring a great deal of time and expertise. Text-to-3D generative models could lower the barrier to entry for novices and improve the workflow of experienced artists.

3D generative models can be trained on explicit representations of structure like voxels and point clouds , but the 3D data needed is relatively scarce compared to plentiful 2D images.

Our approach learns 3D structure using only a 2D diffusion model trained on images, and sidesteps this issue.

GANs can learn controllable 3D generators from photographs of a single object category, by placing an adversarial loss on 2D image renderings of the output 3D object or scene . Though these approaches have yielded promising results on specific object categories such as faces, they have not yet been demonstrated to support arbitrary text.

Neural Radiance Fields, or NeRF are an approach towards inverse rendering in which a volumetric raytracer is combined with a neural mapping from spatial coordinates to color and volumetric density. NeRF has become a critical tool for neural inverse rendering .

Originally, NeRF was found to work well for "classic" 3D reconstruction tasks: many images of a scene are provided as input to a model, and a NeRF is optimized to recover the geometry of that specific scene, which allows for novel views of that scene from unobserved angles to be synthesized.

Many 3D generative approaches have found success in incorporating NeRF-like models as a building block within a larger generative system .

One such approach is Dream Fields , which uses frozen image-text joint embedding models from CLIP and an optimization-based approach to train NeRFs. This work showed that pretrained 2D image-text models may be used for 3D synthesis, though 3D objects produced by this approach tend to lack realism and accuracy. CLIP has been used to guide other approaches based on voxel grids and meshes .

We adopt a similar approach to Dream Fields, but replace CLIP with a loss derived from distillation of a 2D diffusion model. Our loss is based on probabilty density distillation, minimizing the KL divergence between a family of Gaussian distribution with shared means based on the forward process of diffusion and the score functions learned by the pretrained diffusion model. The resulting Score Distillation Sampling ( ) method enables sampling via optimization in differentiable image parameterizations.

By combining with a NeRF variant tailored to this 3D generation task, generates high-fidelity coherent 3D objects and scenes for a diverse set of user-provided text prompts.

@src https://arxiv.org/abs/2210.03629
@title ReAct: Synergizing Reasoning and Acting in Language Models
@section Introduction

While large language models (LLMs) have demonstrated impressive performance across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics.

In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with and gather additional information from external sources such as knowledge bases or environments.

We apply our approach, named , to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines in addition to improved human interpretability and trustworthiness.

Concretely, on question answering (HotpotQA) and fact verification (Fever), overcomes prevalent issues of hallucination and error propagation in chain-of-thought reasoning

by interacting with a simple Wikipedia API, and generating human-like task-solving trajectories that are more interpretable than baselines without reasoning traces.

Furthermore, on two interactive decision making benchmarks (ALFWorld and WebShop), outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples.

A unique feature of human intelligence is the ability to seamlessly combine task-oriented actions with verbal reasoning (or inner speech, ), which has been theorized to play an important role in human cognition for enabling self-regulation or strategization and maintaining a working memory .

Consider the example of cooking up a dish in the kitchen. Between any two specific actions, we may reason in language in order to track progress ("now that everything is cut, I should heat up the pot of water’’), to handle exceptions or adjust the plan according to the situation ("I don’t have salt, so let me use soy sauce and pepper instead’’), and to realize when external information is needed ("how do I prepare dough? Let me search on the Internet’’).

We may also act (open a cookbook to read the recipe, open the fridge, check ingredients) to support the reasoning and to answer questions ("What dish can I make right now?").

This tight synergy between "acting'’ and "reasoning'’ allows humans to learn new tasks quickly and perform robust decision making or reasoning, even under previously unseen circumstances or facing information uncertainties.

Recent results have hinted at the possibility of combining verbal reasoning with interactive decision making in autonomous systems.

On one hand, properly prompted large language models (LLMs) have demonstrated emergent capabilities to carry out several steps of reasoning traces to derive answers from questions in arithmetic, commonsense, and symbolic reasoning tasks . However, this "chain-of-thought’' reasoning is a static black box, in that the model uses its own internal representations to generate thoughts and is not grounded in the external world,

which limits its ability to reason reactively or update its knowledge. This can lead to issues like fact hallucination and error propagation over the reasoning process (Figure (1b)).

On the other hand, recent work has explored the use of pre-trained language models for planning and acting in interactive environments , with a focus on predicting actions via language priors. These approaches usually convert multi-modal observations into text, use a language model to generate domain-specific actions or plans, and then use a controller to choose or execute them.

However, they do not employ language models to reason abstractly about high-level goals or maintain a working memory to support acting, barring who perform a limited form of verbal reasoning to reiterate spatial facts about the current state.

Beyond such simple embodied tasks to interact with a few blocks, there have not been studies on how reasoning and acting can be combined in a synergistic manner for general task solving, and if such a combination can bring systematic benefits compared to reasoning or acting alone.

In this work, we present , a general paradigm to combine reasoning and acting with language models for solving diverse language reasoning and decision making tasks (Figure ).

prompts LLMs to generate both verbal reasoning traces and actions pertaining to a task in an interleaved manner, which allows the model to perform dynamic reasoning to create, maintain, and adjust high-level plans for acting (reason to act), while also interact with the external environments (e.g.\,Wikipedia) to incorporate additional information into reasoning (act to reason).

We conduct empirical evaluations of and state-of-the-art baselines on four diverse benchmarks: question answering (HotPotQA, ), fact verification (Fever, ), text-based game (ALFWorld, ), and webpage navigation (WebShop, ).

For HotPotQA and Fever, with access to a Wikipedia API that the model can interact with, outperforms vanilla action generation models while being competitive with chain-of-thought reasoning ( ) . The best approach overall is a combination of and that allows for the use of both internal knowledge and externally obtained information during reasoning.

On ALFWorld and WebShop, two or even one-shot prompting is able to outperform imitation or reinforcement learning methods trained with MATH task instances, with an absolute improvement of 34% and 10% in success rates respectively. We also demonstrate the importance of sparse, versatile reasoning in decision making by showing consistent advantages over controlled baselines with actions only.

Besides general applicability and performance boost, the combination of reasoning and acting also contributes to model interpretability, trustworthiness, and diagnosability across all domains, as humans can readily distinguish information from model's internal knowledge versus external environments, as well as inspect reasoning traces to understand the decision basis of model actions.

To summarize, our key contributions are the following:

(1) we introduce , a novel prompt-based paradigm to synergize reasoning and acting in language models for general task solving;

(2) we perform extensive experiments across diverse benchmarks to showcase the advantage of in a few-shot learning setup over prior approaches that perform either reasoning or action generation in isolation;

(3) we present systematic ablations and analysis to understand the importance of acting in reasoning tasks, and reasoning in interactive tasks;

(4) we analyze the limitations of under the prompting setup (i.e.\,limited support of reasoning and acting behaviors), and perform initial finetuning experiments showing the potential of to improve with additional training data.

Scaling up to train and operate on more tasks and combining it with complementary paradigms like reinforcement learning could further unlock the potential of large language models.

Consider a general setup of an agent interacting with an environment for task solving. At time step MATH , an agent receives an observation MATH from the environment and takes an action MATH following some policy MATH , where MATH is the context to the agent. Learning a policy is challenging when the mapping MATH is highly implicit and requires extensive computation.

For example, the agent shown in Figure (1c) is unable to generate the correct final action (Act 4) to finish the QA task as it requires complex reasoning over the trajectory context (Question, Act 1-3, Obs 1-3).

Similarly, the agent shown in Figure (2a) fails to comprehend from the context that sinkbasin 1 does not contain peppershaker 1, thus keep producing hallucinating actions.

The idea of is simple: we augment the agent's action space to MATH , where MATH is the space of language. An action MATH in the language space, which we will refer to as a thought or a reasoning trace, does not affect the external environment, thus leading to no observation feedback. Instead, a thought MATH aims to compose useful information by reasoning over the current context MATH , and update the context MATH to support future reasoning or acting.

As shown in Figure , there could be various types of useful thoughts, e.g.\,decomposing task goals and create action plans (2b, Act 1; 1d, Thought 1), injecting commonsense knowledge relevant to task solving (2b, Act 1), extracting important parts from observations (1d, Thought2, 4), track progress and transit action plans (2b, Act 8), handle exceptions and adjust action plans (1d, Thought 3), and so on.

However, as the language space MATH is unlimited, learning in this augmented action space is difficult and requires strong language priors. In this paper, we mainly focus on

the setup where a frozen large language model, PaLM-540B (We show some GPT-3 results in Appendix , which outperforms PaLM-540B. , is prompted with few-shot in-context examples to generate both domain-specific actions and free-form language thoughts for task solving (Figure (1d), (2b)). Each in-context example is a human trajectory of actions, thoughts, and environment observations to solve a task instance (see Appendix ).

For the tasks where reasoning is of primary importance (Figure (1)), we alternate the generation of thoughts and actions so that the task-solving trajectory consists of multiple thought-action-observation steps.

In contrast, for decision making tasks that potentially involve a large number of actions (Figure (2)), thoughts only need to appear sparsely in the most relevant positions of a trajectory, so we let the language model decide the asynchronous occurrence of thoughts and actions for itself.

Since decision making and reasoning capabilities are integrated into a large language model, enjoys several unique features:

A) Intuitive and easy to design: Designing prompts is straightforward as human annotators just type down their thoughts in language on top of their actions taken. No ad-hoc format choice, thought design, or example selection is used in this paper. We detail prompt design for each task in Sections and .

B) General and flexible: Due to the flexible thought space and thought-action occurrence format, works for diverse tasks with distinct action spaces and reasoning needs, including but not limited to QA, fact verification, text game, and web navigation.

C) Performant and robust: shows strong generalization to new task instances while learning solely from one to six in-context examples, consistently outperforming baselines with only reasoning or acting across different domains. We also show in Section additional benefits when finetuning is enabled, and in Section how performance is robust to prompt selections.

D) Human aligned and controllable: promises an interpretable sequential decision making and reasoning process where humans can easily inspect reasoning and factual correctness. Moreover, humans can also control or correct the agent behavior on the go by thought editing, as shown in Figure in Section .

@src https://arxiv.org/abs/2210.08402
@title LAION-5B: An open large-scale dataset for training next generation image-text models
@section Introduction

Groundbreaking language-vision architectures like CLIP and DALL-E proved the utility of training on large amounts of noisy image-text data, without relying on expensive accurate labels used in standard vision unimodal supervised learning. The resulting models showed capabilities of strong text-guided image generation and transfer to downstream tasks, while performing remarkably at zero-shot classification with noteworthy out-of-distribution robustness. Since then, large-scale language-vision models like ALIGN, BASIC, GLIDE, Flamingo and Imagen made further improvements. Studying the training and capabilities of such models requires datasets containing billions of image-text pairs. Until now, no datasets of this size have been made openly available for the broader research community. To address this problem and democratize research on large-scale multi-modal models, we present LAION-5B - a dataset consisting of 5.85 billion CLIP-filtered image-text pairs, of which 2.32B contain English language. We show successful replication and fine-tuning of foundational models like CLIP, GLIDE and Stable Diffusion using the dataset, and discuss further experiments enabled with an openly available dataset of this scale. Additionally we provide several nearest neighbor indices, an improved web-interface for dataset exploration and subset generation, and detection scores for watermark, NSFW, and toxic content detection. (Project page: https://laion.ai/laion-5b-a-new-era-of-open-large-scale-multi-modal-datasets/ https://laion.ai/laion-5b-a-new-era-of-open-large-scale-multi-modal-datasets/

Learning from multimodal data such as text, images, and audio is a longstanding research challenge in machine learning .

Recently, contrastive loss functions combined with large neural networks have led to breakthroughs in the generalization capabilities of vision and language models .

For instance, OpenAI's CLIP models achieved large gains in zero-shot classification on ImageNet , improving from the prior top-1 accuracy of 11.5% to 76.2%.

In addition, CLIP achieved unprecedented performance gains on multiple challenging distribution shifts .

Inspired by CLIP’s performance, numerous groups have further improved image-text models by increasing the amount of computation and the training set size .

Another recent success of multimodal learning is in image generation, where DALL-E and later models demonstrated the potential of text-guided image generation by producing high-quality images specific to the provided text.

A critical ingredient in this new generation of image-text models is the pre-training dataset.

All of the aforementioned advances rely on large datasets containing hundreds of millions or even billions of image-text pairs, e.g., 400 million for CLIP and 6.6 billion for BASIC .

However, none of these datasets are publicly available.

While OpenAI still released the CLIP models publicly , later papers made neither the pre-training dataset nor the resulting models available to the wider research community .

As a result, research in this area has pooled into a small number of industrial research labs, limiting transparency and impeding research progress.

In this work, we address this challenge and make multimodal training more accessible by assembling a public dataset that is suitable for training large image-text models.

Specifically, we introduce LAION-5B, the largest public image-text dataset containing over 5.8 billion examples (see Table for a comparison).

By starting from Common Crawl and filtering this data source with an existing CLIP model, we derive a dataset consisting of three parts: 2.32 billion English image-text examples, 2.26 billion multilingual examples, and 1.27 billion examples that are not specific to a particular language (e.g., places, products, etc.).

Beyond assembling the dataset, we also explore its ethical implications and flaws that emerge with large-scale data collection.

By releasing LAION-5B publicly, we offer the first opportunity for the community to audit and refine a dataset of this magnitude.

Although YFCC100M contains 100M image-text pairs, it is unclear how well the text matches the image for an average example from the dataset. 's curation procedure reduced YFCC100M to 15M samples.

To validate that LAION-5B is indeed suitable for training large image-text models, we conduct multiple experiments.

We focus on matching the performance of OpenAI's CLIP models because they are the largest publicly released image-text models.

OpenAI's CLIP models were trained on 400 million image-text pairs, and hence we also train CLIP models on a subset of LAION-5B containing the same number of examples ("LAION-400M").

Across a diverse range of problem settings including ImageNet (zero-shot), distribution shifts, VTAB, retrieval, and fine-tuning, our models trained on LAION-400M match or come close to the performance of OpenAI's CLIP models.

Our ViT-L/14 models trained with OpenCLIP are the first open source reproductions of the largest CLIP models released by OpenAI.

Despite these validation results, LAION-5B is not a finished data product.

Due to the immense size of current image-text pre-training datasets, curating LAION-5B for widespread use goes beyond the scope of a single research paper.

Hence we do not only release our dataset, but also our software stack we built for assembling LAION-5B.

We view our initial data release and this paper as a first step on the way towards a widely applicable pre-training dataset for multimodal models.

As a result, we strongly recommend that LAION-5B should only be used for academic research purposes in its current form.

We advise against any applications in deployed systems without carefully investigating behavior and possible biases of models trained on LAION-5B.

The remainder of the paper proceeds as follows.

After reviewing related work, we present our data collection process for LAION-5B in Section .

Section then describes LAION-5B's composition including its various subsets.

To validate LAION-5B, we reproduce and evaluate different image-text models in Section .

Before concluding, we discuss the technical limitations of LAION-5B in Section and safety and ethics concerns in Section .

Learning from multimodal data such as text, images, and audio is a longstanding research challenge in machine learning .

Recently, contrastive loss functions combined with large neural networks have led to breakthroughs in the generalization capabilities of vision and language models .

For instance, OpenAI's CLIP models achieved large gains in zero-shot classification on ImageNet , improving from the prior top-1 accuracy of 11.5% to 76.2%.

In addition, CLIP achieved unprecedented performance gains on multiple challenging distribution shifts .

Inspired by CLIP’s performance, numerous groups have further improved image-text models by increasing the amount of computation and the training set size .

Another recent success of multimodal learning is in image generation, where DALL-E and later models demonstrated the potential of text-guided image generation by producing high-quality images specific to the provided text.

A critical ingredient in this new generation of image-text models is the pre-training dataset.

All of the aforementioned advances rely on large datasets containing hundreds of millions or even billions of image-text pairs, e.g., 400 million for CLIP and 6.6 billion for BASIC .

However, none of these datasets are publicly available.

While OpenAI still released the CLIP models publicly , later papers made neither the pre-training dataset nor the resulting models available to the wider research community .

As a result, research in this area has pooled into a small number of industrial research labs, limiting transparency and impeding research progress.

In this work, we address this challenge and make multimodal training more accessible by assembling a public dataset that is suitable for training large image-text models.

Specifically, we introduce LAION-5B, the largest public image-text dataset containing over 5.8 billion examples (see Table for a comparison).

By starting from Common Crawl and filtering this data source with an existing CLIP model, we derive a dataset consisting of three parts: 2.32 billion English image-text examples, 2.26 billion multilingual examples, and 1.27 billion examples that are not specific to a particular language (e.g., places, products, etc.).

Beyond assembling the dataset, we also explore its ethical implications and flaws that emerge with large-scale data collection.

By releasing LAION-5B publicly, we offer the first opportunity for the community to audit and refine a dataset of this magnitude.

Although YFCC100M contains 100M image-text pairs, it is unclear how well the text matches the image for an average example from the dataset. 's curation procedure reduced YFCC100M to 15M samples.

To validate that LAION-5B is indeed suitable for training large image-text models, we conduct multiple experiments.

We focus on matching the performance of OpenAI's CLIP models because they are the largest publicly released image-text models.

OpenAI's CLIP models were trained on 400 million image-text pairs, and hence we also train CLIP models on a subset of LAION-5B containing the same number of examples ("LAION-400M").

Across a diverse range of problem settings including ImageNet (zero-shot), distribution shifts, VTAB, retrieval, and fine-tuning, our models trained on LAION-400M match or come close to the performance of OpenAI's CLIP models.

Our ViT-L/14 models trained with OpenCLIP are the first open source reproductions of the largest CLIP models released by OpenAI.

Despite these validation results, LAION-5B is not a finished data product.

Due to the immense size of current image-text pre-training datasets, curating LAION-5B for widespread use goes beyond the scope of a single research paper.

Hence we do not only release our dataset, but also our software stack we built for assembling LAION-5B.

We view our initial data release and this paper as a first step on the way towards a widely applicable pre-training dataset for multimodal models.

As a result, we strongly recommend that LAION-5B should only be used for academic research purposes in its current form.

We advise against any applications in deployed systems without carefully investigating behavior and possible biases of models trained on LAION-5B.

The remainder of the paper proceeds as follows.

After reviewing related work, we present our data collection process for LAION-5B in Section .

Section then describes LAION-5B's composition including its various subsets.

To validate LAION-5B, we reproduce and evaluate different image-text models in Section .

Before concluding, we discuss the technical limitations of LAION-5B in Section and safety and ethics concerns in Section .

@src https://arxiv.org/abs/2210.08402
@title LAION-5B: An open large-scale dataset for training next generation image-text models
@section Motivation

For what purpose was the dataset created? Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description.

LAION-5B was created as an open solution to training very large multimodal models such as CLIP or DALL-E. Before the curation of this dataset, the closest in size was YFCC with 100 million image/videos and associated metadata. OpenAI previously used a 15 million sample subset to train a publicly comparable CLIP model, but that pales in comparison to the private 400 million sample dataset they used to train the high-performant CLIP models. At the time of writing this, the ImageNet-1k zero-shot top-1 state-of-the-art, Google’s BASIC, used a dataset of 6.6 billion image-text pairs. With the release of LAION-5B, researchers no longer have to be part of a few selected institutions to study these problems.

Who created the dataset (e.g., which team, research group) and on behalf of which entity (e.g., company, institution, organization)?

This dataset is presented by LAION (Large-scale Artificial Intelligence Open Network), a non-profit research organization aiming to democratize access to large-scale open datasets and powerful machine learning models through the research and development of open-source resources. The communication and organization of this project took place on the open LAION discord server (https://discord.gg/xBPBXfcFHd .

Who funded the creation of the dataset? If there is an associated grant, please provide the name of the grantor and the grant name and number.

This work was sponsored by Hugging Face and Stability AI.

@src https://arxiv.org/abs/2212.06817
@title RT-1: Robotics Transformer for Real-World Control at Scale
@section Introduction

(Authors listed in alphabetical order. Contributions in Appendix . Corresponding emails: \ keerthanapg,kanishkarao,karolhausman\ @google.com .

Brohan MATH , Noah Brown MATH , Justice Carbajal MATH , Yevgen Chebotar MATH , Joseph Dabis MATH , Chelsea Finn MATH , Keerthana Gopalakrishnan MATH , Karol Hausman MATH , Alex Herzog MATH , Jasmine Hsu MATH , Julian Ibarz MATH ,

Brian Ichter MATH , Alex Irpan MATH , Tomas Jackson MATH ,

Sally Jesmonth MATH , Nikhil J Joshi MATH , Ryan Julian MATH , Dmitry Kalashnikov MATH , Yuheng Kuang MATH , Isabel Leal MATH , Kuang-Huei Lee MATH ,

Sergey Levine MATH , Yao Lu MATH , Utsav Malla MATH , Deeksha Manjunath MATH , Igor Mordatch MATH , Ofir Nachum MATH , Carolina Parada MATH , Jodilyn Peralta MATH , Emily Perez MATH , Karl Pertsch MATH , Jornell Quiambao MATH ,

Kanishka Rao MATH , Michael Ryoo MATH , Grecia Salazar MATH , Pannag Sanketi MATH , Kevin Sayed MATH , Jaspiar Singh MATH , Sumedh Sontakke MATH , Austin Stone MATH , Clayton Tan MATH ,

Huong Tran MATH , Vincent Vanhoucke MATH , Steve Vega MATH , Quan Vuong MATH , Fei Xia MATH , Ted Xiao MATH , Peng Xu MATH , Sichun Xu MATH , Tianhe Yu MATH , Brianna Zitkovich MATH

MATH http://g.co/robotics Robotics at Google , MATH https://everydayrobots.com/ Everyday Robots ,

MATH https://research.google/teams/brain/ Google Research, Brain Team

By transferring knowledge from large, diverse, task-agnostic datasets, modern machine learning models can solve specific downstream tasks either zero-shot or with small task-specific datasets to a high level of performance.

While this capability has been demonstrated in other fields such as computer vision, natural language processing or speech recognition, it remains to be shown in robotics, where the generalization capabilities of the models are particularly critical due to the difficulty of collecting real-world robotic data.

We argue that one of the keys to the success of such general robotic models lies with open-ended task-agnostic training, combined with high-capacity architectures that can

absorb all of the diverse, robotic data.

In this paper, we present a model class, dubbed Robotics Transformer, that exhibits promising scalable model properties.

We verify our conclusions in a study of different model classes and their ability to generalize as a function of the data size, model size, and data diversity based on a large-scale data collection on real robots performing real-world tasks.

be found at robotics-transformer1.github.io

End-to-end robotic learning, with either imitation or reinforcement, typically involves collecting task-specific data in either single-task or multi-task settings that are narrowly tailored to the tasks that the robot should perform. This workflow mirrors the classic approach to supervised learning in other domains, such as computer vision and NLP, where task-specific datasets would be collected, labeled, and deployed to solve individual tasks, with little interplay between the tasks themselves.

Recent years have seen a transformation in vision, NLP, and other domains, away from siloed, small-scale datasets and models and towards large, general models pre-trained on broad, large datasets. The keys to the success of such models lie with open-ended task-agnostic training, combined with high-capacity architectures that can absorb all of the knowledge present in large-scale datasets.

If a model can "sponge up" experience to learn general patterns in language or perception, then it can bring them to bear on individual tasks more efficiently.

While removing the need for large task-specific datasets is appealing generally in supervised learning, it is even more critical in robotics, where datasets might require engineering-heavy autonomous operation or expensive human demonstrations. We therefore ask: can we train a single, capable, large multi-task backbone model on data consisting of a wide variety of robotic tasks? And does such a model enjoy the benefits observed in other domains, exhibiting zero-shot generalization to new tasks, environments, and objects?

Building such models in robotics is not easy. Although recent years have seen several large multi-task robot policies proposed in the literature , such models

often have limited breadth of real-world tasks, as with Gato , or focus on training tasks rather than generalization to new tasks, as with recent instruction following methods , or attain comparatively lower performance on new tasks .

The two main challenges lie in assembling the right dataset and designing the right model. While data collection and curation is often the "unsung hero" of many large-scale machine learning projects , this is especially true in robotics, where datasets are often robot-specific and gathered manually . As we will show in our evaluations, good generalization requires datasets that combine both scale and breadth, covering a variety of tasks and settings. At the same time, the tasks in the dataset should be sufficiently well-connected to enable generalization, such that the model can discover the patterns between structural similar tasks and perform new tasks that combine those patterns in novel ways.

We utilize a dataset that we gathered over the course of 17 months with a fleet of 13 robots, containing MATH 130k episodes and over 700 tasks, and we ablate various aspects of this dataset in our evaluation.

The second challenge lies in the design of the model itself. Effective robotic multi-task learning requires a high capacity model, and Transformer models excel in this regard, particularly when it is necessary to learn many tasks conditioned, as in our case, on language instructions. However, robotic controllers must also be efficient enough to run in real time, which presents a major challenge for Transformers in particular. We propose a novel architecture that we call ( ), which

by encoding high-dimensional inputs and outputs, including camera images, instructions and motor commands into compact token representations to be used by the Transformer,

allows for efficient inference at runtime to make real-time control feasible.

Our contribution is the RT-1 model and experiments with this model on a large and broad dataset of real-world robotic tasks. Our experiments not only demonstrate that RT-1 can exhibit significantly improved generalization and robustness compared to prior techniques, but also evaluate and ablate many design choices in both the model and in the composition of the training set.

Our results show that can perform over 700 training instructions at 97% success rate, and can generalize to new tasks, distractors, and backgrounds 25%, 36% and 18% better than the next best baseline, respectively. This level of performance allows us to execute very long-horizon tasks in the SayCan framework, with as many as 50 stages. We further show that can incorporate data from simulation or even other robot types, retaining performance on the original tasks and improving generalization to new scenarios. A short overview of capabilities is presented in Fig. (Helper robots shown in Fig. 1-5 are from http://www.everydayrobots.com Everyday Robots .

@src https://arxiv.org/abs/2212.06817
@title RT-1: Robotics Transformer for Real-World Control at Scale
@section System Overview

The goal of this work is to build and demonstrate a general robot learning system that can absorb large amounts of data and generalize effectively.

We use mobile manipulators from Everyday Robots (everydayrobots.com , which have a 7 degree-of-freedom arm, a two-fingered gripper, and a mobile base (see Fig. (d)). To collect data and evaluate our method, we use three kitchen-based environments: two real office kitchens and a training environment modelled off these real kitchens.

The training environment, shown in Fig. (a), consists of partial counters and is constructed for large scale data collection.

The two real environments, shown in Fig. (b, c), have similar counter tops to the training environment, but vary in lighting, background, and full kitchen geometry (e.g., there may be a cabinet instead of a drawer or a sink may be visible).

We evaluate the performance of our policies across these different environments, measuring the policy's performance and ability to generalize.

Our training data consists of human-provided demonstrations, and we annotate each episode with a textual description of the instruction that the robot just performed.

The instructions usually contain a verb and one or more nouns describing the target objects.

To group these instructions together, we split them into a number of skills (e.g., verbs such as "pick", "open" or "place upright") and objects (e.g., nouns such as "coke can", "apple", or "drawer"). We describe the details of our data collection strategy at scale in Sec. .

Our largest dataset contains over 130k individual demonstrations constituting over 700 distinct task instructions using a large variety of objects (see Fig. (f)). We describe the details of the data collected in Sec. .

One of the main contributions of our system is the network architecture, ( ), an efficient model that can absorb large amounts of data, effectively generalize, and output actions at real-time rates for practical robotic control. takes a short sequence of images and a natural language instruction as input and outputs an action for the robot at each time step.

To this end, the architecture (shown in Figure ) leverages several elements: first the images and text are processed via an ImageNet pretrained convolutional network conditioned on a pretrained embedding of the instruction via FiLM , followed by a Token Learner to compute a compact set of tokens, and finally a Transformer to attend over these tokens and produce discretized action tokens.

The actions consist of seven dimensions for the arm movement (x, y, z, roll, pitch, yaw, opening of the gripper), three dimensions for base movement (x, y, yaw) and a discrete dimension to switch between three modes: controlling the arm, the base, or terminating the episode.

performs closed-loop control and commands actions at MATH Hz until it either yields a "terminate" action or hits a pre-set time step limit.

@src https://arxiv.org/abs/2301.12597
@title BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models
@section Introduction

The cost of vision-and-language pre-training has become increasingly prohibitive due to end-to-end training of large-scale models.

This paper proposes BLIP-2, a generic and efficient pre-training strategy that bootstraps vision-language pre-training from off-the-shelf frozen pre-trained image encoders and frozen large language models.

BLIP-2 bridges the modality gap with a lightweight Querying Transformer, which is pre-trained in two stages.

The first stage bootstraps vision-language representation learning from a frozen image encoder.

The second stage bootstraps vision-to-language generative learning from a frozen language model.

BLIP-2 achieves state-of-the-art performance on various vision-language tasks,

despite having significantly fewer trainable parameters than existing methods.

our model outperforms Flamingo80B by 8.7% on

zero-shot VQAv2 with 54x fewer trainable parameters.

We also demonstrate the model's emerging capabilities of zero-shot image-to-text generation that can follow natural language instructions.

Vision-language pre-training (VLP) research has witnessed a rapid advancement in the past few years,

where pre-trained models with increasingly larger scale have been developed to continuously push the state-of-the-art on various downstream tasks .

However, most state-of-the-art vision-language models incur a high computation cost during pre-training, due to

end-to-end training using large-scale models and datasets.

Vision-language research sits at the intersection between vision and language,

therefore it is naturally expected that vision-language models can harvest from the readily-available unimodal models from the vision and natural language communities.

In this paper, we propose a generic and compute-efficient VLP method by

bootstrapping from off-the-shelf pre-trained vision models and language models.

Pre-trained vision models offer high-quality visual representation.

Pre-trained language models, in particular large language models (LLMs), offer strong language generation and zero-shot transfer abilities.

To reduce computation cost and counteract the issue of catastrophic forgetting, the unimodal pre-trained models remain frozen during the pre-training.

In order to leverage pre-trained unimodal models for VLP, it is key to facilitate cross-modal alignment.

However, since LLMs have not seen images during their unimodal pre-training,

freezing them makes vision-language alignment in particular challenging.

In this regard, existing methods ( Frozen , Flamingo ) resort to an image-to-text generation loss,

which we show is insufficient to bridge the modality gap.

To achieve effective vision-language alignment with frozen unimodal models, we propose a Querying Transformer ( ) pre-trained with a new two-stage pre-training strategy.

is a lightweight transformer which employs a set of learnable query vectors to extract visual features from the frozen image encoder.

It acts as an information bottleneck between the frozen image encoder and the frozen LLM,

where it feeds the most useful visual feature for the LLM to output the desired text.

we perform vision-language representation learning

which enforces the to learn visual representation most relevant to the text.

we perform vision-to-language generative learning by connecting the output of the to a frozen LLM,

and trains the such that its output visual representation can be interpreted by the LLM.

We name our VLP framework as BLIP-2: Bootstrapping Language-Image Pre-training with frozen unimodal models.

BLIP-2 effectively leverages both frozen pre-trained image models and language models.

We bridge the modality gap using a pre-trained in two-stages: representation learning stage and generative learning stage.

BLIP-2 achieves state-of-the-art performance on various vision-language tasks including visual question answering, image captioning, and image-text retrieval.

Powered by LLMs ( OPT , FlanT5 ), BLIP-2 can be prompted to perform zero-shot image-to-text generation that follows natural language instructions, which enables emerging capabilities such as visual knowledge reasoning, visual conversation, etc. (see Figure for examples).

Due to the use of frozen unimodal models and a lightweight ,

BLIP-2 is more compute-efficient than exisiting state-of-the-arts.

For example, BLIP-2 outperforms Flamingo by 8.7% on zero-shot VQAv2, while using 54 MATH fewer trainable parameters.

our results show that BLIP-2 is a generic method that can harvest more advanced unimodal models for better VLP performance.

@src https://arxiv.org/abs/2304.07193
@title DINOv2: Learning Robust Visual Features without Supervision
@section Introduction

All the authors are affiliated to Meta, except Julien Mairal who is affiliated to Inria.

Timothée Darcet and Pierre Fernandez have a co-affiliation with Inria.

Théo Moutakanni has a co-affiliation with Université Paris Saclay.

Alaaeldin El-Nouby has a co-affiliation with Inria and ENS-PSL.

Correspondence: \ qas, timdarcet, theomoutakanni, ajoulin, bojanowski\ @meta.com

The recent breakthroughs in natural language processing for model pretraining on large quantities of data have opened the way for similar foundation models in computer vision.

These models could greatly simplify the use of images in any system by producing general-purpose visual features, i.e., features that work across image distributions and tasks without finetuning.

This work shows that existing pretraining methods, especially self-supervised methods, can produce such features if trained on enough curated data from diverse sources.

We revisit existing approaches and combine different techniques to scale our pretraining in terms of data and model size.

Most of the technical contributions aim at accelerating and stabilizing the training at scale.

In terms of data, we propose an automatic pipeline to build a dedicated, diverse, and curated image dataset instead of uncurated data, as typically done in the self-supervised literature.

In terms of models, we train a ViT model with 1B parameters and distill it into a series of smaller models that surpass the best available general-purpose features, OpenCLIP on most of the benchmarks at image and pixel levels.

Learning task-agnostic pretrained representations have become the standard in Natural Language Processing (NLP) .

One can use these features "as they are", i.e., without fine-tuning, and achieve performances on downstream tasks that are significantly better than those produced by task-specific models .

This success has been fueled by pretraining on large quantities of raw text using pretext objectives, such as language modeling or word vectors , that require no supervision.

Following this paradigm shift in NLP, we expect similar "foundation" models to appear in computer vision .

These models should generate visual features that work out of the box on any task, both at the image level, e.g., image classification, and pixel level, e.g., segmentation.

Most promising efforts towards these foundation models focus on text-guided pretraining, i.e., using a form of textual supervision to guide the training of the features .

This form of text-guided pretraining limits the information that can be retained about the image since captions only approximate the rich information in images, and complex pixel-level information may not surface with this supervision.

Furthermore, these image encoders require aligned text-image corpora and hence, do not offer the flexibility of their text counterparts, that is, to learn from raw data alone.

An alternative to text-guided pretraining is self-supervised learning where features are learned from images alone.

These approaches are conceptually closer to pretext tasks such as language modeling and can capture information at the image and pixel level .

Additionally, the features output by self-supervised models have been shown to exhibit various useful properties, and have enabled enabled a wide variety of applications .

However, despite their potential to learn general-purpose features, most of the advances in self-supervised learning were made in the context of pretraining on a small curated dataset, ImageNet-1k .

Some efforts on scaling these approaches beyond ImageNet-1k have been attempted , but they focused on uncurated datasets, which typically lead to a significant drop in the quality of the features.

This is explained by the lack of control over the data quality and diversity, which are essential to produce good features.

In this work, we explore if self-supervised learning has the potential to learn general-purpose visual features if pretrained on a large quantity of curated data.

We revisit existing discriminative self-supervised approaches that learn features at both the image and patch level, such as iBOT , and we reconsider some of their design choices under the lens of a larger dataset.

Most of our technical contributions are tailored toward stabilizing and accelerating discriminative self-supervised learning when scaling in model and data sizes.

These improvements make our approach around 2 MATH faster and require 3 MATH less memory than similar discriminative self-supervised methods, allowing us to leverage longer training with larger batch sizes.

Regarding pretraining data, we have built an automatic pipeline to filter and rebalance datasets from an extensive collection of uncurated images.

This pipeline is inspired by pipelines used in NLP , where data similarities are used instead of external metadata and do not require manual annotation.

A major difficulty when dealing with images in the wild is to rebalance concepts and avoid overfitting on a few dominant modes.

In this work, a naive clustering approach works reasonably well to resolve this issue.

We gathered a small but diverse corpus of 142M images to validate our approach.

Finally, we provide a variety of pretrained visual models, called , trained with different Vision Transformers (ViT) architectures on our data.

We release all the models and the code to retrain on any data.

We validate the quality of on various computer vision benchmarks at both image and pixel levels as we scale them, as summarized in Fig. .

We conclude that self-supervised pretraining alone is a good candidate for learning transferable frozen features that are competitive with the best openly available weakly-supervised models.

@src https://arxiv.org/abs/2304.08485
@title Visual Instruction Tuning
@section Introduction

Instruction tuning large language models (LLMs) using machine-generated instruction-following data has been shown to improve zero-shot capabilities on new tasks, but the idea is less explored in the multimodal field.

We present the first attempt to use language-only GPT-4 to generate multimodal language-image instruction-following data.

By instruction tuning on such generated data, we introduce : , an end-to-end trained large multimodal model that connects a vision encoder and an LLM for general-purpose visual and language understanding.

To facilitate future research on visual instruction following, we construct two evaluation benchmarks with diverse and challenging application-oriented tasks.

Our experiments show that demonstrates impressive multimodal chat abilities, sometimes exhibiting the behaviors of multimodal GPT-4 on unseen images/instructions, and yields a 85.1% relative score compared with GPT-4 on a synthetic multimodal instruction-following dataset.

When fine-tuned on Science QA, the synergy of and GPT-4 achieves a new state-of-the-art accuracy of 92.53%. We make GPT-4 generated visual instruction tuning data, our model, and code publicly available.

Humans interact with the world through many channels such as vision and language, as each individual channel has a unique advantage in representing and communicating certain concepts, and thus facilitates a better understanding of the world. One of the core aspirations in artificial intelligence is to develop a general-purpose assistant that can effectively follow multi-modal vision-and-language instructions, aligned with human intent to complete various real-world tasks in the wild .

To this end, the community has witnessed an emergent interest in developing language-augmented foundation vision models , with strong capabilities in open-world visual understanding such as classification , detection , segmentation and captioning , as well as visual generation and editing . We refer readers to the Computer Vision in the Wild reading list for a more up-to-date literature compilation . In this line of work, each task is solved independently by one single large vision model, with the task instruction implicitly considered in the model design. Further, language is only utilized to describe the image content. While this allows language to play an important role in mapping visual signals to language semantics—a common channel for human communication, it leads to models that usually have a fixed interface with limited interactivity and adaptability to the user's instructions.

Large language models (LLM), on the other hand, have shown that language can play a wider role: a universal interface for a general-purpose assistant, where various task instructions can be explicitly represented in language and guide the end-to-end trained neural assistant to switch to the task of interest to solve it. For example, the recent success of ChatGPT and GPT-4 have demonstrated the power of aligned LLMs in following human instructions, and have stimulated tremendous interest in developing open-source LLMs. Among them, LLaMA is an open-source LLM that matches the performance of GPT-3. Alpaca , Vicuna , GPT-4-LLM utilize various machine-generated high-quality instruction-following samples to improve the LLM's alignment ability, reporting impressive performance compared with proprietary LLMs. Importantly, this line of work is text-only.

In this paper, we present visual instruction-tuning , the first attempt to extend instruction-tuning to the language-image multimodal space, to pave the way towards building a general-purpose visual assistant. In particular, our paper makes the following contributions:

Multimodal instruction-following data . One key challenge is the lack of vision-language instruction-following data. We present a data reformation perspective and pipeline to convert image-text pairs into an appropriate instruction-following format, using ChatGPT/GPT-4.

Large multimodal models . We develop a large multimodal model (LMM), by connecting the open-set visual encoder of CLIP with the language decoder Vicuna , and fine-tuning end-to-end on our generated instructional vision-language data.

Our empirical study validates the effectiveness of using generated data for LMM instruction-tuning, and suggests practical tips for building a general-purpose instruction-following visual agent. When ensembled with GPT-4, our approach achieves SoTA on the Science QA multimodal reasoning dataset.

Multimodal instruction-following benchmark . We present LLaVA-Bench with two challenging benchmarks, with a diverse selection of paired images, instructions and detailed annotations.

Open-source . We release the following assets to the public: the generated multimodal instruction data, the codebase, the model checkpoints, and a visual chat demo.

@src https://arxiv.org/abs/2304.10592
@title MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models
@section Introduction

The recent GPT-4 has demonstrated extraordinary multi-modal abilities, such as directly generating websites from handwritten text and identifying humorous elements within images. These features are rarely observed in previous vision-language models. However, the technical details behind GPT-4 continue to remain undisclosed.

We believe that the enhanced multi-modal generation capabilities of GPT-4 stem from the utilization of sophisticated large language models (LLM).

To examine this phenomenon, we present MiniGPT-4, which aligns a frozen visual encoder with a frozen advanced LLM, Vicuna, using one projection layer.

Our work, for the first time, uncovers that properly aligning the visual features with an advanced large language model can possess numerous advanced multi-modal abilities demonstrated by GPT-4,

such as detailed image description generation and website creation from hand-drawn drafts.

Furthermore, we also observe other emerging capabilities in MiniGPT-4, including writing stories and poems inspired by given images, teaching users how to cook based on food photos, and so on.

In our experiment, we found that the model trained on short image caption pairs could produce unnatural language outputs (e.g., repetition and fragmentation). To address this problem, we curate a detailed image description dataset in the second stage to finetune the model, which consequently improves the model's generation reliability and overall usability.

Our code, pre-trained model, and collected dataset are available at https://minigpt-4.github.io/.

In recent years, large language models (LLMs) have experienced rapid advancements . With exceptional language understanding capabilities, these models can perform a variety of intricate linguistic tasks in a zero-shot manner. Notably, GPT-4, a large-scale multimodal model, has been recently introduced and demonstrated several impressive capabilities of vision-language understanding and generation . For example, GPT-4 can produce detailed and accurate image descriptions, explain unusual visual phenomena, and even construct websites based on handwritten text instructions.

Although GPT-4 has exhibited remarkable vision language capabilities,

exceptional abilities are still a mystery .

We believe that these impressive skills may stem from the utilization of a more advanced large language model (LLM).

LLMs have demonstrated various emergent abilities, as evidenced in GPT-3's few-shot prompting setup and the findings of Wei et al. (2022) . Such emergent properties are hard to find in smaller-scale models. It is conjectured that these emergent abilities are also applicable to multi-modal models, which could be the foundation of GPT-4's impressive visual description capabilities.

To substantiate our hypothesis, we present a novel vision-language model named MiniGPT-4.

It utilizes an advanced large language model (LLM), Vicuna , which is built upon LLaMA and reported to achieve 90% of ChatGPT's quality as per GPT-4's evaluation, as the language decoder.

In terms of visual perception, we employ the same pretrained vision components of BLIP-2 that consists of a ViT-G/14 from EVA-CLIP and a Q-Former network.

MiniGPT-4 adds a single projection layer to align the encoded visual features with the Vicuna language model and freezes all the other vision and language components.

MiniGPT-4 is initially trained for 20k steps using a batch size of 256 on 4 A100 GPUs, leveraging a combined image captioning dataset that includes images from LAION , Conceptual Captions , and SBU to align visual features with the Vicuna language model.

Nevertheless, merely aligning visual features with the language model (LLM) is inadequate to ensure robust visual conversation capabilities, resembling that of a chatbot.

The presence of underlying noise in raw image-text pairs can lead to subpar language outputs.

Therefore, we collect another 3,500 detailed image description pairs to further fine-tune the model with a designed conversational template in order to improve the naturalness of the generated language and its usability.

In our experiments, we discovered that MiniGPT-4 possesses numerous capabilities similar to those demonstrated by GPT-4.

For instance, MiniGPT-4 can generate intricate image descriptions, create websites based on handwritten text instructions, and explain unusual visual phenomena.

Furthermore, our findings revealed that MiniGPT-4 also has a variety of other intriguing abilities not showcased in the GPT-4 demonstrations.

For example, MiniGPT-4 can directly generate detailed cooking recipes from food photos, write stories or poems inspired by images, write advertisements for products in images, identify problems shown in photos and provide corresponding solutions, and retrieve rich facts about people, movies, or art directly from images, among other capabilities.

These abilities are absent in previous vision-language models like Kosmos-1 and BLIP-2 that use less powerful language models.

This further validates that integrating visual features with an advanced language model is one of the keys to enhancing vision-language models.

We present a summary of our key findings:

Our research reveals with compelling evidence that by aligning visual features with advanced large language models like Vicuna, MiniGPT-4 can achieve advanced vision-language capabilities comparable to those exhibited in the GPT-4 demonstrations.

Our findings suggest that training merely one projection layer can effectively align a pretrained vision encoder with the large language model. Our MiniGPT-4 only requires training approximately 10 hours on 4 A100 GPUs.

We discovered that simply aligning visual features with large language models using short image caption pairs is not sufficient for developing a well-performing model and leads to unnatural language generation. Further finetuning with a small but detailed image description pairs can address this limitation and significantly improves its usability.

@src https://arxiv.org/abs/2305.10601
@title Tree of Thoughts: Deliberate Problem Solving with Large Language Models
@section Introduction

Language models are increasingly being deployed for general problem solving across a wide range of tasks, but are still confined to token-level, left-to-right decision-making processes during inference. This means they can fall short in tasks that require exploration, strategic lookahead, or where initial decisions play a pivotal role.

To surmount these challenges, we introduce a new framework for language model inference, "Tree of Thoughts" (ToT), which generalizes over the popular "Chain of Thought" approach to prompting language models, and enables exploration over coherent units of text ("thoughts") that serve as intermediate steps toward problem solving.

ToT allows LMs to perform deliberate decision making by considering multiple different reasoning paths and self-evaluating choices to decide the next course of action, as well as looking ahead or backtracking when necessary to make global choices.

Our experiments show that ToT significantly enhances language models’ problem-solving abilities on three novel tasks requiring non-trivial planning or search: Game of 24, Creative Writing, and Mini Crosswords.

For instance, in Game of 24, while GPT-4 with chain-of-thought prompting only solved 4% of tasks, our method achieved a success rate of 74%. Code repo with all prompts: https://github.com/princeton-nlp/tree-of-thought-llm.

Originally designed to generate text, scaled-up versions of language models (LMs) such as GPT and PaLM have been shown to be increasingly capable of performing an ever wider range of tasks

requiring mathematical, symbolic, commonsense, and knowledge reasoning. It is perhaps surprising that underlying all this progress is still the original autoregressive mechanism for generating text, which makes token-level decisions one by one and in a left-to-right fashion.

Is such a simple mechanism sufficient for a LM to be built toward a general problem solver?

If not, what problems would challenge the current paradigm, and what should be alternative mechanisms?

The literature on human cognition provides some clues to answer these questions.

Research on "dual process" models suggests that people have two modes in which they engage with decisions – a fast, automatic, unconscious mode ("System 1") and a slow, deliberate, conscious mode ("System 2") .

These two modes have previously been connected to a variety of mathematical models used in machine learning. For example, research on reinforcement learning in humans and other animals has explored the circumstances under which they engage in associative "model free" learning or more deliberative "model based" planning .

The simple associative token-level choices of LMs are also reminiscent of "System 1", and thus might benefit from augmentation by a more deliberate "System 2" planning process that (1) maintains and explores diverse alternatives for current choices instead of just picking one, and (2) evaluates its current status and actively looks ahead or backtracks to make more global decisions.

To design such a planning process, we return to the origins of artificial intelligence (and cognitive science), drawing inspiration from the planning processes explored by Newell, Shaw, and Simon starting in the 1950s . Newell and colleagues characterized

as search through a combinatorial problem space, represented as a tree. We thus propose the Tree of Thoughts (ToT) framework for general problem solving with language models. As Figure illustrates, while existing methods (detailed below) sample continuous language sequences for problem solving, ToT actively maintains a tree of thoughts, where each thought is a coherent language sequence that serves as an intermediate step toward problem solving (Table ). Such a high-level semantic unit allows the LM to self-evaluate the progress different intermediate thoughts make towards solving the problem through a deliberate reasoning process that is also instantiated in language (Figures , , ). This implementation of search heuristics via LM self-evaluation and deliberation is novel, as previous search heuristics are either programmed or learned. Finally, we combine this language-based capability to generate and evaluate diverse thoughts with search algorithms, such as breadth-first search (BFS) or depth-first search (DFS), which allow systematic exploration of the tree of thoughts with lookahead and backtracking.

Empirically, we propose three new problems that challenge existing LM inference methods even with the state-of-the-art language model, GPT-4 : Game of 24, Creative Writing, and Crosswords (Table ).

These tasks require deductive, mathematical, commonsense, lexical reasoning abilities, and a way to incorporate systematic planning or search.

We show ToT obtains superior results on all three tasks by being general and flexible enough to support different levels of thoughts, different ways to generate and evaluate thoughts, and different search algorithms that adapt to the nature of different problems. We also analyze how such choices affect model performances via systematic ablations and discuss future directions to better train and use LMs.

@src https://arxiv.org/abs/2305.14314
@title QLoRA: Efficient Finetuning of Quantized LLMs
@section Introduction

We present , an efficient finetuning approach that reduces memory usage enough to finetune a 65B parameter model on a single 48GB GPU while preserving full 16-bit finetuning task performance. backpropagates gradients through a frozen, 4-bit quantized pretrained language model into Low Rank Adapters (LoRA). Our best model family, which we name , outperforms all previous openly released models on the Vicuna benchmark, reaching 99.3% of the performance level of ChatGPT while only requiring 24 hours of finetuning on a single GPU. introduces a number of innovations to save memory without sacrificing performance: (a) 4-bit NormalFloat (NF4), a new data type that is information theoretically optimal for normally distributed weights (b) to reduce the average memory footprint by quantizing the quantization constants, and (c) to manage memory spikes. We use to finetune more than 1,000 models, providing a detailed analysis of instruction following and chatbot performance across 8 instruction datasets, multiple model types (LLaMA, T5), and model scales that would be infeasible to run with regular finetuning (e.g. 33B and 65B parameter models). Our results show that QLoRA finetuning on a small high-quality dataset leads to state-of-the-art results, even when using smaller models than the previous SoTA. We provide a detailed analysis of chatbot performance based on both human and GPT-4 evaluations showing that GPT-4 evaluations are a cheap and reasonable alternative to human evaluation. Furthermore, we find that current chatbot benchmarks are not trustworthy to accurately evaluate the performance levels of chatbots. A lemon-picked analysis demonstrates where fails compared to ChatGPT. We release all of our models and code, including CUDA kernels for 4-bit training. (https://github.com/artidoro/qlora and https://github.com/TimDettmers/bitsandbytes

Finetuning large language models (LLMs) is a highly effective way to improve their performance, and to add desirable or remove undesirable behaviors .

However, finetuning very large models is prohibitively expensive; regular 16-bit finetuning of a LLaMA 65B parameter model requires more than 780 GB of GPU memory. While recent quantization methods can reduce the memory footprint of LLMs , such techniques only work for inference and break down during training .

We demonstrate for the first time that it is possible to finetune a quantized 4-bit model without any performance degradation. Our method, , uses a novel high-precision technique to quantize a pretrained model to 4-bit,

then adds a small set of learnable Low-rank Adapter weights

Elo ratings for a competition between models, averaged for 10,000 random initial orderings. The winner of a match is determined by GPT-4 which declares which response is better for a given prompt of the . 95% confidence intervals are shown ( MATH ). After GPT-4, Guanaco 33B and 65B win the most matches, while Guanaco 13B scores better than Bard.

that are tuned by backpropagating gradients through the quantized weights.

reduces the average memory requirements of finetuning a 65B parameter model from MATH 780GB of GPU memory to MATH 48GB without degrading the runtime or predictive performance compared to a 16-bit fully finetuned baseline.

This marks a significant shift in accessibility of LLM finetuning: now the largest publicly available models to date finetunable on a single GPU.

Using , we train the family of models, with the second best model reaching 97.8% of the performance level of ChatGPT on the Vicuna benchmark, while being trainable in less than 12 hours on a single consumer GPU; using a single professional GPU over 24 hours we achieve 99.3% with our largest model, essentially closing the gap to ChatGPT on the Vicuna benchmark. When deployed, our smallest model (7B parameters) requires just 5 GB of memory and outperforms a 26 GB Alpaca model by more than 20 percentage points on the Vicuna benchmark (Table ).

introduces multiple innovations designed to reduce memory use without sacrificing performance: (1) 4-bit NormalFloat, an information theoretically optimal quantization data type for normally distributed data that yields better empirical results than 4-bit Integers and 4-bit Floats. (2) , a method that quantizes the quantization constants, saving an average of about 0.37 bits per parameter (approximately 3 GB for a 65B model). (3) , using NVIDIA unified memory to avoid the gradient checkpointing memory spikes that occur when processing a mini-batch with a long sequence length. We combine these contributions into a better tuned LoRA approach that includes adapters at every network layer and thereby avoids almost all of the accuracy tradeoffs seen in prior work.

's efficiency enables us to perform an in-depth study of instruction finetuning and chatbot performance on model scales that would be impossible using regular finetuning due to memory overhead. Therefore, we train more than 1,000 models across several instruction tuning datasets, model architectures, and sizes between 80M to 65B parameters. In addition to showing that recovers 16-bit performance ( ) and training a state-of-the-art chatbot, , ( ), we also analyze trends in the trained models. First, we find that data quality is far more important than dataset size, e.g., a 9k sample dataset (OASST1) outperformed a 450k sample dataset (FLAN v2, subsampled) on chatbot performance, even when both are meant to support instruction following generalization. Second, we show that strong Massive Multitask Language Understanding (MMLU) benchmark performance does not imply strong Vicuna chatbot benchmark performance and vice versa—in other words, dataset suitability matters more than size for a given task.

Furthermore, we also provide a extensive analysis of chatbot performance that uses both human raters and GPT-4 for evaluation. We use tournament-style benchmarking where models compete against each other in matches to produce the best response for a given prompt. The winner of a match is judged by either GPT-4 or human annotators. The tournament results are aggregated into Elo scores which determine the ranking of chatbot performance. We find that GPT-4 and human evaluations largely agree on the rank of model performance in the tournaments, but we also find there are instances of strong disagreement. As such, we highlight that model-based evaluation while providing a cheap alternative to human-annotation also has its uncertainties.

We augment our chatbot benchmark results with a qualitative analysis of models. Our analysis highlights success and failure cases that were not captured by the quantitative benchmarks.

We release all model generations with human and GPT-4 annotations to facilitate further study. We open-source our codebase and CUDA kernels and integrate our methods into the Hugging Face transformers stack , making them easily accessible to all. We release a collection of adapters for 7/13/33/65B size models, trained on 8 different instruction following datasets, for a total of 32 different open sourced, finetuned models.

@src https://arxiv.org/abs/2305.18290
@title Direct Preference Optimization: Your Language Model is Secretly a Reward Model
@section Introduction

While large-scale unsupervised language models (LMs) learn broad world knowledge and some reasoning skills, achieving precise control of their behavior is difficult due to the completely unsupervised nature of their training.

Existing methods for gaining such steerability collect human labels of the relative quality of model generations and fine-tune the unsupervised LM to align with these preferences, often with reinforcement learning from human feedback (RLHF).

However, RLHF is a complex and often unstable procedure, first fitting a reward model that reflects the human preferences, and then fine-tuning the large unsupervised LM using reinforcement learning to maximize this estimated reward without drifting too far from the original model.

In this paper, we leverage a mapping between reward functions and optimal policies to show that this constrained reward maximization problem can be optimized exactly with a single stage of policy training, essentially solving a classification problem on the human preference data. In this paper we introduce a new parameterization of the reward model in RLHF that enables extraction of the corresponding optimal policy in closed form, allowing us to solve the standard RLHF problem with only a simple classification loss.

The resulting algorithm, which we call Direct Preference Optimization (DPO), is stable, performant, and computationally lightweight, eliminating the need for fitting a reward model, sampling from the LM during fine-tuning or performing significant hyperparameter tuning.

Our experiments show that DPO can fine-tune LMs to align with human preferences as well as or better than existing methods. Notably, fine-tuning with DPO exceeds PPO-based RLHF in ability to control sentiment of generations, and matches or improves response quality in summarization and single-turn dialogue while being substantially simpler to implement and train.

Large unsupervised language models (LMs) trained on very large datasets

acquire surprising capabilities . However, these models are trained on data generated by humans with a wide variety of goals, priorities, and skillsets. Some of these goals and skillsets may not be desirable to imitate; for example, while we may want our AI coding assistant to understand common programming mistakes in order to correct them, nevertheless, when generating code, we would like to bias our model toward the (potentially rare) high-quality coding ability present in its training data. Similarly, we might want our language model to be aware of a common misconception believed by 50% of people, but we certainly do not want the model to claim this misconception to be true in 50% of queries about it! In other words, selecting the model's desired responses and behavior from its very wide knowledge and abilities is crucial to building AI systems that are safe, performant, and controllable . While existing methods typically steer LMs to match human preferences using reinforcement learning (RL), we will show that the RL-based objective used by existing methods can be optimized exactly with a simple binary cross-entropy objective, greatly simplifying the preference learning pipeline.

At a high level, existing methods instill the desired behaviors into a language model using curated sets of human preferences representing the types of behaviors that humans find safe and helpful. This preference learning stage occurs after an initial stage of large-scale unsupervised pre-training on a large text dataset. While the most straightforward approach to preference learning is supervised fine-tuning on human demonstrations of high quality responses, the most successful class of methods is reinforcement learning from human (or AI) feedback (RLHF/RLAIF; ). RLHF methods fit a reward model to a dataset of human preferences and then use RL to optimize a language model policy to produce responses assigned high reward without drifting excessively far from the original model. While RLHF produces models with impressive conversational and coding abilities, the RLHF pipeline is considerably more complex than supervised learning, involving training multiple LMs and sampling from the LM policy in the loop of training, incurring significant computational costs.

In this paper, we show how to directly optimize a language model to adhere to human preferences, without explicit reward modeling or reinforcement learning.

( ) , an algorithm that implicitly optimizes the same objective as existing RLHF algorithms (reward maximization with a KL-divergence constraint) but is simple to implement and straightforward to train. Intuitively, the update increases the relative log probability of preferred to dispreferred responses, but it incorporates a dynamic, per-example importance weight that prevents the model degeneration that we find occurs with a naive probability ratio objective. Like existing algorithms, relies on a theoretical preference model (such as the Bradley-Terry model; ) that measures how well a given reward function aligns with empirical preference data. However, while existing methods use the preference model to define a preference loss to train a reward model and then train a policy that optimizes the learned reward model, uses a change of variables to define the preference loss as a function of the policy directly. Given a dataset of human preferences over model responses, can therefore optimize a policy using a simple binary cross entropy objective, without learning an explicit, standalone reward model or sampling from the policy during training producing the optimal policy to an implicit reward function fit to the preference data .

Our main contribution is ( ), a simple RL-free algorithm for training language models from preferences. Our experiments show that is at least as effective as existing methods, including PPO-based RLHF, for learning from preferences in tasks such as sentiment modulation, summarization, and dialogue, using language models with up to 6B parameters.

@src https://arxiv.org/abs/2305.20050
@title Let's Verify Step by Step
@section Introduction

In recent years, large language models have greatly improved in their ability to perform complex multi-step reasoning. However, even state-of-the-art models still regularly produce logical mistakes. To train more reliable models, we can turn either to outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step. Given the importance of training reliable models, and given the high cost of human feedback, it is important to carefully compare the both methods. Recent work has already begun this comparison, but many questions still remain. We conduct our own investigation, finding that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset. Our process-supervised model solves 78% of problems from a representative subset of the MATH test set. Additionally, we show that active learning significantly improves the efficacy of process supervision. To support related research, we also release PRM800K, the complete dataset of 800,000 step-level human feedback labels used to train our best reward model.

Large language models are capable of solving tasks that require complex multi-step reasoning by generating solutions in a step-by-step chain-of-thought format . However, even state-of-the-art models are prone to producing falsehoods — they exhibit a tendency to invent facts in moments of uncertainty . These hallucinations are particularly problematic in domains that require multi-step reasoning, since a single logical error is enough to derail a much larger solution. Detecting and mitigating hallucinations is essential to improve reasoning capabilities.

One effective method involves training reward models to discriminate between desirable and undesirable outputs. The reward model can then be used in a reinforcement learning pipeline or to perform search via rejection sampling . While these techniques are useful, the resulting system is only as reliable as the reward model itself. It is therefore important that we study how to most effectively train reliable reward models.

In closely related work, describe two distinct methods for training reward models: outcome supervision and process supervision. Outcome-supervised reward models (ORMs) are trained using only the final result of the model's chain-of-thought, while process-supervised reward models (PRMs) receive feedback for each step in the chain-of-thought. There are compelling reasons to favor process supervision. It provides more precise feedback, since it specifies the exact location of any errors that occur. It also has several advantages relevant to AI alignment: it is easier for humans to interpret, and it more directly rewards models for following a human-endorsed chain-of-thought. Within the domain of logical reasoning, models trained with outcome supervision regularly use incorrect reasoning to reach the correct final answer . Process supervision has been shown to mitigate this misaligned behavior .

Despite these advantages, found that outcome supervision and process supervision led to similar final performance in the domain of grade school math. We conduct our own detailed comparison of outcome and process supervision, with three main differences: we use a more capable base model, we use significantly more human feedback, and we train and test on the more challenging MATH dataset .

We show that process supervision can train much more reliable reward models than outcome supervision. We use our state-of-the-art PRM to solve MATH of problems from a representative subset of the MATH test set.

We show that a large reward model can reliably approximate human supervision for smaller reward models, and that it can be used to efficiently conduct large-scale data collection ablations.

We show that active learning leads to a MATH improvement in the data efficiency of process supervision.

We release our full process supervision dataset, PRM800K, to promote related research.

@src https://arxiv.org/abs/2307.01952
@title SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis
@section Introduction

We present , a latent diffusion model for text-to-image synthesis.

Compared to previous versions of , leverages a three times larger UNet backbone: The increase of model parameters is mainly due to more attention blocks and a larger cross-attention context as uses a second text encoder.

We design multiple novel conditioning schemes and train on multiple aspect ratios.

We also introduce a refinement model which is

used to improve the visual fidelity of samples generated by using a post-hoc image-to-image technique.

We demonstrate that shows drastically improved performance compared to previous versions of and achieves results competitive with those of black-box state-of-the-art image generators.

In the spirit of promoting open research and fostering transparency in large model training and evaluation, we provide access to code and model weights.

The last year has brought enormous leaps in deep generative modeling across various data domains, such as natural language , audio , and visual media .

In this report, we focus on the latter and unveil , a drastically improved version of .

is a latent text-to-image diffusion model (DM) which serves as the foundation for an array of recent advancements in, e.g.,

3D classification , controllable image editing ,

image personalization , synthetic data augmentation ,

graphical user interface prototyping , etc. Remarkably, the scope of applications has been extraordinarily extensive, encompassing fields as diverse as music generation and reconstructing images from fMRI brain scans .

User studies demonstrate that consistently surpasses all previous versions of by a significant margin (see fig:userstudyandmodel ).

the design choices which lead to this boost in performance encompassing i) a 3 MATH larger UNet-backbone

compared to previous models ( subsec:archi_and_scale ), ii)

two simple yet effective additional conditioning techniques ( subsec:condtricks ) which do not require any form of additional supervision, and iii) a separate diffusion-based refinement model which applies a noising-denoising process to the latents produced by to improve the visual quality of its samples ( subsec:putting ).

A major concern in the field of visual media creation is that while black-box-models

recognized as state-of-the-art, the opacity of their architecture

prevents faithfully assessing and validating their performance. This lack of transparency hampers reproducibility, stifles innovation, and prevents the community from building upon these models to further the progress of science and art. Moreover,

these closed-source strategies make it challenging to assess the biases and limitations of these models in an impartial and objective way, which is crucial for their responsible and ethical deployment. With we are releasing an open model that achieves competitive performance with black-box image generation models (see fig:mjcomp_categories & fig:mjcomp_challenges ).

@src https://arxiv.org/abs/2307.08691
@title FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning
@section Introduction

Scaling Transformers to longer sequence lengths has been a major problem in the

last several years, promising to improve performance in language modeling and

high-resolution image understanding, as well as to unlock new applications in

The attention layer is the main bottleneck in scaling to longer sequences, as

its runtime and memory increase quadratically in the sequence length.

hierarchy to bring significant memory saving (linear instead of quadratic) and

runtime speedup (2-4 MATH compared to optimized baselines), with no approximation.

However, is still not nearly as fast as optimized matrix-multiply

(GEMM) operations, reaching only 25-40% of the theoretical maximum FLOPs/s.

We observe that the inefficiency is due to suboptimal work partitioning between

different thread blocks and warps on the GPU, causing either low-occupancy or

We propose , with better work partitioning to address these issues.

In particular, we (1) tweak the algorithm to reduce the number of non-matmul

FLOPs (2) parallelize the attention computation, even for a single head, across

different thread blocks to increase occupancy, and (3) within each thread block,

distribute the work between warps to reduce communication through shared memory.

These yield around 2 MATH speedup compared to , reaching 50-73% of the

theoretical maximum FLOPs/s on A100 and getting close to the efficiency of GEMM

We empirically validate that when used end-to-end to train GPT-style models,

reaches training speed of up to 225 TFLOPs/s per A100 GPU (72% model

FLOPs utilization). ( is available at https://github.com/Dao-AILab/flash-attention

Scaling up the context length of Transformers is a

challenge, since the attention layer at their heart has runtime and

memory requirements quadratic in the input sequence length.

Ideally, we would like to go beyond the standard 2k sequence length limit to

train models to understand books, high resolution images, and long-form videos.

Just within the last year, there have been several language models with much

longer context than before: GPT-4 with context

length 32k, MosaicML's MPT with context length 65k, and Anthropic's

Emerging use cases such as long document querying and story writing have

demonstrated a need for models with such long context.

To reduce the computational requirement of attention on such long context, there

have been numerous methods proposed to approximate

Though these methods have seen some use cases, as far as we know, most

large-scale training runs still use standard attention.

Motivated by this, proposed to reorder the

attention computation and leverages classical techniques (tiling, recomputation)

to significantly speed it up and reduce memory usage from quadratic to linear in

This yields 2-4 MATH wall-clock time speedup over optimized baselines, up to

10-20 MATH memory saving, with no approximation, and as a result has

seen wide adoption in large-scale training and inference of Transformers.

However, context length increases even more, is still not nearly as

efficient as other primitives such as matrix-multiply (GEMM).

In particular, while is already 2-4 MATH faster than a standard

attention implementation, the forward pass only reaches 30-50% of the

theoretical maximum FLOPs/s of the device ( fig:benchmark_attn_fwd ), while

the backward pass is even more challenging, reaching only 25-35% of maximum

throughput on A100 GPU ( fig:benchmark_attn_bwd ).

In contrast, optimized GEMM can reach up to 80-90% of the theoretical maximum

Through careful profiling, we observe that still has suboptimal work

partitioning between different thread blocks and warps on the GPU, causing

either low-occupancy or unnecessary shared memory reads/writes.

Building on , we propose with better parallelism and work

partitioning to address these challenges.

In subsec:algo , we tweak the algorithms to reduce the number of non-matmul FLOPs while not

While the non-matmul FLOPs only account for a small fraction of the total FLOPs,

they take longer to perform as GPUs have specialized units for matrix multiply,

and as a result the matmul throughput can be up to 16 MATH higher than non-matmul

It is thus important to reduce non-matmul FLOPs and spend as much time as

We propose to parallelize both the forward pass and backward pass along

the sequence length dimension, in addition to the batch and number of heads

dimension. This increases occupancy (utilization of GPU resources) in the case

where the sequences are long (and hence batch size is often small).

Even within one block of attention computation, we partition the work

between different warps of a thread block to reduce communication and shared

In sec:experiments , we empirically validate that yields significant speedup compared to

even . Benchmarks on different settings (with or without causal mask,

different head dimensions) show that achieves around 2 MATH speedup over

, reaching up to 73% of the theoretical max throughput in the

forward pass, and up to 63% of the theoretical max throughput in the backward pass.

When used end-to-end to train GPT-style models, we reach training speed of up to

@src https://arxiv.org/abs/2307.15818
@title RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control
@section Introduction

High-capacity models pretrained on broad web-scale datasets provide an effective and powerful platform for a wide range of downstream tasks: large language models can enable not only fluent text generation but emergent problem-solving and creative generation of prose and code , while vision-language models enable open-vocabulary visual recognition and can even make complex inferences about object-agent interactions in images . Such semantic reasoning, problem solving, and visual interpretation capabilities would be tremendously useful for generalist robots that must perform a variety of tasks in real-world environments. However, it is unclear how robots should acquire such capabilities. While a brute force approach might entail collecting millions of robotic interaction trials, the most capable language and vision-language models are trained on billions of tokens and images from the web – an amount unlikely to be matched with robot data in the near future. On the other hand, directly applying such models to robotic tasks is also difficult: such models reason about semantics, labels, and textual prompts, whereas robots require grounded low-level actions, such as Cartesian end-effector commands. While a number of recent works have sought to incorporate language models (LLMs) and vision-language models (VLMs) into robotics , such methods generally address only the "higher level" aspects of robotic planning, essentially taking the role of a state machine that interprets commands and parses them into individual primitives (such as picking and placing objects),

which are then executed by separate low-level controllers that themselves do not benefit from the rich semantic knowledge of Internet-scale models during training. Therefore, in this paper we ask: can large pretrained vision-language models be integrated directly into low-level robotic control to boost generalization and enable emergent semantic reasoning?

To this end, we explore an approach that is both simple and surprisingly effective: we directly train vision-language models designed for open-vocabulary visual question answering and visual dialogue to output low-level robot actions, along with solving other Internet-scale vision-language tasks. Although such models are typically trained to produce natural language tokens, we can train them on robotic trajectories by tokenizing the actions into text tokens and creating "multimodal sentences" that "respond" to robotic instructions paired with camera observations by producing corresponding actions.

In this way, vision-language models can be directly trained to act as instruction following robotic policies. This simple approach is in contrast with prior alternatives for incorporating VLMs into robot policies or designing new vision-language-action architectures from scratch : instead, pre-existing vision-language models, with already-amortized significant compute investment, are trained without any new parameters to output text-encoded actions. We refer to this category of models as ( ) models.

We instantiate models by building on the protocol proposed for RT-1 , using a similar dataset, but expanding the model to use a large vision-language backbone. Hence we refer to our model as ( ). We provide an overview in Figure .

We observe that robotic policies derived from such vision-language models exhibit a range of remarkable capabilities, combining the physical motions learned from the robot data with the ability to interpret images and text learned from web data into a single model.

Besides the expected benefit of dramatically improving generalization to novel objects and semantically varied instructions, we observe a number of emergent capabilities. While the model's physical skills are still limited to the distribution of skills seen in the robot data, the model acquires the ability to deploy those skills in new ways by interpreting images and language commands using knowledge gleaned from the web.

Some example highlights are shown in Figure . The model is able to re-purpose pick and place skills learned from robot data to place objects near semantically indicated locations, such as specific numbers or icons, despite those cues not being present in the robot data. The model can also interpret relations between objects to determine which object to pick and where to place it, despite no such relations being provided in the robot demonstrations. Furthermore, if we augment the command with chain of thought prompting, the model is able to make even more complex semantic inferences, such as figuring out which object to pick up for use as an improvised hammer (a rock), or which type of drink is best suited for someone who is tired (an energy drink).

Our main contribution is , a family of models derived from fine-tuning large vision-language models trained on web-scale data to directly act as generalizable and semantically aware robotic policies. Our experiments investigate models with up to 55B parameters trained on Internet data and instruction-annotated robotic trajectories from previous work . Over the course of 6k robotic evaluations, we show that enable significant improvements to generalization over objects, scenes, and instructions, and exhibit a breadth of emergent capabilities inherited from web-scale vision-language pretraining.

@src https://arxiv.org/abs/2310.06770
@title SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
@section Introduction

Language models have outpaced our ability to evaluate them effectively, but for their future development it is essential to study the frontier of their capabilities.

We find real-world software engineering to be a rich, sustainable, and challenging testbed for evaluating the next generation of language models.

To this end, we introduce , an evaluation framework consisting of MATH software engineering problems drawn from real GitHub issues and corresponding pull requests across MATH popular Python repositories.

Given a codebase along with a description of an issue to be resolved, a language model is tasked with editing the codebase to address the issue.

Resolving issues in frequently requires understanding and coordinating changes across multiple functions, classes, and even files simultaneously, calling for models to interact with execution environments, process extremely long contexts and perform complex reasoning that goes far beyond traditional code generation tasks.

Our evaluations show that both state-of-the-art proprietary models and our fine-tuned model can resolve only the simplest issues. The best-performing model, Claude 2, is able to solve a mere MATH % of the issues.

Advances on represent steps towards LMs that are more practical, intelligent, and autonomous.

Correspondence to mailto:carlosej@princeton.edu carlosej@princeton.edu ,

mailto:johnby@stanford.edu johnby@stanford.edu .

( Data, code, and leaderboard at https://swebench.com swebench.com

Language models (LMs) are rapidly being deployed in commercial products such as chatbots and coding assistants.

At the same time, existing benchmarks have become saturated and fail to capture the frontier of what state-of-the-art LMs can and cannot do.

There is a need for challenging benchmarks that more accurately reflect real-world applications of LMs to help shape their future development and usage .

Building a good benchmark is difficult since tasks must be challenging enough to stump existing models, but model predictions must also be easy to verify .

Coding tasks are appealing as they pose challenging problems to LMs yet generated solutions can be easily verified by running unit tests.

However, existing coding benchmarks, such as HumanEval , mostly involve self-contained problems that can be solved in a few lines of code.

In the real world, software engineering is not as simple.

Fixing a bug might involve navigating a large repository, understanding the interplay between functions in different files, or spotting a small error in convoluted code.

Inspired by this, we introduce , a benchmark that evaluates LMs in a realistic software engineering setting.

As shown in Figure , models are tasked to resolve issues (typically a bug report or a feature request) submitted to popular GitHub repositories.

Each task requires generating a patch describing changes to apply to the existing codebase.

The revised codebase is then evaluated using the repository's testing framework.

offers several advantages over existing LM programming benchmarks.

These include, a realistic setting that utilizes user-submitted issues and solutions, diverse inputs featuring unique code problems from MATH repositories, a robust framework for execution-based evaluation, and the ability to continuously update the benchmark with new instances, requiring minimal human intervention.

We evaluate multiple state-of-the-art LMs on and find that they fail to solve all except the simplest issues.

Using a BM25 retriever, Claude 2 is only able to resolve MATH of the issues.

In addition to our contributions include the release of a training dataset, -train, which is essential for advancing open model development in this challenging domain.

This dataset comprises a collection of MATH non-testing task instances derived from MATH repositories.

Utilizing -train, we release two fine-tuned models, MATH b and MATH b, based on the CodeLlama model.

We find that in some settings MATH b is competitive with Claude 2 and is capable of processing contexts exceeding MATH tokens.

is a benchmark featuring GitHub issues from popular repositories that report bugs or request new features, and pull requests that make changes to the repository to resolve these issues.

The task is to generate a pull request that addresses a given issue and passes tests related to the issue.

@src https://arxiv.org/abs/2310.06770
@title SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
@section High Level Overview

Pull request scraping. From a list of the top MATH most downloaded PyPI libraries during August 2023 (https://hugovk.github.io/top-pypi-packages/ https://hugovk.github.io/top-pypi-packages/ , we select the top MATH packages, identify each library's corresponding open-source GitHub repository, verify which packages have licenses allowing for free software use, and collect all PRs for these repositories via the GitHub developer API.

We elect to source problems from well-trafficked repositories because widespread use usually suggests that the repository has extensive documentation, structured open-source development guidelines, and working, well-formatted code.

Task instance construction. We construct candidate task instances from PRs that satisfy three conditions.

A Merged status indicates that the PR's associated code changes were accepted and incorporated into its parent repository.

Second, the PR resolves one or more issues in its repository.

An issue is defined according to its canonical usage in GitHub as a digital ticket for tracking bugs, enhancements, or any general development goals for a software project.

We scan a PR's title, body, and commit messages for linked issues (i.e. "fixes # MATH ").

Third, the PR must introduce one or more new tests.

A new test is counted when a PR's code changes edits a file path containing a testing-related keyword (e.g. "test", "testing").

A PR that satisfies these criteria is then converted into a candidate task instance such as the example in Figure .

The codebase MATH is identified by the repository's owner/name moniker and the pull request's base commit.

Recovering the actual codebase from this information is straightforward.

We create mirrors of the original GitHub repositories, where each mirror is uniquely identified as owner__name.

Cloning a repository's corresponding mirror and checking out the base commit yields MATH in its pre-PR state.

The problem statement MATH is an aggregate of all related issues' titles and descriptions along with any subsequent comments written before the timestamp of the PR's initial commit to avoid leakage of solution details.

A PR's code changes are separated into a test patch and a gold patch MATH . MATH consists of all tests from files edited in the test patch.

As shown in Figure , both MATH and MATH are stored as patch files.

Further details about parsing PR and semantic data is in Appendix .

Execution-based validation. We verify the usability of a task instance via execution.

For each candidate, we first define a virtual environment to serve as an execution context, then install MATH before applying any patches, and finally run MATH once before and once after the solution MATH is applied.

A candidate is removed from consideration for the final dataset if any step in the verification process fails.

In addition, to ensure that a solution MATH is non-trivial, we compare the pre-solution and post-solution validation logs to check for whether there are one or more tests in MATH where the status changes from fail to pass.

Lastly, we exclude task instances with tests that invoke newly created functions or classes first introduced in the solution MATH .

Since naming such constructs is typically an arbitrary process and usually not explicitly specified in the problem statement, resolving tests such as these may be an impossible task even for human developers.

Information about execution contexts, codebase installation, determining test statuses from logs, and more are in Appendix .

Continuous Updates. 's collection process is easily extensible to any open source code repositories, allowing for easy and low-maintenance extension to new programming languages and code domains.

This design also provides with temporal robustness; as new language models trained on more recent source code are released over time, can simply be updated to produce new task instances based on PRs created after any LM's training date.

@src https://arxiv.org/abs/2310.11511
@title Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection
@section Introduction

Despite their remarkable capabilities, large language models (LLMs) often produce responses containing factual inaccuracies due to their sole reliance on the parametric knowledge they encapsulate.

Retrieval-Augmented Generation (RAG), an ad hoc approach that augments LMs with retrieval of relevant knowledge, decreases such issues.

However, indiscriminately retrieving and incorporating a fixed number of retrieved passages, regardless of whether retrieval is necessary, or passages are relevant, diminishes LM versatility or can lead to unhelpful response generation.

We introduce a new framework called Self-Reflective Retrieval-Augmented Generation ( ) that enhances an LM's quality and factuality through retrieval and self-reflection.

Our framework trains a single arbitrary LM that adaptively retrieves passages on-demand, and generates and reflects on retrieved passages and its own generations using special tokens, called reflection tokens. Generating reflection tokens makes the LM controllable during the inference phase, enabling it to tailor its behavior to diverse task requirements.

Experiments show that (7B and 13B parameters) significantly outperforms state-of-the-art LLMs and retrieval-augmented models on a diverse set of tasks.

Specifically, outperforms ChatGPT and retrieval-augmented Llama2-chat on Open-domain QA, reasoning and fact verification tasks, and it shows significant gains in improving factuality and citation accuracy for long-form generations relative to these models. ( Our code and trained models are available at https://selfrag.github.io/ .

State-of-the-art LLMs continue to struggle with factual errors despite their increased model and data scale .

Retrieval-Augmented Generation (RAG) methods (Figure left; ) augment the input of LLMs with relevant retrieved passages, reducing factual errors in knowledge-intensive tasks .

However, these methods may hinder the versatility of LLMs or introduce unnecessary or off-topic passages that lead to low-quality generations since they retrieve passages indiscriminately regardless of whether the factual grounding is helpful.

Moreover, the output is not guaranteed to be consistent with retrieved relevant passages since the models are not explicitly trained to leverage and follow facts from provided passages.

This work introduces Self-Reflective Retrieval-augmented Generation ( ) to improve an LLM's generation quality, including its factual accuracy without hurting its versatility, via on-demand retrieval and self-reflection.

We train an arbitrary LM in an end-to-end manner to learn to reflect on its own generation process given a task input by generating both task output and intermittent special tokens (i.e., reflection tokens). Reflection tokens are categorized into retrieval and critique tokens to indicate the need for retrieval and its generation quality respectively (Figure right).

In particular, given an input prompt and preceding generations, first determines if augmenting the continued generation with retrieved passages would be helpful. If so,

it outputs a retrieval token that calls a retriever model on demand (Step 1).

Subsequently, concurrently processes multiple retrieved passages, evaluating their relevance and then generating corresponding task outputs (Step 2). It then generates critique tokens to criticize its own output and choose best one (Step 3) in terms of factuality and overall quality.

This process differs from conventional RAG (Figure left), which consistently retrieves a fixed number of documents for generation regardless of the retrieval necessity (e.g., the bottom figure example does not require factual knowledge) and never second visits the generation quality.

Moreover, provides citations for each segment with its self-assessment of whether the output is supported by the passage, leading to easier fact verification.

trains an arbitrary LM to generate text with reflection tokens by unifying them as the next token prediction from the expanded model vocabulary.

We train our generator LM on a diverse collection of text interleaved with reflection tokens and retrieved passages.

Reflection tokens, inspired by reward models used in reinforcement learning , are inserted offline into the original corpus by a trained critic model. This eliminates the need to host a critic model during training, reducing overhead.

The critic model, in part, is supervised on a dataset of input, output, and corresponding reflection tokens collected by prompting a propriety LM (i.e., GPT-4; ).

While we draw inspiration from studies that use control tokens

our trained LM uses critique tokens to assess its own predictions after each generated segment as an integral part of the generation output.

decoding algorithm to satisfy hard or soft constraints, which are defined by reflection token predictions.

In particular, our inference-time algorithm enables us to (1) flexibly adjust retrieval frequency for different downstream applications and (2) customize models' behaviors to user preferences by leveraging reflection tokens through segment-level beam search using the weighted linear sum of the reflection token probabilities as segment score.

Empirical results on six tasks, including reasoning and long-form generation, demonstrate that significantly outperforms pre-trained and instruction-tuned LLMs that have more parameters and widely adopted RAG approaches with higher citation accuracy.

In particular, outperforms retrieval-augmented ChatGPT on four tasks, Llama2-chat and Alpaca on all tasks.

Our analysis demonstrates the effectiveness of training and inference with reflection tokens for overall performance improvements as well as test-time model customizations (e.g., balancing the trade-off between citation previsions and completeness).

@src https://arxiv.org/abs/2310.11511
@title Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection
@section Problem Formalization and Overview

Formally, given input MATH , we train to sequentially generate textual outputs MATH consisting of multiple segments MATH , where MATH indicates a sequence of tokens for the MATH -th segment. (

In this paper, we treat one sentence as a segment in our experiments, but our framework is applicable to any segment unit (i.e., sub-sentence).

Generated tokens in MATH include text from the original vocabulary as well as the reflection tokens (Table ).

Figure and Algorithm present an overview of at inference.

For every MATH and preceding generation MATH , the model decodes a retrieval token to evaluate the utility of retrieval. If retrieval is not required, the model predicts the next output segment, as it does in a standard LM.

If retrieval is needed, the model generates: a critique token to evaluate the retrieved passage's relevance, the next response segment, and a critique token to evaluate if the information in the response segment is supported by the passage. Finally, a new critique token evaluates the overall utility of the response. (We follow in using a "perceived" utility value that is independent of retrieved passages.

To generate each segment, processes multiple passages in parallel and uses its own generated reflection tokens to enforce soft constraints (Section ) or hard control (Algorithm ) over the generated task output.

For instance, in Figure (right), the retrieved passages MATH is selected at the first time step since MATH does not provide direct evidence ( is Irrelevant ) and MATH output is only partially supported while MATH are fully supported.

enables an arbitrary LM to generate text with reflection tokens by unifying them as next token predictions from the expanded model vocabulary (i.e., the original vocabulary plus reflection tokens). Specifically, we train the generator model on a curated corpus with interleaving passages retrieved by a retriever and reflection tokens predicted by a critic model (summarized in Appendix Algorithm ). We train to generate reflection tokens for evaluating retrieved passages and the quality of a given task output (Section ).

Using the critic model, we update the training corpus by inserting reflection tokens into task outputs offline.

Subsequently, we train the final generator model ( ) using the conventional LM objective (Section ) to enable to generate reflection tokens by itself without relying on the critic at inference time.

@src https://arxiv.org/abs/2402.13753
@title LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens
@section Introduction

Large context window is a desirable feature in large language models (LLMs).

However, due to high fine-tuning costs, scarcity of long texts, and catastrophic values introduced by new token positions, current extended context windows are limited to around 128k tokens.

This paper introduces that, for the first time, extends the context window of pre-trained LLMs to an impressive 2048k tokens, with up to only 1k fine-tuning steps at within 256k training lengths, while maintaining performance at the original short context window. This is achieved

by three key innovations: (i) we identify and exploit two forms of non-uniformities in positional interpolation through an efficient search, providing a better initialization for fine-tuning and enabling an 8 MATH extension in non-fine-tuning scenarios; (ii) we introduce a progressive extension strategy that first fine-tunes a 256k length LLM and then conducts a second positional interpolation on the fine-tuned extended LLM to achieve a 2048k context window; (iii) we readjust on 8k length to recover the short context window performance.

Extensive experiments on LLaMA2 and Mistral across various tasks demonstrate the effectiveness of our method. Models extended via retain the original architecture with minor modifications to the positional embedding, and can reuse most pre-existing optimizations. Code will be available at https://github.com/microsoft/LongRoPE

Large Language Models (LLMs), despite remarkable success on various tasks , often suffer from limited context window size, e.g., LLaMA2's 4096 token limit .

Beyond the context window, LLM's performance declines due to the additional positions that the model has not been trained on. This poses challenges in important scenarios like in-context learning with numerous examples and LLM agents .

Recent works show that a pre-trained LLM context window can be extended to around 128k by fine-tuning on longer texts .

There are three major obstacles to further extend the context window.

untrained new position indices introduce many catastrophic values, leading to out-of-distribution issues and making fine-tuning difficult to converge . This is particularly challenging when an extension from 4k to MATH 1000k introduces more than 90% new positions. Second, fine-tuning usually requires texts of corresponding lengths. However, long texts in current datasets, especially those exceeding 1000k, are limited. Moreover, training on extra-long texts is computationally expensive, requiring prohibitively extensive training hours and GPU resources. Third, when extending to extremely long context windows, the attention becomes dispersed as it's spread thinly across numerous token positions, degrading performance on the original short context .

One approach to mitigate the first challenge is to interpolate RoPE positional embedding , which downscales new position indices to the pretrained range, as shown in Fig. . Position Interpolation (PI) linearly interpolates RoPE's rotary angles by the extension ratio. NTK advocates unequal interpolation and extrapolation across RoPE dimensions. YaRN categorizes RoPE dimensions into three frequency-based groups and applies extrapolation, NTK, and linear interpolations, respectively. However, positional embedding exhibits complex non-uniform information entropy in the Transformer architecture.

Such subtle non-uniformity is not effectively leveraged by existing approaches, leading to information loss and hence limiting the context window size.

Section reveals two key findings empirically: (1) Effective positional interpolation should consider two forms of non-uniformities: varying RoPE dimensions and token positions. Lower RoPE dimensions and initial starting token positions benefit from less interpolation, but the optimal solutions depend on the target extended length.

(2) By considering these non-uniformities into positional interpolation, we can effectively retain information in the original RoPE, particularly key dimensions and token positions. This minimizes the loss caused by positional interpolation, and thus provides better initialization for fine-tuning. Moreover, it allows an 8 MATH extension in non-fine-tuning scenarios.

Motivated by the findings, we introduce , an effective method

that extends the LLM context window beyond 2 million tokens. is based on three key innovations. First, fully exploits multidimensional non-uniformities in positional interpolation.

It identifies effective rescale factors for RoPE's rotation angles for each RoPE dimension, based on token positions.

As the search space that identifies rescale factors expands exponentially with the target extension ratio, introduces an evolutionary search algorithm with two optimization techniques to boost search efficiency. Fig. shows an example of the searched rescaled RoPE.

Then, leverages an efficient, progressive extension strategy to achieve a 2048k context window without the need of direct fine-tuning on texts with extremely long lengths, which are scarce and hardly available. The strategy begins by searching for a 256k length on the pre-trained LLM and fine-tuning it under this length. Then, as our non-uniform positional interpolation allows for an 8 MATH extension in non-fine-tuning settings, we conduct a second search for new RoPE rescale factors on the fine-tuned extended LLM. This ultimately achieves the 2048k context window for LLaMA2 and Mistral .

to mitigate performance degradation on the original (shorter) context window,

the RoPE rescale factors on the extended LLM.

Similar to scaling up from 256k to 2048k, we scale down to 4k and 8k context windows on the 256k fine-tuned LLM using our search algorithm to encourage less positional interpolation. During inference, if the sequence length is less than 8k, we update RoPE with the searched rescale factors.

Extensive experiments across different LLMs and various long-context tasks demonstrate the effectiveness of our method. We show that is highly effective in maintaining low perplexity from 4k to 2048k evaluation length, achieving over 90% passkey retrieval accuracy, and delivering comparable accuracy on standard benchmarks designed within the 4096 context window. can be applied to any LLMs based on RoPE embedding. We will release our code and -2048k models.

@src https://arxiv.org/abs/2407.10671
@title Qwen2 Technical Report
@section Introduction

This report introduces the Qwen2 series, the latest addition to our large language models and large multimodal models.

We release a comprehensive suite of foundational and instruction-tuned language models, encompassing a parameter range from 0.5 to 72 billion, featuring dense models and a Mixture-of-Experts model.

Qwen2 surpasses most prior open-weight models, including its predecessor Qwen1.5, and exhibits competitive performance relative to proprietary models across diverse benchmarks on language understanding, generation, multilingual proficiency, coding, mathematics, and reasoning.

The flagship model, Qwen2-72B, showcases remarkable performance: 84.2 on MMLU, 37.9 on GPQA, 64.6 on HumanEval, 89.5 on GSM8K, and 82.4 on BBH as a base language model.

The instruction-tuned variant, Qwen2-72B-Instruct, attains 9.1 on MT-Bench, 48.1 on Arena-Hard, and 35.7 on LiveCodeBench.

Moreover, Qwen2 demonstrates robust multilingual capabilities, proficient in approximately 30 languages, spanning English, Chinese, Spanish, French, German, Arabic, Russian, Korean, Japanese, Thai, Vietnamese, and more, underscoring its versatility and global reach.

To foster community innovation and accessibility, we have made the Qwen2 model weights openly available on Hugging Face (https://huggingface.co/Qwen and ModelScope (https://modelscope.cn/organization/qwen , and the supplementary materials including example code on GitHub (https://github.com/QwenLM/Qwen2 .

These platforms also include resources for quantization, fine-tuning, and deployment, facilitating a wide range of applications and research endeavors.

Following the emergence of ChatGPT , enthusiasm for large language models (LLMs) has escalated globally.

The release of the Llama series has further ignited interests within the open-source community, particularly regarding GPT-level local LLMs.

Recently, Claude-3 Opus and GPT-4o (omni) , the updated model for ChatGPT, have ascended to the pinnacle of the Chatbot Arena in quick succession. This platform is well-regarded for its human evaluations of LLMs.

Moreover, Llama-3 has emerged as the state-of-the-art open-weight model series, narrowing the performance gap with leading proprietary models and widely acknowledged as GPT-4–level.

An increasing number of competitive LLMs are now pursuing advancements similar to those made by the GPT series from OpenAI.

Many of these models, including Qwen , Mistral ,

Gemma , etc., have been released in an open-weight manner.

Over recent months, we have successively introduced the Qwen series and progressed to Qwen1.5 .

In the meantime, we have unveiled the vision-language model Qwen-VL , and launched the audio-language model Qwen-Audio .

In this work, we introduce the newest addition to the Qwen family of large language models and large multimodal modles: Qwen2.

Qwen2 is a series of LLMs, grounded in the Transformer architecture , trained using next-token prediction.

The model series encompasses foundational, i.e., base language models, pre-trained but unaligned to human preferences, and instruction-tuned models, fine-tuned with single-turn and multi-turn instruction-following datasets suitable for chat and agent purposes.

Our release comprises four dense models with parameter counts of 0.5 billion, 1.5 billion, 7 billion, and 72 billion, plus a Mixture-of-Experts (MoE) model with 57 billion parameters, of which 14 billion are activated for each token.

The smaller models, specifically Qwen2-0.5B and Qwen2-1.5B, are designed for easy deployment on portable devices such as smartphones, earphones, and smart glasses.

Conversely, the larger models cater to deployment across GPUs of varying scales.

All models were pre-trained on a high-quality, large-scale dataset comprising over 7 trillion tokens, covering a wide range of domains and languages.

Compared to previous editions of Qwen, Qwen2 includes a broader spectrum of linguistic data, enhancing the quantity and quality of code and mathematics content.

This enrichment is hypothesized to improve reasoning abilities of LLMs.

Regarding post-training, all models underwent supervised fine-tuning and direct preference optimization (DPO, ), aligning them with human preferences through learning from human feedback.

This process endows the models with the capability to follow instructions effectively.

We have conducted a thorough evaluation of Qwen2, alongside a selection of baseline models including both open-weight and proprietary models accessible via API.

Qwen2 outperforms competing models in evaluations of both fundamental language capabilities and instruction-tuned functionalities

Specifically, Qwen2-72B-Instruct, our instruction-tuned variant, scores 9.1 on MT-Bench , 48.1 on Arena-Hard , and 35.7 on LiveCodeBench .

Meanwhile, Qwen2-72B, the base language model, achieves 84.2 on MMLU , 37.9 on GPQA , 64.6 on HumanEval , 89.5 on GSM8K , and 82.4 on BBH .

@src https://arxiv.org/abs/2408.00714
@title SAM 2: Segment Anything in Images and Videos
@section Introduction

Segment Anything (SA) introduced a foundation model for promptable segmentation in images . However an image is only a static snapshot of the real world in which visual segments can exhibit complex motion, and with the rapid growth of multimedia content, a significant portion is now recorded with a temporal dimension, particularly in video data. Many important applications in AR/VR, robotics, autonomous vehicles, and video editing require temporal localization beyond image-level segmentation. We believe a universal visual segmentation system should be applicable to both images and videos.

Segmentation in video aims to determine the spatio-temporal extent of entities, which presents unique challenges beyond those in images. Entities can undergo significant changes in appearance due to motion, deformation, occlusion, lighting changes, and other factors. Videos often have lower quality than images due to camera motion, blur, and lower resolution. Further, efficient processing of a large number of frames is a key challenge. While SA successfully addresses segmentation in images, existing video segmentation models and datasets fall short in providing a comparable capability to "segment anything in videos".

We introduce the Segment Anything Model 2 (SAM 2), a unified model for video and image segmentation (we consider an image as a single-frame video). Our work includes a task, model, and dataset (see fig:teaser ).

We focus on the Promptable Visual Segmentation (PVS) task that generalizes image segmentation to the video domain. The task takes as input points, boxes, or masks on any frame of the video to define a segment of interest for which the spatio-temporal mask (i.e., a 'masklet') is to be predicted. Once a masklet is predicted, it can be iteratively refined by providing prompts in additional frames.

Our model ( ) produces segmentation masks of the object of interest, in single images and across video frames. SAM 2 is equipped with a memory that stores information about the object and previous interactions, which allows it to generate masklet predictions throughout the video, and also effectively correct these based on the stored memory context of the object from previously observed frames. Our streaming architecture is a natural generalization of SAM to the video domain, processing video frames one at a time, equipped with a memory attention module to attend to the previous memories of the target object. When applied to images, the memory is empty and the model behaves like SAM.

We employ a data engine ( ) to generate training data by using our model in the loop with annotators to interactively annotate new and challenging data. Different from most existing video segmentation datasets, our data engine is not restricted to objects of specific categories, but instead targeted to provide training data for segmenting any object with a valid boundary, including parts and subparts. Compared to existing model-assisted approaches, our data engine with SAM 2 in the loop is 8.4 faster at comparable quality. Our final Segment Anything Video (SA-V) dataset ( ) consists of masks across videos,

more masks than any existing video segmentation dataset. SA-V is challenging with small objects and parts that get occluded and re-appear throughout the video. Our SA-V dataset is geographically diverse, and a fairness evaluation of SAM 2 indicates minimal performance discrepancy in video segmentation based on perceived gender, and little variance among the three perceived age groups we evaluated.

Our experiments ( sec:zero_shot_experiments ) show that SAM 2 delivers a step-change in the video segmentation experience.

SAM 2 can produce better segmentation accuracy while using 3 fewer interactions than prior approaches. Further, SAM 2 outperforms prior work in established video object segmentation benchmarks, under multiple evaluation settings, and delivers better performance compared to SAM on image segmentation benchmarks, while being 6 faster. SAM 2 is shown to be effective across a variety of video and image distributions as observed through numerous zero-shot benchmarks including 17 for video segmentation and 37 for single-image segmentation.

We are releasing our work under permissive open licences, including the SA-V dataset (CC by 4.0), the SAM 2 model checkpoints (All the results presented in this paper are based on a new version of SAM 2 (improved over our initial release; denoted as "SAM 2.1" in https://github.com/facebookresearch/sam2), which we will refer to as SAM 2 throughout for brevity. , training code (Apache 2.0), and code for our interactive online demo (Apache 2.0).

@src https://arxiv.org/abs/2408.06072
@title CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer
@section Introduction

*Equal contributions. Core contributors: Zhuoyi, Jiayan, Wendi, Ming, Shiyu and Xiaotao.

\ yangzy22,tengjy24\ @mails.tsinghua.edu.cn , corresponding author: jietang@tsinghua.edu.cn

Visiting our demo website https://yzy-thu.github.io/CogVideoX-demo/ https://yzy-thu.github.io/CogVideoX-demo/ to watch more videos!

We present , a large-scale text-to-video generation model based on diffusion transformer, which can generate 10-second continuous videos that align seamlessly with text prompts, with a frame rate of 16 fps and resolution of 768 MATH 1360 pixels.

Previous video generation models often struggled with limited motion and short durations.

It is especially difficult to generate videos with coherent narratives based on text.

We propose several designs to address these issues.

First, we introduce a 3D Variational Autoencoder (VAE) to compress videos across spatial and temporal dimensions, enhancing both the compression rate and video fidelity.

Second, to improve text-video alignment, we propose an expert transformer with expert adaptive LayerNorm to facilitate the deep fusion between the two modalities.

Third, by employing progressive training and multi-resolution frame packing, excels at generating coherent, long-duration videos with diverse shapes and dynamic movements.

In addition, we develop an effective pipeline that includes various pre-processing strategies for text and video data.

Our innovative video captioning model significantly improves generation quality and semantic alignment.

Results show that achieves state-of-the-art performance in both automated benchmarks and human evaluation.

We publish the code and model checkpoints of along with our VAE model and video captioning model at https://github.com/THUDM/CogVideo https://github.com/THUDM/CogVideo .

The rapid development of text-to-video models has been phenomenal, driven by both the Transformer architecture and diffusion model .

Early attempts to pretrain and scale Transformers to generate videos from text have shown great promise, such as CogVideo and Phenaki .

Meanwhile, diffusion models have recently made exciting advancements in video generation .

By using Transformers as the backbone of diffusion models, i.e., Diffusion Transformers (DiT) , text-to-video generation has reached a new milestone, as evidenced by the impressive Sora showcases .

Despite these rapid advancements in DiTs, it remains technically unclear how to achieve long-term consistent video generation with dynamic plots. For example, previous models had difficulty generating a video based on a prompt like "a bolt of lightning splits a rock, and a person jumps out from inside the rock".

In this work, we train and introduce , a set of large-scale diffusion transformer models designed for generating long-term, temporally consistent videos with rich motion semantics.

We address the challenges mentioned above by developing a 3D Variational Autoencoder, an expert Transformer, a progressive training pipeline, and a video data filtering and captioning pipeline, respectively.

First, to efficiently consume high-dimension video data, we design and train a 3D causal VAE that compresses the video along both spatial and temporal dimensions.

Compared to previous method of fine-tuning 2D VAE, this strategy helps significantly reduce the sequence length and associated training compute and also helps prevent flicker in the generated videos, that is, ensuring continuity among frames.

Second, to improve the alignment between videos and texts, we propose an expert Transformer with expert adaptive LayerNorm to facilitate the fusion between the two modalities.

To ensure the temporal consistency in video generation and capture large-scale motions, we propose to use 3D full attention to comprehensively model the video along both temporal and spatial dimensions.

Third, as most video data available online lacks accurate textual descriptions, we develop a video captioning pipeline capable of accurately describing video content.

This pipeline is used to generate new textual descriptions for all video training data, which significantly enhances 's ability to grasp precise semantic understanding.

In addition, we adopt and design progressive training techniques, including multi-resolution frame pack and resolution progressive training, to further enhance the generation performance and stability of . Furthermore, we propose Explicit Uniform Sampling, which stablizes the training loss curve and accelerates convergence by setting different timestep sampling intervals on each data parallel rank.

To date, we have completed the training with two sizes: 5 billion and 2 billion, respectively.

Both machine and human evaluations suggest that -5B outperforms well-known video models and -2B is very competitive across most dimensions.

Figure shows the performance of -5B and -2B in different aspects.

It shows that has the property of being scalable. As the size of model parameters, data volume, and training volume increase, the performance will get better in the future.

Our contributions can be summarized as follows:

We propose , a simple and scalable structure with a 3D causal VAE and an expert transformer, designed for generating coherent, long-duration, high-action videos. It can generate long videos with multiple aspect ratios, up to 768 MATH 1360 resolution, 10 seconds in length, at 16fps.

We evaluate through automated metric evaluation and human assessment, compared with openly-accessible top-performing text-to-video models. achieves state-of-the-art performance.

We publicly release our 5B and 2B models, including text-to-video and image-to-video versions, the first commercial-grade open-source video generation models. We hope it can advance the filed of video generation.

@src https://arxiv.org/abs/2408.06072
@title CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer
@section Introduction

In recent years, diffusion models have made groundbreaking advancements in multimodal generation, such as image, video, speech and 3D generation. Among these, video generation is a rapidly evolving field and being extensively explored. Given the successful experiences with Large Language Models (LLMs), comprehensive scaling up of data volume, training iterations, and model size consistently enhances model performance. Additionally, there is more mature scaling experience with transformers compared to UNet. And DiT has shown that transformers can effectively replace UNet as the backbone of diffusion models. Thus, transformer is a better choice for video generation.

However, long-term consistent video generation remains a significant challenge.

The first challenge is that constructing a web-scale video data pipeline is considerably more difficult than for textual data. Video data is extremely diverse in distribution, quality varies greatly, and simple rule-based filtering is often insufficient for effective data selection. Consequently, processing video data is both time-consuming and highly complex.

There are numerous meaningless unrealistic videos, such as poor-quality edits and computer screen recordings. And many videos are difficult to watch normally, such as those with excessively shaky cameras. These types of data are harmful to the generative model's ability to learn genuine dynamic information. They need to be meticulously processed and filtered out to ensure the quality of the training dataset.

Additionally, most video data available online lacks accurate textual descriptions, significantly limiting the model's ability to grasp precise semantic understanding. To address this issue, we trained a video understanding model capable of accurately describing video content. We use it to generate new textual descriptions for all video data.

To advance the field of video generation, we have decided to open-source this description model.

The high training cost is another significant challenge. If the video is unfolded into a one-dimensional sequence in the pixel space, the length would be extraordinarily long. To keep the computational cost within a feasible range, we trained a 3D VAE that compresses the video along both spatial and temporal dimensions. Additionally, unlike previous video models that use a 2D VAE to encode each frame separately, 3D VAE ensures continuity among frames so that the generated videos do not flicker.

Moreover, to improve the alignment between videos and texts, we propose an expert transformer to facilitate the interaction between the two modalities. Then, to ensure the consistency of video generation and to capture large-scale motions, it is necessary to comprehensively model the video along both temporal and spatial dimensions. Therefore, we opt for 3D full attention, as detailed in Section .

@src https://arxiv.org/abs/2408.12528
@title Show-o: One Single Transformer to Unify Multimodal Understanding and Generation
@section Introduction

MATH Equal Contribution MATH Corresponding Author

We present a unified transformer, i.e., Show-o, that unifies multimodal understanding and generation. Unlike fully autoregressive models, Show-o unifies autoregressive and (discrete) diffusion modeling to adaptively handle inputs and outputs of various and mixed modalities. The unified model flexibly supports a wide range of vision-language tasks including visual question-answering, text-to-image generation, text-guided inpainting/extrapolation, and mixed-modality generation. Across various benchmarks, it demonstrates comparable or superior performance to existing individual models with an equivalent or larger number of parameters tailored for understanding or generation. This significantly highlights its potential as a next-generation foundation model. Code and models are released at https://github.com/showlab/Show-o https://github.com/showlab/Show-o .

"Alone we can do so little; together we can do so much." – Helen Keller

Over the past few years, significant advancements have blossomed in the two key pillars of multimodal intelligence: understanding and generation (Fig. (a) and (b)). For multimodal understanding, Multimodal Large Language Models (MLLMs) like LLaVA have demonstrated exceptional capabilities in vision-language tasks such as visual question-answering (VQA). For the other pillar of visual generation, denoising diffusion probabilistic models (DDPMs) have revolutionized the traditional generative paradigms , achieving unprecedented performance in text-to-image/video generation .

Given these achievements in individual fields, it is natural to explore the potential of connecting them.

Recent works have tried to assemble expert models from different domains to form a unified system that can handle both multimodal understanding and generation. However, existing attempts mainly treat each domain independently and often involve individual models responsible for understanding and generation separately (as shown on the left of Fig. (c)). For instance, NExT-GPT employs a base language model for multimodal understanding but requires an additional pre-trained diffusion model for image generation. Nonetheless, the mainstream understanding models like LLaVA are of transformer architecture while each leading generation models like Stable Diffusion 3 (SD3) are just another transformer. This motivates a research question: can one single transformer handle both multimodal understanding and generation?

Very recently, Chameleon has demonstrated this is possible. Specifically, Chameleon enables an early fusion of different modalities to generate both text and image tokens through the same manner of autoregressive modeling. While it is reasonable to model text tokens autoregressively , it is less clear whether it is better to model image/video patches (or pixels) autoregressively as well. An apparent and significant bottleneck of autoregressively predicting an image is the large number of sampling steps required due to its causal attention, particularly when dealing with images/videos in higher resolution. Further, (continuous) diffusion models have exhibited superior capabilities in visual generation than autoregressive ones and are in full attention.

This motivates us to ponder: can such one single transformer involve both autoregressive and diffusion modeling? Here we envision a new paradigm that text is represented as discrete tokens and modeled autoregressively, same with large language models (LLMs), and continuous image pixels are modeled using denoising diffusion. However, it is non-trivial to integrate these two distinct techniques into one single network due to the significant differences between discrete text tokens and continuous image/video representations. Another challenge lies in the fact that existing state-of-the-art diffusion models typically rely on two distinct models, i.e., a text encoder to encode text conditional information and a denoising network to predict noise.

To this end, we present a novel unified model, i.e., Show-o, capable of addressing both multimodal understanding and generation tasks simultaneously with mixed autoregressive and diffusion modeling (as shown in Fig. ). Specifically, Show-o is built upon a pre-trained LLM and inherits the autoregressive modeling capability for text-based reasoning. Inspired by , we employ a simplified discrete denoising diffusion, similar to MaskGIT , to model discrete image tokens instead of continuous diffusion used in existing works . Besides, Show-o inherently encodes text conditional information, eliminating additional text encoders. To accommodate diverse input data and variations of tasks, a text tokenizer and image tokenizer are employed to encode them into discrete tokens, and a unified prompting strategy is proposed further to process these tokens into structure sequences as input. Consequently, given an image accompanying questions, Show-o gives the answers autoregressively. When provided only text tokens, Show-o generates images in a style of discrete denoising diffusion.

Quantitatively, Show-o demonstrates comparable even better performance to individual models with an equivalent or larger number of parameters across benchmarks. In contrast to autoregressively generating an image, Show-o requires approximately 20 times fewer sampling steps, exhibiting inherent potential in acceleration. Besides, as shown in Fig. , Show-o naturally supports various downstream applications like text-guided inpainting and extrapolation, without any fine-tuning. Moreover, we have demonstrated that Show-o has the potential for mixed-modality generation like interleaved video keyframe generation with text descriptions, video understanding, and video generation. This demonstrates the potential of the unified model as a feasible paradigm for long-form video understanding and generation. Beyond, we investigate the impact of dataset scale, image resolution, and different types of image representations (discrete or continuous) on the multimodal understanding performance, presenting systematic insights for the design of a unified model in the future.

In Fig. , we present a comparison of model characteristics between Show-o and existing representative methods across various domains. One can observe that Show-o is a unified model that flexibly involves existing advanced techniques to comprehensively address multimodal understanding and generation. Collectively, the main contributions of this paper can be summarized as:

We present a unified model, i.e., Show-o, which unifies multimodal understanding and generation using one single transformer.

Show-o innovatively unifies autoregressive and (discrete) diffusion modeling within one single transformer, demonstrating versatility in handling both text and images distinctly.

As a unified model, Show-o demonstrates comparable even better performance to individual baseline models with an equivalent or larger number of parameters in multimodal understanding and generation benchmarks.

Show-o inherently supports various downstream applications like text-based inpainting and extrapolation, without necessitating any fine-tuning. Besides, it also demonstrates the potential for mixed-modality generation, video understanding, and video generation.

We explore the impact of dataset scale, image resolution, and different types of representations (discrete or continuous) on multimodal understanding, providing valuable insights for improving multimodal understanding capabilities of a unified model.

@src https://arxiv.org/abs/2410.18072
@title WorldSimBench: Towards Video Generation Models as World Simulators
@section Introduction

MATH Equal contribution MATH Corresponding author MATH Project lead

Recent advancements in predictive models have demonstrated exceptional capabilities in predicting the future state of objects and scenes.

However, the lack of categorization based on inherent characteristics continues to hinder the progress of predictive model development.

Additionally, existing benchmarks are unable to effectively evaluate higher-capability, highly embodied predictive models from an embodied perspective.

In this work, we classify the functionalities of predictive models into a hierarchy and take the first step in evaluating World Simulators by proposing a dual evaluation framework called .

includes and , encompassing human preference assessments from the visual perspective and action-level evaluations in embodied tasks, covering three representative embodied scenarios: , , and .

In the , we introduce the , a video assessment dataset based on fine-grained human feedback, which we use to train a that aligns with human perception and explicitly assesses the visual fidelity of World Simulators.

In the , we assess the video-action consistency of World Simulators by evaluating whether the generated situation-aware video can be accurately translated into the correct control signals in dynamic environments.

Our comprehensive evaluation offers key insights that can drive further innovation in video generation models, positioning World Simulators as a pivotal advancement toward embodied artificial intelligence.

Before taking action, humans make predictions based on their objectives and observations of the current environment.

These predictions manifest in various forms, , textual planning, visual imagination of future scene changes, or even subconscious planning at the action level.

With the development of generative models, agents driven by these models are exhibiting predictive capabilities that enable them to complete embodied tasks by making human-like predictions, , high-level planning , image-based guidance , or future video prediction to drive actions ). We refer to these models as Predictive Models.

Recently, these models have been widely applied across various domains spanning from developing agents to solve inference tasks to leveraging predictions for driving robots to perform specific actions.

Nevertheless, the rich application scenarios and diverse model designs make predictive models a broad family.

However, without categorizing them based on their inherent characteristics, the advancement of predictive model development remains limited.

This leads to our first question: Can we establish a reasonable hierarchical system for Predictive Models based on their degree of embodiment?

With a well-defined categorization, we can better target the evaluation of Predictive Models from different perspectives of embodiment, ensuring that their strengths and weaknesses are adequately assessed.

In the literature, existing evaluations have typically focused on task planning capabilities by assessing text outputs or evaluating visual outputs from an aesthetic perspective.

However, such approaches significantly limit the evaluation of highly embodied Predictive Models, as embodied scenarios are more concerned with physical properties ( , perspective consistency, object breakability), which these methods fail to effectively assess.

This brings us to our second question: Can we conduct a more detailed evaluation of highly embodied Predictive Models from an embodied perspective?

To answer the first question, we categorize the functionalities of Predictive Models into a hierarchy from MATH to MATH , defined by the model's capabilities and level of embodiment, accompanied by corresponding evaluation benchmarks as illustrated in Fig. .

Models are classified based on the degree of embodiment in their output modalities.

From lower to higher stages, the models are capable of generating: text, images, videos, and actionable videos ( , the videos that can be translated into actions).

It is worth noting that Predictive Models at MATH capable of generating actionable videos integrate robust 3D scene understanding and physical rule priors to provide precise guidance for generating executable actions. These models are closely aligned with the recently proposed concept of World Simulators .

To answer the second question, we review the related benchmarks, as listed in Tab. .

Evaluations on models in MATH that generate text primarily focus on assessing task planning capabilities, while MATH and MATH assessments on visual output measure aesthetic quality through feature similarity analyses with ground truth data.

With clearly defined evaluation dimensions and extensive annotated datasets, both types of assessments can be effectively conducted.

However, evaluating World Simulators introduces complexities due to the intricate physical definitions involved.

Additionally, conventional evaluation methods are inadequate for assessing the actionablilty of the generated videos, as there is no definite ground truth for actionable videos towards completing a specific embodied task.

These factors pose significant challenges to the evaluation of World Simulators.

We argue that an evaluation aligned with human perception could provide a more intuitive and accurate reflection of the characteristics of the synthesized videos, including their adherence to physical rules.

Besides, the actionability can be assessed through a closed-loop manner in simulations deployed with a unified video-to-action policy network.

Considering these aspects, we take the very first step in evaluating World Simulators by proposing a dual evaluation framework called .

As shown in Fig. , assesses World Simulators through two complementary approaches: , which focuses on the Visual Quality, Condition consistency, and Embodiment of the generated content, and , which measures the World Simulator's performance through the conversion of video into control signals.

We present three representative embodied scenarios: ( ), ( ), and ( ), to thoroughly evaluate the capability of World Simulators in generating and representing scenario-specific attributes.

In the , we first define evaluation criteria which is used to construct a comprehensive set of prompts specific to each scenario.

The prompt lists are then used by various video generation models to produce a large number of video clips.

Following extensive human feedback and annotation, these video clips are compiled into the HF-Embodied dataset which consists of a total of tuples with multi-dimensional scores and fine-grained human feedback.

Additionally, we train , using the HF-Embodied dataset to assess World Simulators at the perceptual level, offering a robust evaluation of both their visual fidelity and contextual accuracy.

For the , we deploy three simulation environments for the three embodied scenarios respectively. These environments are used to collect data and train inverse dynamic or goal-based video-to-action models capable of mapping future videos to actions.

In each of these embodied scenarios, the World Simulator is tasked with generating situation-aware videos in real-time, based on current observations and provided text instructions.

These generated videos are then converted into actions using the pre-trained video-to-action models.

The effectiveness of the World Simulator is implicitly evaluated by measuring the performance of the tasks, using relevant metrics to reflect the quality and accuracy of the generated video.

In summary, the main contributions are as follows:

(1)We categorize the functionalities of Predictive Models into a hierarchy, defined by the model's capabilities and level of embodiment, to advance research and development in the field and take the very first step in evaluating World Simulators.

(2)We propose a dual evaluation framework called , through and , we conducted a comprehensive evaluation of the World Simulator's capabilities from an embodied perspective, focusing on both the visual and action levels.

(3)We conducted extensive testing across multiple models and performed a thorough analysis of the experimental results. Our findings highlight the strengths and limitations of current World Simulators and provide actionable insights for improving future video generation models.

(4)We developed , which includes fine-grained human feedback across three scenarios and 20 dimensions, with a total of entries. This dataset, containing both human ratings and the reasons behind them, not only enables the evaluation of World Simulators but also provides broader applications ( , alignment) for future video generation models.

@src https://arxiv.org/abs/2412.08821
@title Large Concept Models: Language Modeling in a Sentence Representation Space
@section Introduction

Large Language models ( ) are dominating current research in natural language processing, and with their recent extension to more modalities, namely images, video and speech, they seem to be considered as the de-facto technique to follow to approach human intelligence. achieve indeed impressive performance on a large variety of tasks, such as providing detailed answers for general knowledge questions, helping in performing long document analysis, or drafting different types of messages, and writing or debugging code.

Building an from scratch requires access to enormous computational resources to process ever larger amounts of data and train models, the size of which now exceeds four hundred billion parameters.

Knowledge acquisition in is heavily data-driven and extending them to more languages or modalities usually requires injecting additional (synthetic) data to cover them.

The landscape of available can be structured into open models such as , , or , on the one hand,

and closed models such as , or , on the other.

It is striking that all these models are based on the same underlying architecture: a transformer-based, decoder-only language model, which is pretrained to predict the next token, given a long context of preceding tokens.

Despite the undeniable success of and continued progress, all current miss a crucial characteristic of human intelligence: explicit reasoning and planning at multiple levels of abstraction.

The human brain does not operate at the word level only.

We usually have a top-down process to solve a complex task or compose a long document: we first plan at a higher level the overall structure, and then step-by-step, add details at lower levels of abstraction.

One may argue that are implicitly learning a hierarchical representation, but we stipulate that models with an explicit hierarchical architecture are better suited to create coherent long-form output.

Imagine a researcher giving a fifteen-minute talk. In such a situation, researchers do not usually prepare detailed speeches by writing out every single word they will pronounce. Instead, they outline a flow of higher-level ideas they want to communicate. Should they give the same talk multiple times, the actual words being spoken may differ, the talk could even be given in different languages, but the flow of higher-level abstract ideas will remain the same.

Similarly, when writing a research paper or essay on a specific topic, humans usually start by preparing an outline that structures the whole document into sections, which they then refine iteratively.

Humans also detect and remember dependencies between the different parts of a longer document at an abstract level. If we expand on our previous research writing example, keeping track of dependencies means that we need to provide results for each of the experiment mentioned in the introduction. Finally, when processing and analyzing information, humans rarely consider every single word in a large document. Instead, we use a hierarchical approach: we remember which part of a long document we should search to find a specific piece of information.

To the best of our knowledge, this explicit hierarchical structure of information processing and generation, at an abstract level, independent of any instantiation in a particular language or modality, cannot be found in any of the current .

In this work, we present a new approach which moves away from processing at the token level and closer to (hierarchical) reasoning in an abstract embedding space. This abstract embedding space is designed to be independent of the language or modality in which the content is expressed; in other words, we aim to model the underlying reasoning process at a purely semantic level, not its instantiation in a specific language.

In order to verify our approach, we limit our study to two levels of abstraction: subword tokens and concepts. We define a concept as an abstract atomic idea.

In practice, a concept would often correspond to a sentence in a text document, or an equivalent speech utterance. We posit that a sentence is an appropriate unit to achieve language independence, in opposition to single words.

This is in sharp contrast to current techniques which are heavily English centric and token based.

Our fundamental idea could be based on any fixed-size sentence embedding space for which an encoder and decoder are available. In particular, we could aim to train a new embedding space specifically optimized to our reasoning architecture. In this work, we chose an existing and freely available sentence embedding, named . supports text input and output in 200 languages, speech input in languages, and speech output in English. We discuss the constraints and impact of this choice in sec:archi:sonar , and share some ideas on alternative embedding spaces in sec:limits .

fig:intro:idea -left visualizes reasoning in an embedding space with the example of a summarization task, which is materialized by a function on the embedding space, mapping five concept representations into two.

fig:intro:idea -right summarizes the overall architecture and processing flow. The input is first segmented into sentences, and each one is encoded with to achieve a sequence of concepts, sentence embeddings.

This sequence of concepts is then processed by a ( ) to generate at the output a new sequence of concepts. Finally, the generated concepts are decoded by into a sequence of subwords. The encoder and decoder are fixed and are not trained. It is important to highlight that the unchanged sequence of concepts at the output of the can be decoded into other languages or modalities without performing again the whole reasoning process. In the same spirit, a particular reasoning operation such as summarization can be performed in a zero-shot setting on input in any language or modality, since it solely operates on concepts. To summarize, the neither has information on the input language or modality nor generates output in a particular language or modality.

We explore multiple architectures to train the , in particular several variants of diffusion.

Finally, we envision an additional level of abstraction beyond concepts which could correspond to a short description of a paragraph or small section. In sec:planlcm we report initial ideas on how conditioning and predicting such higher-level representations can improve consistency of output generated by an .

To some extent, the architecture resembles the approach that also aims to predict the representation of the next observation in an embedding space. However, unlike that places more emphasis on learning a representation space in a self-supervised way, the focuses on accurate prediction in the existing embedding space.

The mains characteristics of our generic approach are as follows:

Reasoning at an abstract language- and modality-agnostic level beyond tokens:

We model the underlying reasoning process, not its instantiation in a particular language.

The can be trained, i.e. acquire knowledge, on all languages and modalities at once, promising scalability in an unbiased way.

Better readability of long-form output by a human.

Facilitates local interactive edits by a user.

Handling of long context and long-form output:

The complexity of a vanilla transformer model increases quadratically with the sequence length. This makes handling of large context windows challenging and several techniques have been developed to alleviate this problem, sparse attention or LSH attention .

Our operates on sequences which are at least an order of magnitude shorter. (We assume an average sentence length of 10–20 tokens.

Independently of the language or modality the is pre-trained and fine-tuned on, it can be applied to any language and modality supported by the encoders, without the need of additional data or fine-tuning. We report results for multiple languages in the text modality.

Unlike multimodal that can suffer from modality competition , concept encoders and decoders can be independently developed and optimized without any competition or interference.

New languages or modalities can be easily added for an existing system.

The goal of this paper is to provide a proof of concept of this high-level vision of an alternative architecture to current best practice in language modeling.

In the next section we present the main design principles of our models and discuss several variants to build and train a .

We discuss several designs to implement diffusion approaches with concept embeddings and carefully study noise scheduling. This section is completed by a compute complexity comparison with token-based .

sec:bigmodel is dedicated to the analysis of a larger 7B parameter model. We discuss challenges when instruction fine-tuning this model on multiple generative tasks, and provide a comparison with existing of comparable size.

The paper concludes with a discussion of related work, the current limitations and perspectives of our approach.

To foster research in this area, we make our training code ( as well as SONAR encoders and decoders ( for up to 200 languages and multiple modalities freely available.

@src https://arxiv.org/abs/2412.13663
@title Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference
@section Introduction

Encoder-only transformer models such as BERT offer a great performance-size tradeoff for retrieval and classification tasks with respect to larger decoder-only models. Despite being the workhorse of numerous production pipelines, there have been limited Pareto improvements to BERT since its release. In this paper, we introduce ModernBERT, bringing modern model optimizations to encoder-only models and representing a major Pareto improvement over older encoders. Trained on 2 trillion tokens with a native 8192 sequence length, ModernBERT models exhibit state-of-the-art results on a large pool of evaluations encompassing diverse classification tasks and both single and multi-vector retrieval on different domains (including code). In addition to strong downstream performance, ModernBERT is also the most speed and memory efficient encoder and is designed for inference on common GPUs.

After the release of BERT , encoder-only transformer-based language models dominated most applications of modern Natural Language Processing (NLP). Despite the rising popularity of Large Language Models (LLMs) such as GPT , Llama , and Qwen , encoder-only models remain widely used in a variety of non-generative downstream applications. https://github.com/AnswerDotAI/ModernBERT https://github.com/AnswerDotAI/ModernBERT

The encoder's popularity is largely due to their modest inference requirements, enabling them to efficiently process corpora of documents at scale for retrieval and quickly perform discriminative tasks. Encoder models offer a compelling trade-off in quality versus size, making them a popular option against encoder-decoder and decoder-only language models when dealing with substantial amounts of data .

Encoder models are particularly popular in Information Retrieval (IR) applications, e.g., semantic search, with notable progress on leveraging encoders for this task . While LLMs have taken the spotlight in recent years, they have also motivated a renewed interest in encoder-only models for IR. Indeed, encoder-based semantic search is a core component of Retrieval-Augmented Generation (RAG) pipelines , where encoder models are used to retrieve and feed LLMs with context relevant to user queries.

Encoder-only models are also still frequently used for a variety of discriminative tasks such as classification or Natural Entity Recognition (NER) , where they often match the performance of specialized LLMs. Here again, they can be used in conjunction with LLMs, for example detecting toxic prompts and preventing responses, or routing queries in an agentic framework .

Surprisingly, these pipelines currently rely on older models, and quite often on the original BERT itself as their backbone , without leveraging improvements developed in recent years. Practitioners face many drawbacks: sequence lengths limited to 512 tokens, suboptimal model design and vocabulary sizes , and generally inefficient architectures, whether in terms of downstream performance or computational efficiency. Finally, training data is limited in volume and restricted to narrow domains (especially lacking code data) or lacking knowledge of recent events.

Recent modernization efforts have only partially addressed the shortcomings of encoder-only models due to limited breadth. MosaicBERT , CrammingBERT , and AcademicBERT focused on matching BERT performance with better training efficiency. NomicBERT and GTE-en-MLM (developed concurrently to this work) introduced longer-context encoder models focused on retrieval applications, but did not optimize for efficiency or classification performance, and re-used older training data mixtures which is especially apparent in programming-related tasks.

Contributions We present ModernBERT, a modernized encoder-only transformer model, with an improved architecture designed to increase downstream performance and efficiency, especially over longer sequence lengths. We also bring encoder-only models to modern, larger data scales, by training on 2 trillion tokens, with a data mixture including code data. We release two models, https://huggingface.co/answerdotai/ModernBERT-base ModernBERT-base and https://huggingface.co/answerdotai/ModernBERT-large ModernBERT-large , which reach state-of-the-art overall performance against all existing encoder models on a wide variety of downstream tasks. These results are achieved with considerably higher inference efficiency, processing sequences of 8192 tokens almost two times faster than previous models.

To support future research on encoder-only models, we release https://github.com/AnswerDotAI/ModernBERT FlexBERT (FlexBERT is built on top of a revised MosaicBERT codebase. , our modular architecture framework allowing easy experimentation, and inspired by Pythia , all intermediate training checkpoints (further detailed in Section ).

@src https://arxiv.org/abs/2501.12948
@title DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
@section Introduction

Large Language Model, Reasoning, Reinforcement Learning

Reasoning capability, the cornerstone of human intelligence, enables complex cognitive tasks ranging from mathematical problem-solving to logical deduction and programming. Recent advances in artificial intelligence have demonstrated that large language models (LLMs) can exhibit emergent behaviors, including reasoning abilities, when scaled to a sufficient size . However, achieving such capabilities in pre-training typically demands substantial computational resources.

In parallel, a complementary line of research has demonstrated that large language models can be effectively augmented through chain-of-thought (CoT) prompting. This technique, which involves either providing carefully designed few-shot examples or using minimalistic prompts such as “Let’s think step by step” , enables models to produce intermediate reasoning steps, thereby substantially enhancing their performance on complex tasks.

Similarly, further performance gains have been observed when models learn high-quality, multi-step reasoning trajectories during the post-training phase .

Despite their effectiveness, these approaches exhibit notable limitations. Their dependence on human-annotated reasoning traces hinders scalability and introduces cognitive biases. Furthermore, by constraining models to replicate human thought processes, their performance is inherently capped by the human-provided exemplars, which prevents the exploration of superior, non-human-like reasoning pathways.

To tackle these issues, we aim to explore the potential of LLMs for developing reasoning abilities through self-evolution in an RL framework, with minimal reliance on human labeling efforts.

Specifically, we build upon DeepSeek-V3-Base and employ Group Relative Policy Optimization (GRPO) as our RL framework. The reward signal is solely based on the correctness of final predictions against ground-truth answers, without imposing constraints on the reasoning process itself. Notably, we bypass the conventional supervised fine-tuning (SFT) phase before RL training. This design choice stems from our hypothesis that human-defined reasoning patterns may limit model exploration, whereas unrestricted RL training can better incentivize the emergence of novel reasoning capabilities in LLMs.

Through this process, detailed in Section , our model (referred to as DeepSeek-R1-Zero) naturally developed diverse and sophisticated reasoning behaviors.

In solving reasoning problems, the model exhibits a tendency to generate longer responses, incorporating verification, reflection, and the exploration of alternative approaches within each response. Although we do not explicitly teach the model how to reason, it successfully learns improved reasoning strategies through reinforcement learning.

Although DeepSeek-R1-Zero demonstrates excellent reasoning capabilities, it faces challenges such as poor readability and language mixing, occasionally combining English and Chinese within a single chain-of-thought response. Furthermore, the rule-based RL training stage of DeepSeek-R1-Zero is narrowly focused on reasoning tasks, resulting in limited performance in broader areas such as writing and open-domain question answering.

To address these challenges, we introduce DeepSeek-R1, a model trained through a multi-stage learning framework that integrates rejection sampling, reinforcement learning, and supervised fine-tuning, detailed in Section . This training pipeline enables DeepSeek-R1 to inherit the reasoning capabilities of its predecessor, DeepSeek-R1-Zero, while aligning model behavior with human preferences through additional non-reasoning data.

powerful AI at a lower energy cost, we have distilled several smaller models and made them publicly available. These distilled models exhibit strong reasoning capabilities, surpassing the performance of their original instruction-tuned counterparts. We believe that these instruction-tuned versions will also significantly contribute to the research community by providing a valuable resource for understanding the mechanisms underlying long chain-of-thought (CoT) reasoning models and for fostering the development of more powerful reasoning models. We release DeepSeek-R1 series models to the public at https://huggingface.co/deepseek-ai.

@src https://arxiv.org/abs/2503.14476
@title DAPO: An Open-Source LLM Reinforcement Learning System at Scale
@section Introduction

Test-time scaling such as OpenAI's o1 and DeepSeek's R1 brings a profound paradigm shift to Large Language Models (LLMs) . Test-time scaling enables longer Chain-of-Thought thinking and induces sophisticated reasoning behaviors, which makes the models superior in competitive math and coding tasks like AIME and Codeforces.

The central technique driving the revolution is large-scale Reinforcement Learning (RL), which elicits complex reasoning behaviors such as self-verification and iterative refinement. However, the actual algorithm and key recipe for scalable RL training remains a myth, hidden from technical reports of existing reasoning models . In this paper, we reveal significant obstacles in large-scale RL training and open-source a scalable RL system with fully open-sourced algorithm, training code and dataset that provides democratized solutions with industry-level RL results.

We experiment over Qwen2.5-32B as the pretrained model for RL. In our initial GRPO run, we achieved only 30 points on AIME — a performance significantly below DeepSeek’s RL (47 points). A thorough analysis reveals that the naive GRPO baseline suffers from several key issues such as entropy collapse, reward noise, and training instability. The broader community has encountered similar challenges in reproducing DeepSeek's results suggesting that critical training details may have been omitted in the R1 paper that are required to develop an industry-level, large-scale, and reproducible RL system.

To close this gap, we release an open-source state-of-the-art system for large-scale LLM RL, which achieves 50 points on AIME 2024 based on Qwen2.5-32B model, outperforming previous state-of-the-art results achieved by DeepSeek-R1-Zero-Qwen-32B (47 points) using 50% training steps (Figure ). We propose the Decoupled Clip and Dynamic sAmpling Policy Optimization (DAPO) algorithm, and introduce 4 key techniques to make RL shine in the long-CoT RL scenario. Details are presented in Section .

Clip-Higher, which promotes the diversity of the system and avoids entropy collapse;

Dynamic Sampling, which improves training efficiency and stability;

Token-Level Policy Gradient Loss, which is critical in long-CoT RL scenarios;

Overlong Reward Shaping, which reduces reward noise and stabilizes training.

Our implementation is based on verl . By fully releasing our state-of-the-art RL system including training code and data, we aim to reveal valuable insights to large-scale LLM RL that benefit the larger community.
