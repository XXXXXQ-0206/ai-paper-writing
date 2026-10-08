# method corpus (167 sources)

@src https://arxiv.org/abs/1706.03762
@title Attention Is All You Need
@section Model Architecture

Most competitive neural sequence transduction models have an encoder-decoder structure . Here, the encoder maps an input sequence of symbol representations MATH to a sequence of continuous representations MATH . Given MATH , the decoder then generates an output sequence MATH of symbols one element at a time. At each step the model is auto-regressive , consuming the previously generated symbols as additional input when generating the next.

The Transformer follows this overall architecture using stacked self-attention and point-wise, fully connected layers for both the encoder and decoder, shown in the left and right halves of Figure , respectively.

@src https://arxiv.org/abs/1706.03762
@title Attention Is All You Need
@section Applications of Attention in our Model

The Transformer uses multi-head attention in three different ways:

In "encoder-decoder attention" layers, the queries come from the previous decoder layer, and the memory keys and values come from the output of the encoder. This allows every position in the decoder to attend over all positions in the input sequence. This mimics the typical encoder-decoder attention mechanisms in sequence-to-sequence models such as .

The encoder contains self-attention layers. In a self-attention layer all of the keys, values and queries come from the same place, in this case, the output of the previous layer in the encoder. Each position in the encoder can attend to all positions in the previous layer of the encoder.

Similarly, self-attention layers in the decoder allow each position in the decoder to attend to all positions in the decoder up to and including that position. We need to prevent leftward information flow in the decoder to preserve the auto-regressive property. We implement this inside of scaled dot-product attention by masking out (setting to MATH ) all values in the input of the softmax which correspond to illegal connections. See Figure .

@src https://arxiv.org/abs/1706.03762
@title Attention Is All You Need
@section Training Data and Batching

We trained on the standard WMT 2014 English-German dataset consisting of about 4.5 million sentence pairs. Sentences were encoded using byte-pair encoding , which has a shared source-target vocabulary of about 37000 tokens. For English-French, we used the significantly larger WMT 2014 English-French dataset consisting of 36M sentences and split tokens into a 32000 word-piece vocabulary . Sentence pairs were batched together by approximate sequence length. Each training batch contained a set of sentence pairs containing approximately 25000 source tokens and 25000 target tokens.

@src https://arxiv.org/abs/1804.07461
@title GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding
@section Training

We train our models with the BiLSTM sentence encoder and post-attention BiLSTMs shared across tasks, and classifiers trained separately for each task.

For each training update, we sample a task to train with a probability proportional to the number of training examples for each task.

We scale each task's loss inversely proportional to the number of examples for that task, which we found to improve overall performance.

We train our models with Adam with initial learning rate MATH , batch size 128, and gradient clipping.

We use macro-average score over all tasks as our validation metric, and perform a validation check every 10k updates.

We divide the learning rate by 5 whenever validation performance does not improve.

We stop training when the learning rate drops below MATH or performance does not improve after 5 validation checks.

@src https://arxiv.org/abs/1810.04805
@title BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
@section Unsupervised Feature-based Approaches

Learning widely applicable representations of words has been an active area of research for decades, including non-neural and neural methods. Pre-trained word embeddings are an integral part of modern NLP systems, offering significant improvements over embeddings learned from scratch . To pre-train word embedding vectors, left-to-right language modeling objectives have been used , as well as objectives to discriminate correct from incorrect words in left and right context .

These approaches have been generalized to coarser granularities, such as sentence embeddings or paragraph embeddings . To train sentence representations, prior work has used objectives to rank candidate next sentences , left-to-right generation of next sentence words given a representation of the previous sentence , or denoising auto-encoder derived objectives .

ELMo and its predecessor generalize traditional word embedding research along a different dimension. They extract context-sensitive features from a left-to-right and a right-to-left language model. The contextual representation of each token is the concatenation of the left-to-right and right-to-left representations. When integrating contextual word embeddings with existing task-specific architectures, ELMo advances the state of the art for several major NLP benchmarks including question answering , sentiment analysis , and named entity recognition .

proposed learning contextual representations through a task to predict a single word from both left and right context

using LSTMs. Similar to ELMo, their model is feature-based and not deeply bidirectional.

shows that the cloze task can be used to improve the robustness of text generation models.

@src https://arxiv.org/abs/1810.04805
@title BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
@section Unsupervised Fine-tuning Approaches

As with the feature-based approaches, the first works in this direction only pre-trained word embedding parameters from unlabeled text .

More recently, sentence or document encoders which produce contextual token representations have been pre-trained from unlabeled text and fine-tuned for a supervised downstream task . The advantage of these approaches is that few parameters need to be learned from scratch. At least partly due to this advantage, OpenAI GPT achieved previously state-of-the-art results on many sentence-level tasks from the GLUE benchmark . Left-to-right language modeling and auto-encoder objectives have been used for pre-training such models .

@src https://arxiv.org/abs/1810.04805
@title BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
@section Pre-training BERT

Unlike and , we do not use traditional left-to-right or right-to-left language models to pre-train BERT. Instead, we pre-train BERT using two unsupervised tasks, described in this section. This step

is presented in the left part of Figure .

Intuitively, it is reasonable to believe that a deep bidirectional model is strictly more powerful than either a left-to-right model or the shallow concatenation of a left-to-right and a right-to-left model. Unfortunately, standard conditional language models can only be trained left-to-right or right-to-left, since bidirectional conditioning would

allow each word to indirectly "see itself", and

the model could trivially predict the target word in a multi-layered context.

In order to train a deep bidirectional representation, we simply mask some percentage of the input tokens at random, and then predict those masked tokens. We refer to this procedure as a "masked LM" (MLM), although it is often referred to as a Cloze task in the literature . In this case, the final hidden vectors corresponding to the mask tokens are fed into an output softmax over the vocabulary, as in a standard LM. In all of our experiments, we mask 15% of all WordPiece tokens in each sequence at random. In contrast to denoising auto-encoders , we only predict the masked words rather than reconstructing the entire input.

Although this allows us to obtain a bidirectional pre-trained model, a downside is that we are creating a mismatch between pre-training and fine-tuning, since the token does not appear during fine-tuning. To mitigate this, we do not always replace "masked" words with the actual token. The training data generator chooses 15% of the token positions at random for prediction. If the MATH -th token is chosen, we replace the MATH -th token with (1) the token 80% of the time (2) a random token 10% of the time (3) the unchanged MATH -th token 10% of the time. Then, MATH will be used to predict the original token with cross entropy loss.

We compare variations of this procedure in Appendix .

Many important downstream tasks such as Question Answering (QA) and Natural Language Inference (NLI) are based on understanding the relationship between two sentences, which is not directly captured by language modeling. In order to train a model that understands sentence relationships, we pre-train for a binarized next sentence prediction task that can be trivially generated from any monolingual corpus. Specifically, when choosing the sentences A and B for each pre-training example, 50% of the time B is the actual next sentence that follows A (labeled

as IsNext ), and 50% of the time it is a random sentence from the corpus

As we show in Figure , MATH is used for next sentence prediction (NSP). (The final model achieves 97%-98% accuracy on NSP. Despite its simplicity, we demonstrate in Section that pre-training towards this task is very beneficial to both QA and NLI.

(The vector MATH is not a meaningful sentence representation without fine-tuning, since it was trained with NSP.

The NSP task is closely related to representation-learning objectives used in and . However, in prior work, only sentence embeddings are transferred to down-stream tasks, where BERT transfers all parameters to initialize end-task model parameters.

The pre-training procedure largely follows the existing literature on language model pre-training. For the pre-training corpus we use the BooksCorpus (800M words) and English Wikipedia (2,500M words). For Wikipedia we extract only the text passages and ignore lists, tables, and headers. It is critical to use a document-level corpus rather than a shuffled sentence-level corpus such as the Billion Word Benchmark in order to extract long contiguous sequences.

@src https://arxiv.org/abs/1810.04805
@title BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
@section Effect of Pre-training Tasks

We demonstrate the importance of the deep bidirectionality of BERT by evaluating two pre-training objectives using exactly the same pre-training data, fine-tuning scheme, and hyperparameters as :

NSP: A bidirectional model which is trained using the "masked LM" (MLM) but without the "next sentence prediction" (NSP) task.

& No NSP: A left-context-only model which is trained using a standard Left-to-Right (LTR) LM, rather than an MLM. The left-only constraint was also applied at fine-tuning, because removing it introduced a pre-train/fine-tune mismatch that degraded downstream performance. Additionally, this model was pre-trained without the NSP task. This is directly comparable to OpenAI GPT, but using our larger training dataset, our input representation, and our fine-tuning scheme.

We first examine the impact brought by the NSP task. In Table , we show that removing NSP hurts performance significantly on QNLI, MNLI, and SQuAD 1.1. Next, we evaluate the impact of training bidirectional representations by comparing "No NSP" to "LTR & No NSP". The LTR model performs worse than the MLM model on all tasks, with large drops on MRPC and SQuAD.

For SQuAD it is intuitively clear that a LTR model will perform poorly at token predictions, since the token-level hidden states have no right-side context.

In order to make a good faith attempt at strengthening the LTR system, we added a randomly initialized BiLSTM on top. This does significantly improve results on SQuAD, but the results are still far worse than those of the pre-trained bidirectional models. The BiLSTM hurts performance on the GLUE tasks.

We recognize that it would also be possible to train separate LTR and RTL models and represent each token as the concatenation of the two models, as ELMo does. However: (a) this is twice as expensive as a single bidirectional model; (b) this is non-intuitive for tasks like QA, since the RTL model would not be able to condition the answer on the question; (c) this it is strictly less powerful than a deep bidirectional model, since it can use both left and right context at every layer.

@src https://arxiv.org/abs/1810.04805
@title BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
@section Feature-based Approach with BERT

All of the BERT results presented so far have used the fine-tuning approach, where a simple classification layer is added to the pre-trained model, and all parameters are jointly fine-tuned on a downstream task. However, the feature-based approach, where fixed features are extracted from the pre-trained model, has certain advantages. First, not all

tasks can be easily represented by a Transformer encoder architecture, and therefore require a task-specific model architecture to be added. Second, there are major computational benefits to

pre-compute an expensive representation of the training data once and then run many experiments with

In this section, we compare the two approaches by applying BERT to the CoNLL-2003 Named Entity Recognition (NER) task . In the input to BERT, we use a case-preserving WordPiece model, and we include the maximal document context provided by the data. Following standard practice, we formulate this as a tagging task but do not use a CRF layer in the output. We use the representation of the first sub-token as the input to the token-level classifier over the NER label set.

To ablate the fine-tuning approach, we apply the feature-based approach by extracting the activations from one or more layers without fine-tuning any parameters of BERT. These contextual embeddings are used as input to a randomly initialized two-layer 768-dimensional BiLSTM before the classification layer.

Results are presented in Table . performs competitively with state-of-the-art methods. The best performing method concatenates the token representations from the top four hidden layers of the pre-trained Transformer, which is only 0.3 F1 behind fine-tuning the entire model. This demonstrates that BERT is effective for both fine-tuning and feature-based approaches.

@src https://arxiv.org/abs/1810.04805
@title BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
@section Illustration of the Pre-training Tasks

We provide examples of the pre-training tasks in the following.

Assuming the unlabeled sentence is my dog is hairy ,

and during the random masking procedure we chose the 4-th token (which corresponding to hairy ), our masking procedure

80% of the time: Replace the word with the token, e.g., my dog is hairy MATH my dog is [MASK]

10% of the time: Replace the word with a random word, e.g., my dog is hairy MATH my dog is apple

10% of the time: Keep the word unchanged, e.g., my dog is hairy MATH my dog is hairy . The purpose of this is to bias the representation towards the actual observed word.

The advantage of this procedure is that the Transformer encoder does not know which words it will be asked to predict or which have been replaced by random words, so it is forced to keep a distributional contextual representation of every input token. Additionally, because random replacement only occurs for 1.5% of all tokens (i.e., 10% of 15%), this does not seem to harm the model's language understanding capability. In Section ,

Compared to standard langauge model training, the masked LM only

make predictions on 15% of tokens in each batch, which suggests that more pre-training steps may be required for the model to converge. In Section we demonstrate that MLM does converge marginally slower than a left-to-right model (which predicts every token), but the empirical improvements of the MLM model far outweigh the increased training cost.

The next sentence prediction task can be illustrated in the following examples.

@src https://arxiv.org/abs/1810.04805
@title BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
@section Pre-training Procedure

To generate each training input sequence, we sample two spans of text from the corpus, which we refer to as "sentences" even though they are typically much longer than single sentences (but can be shorter also). The first sentence receives the A embedding and the second receives the B embedding. 50% of the time B is the actual next sentence that follows A and 50% of the time it is a random sentence, which is done for the "next sentence prediction" task. They are sampled such that the combined length is MATH 512 tokens. The LM masking is applied after WordPiece tokenization with a uniform masking rate of 15%, and no special consideration given to partial word pieces.

We train with batch size of 256 sequences (256 sequences * 512 tokens = 128,000 tokens/batch) for 1,000,000 steps, which is approximately 40 epochs over the 3.3 billion word corpus. We use Adam with learning rate of 1e-4, MATH , MATH , L2 weight decay of MATH , learning rate warmup over the first 10,000 steps, and linear decay of the learning rate. We use a dropout probability of 0.1 on all layers. We use a gelu activation rather than the standard relu , following OpenAI GPT. The training loss is the sum of the mean masked LM likelihood and the mean next sentence prediction likelihood.

Training of was performed on 4 Cloud TPUs in Pod configuration (16 TPU chips total). (https://cloudplatform.googleblog.com/2018/06/Cloud-TPU-now-offers-preemptible-pricing-and-global-availability.html Training of was performed on 16 Cloud TPUs (64 TPU chips total). Each pre-training took 4 days to complete.

Longer sequences are disproportionately expensive because attention is quadratic to the sequence length. To speed up pretraing in our experiments, we pre-train the model with sequence length of 128 for 90% of the steps. Then, we train

the rest 10% of the steps of sequence of 512 to learn the positional embeddings.

@src https://arxiv.org/abs/1810.04805
@title BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
@section Effect of Number of Training Steps

Figure presents MNLI Dev accuracy after fine-tuning from a checkpoint that has been pre-trained for MATH steps. This allows us to answer the following questions:

Question: Does BERT really need such a large amount of pre-training (128,000 words/batch * 1,000,000 steps) to achieve high fine-tuning accuracy?

Answer: Yes, achieves almost 1.0% additional accuracy on MNLI when trained on 1M steps compared to 500k steps.

Question: Does MLM pre-training converge slower than LTR pre-training, since only 15% of words are predicted in each batch rather than every word?

Answer: The MLM model does converge slightly slower than the LTR model. However, in terms of absolute accuracy the MLM model begins to outperform the LTR model almost immediately.

@src https://arxiv.org/abs/1906.08237
@title XLNet: Generalized Autoregressive Pretraining for Language Understanding
@section Architecture: Two-Stream Self-Attention for Target-Aware Representations

While the permutation language modeling objective has desired properties, naive implementation with standard Transformer parameterization may not work.

To see the problem, assume we parameterize the next-token distribution MATH using the standard Softmax formulation, i.e.,

where MATH denotes the hidden representation of MATH produced by the shared Transformer network after proper masking.

Now notice that the representation MATH does not depend on which position it will predict, i.e., the value of MATH .

Consequently, the same distribution is predicted regardless of the target position,

which is not able to learn useful representations (see Appendix for a concrete example).

To avoid this problem, we propose to re-parameterize the next-token distribution to be target position aware:

where MATH denotes a new type of representations which additionally take the target position MATH as input.

While the idea of target-aware representations removes the ambiguity in target prediction, how to formulate MATH remains a non-trivial problem.

Among other possibilities, we propose to "stand" at the target position MATH and rely on the position MATH to gather information from the context MATH through attention.

For this parameterization to work, there are two requirements that are contradictory in a standard Transformer architecture: (1) to predict the token MATH , MATH should only use the position MATH and not the content MATH , otherwise the objective becomes trivial; (2) to predict the other tokens MATH with MATH , MATH should also encode the content MATH to provide full contextual information.

To resolve such a contradiction, we propose to use two sets of hidden representations instead of one:

itemize [leftmargin=*,topsep=0em,itemsep=0em]

The content representation MATH , or abbreviated as MATH , which serves a similar role to the standard hidden states in Transformer. This representation encodes both the context and MATH itself.

The query representation MATH , or abbreviated as MATH , which only has access to the contextual information MATH and the position MATH , but not the content MATH , as discussed above.

Computationally, the first layer query stream is initialized with a trainable vector, i.e. MATH , while the content stream is set to the corresponding word embedding, i.e. MATH .

For each self-attention layer MATH , the two streams of representations are schematically (To avoid clutter, we omit the implementation details including multi-head attention, residual connection, layer normalization and position-wise feed-forward as used in Transformer(-XL). The details are included in Appendix for reference. updated with a shared set of parameters as follows (illustrated in Figures (a) and (b)):

where Q, K, V denote the query, key, and value in an attention operation .

The update rule of the content representations is exactly the same as the standard self-attention, so during finetuning, we can simply drop the query stream and use the content stream as a normal Transformer(-XL).

Finally, we can use the last-layer query representation MATH to compute Eq. ( ).

While the permutation language modeling objective has several benefits, it is a much more challenging optimization problem due to the permutation and causes slow convergence in preliminary experiments. To reduce the optimization difficulty, we choose to only predict the last tokens in a factorization order. Formally, we split MATH into a non-target subsequence MATH and a target subsequence MATH , where MATH is the cutting point. The objective is to maximize the log-likelihood of the target subsequence conditioned on the non-target subsequence, i.e.,

Note that MATH is chosen as the target because it possesses the longest context in the sequence given the current factorization order MATH .

A hyperparameter MATH is used such that about MATH tokens are selected for predictions; i.e., MATH . For unselected tokens, their query representations need not be computed, which saves speed and memory.

@src https://arxiv.org/abs/1906.08237
@title XLNet: Generalized Autoregressive Pretraining for Language Understanding
@section Pretraining and Implementation

Following BERT , we use the BooksCorpus and English Wikipedia as part of our pretraining data, which have 13GB plain text combined. In addition, we include Giga5 (16GB text) , ClueWeb 2012-B (extended from ), and Common Crawl for pretraining. We use heuristics to aggressively filter out short or low-quality articles for ClueWeb 2012-B and Common Crawl, which results in 19GB and 110GB text respectively. After tokenization with SentencePiece , we obtain 2.78B, 1.09B, 4.75B, 4.30B, and 19.97B subword pieces for Wikipedia, BooksCorpus, Giga5, ClueWeb, and Common Crawl respectively, which are 32.89B in total.

Our largest model XLNet-Large has the same architecture hyperparameters as BERT-Large, which results in a similar model size.

During pretraining, we always use a full sequence length of 512.

Firstly, to provide a fair comparison with BERT (section ), we also trained XLNet-Large-wikibooks on BooksCorpus and Wikipedia only, where we reuse all pretraining hyper-parameters as in the original BERT.

Then, we scale up the training of XLNet-Large by using all the datasets described above.

Specifically, we train on 512 TPU v3 chips for 500K steps with an Adam weight decay optimizer, linear learning rate decay, and a batch size of 8192, which takes about 5.5 days.

It was observed that the model still underfits the data at the end of training.

Finally, we perform ablation study (section ) based on the XLNet-Base-wikibooks.

Since the recurrence mechanism is introduced, we use a bidirectional data input pipeline where each of the forward and backward directions takes half of the batch size.

For training XLNet-Large, we set the partial prediction constant MATH as 6 (see Section ).

Our finetuning procedure follows BERT except otherwise specified (Hyperparameters for pretraining and finetuning are in Appendix . .

We employ an idea of span-based prediction, where we first sample a length MATH , and then randomly select a consecutive span of MATH tokens as prediction targets within a context of MATH tokens.

We use a variety of natural language understanding datasets to evaluate the performance of our method. Detailed descriptions of the settings for all the datasets can be found in Appendix .

@src https://arxiv.org/abs/1906.08237
@title XLNet: Generalized Autoregressive Pretraining for Language Understanding
@section Bridging the Gap Between Language Modeling and Pretraining

With a deep root in density estimation (The problem of language modeling is essentially density estimation for text data. , language modeling has been a rapidly-developing research area . However, there has been a gap between language modeling and pretraining due to the lack of the capability of bidirectional context modeling, as analyzed in Section . It has even been challenged by some machine learning practitioners whether language modeling is a meaningful pursuit if it does not directly improve downstream tasks (https://openreview.net/forum?id=HJePno0cYm . XLNet generalizes language modeling and bridges such a gap. As a result, it further "justifies" language modeling research. Moreover, it becomes possible to leverage the rapid progress of language modeling research for pretraining. As an example, we integrate Transformer-XL into XLNet to demonstrate the usefulness of the latest language modeling progress.

@src https://arxiv.org/abs/1907.11692
@title RoBERTa: A Robustly Optimized BERT Pretraining Approach
@section Training Objectives

During pretraining, BERT uses two objectives: masked language modeling and next sentence prediction.

Masked Language Model (MLM) A random sample of the tokens in the input sequence is selected and replaced with the special token MATH . The MLM objective is a cross-entropy loss on predicting the masked tokens. BERT uniformly selects 15% of the input tokens for possible replacement. Of the selected tokens, 80% are replaced with MATH , 10% are left unchanged, and 10% are replaced by a randomly selected vocabulary token.

In the original implementation, random masking and replacement is performed once in the beginning and saved for the duration of training, although in practice, data is duplicated so the mask is not always the same for every training sentence (see Section ).

Next Sentence Prediction (NSP) NSP is a binary classification loss for predicting whether two segments follow each other in the original text. Positive examples are created by taking consecutive sentences from the text corpus. Negative examples are created by pairing segments from different documents. Positive and negative examples are sampled with equal probability.

The NSP objective was designed to improve performance on downstream tasks, such as Natural Language Inference , which require reasoning about the relationships between pairs of sentences.

@src https://arxiv.org/abs/1907.11692
@title RoBERTa: A Robustly Optimized BERT Pretraining Approach
@section Implementation

We primarily follow the original BERT optimization hyperparameters, given in Section , except for the peak learning rate and number of warmup steps, which are tuned separately for each setting.

We additionally found training to be very sensitive to the Adam epsilon term, and in some cases we obtained better performance or improved stability after tuning it.

Similarly, we found setting MATH to improve stability when training with large batch sizes.

We pretrain with sequences of at most MATH tokens.

Unlike devlin2018bert , we do not randomly inject short sequences, and we do not train with a reduced sequence length for the first 90% of updates.

We train only with full-length sequences.

We train with mixed precision floating point arithmetic on DGX-1 machines, each with 8 MATH 32GB Nvidia V100 GPUs interconnected by Infiniband .

@src https://arxiv.org/abs/1907.11692
@title RoBERTa: A Robustly Optimized BERT Pretraining Approach
@section Training with large batches

Past work in Neural Machine Translation has shown that training with very large mini-batches can both improve optimization speed and end-task performance when the learning rate is increased appropriately .

Recent work has shown that BERT is also amenable to large batch training .

devlin2018bert originally trained for 1M steps with a batch size of 256 sequences.

This is equivalent in computational cost, via gradient accumulation, to training for 125K steps with a batch size of 2K sequences, or for 31K steps with a batch size of 8K.

In Table we compare perplexity and end-task performance of as we increase the batch size, controlling for the number of passes through the training data.

We observe that training with large batches improves perplexity for the masked language modeling objective, as well as end-task accuracy.

Large batches are also easier to parallelize via distributed data parallel training, (Large batch training can improve training efficiency even without large scale parallel hardware through gradient accumulation, whereby gradients from multiple mini-batches are accumulated locally before each optimization step. This functionality is supported natively in fairseq . and in later experiments we train with batches of 8K sequences.

Notably you2019reducing train BERT with even larger batche sizes, up to 32K sequences.

We leave further exploration of the limits of large batch training to future work.

@src https://arxiv.org/abs/1909.11942
@title ALBERT: A Lite BERT for Self-supervised Learning of Language Representations
@section Pretraining

Following , we use BookCorpus and English Wikipedia for pretraining baseline models, which consist of 16GB uncompressed text. In particular, we format input as "[CLS] MATH [SEP] MATH [SEP]", where MATH and MATH are two segments. (A segment is usually comprised of more than one natural sentence, which has been shown to benefit performances in . Unlike , we always limit the maximum input length to be 512 and randomly generate input sequences shorter than 512 with a probability of 10%. We use a vocabulary size of 30,000, tokenized by SentencePiece . For our best model, we also use additional training data from and . When generating masked inputs, we use n-gram masking, similar to where the length of each n-gram mask is selected randomly. The probability for the length MATH is

We set the maximum length of n-gram (i.e. MATH ) to be 3 as empirically it gives the best performance.

All the models are pretrained with a batch size of 4096 using Lamb optimizer , and the learning rate is set to be 0.00176 . All of our models are trained 125,000 steps unless specified.

@src https://arxiv.org/abs/1909.11942
@title ALBERT: A Lite BERT for Self-supervised Learning of Language Representations
@section Model architectures

BERT uses the popular transformer encoder architecture , which we will not review in detail. Following the annotation of BERTs,

we denote the number transformer encoder layers as MATH , the hidden size as MATH , the number of self-attention heads as MATH ,

and the vocab embedding size as MATH . We also set the feed-forward/filter size to be MATH . We primary report results on the models listed in Table .

The major differences between BERT and ALBERT are smaller vocabulary embedding size and cross-layer parameter sharing. Because of these two techniques, ALBERTs have much smaller parameter size compared to BERT with similar architecture. For example, ALBERT-large has about 18x less parameters compared to BERT-large. For BERTs, besides base and large models as reported by , we are able to train an xlarge model with a hidden size 2x as large as the BERT-large model. However, this BERT-xlarge has about 1.3 billions parameters, which make it difficult to train as it requires a Cloud-TPU machine with 1024 chips that is hard to get. On the contrary, ALBERTs have much smaller parameter size hence memory footprint, so we are able to scale to a model with 4x larger hidden size than BERT-large while having smaller parameter size.

@src https://arxiv.org/abs/1909.11942
@title ALBERT: A Lite BERT for Self-supervised Learning of Language Representations
@section Model architecture choices

The backbone of the ALBERT architecture is similar to BERT in that it uses a transformer encoder with GELU nonlinearities .

We follow the BERT notation conventions and denote the vocabulary embedding size as MATH , the number of encoder layers as MATH , and the hidden size as MATH . Following ,

we set the feed-forward/filter size to be MATH and the number of attention heads to be MATH .

There are three main contributions that ALBERT makes over the design choices of BERT.

In BERT, as well as subsequent modeling improvements such as and , the WordPiece embedding size MATH is tied with the hidden layer size MATH , i.e., MATH .

This decision appears suboptimal for both modeling and practical reasons, as follows.

From a modeling perspective, WordPiece embeddings are meant to learn context-independent representations, whereas hidden-layer embeddings are meant to learn context-dependent representations.

As experiments with context length indicate , the power of BERT-like representations comes from the use of context to provide the signal for learning such context-dependent representations.

As such, untying the WordPiece embedding size MATH from the hidden layer size MATH allows us to make a more efficient usage of the total model parameters as informed by modeling needs, which dictate that MATH .

From a practical perspective, natural language processing usually require the vocabulary size MATH to be large. (Similar to BERT, all the experiments in this paper use a vocabulary size MATH of 30,000.

If MATH , then increasing MATH increases the size of the embedding matrix, which has size MATH .

This can easily result in a model with billions of parameters, most of which are only updated sparsely during training.

Therefore, for ALBERT we use a factorization of the embedding parameters, decomposing them into two smaller matrices.

Instead of projecting the one-hot vectors directly into the hidden space of size MATH , we first project them into a lower dimensional embedding space of size MATH , and then project it to the hidden space.

By using this decomposition, we reduce the embedding parameters from MATH to MATH .

This parameter reduction is significant when MATH . We choose to use the same E for all word pieces because they are much more evenly distributed across documents compared to whole-word embedding, where having different embedding size ( ) for different words is important.

For ALBERT, we propose cross-layer parameter sharing as another way to improve parameter efficiency.

There are multiple ways to share parameters, e.g., only sharing feed-forward network (FFN) parameters across layers, or only sharing attention parameters.

The default decision for ALBERT is to share all parameters across layers. All our experiments use this default decision unless otherwise specified.

We compare this design decision against other strategies in our experiments in Sec. .

Similar strategies have been explored by (Universal Transformer, UT) and (Deep Equilibrium Models, DQE) for Transformer networks.

Different from our observations, show that UT outperforms a vanilla Transformer.

show that their DQEs reach an equilibrium point for which the input and output embedding of a certain layer stay the same.

Our measurement on the L2 distances and cosine similarity show that our embeddings are oscillating rather than converging.

Figure shows the L2 distances and cosine similarity of the input and output embeddings for each layer, using BERT-large and ALBERT-large configurations (see Table ).

We observe that the transitions from layer to layer are much smoother for ALBERT than for BERT.

These results show that weight-sharing has an effect on stabilizing network parameters.

Although there is a drop for both metrics compared to BERT, they nevertheless do not converge to 0 even after 24 layers.

This shows that the solution space for ALBERT parameters is very different from the one found by DQE.

In addition to the masked language modeling (MLM) loss , BERT uses an additional loss called next-sentence prediction (NSP).

NSP is a binary classification loss for predicting whether two segments appear consecutively in the original text, as follows:

positive examples are created by taking consecutive segments from the training corpus;

negative examples are created by pairing segments from different documents;

positive and negative examples are sampled with equal probability.

The NSP objective was designed to improve performance on downstream tasks, such as natural language inference, that require reasoning about the relationship between sentence pairs.

However, subsequent studies found NSP's impact unreliable and decided to eliminate it, a decision supported by an improvement in downstream task performance across several tasks.

We conjecture that the main reason behind NSP's ineffectiveness is its lack of difficulty as a task, as compared to MLM.

As formulated, NSP conflates topic prediction and coherence prediction in a single task (Since a negative example is constructed using material from a different document, the negative-example segment is misaligned both from a topic and from a coherence perspective. .

However, topic prediction is easier to learn compared to coherence prediction, and also overlaps more with what is learned using the MLM loss.

We maintain that inter-sentence modeling is an important aspect of language understanding, but we propose a loss based primarily on coherence .

That is, for ALBERT, we use a sentence-order prediction (SOP) loss, which avoids topic prediction and instead focuses on modeling inter-sentence coherence.

The SOP loss uses as positive examples the same technique as BERT (two consecutive segments from the same document), and as negative examples the same two consecutive segments but with their order swapped.

This forces the model to learn finer-grained distinctions about discourse-level coherence properties.

As we show in Sec. , it turns out that NSP cannot solve the SOP task at all (i.e., it ends up learning the easier topic-prediction signal, and performs at random-baseline level on the SOP task), while SOP can solve the NSP task to a reasonable degree, presumably based on analyzing misaligned coherence cues.

As a result, ALBERT models consistently improve downstream task performance for multi-sentence encoding tasks.

@src https://arxiv.org/abs/1909.11942
@title ALBERT: A Lite BERT for Self-supervised Learning of Language Representations
@section Additional training data and dropout effects

The experiments done up to this point use only the Wikipedia and BookCorpus datasets, as in .

In this section, we report measurements on the impact of the additional data used by both XLNet and RoBERTa .

Fig. plots the dev set MLM accuracy under two conditions, without and with additional data, with the latter condition giving a significant boost.

We also observe performance improvements on the downstream tasks in Table , except for the SQuAD benchmarks (which are Wikipedia-based, and therefore are negatively affected by out-of-domain training material).

We also note that, even after training for 1M steps, our largest models still do not overfit to their training data.

As a result, we decide to remove dropout to further increase our model capacity.

The plot in Fig. shows that removing dropout significantly improves MLM accuracy.

Intermediate evaluation on ALBERT-xxlarge at around 1M training steps (Table ) also confirms that removing dropout helps the downstream tasks.

There is empirical and theoretical evidence showing that a combination of batch normalization and dropout in Convolutional Neural Networks may have harmful results.

To the best of our knowledge, we are the first to show that dropout can hurt performance in large Transformer-based models. However, the underlying network structure of ALBERT is a special case of the transformer and further experimentation is needed to see if this phenomenon appears with other transformer-based architectures or not.

@src https://arxiv.org/abs/1910.10683
@title Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer
@section Training

As described in sec:format , all tasks are formulated as text-to-text tasks.

This allows us to always train using standard maximum likelihood, i.e.\ using teacher forcing and a cross-entropy loss.

At test time, we use greedy decoding (i.e.\ choosing the highest-probability logit at every timestep).

We pre-train each model for MATH steps on C4 before fine-tuning.

We use a maximum sequence length of MATH and a batch size of MATH sequences.

Whenever possible, we "pack" multiple sequences into each entry of the batch (https://www.pydoc.io/pypi/tensor2tensor-1.5.7/autoapi/data_generators/generator_utils/index.html#data_generators.generator_utils.pack_examples so that our batches contain roughly MATH tokens.

In total, this batch size and number of steps corresponds to pre-training on MATH tokens.

This is considerably less than BERT , which used roughly MATH tokens, or RoBERTa , which used roughly MATH tokens.

Using only MATH tokens results in a reasonable computational budget while still providing a sufficient amount of pre-training for acceptable performance.

We consider the effect of pre-training for more steps in sec:scaling,sec:together .

Note that MATH tokens only covers a fraction of the entire C4 data set, so we never repeat any data during pre-training.

During pre-training, we use an "inverse square root" learning rate schedule: MATH where MATH is the current training iteration and MATH is the number of warm-up steps (set to MATH in all of our experiments).

This sets a constant learning rate of MATH for the first MATH steps, then exponentially decays the learning rate until pre-training is over.

We also experimented with using a triangular learning rate , which produced slightly better results but requires knowing the total number of training steps ahead of time.

Since we will be varying the number of training steps in some of our experiments, we opt for the more generic inverse square root schedule.

Our models are fine-tuned for MATH steps on all tasks.

This value was chosen as a trade-off between the high-resource tasks (i.e.\ those with large data sets), which benefit from additional fine-tuning, and low-resource tasks (smaller data sets), which overfit quickly.

During fine-tuning, we continue using batches with MATH length- MATH sequences (i.e.\ MATH tokens per batch).

We use a constant learning rate of MATH when fine-tuning.

We save a checkpoint every MATH steps and report results on the model checkpoint corresponding to the highest validation performance.

For models fine-tuned on multiple tasks, we choose the best checkpoint for each task independently.

For all of the experiments except those in sec:together , we report results in the validation set to avoid performing model selection on the test set.

@src https://arxiv.org/abs/1910.10683
@title Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer
@section Disparate High-Level Approaches

To begin with, we compare three techniques that are inspired by commonly-used objectives but differ significantly in their approach.

First, we include a basic "prefix language modeling" objective as was used in sec:architecture_objectives .

This technique splits a span of text into two components, one to use as inputs to the encoder and the other to use as a target sequence to be predicted by the decoder.

Second, we consider an objective inspired by the "masked language modeling" (MLM) objective used in BERT .

MLM takes a span of text and corrupts MATH of the tokens.

MATH of the corrupted tokens are replaced with a special mask token and MATH are replaced with a random token.

Since BERT is an encoder-only model, its goal during pre-training is to reconstruct masked tokens at the output of the encoder.

In the encoder-decoder case, we simply use the entire uncorrupted sequence as the target.

Note that this differs from our baseline objective, which uses only the corrupted tokens as targets; we compare these two approaches in sec:simplifying_bert .

Finally, we also consider a basic deshuffling objective as used e.g.\ in where it was applied to a denoising sequential autoencoder.

This approach takes a sequence of tokens, shuffles it, and then uses the original deshuffled sequence as a target.

We provide examples of the inputs and targets for these three methods in the first three rows of tab:objectives .

The performance of these three objectives is shown in tab:objectives_highlevel .

Overall, we find that the BERT-style objective performs best, though the prefix language modeling objective attains similar performance on the translation tasks.

Indeed, the motivation for the BERT objective was to outperform language model-based pre-training.

The deshuffling objective performs considerably worse than both prefix language modeling and the BERT-style objective.

@src https://arxiv.org/abs/1910.10683
@title Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer
@section Pre-training Data set

Like the unsupervised objective, the pre-training data set itself is a crucial component of the transfer learning pipeline.

However, unlike objectives and benchmarks, new pre-training data sets are usually not treated as significant contributions on their own and are often not released alongside pre-trained models and code.

Instead, they are typically introduced in the course of presenting a new method or model.

As a result, there has been relatively little comparison of different pre-training data sets as well as a lack of a "standard" data set used for pre-training.

Some recent notable exceptions have compared pre-training on a new large (often Common Crawl-sourced) data set to using a smaller preexisting data set (often Wikipedia).

To probe more deeply into the impact of the pre-training data set on performance, in this section we compare variants of our C4 data set and other potential sources of pre-training data.

We release all of the C4 data set variants we consider as part of TensorFlow Datasets. (https://www.tensorflow.org/datasets/catalog/c4

@src https://arxiv.org/abs/1910.10683
@title Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer
@section Pre-training Data set Size

The pipeline we use to create C4 was designed to be able to create extremely large pre-training data sets.

The access to so much data allows us to pre-train our models without repeating examples.

It is not clear whether repeating examples during pre-training would be helpful or harmful to downstream performance because our pre-training objective is itself stochastic and can help prevent the model from seeing the same exact data multiple times.

To test the effect of limited unlabeled data set sizes, we pre-trained our baseline model on artificially truncated versions of C4.

Recall that we pre-train our baseline model on MATH tokens (a small fraction of the total size of C4).

We consider training on truncated variants of C4 consisting of MATH , MATH , MATH and MATH tokens.

These sizes correspond to repeating the data set MATH , MATH , MATH , and MATH times respectively over the course of pre-training.

The resulting downstream performance is shown in tab:datasets_take .

As expected, performance degrades as the data set size shrinks.

We suspect this may be due to the fact that the model begins to memorize the pre-training data set.

To measure if this is true, we plot the training loss for each of these data set sizes in fig:datasets_take_loss .

Indeed, the model attains significantly smaller training losses as the size of the pre-training data set shrinks, suggesting possible memorization.

similarly observed that truncating the pre-training data set size can degrade downstream task performance.

We note that these effects are limited when the pre-training data set is repeated only MATH times.

This suggests that some amount of repetition of pre-training data might not be harmful.

However, given that additional pre-training can be beneficial (as we will show in sec:scaling ) and that obtaining additional unlabeled data is cheap and easy, we suggest using large pre-training data sets whenever possible.

We also note that this effect may be more pronounced for larger model sizes, i.e.\ a bigger model may be more prone to overfitting to a smaller pre-training data set.

@src https://arxiv.org/abs/1910.10683
@title Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer
@section Training Strategy

So far we have considered the setting where all parameters of a model are pre-trained on an unsupervised task before being fine-tuned on individual supervised tasks.

While this approach is straightforward, various alternative methods for training the model on downstream/supervised tasks have been proposed.

In this section, we compare different schemes for fine-tuning the model in addition to the approach of training the model simultaneously on multiple tasks.

@src https://arxiv.org/abs/1910.10683
@title Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer
@section Fine-tuning Methods

It has been argued that fine-tuning all of the model's parameters can lead to suboptimal results, particularly on low-resource tasks .

Early results on transfer learning for text classification tasks advocated fine-tuning only the parameters of a small classifier that was fed sentence embeddings produced by a fixed pre-trained model .

This approach is less applicable to our encoder-decoder model because the entire decoder must be trained to output the target sequences for a given task.

Instead, we focus on two alternative fine-tuning approaches that update only a subset of the parameters of our encoder-decoder model.

The first, "adapter layers" , is motivated by the goal of keeping most of the original model fixed while fine-tuning.

Adapter layers are additional dense-ReLU-dense blocks that are added after each of the preexisting feed-forward networks in each block of the Transformer.

These new feed-forward networks are designed so that their output dimensionality matches their input.

This allows them to be inserted into the network with no additional changes to the structure or parameters.

When fine-tuning, only the adapter layer and layer normalization parameters are updated.

The main hyperparameter of this approach is the inner dimensionality MATH of the feed-forward network, which changes the number of new parameters added to the model.

We experiment with various values for MATH .

The second alternative fine-tuning method we consider is "gradual unfreezing" .

In gradual unfreezing, more and more of the model's parameters are fine-tuned over time.

Gradual unfreezing was originally applied to a language model architecture consisting of a single stack of layers.

In this setting, at the start of fine-tuning only the parameters of the final layer are updated, then after training for a certain number of updates the parameters of the second-to-last layer are also included, and so on until the entire network's parameters are being fine-tuned.

To adapt this approach to our encoder-decoder model, we gradually unfreeze layers in the encoder and decoder in parallel, starting from the top in both cases.

Since the parameters of our input embedding matrix and output classification matrix are shared, we update them throughout fine-tuning.

Recall that our baseline model consists of MATH layers each in the encoder and decoder and is fine-tuned for MATH steps.

As such, we subdivide the fine-tuning process into MATH episodes of MATH steps each and train from layers MATH to MATH in the MATH th episode.

We note that suggested fine-tuning an additional layer after each epoch of training.

However, since our supervised data sets vary so much in size and since some of our downstream tasks are actually mixtures of many tasks (GLUE and SuperGLUE), we instead adopt the simpler strategy of fine-tuning an additional layer after every MATH steps.

A comparison of the performance of these fine-tuning approaches is shown in tab:finetuning .

For adapter layers, we report the performance using an inner dimensionality MATH of MATH , MATH , MATH , MATH .

Pursuant with past results we find that lower-resource tasks like SQuAD work well with a small value of MATH whereas higher resource tasks require a large dimensionality to achieve reasonable performance.

This suggests that adapter layers could be a promising technique for fine-tuning on fewer parameters as long as the dimensionality is scaled appropriately to the task size.

Note that in our case we treat GLUE and SuperGLUE each as a single "task" by concatenating their constituent data sets, so although they comprise some low-resource data sets the combined data set is large enough that it necessitates a large value of MATH .

We found that gradual unfreezing caused a minor degradation in performance across all tasks, though it did provide some speedup during fine-tuning.

Better results may be attainable by more carefully tuning the unfreezing schedule.

@src https://arxiv.org/abs/1910.13461
@title BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension
@section Architecture

BART uses the standard sequence-to-sequence Transformer architecture from , except, following GPT, that we modify ReLU activation functions to GeLUs and initialise parameters from MATH . For our base model, we use 6 layers in the encoder and decoder, and for our large model we use 12 layers in each. The architecture is closely related to that used in BERT, with the following differences: (1) each layer of the decoder additionally performs cross-attention over the final hidden layer of the encoder (as in the transformer sequence-to-sequence model); and (2) BERT uses an additional feed-forward network before word-prediction, which BART does not. In total, BART contains roughly 10% more parameters than the equivalently sized BERT model.

@src https://arxiv.org/abs/1910.13461
@title BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension
@section Pre-training BART

BART is trained by corrupting documents and then optimizing a reconstruction loss—the cross-entropy between the decoder's output and the original document. Unlike existing denoising autoencoders, which are tailored to specific noising schemes, BART allows us to apply any type of document corruption.

In the extreme case, where all information about the source is lost, BART is equivalent to a language model.

We experiment with several previously proposed and novel transformations, but we believe there is a significant potential for development of other new alternatives. The transformations we used are summarized below, and examples are shown in Figure .

Token Masking Following BERT , random tokens are sampled and replaced with [MASK] elements.

Token Deletion Random tokens are deleted from the input. In contrast to token masking, the model must decide which positions are missing inputs.

Text Infilling A number of text spans are sampled, with span lengths drawn from a Poisson distribution ( MATH ). Each span is replaced with a single [MASK] token. 0-length spans correspond to the insertion of [MASK] tokens.

Text infilling is inspired by SpanBERT , but SpanBERT samples span lengths from a different (clamped geometric) distribution, and replaces each span with a sequence of [MASK] tokens of exactly the same length. Text infilling teaches the model to predict how many tokens are missing from a span.

Sentence Permutation A document is divided into sentences based on full stops, and these sentences are shuffled in a random order.

Document Rotation A token is chosen uniformly at random, and the document is rotated so that it begins with that token. This task trains the model to identify the start of the document.

@src https://arxiv.org/abs/2003.10555
@title ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators
@section Method

We first describe the replaced token detection pre-training task; see Figure for an overview.

We suggest and evaluate several modeling improvements for this method in Section .

Our approach trains two neural networks, a generator MATH and a discriminator MATH .

Each one primarily consists of an encoder (e.g., a Transformer network) that maps a sequence on input tokens MATH into a sequence of contextualized vector representations

For a given position MATH , (in our case only positions where MATH ),

the generator outputs a probability for generating a particular token MATH with a softmax layer:

p_G(x_t | ) = exp (e(x_t)^T h_G( )_t ) / _ x' (e(x')^T h_G( )_t )

For a given position MATH , the discriminator predicts whether the token MATH is "real," i.e., that it comes from the data rather than the generator distribution, with a sigmoid output layer:

The generator is trained to perform masked language modeling (MLM). Given an input MATH , MLM first select a random set of positions (integers between 1 and MATH ) to mask out MATH . (Typically MATH , i.e., 15% of the tokens are masked out.

The tokens in the selected positions are replaced with a MATH token: we denote this as MATH .

The generator then learns to predict the original identities of the masked-out tokens.

The discriminator is trained to distinguish tokens in the data from tokens that have been replaced by generator samples.

More specifically, we create a corrupted example MATH by replacing the masked-out tokens with generator samples and train the discriminator to predict which tokens in MATH match the original input MATH . Formally, model inputs are constructed according to

& = ( _ t=1 ^n - 1 ( _t = x_t) ( , t) - 1 ( _t x_t) (1 - ( , t)) )

Although similar to the training objective of a GAN, there are several key differences.

First, if the generator happens to generate the correct token, that token is considered "real" instead of "fake"; we found this formulation to moderately improve results on downstream tasks.

More importantly, the generator is trained with maximum likelihood rather than being trained adversarially to fool the discriminator.

Adversarially training the generator is challenging because it is impossible to back-propagate through sampling from the generator.

Although we experimented circumventing this issue by using reinforcement learning to train the generator (see Appendix ), this performed worse than maximum-likelihood training.

Lastly, we do not supply the generator with a noise vector as input, as is typical with a GAN.

over a large corpus MATH of raw text. We approximate the expectations in the losses with a single sample.

We don't back-propagate the discriminator loss through the generator (indeed, we can't because of the sampling step).

After pre-training, we throw out the generator and fine-tune the discriminator on downstream tasks.

@src https://arxiv.org/abs/2003.10555
@title ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators
@section Pre-Training Details

The following details apply to both our ELECTRA models and BERT baselines.

We mostly use the same hyperparameters as BERT.

We set MATH , the weight for the discriminator objective in the loss to 50. (As a binary classification task instead of the 30,000-way classification task in MLM, the discriminator's loss was typically much lower than the generator's.

We use dynamic token masking with the masked positions decided on-the-fly instead of during preprocessing.

Also, we did not use the next sentence prediction objective proposed in the original BERT paper, as recent work has suggested it does not improve scores .

For our ELECTRA-Large model, we used a higher mask percent (25 instead of 15) because we noticed the generator was achieving high accuracy with 15% masking, resulting in very few replaced tokens.

We searched for the best learning rate for the Base and Small models out of [1e-4, 2e-4, 3e-4, 5e-4] and selected MATH out of [1, 10, 20, 50, 100] in early experiments. Otherwise we did no hyperparameter tuning beyond the experiments in Section .

The full set of hyperparameters are listed in Table .

@src https://arxiv.org/abs/2003.10555
@title ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators
@section Adversarial Training

Here we detail attempts to adversarially train the generator instead of using maximum likelihood.

In particular we train the generator MATH to maximize the discriminator loss MATH .

As our discriminator isn't precisely the same as the discriminator of a GAN (see the discussion in Section ), this method is really an instance of Adversarial Contrastive Estimation rather than Generative Adversarial Training.

It is not possible to adversarially train the generator by back-propagating through the discriminator (e.g., as in a GAN trained on images) due to the discrete sampling from the generator, so we use reinforcement learning instead.

Our generator is different from most text generation models in that it is non-autogregressive: predictions are made independently.

In other words, rather than taking a sequence of actions where each action generates a token, the generator takes a single giant action of generating all tokens simultaneously, where the probability for the action factorizes as the product of generator probabilities for each token.

To deal with this enormous action space, we make the following simplifying assumption: that the discriminator's prediction MATH depends only on the token MATH and the non-replaced tokens MATH , i.e., it does not depend on other generated tokens MATH . This isn't too bad of an assumption because a relatively small number of tokens are replaced, and it greatly simplifies credit assignment when using reinforcement learning.

Notationally, we show this assumption by (in a slight abuse of notation) by writing MATH for the discriminator predicting whether the generated token MATH equals the original token MATH given the masked context MATH .

A useful consequence of this assumption is that the discriminator score for non-replaced tokens ( MATH for MATH ) is independent of MATH because we are assuming it does not depend on any replaced token. Therefore these tokens can be ignored when training MATH to maximize MATH .

_ _G = _ _G _ , , ( _ t=1 ^n -& 1 ( _t = x_t) ( , t) - & 1 ( _t x_t) (1 - ( , t)) )

Using the simplifying assumption, we approximate the above by finding the argmax of

& _ , , ( _ t - 1 ( x _t = x_t) ( x | ) - 1 ( x _t x_t) (1 - ( x | )) )

In short, the simplifying assumption allows us to decompose the loss over the individual generated tokens.

We cannot directly find MATH using gradient ascent because it is impossible to back-propagate through discrete sampling of MATH .

Instead, we use policy gradient reinforcement learning .

In particular, we use the REINFORCE gradient

_ _G _ , _ t _ x _t p_G _ _g p_G( x _t| ) [R( x _t, ) - b( , t)]

Where MATH is a learned baseline implemented as MATH

where MATH are the outputs of the generator's Transformer encoder.

The baseline is trained with cross-entropy loss to match the reward for the corresponding position.

We approximate the expectations with a single sample and learn MATH with gradient ascent.

Despite receiving no explicit feedback about which generated tokens are correct, we found the adversarial training resulted in a fairly accurate generator (for a 256-hidden-size generator, the adversarially trained one achieves 58% accuracy at masked language modeling while the same sized MLE generator gets 65%).

However, using this generator did not improve over the MLE-trained one on downstream tasks (see the right of Figure in the main paper).

@src https://arxiv.org/abs/2005.11401
@title Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
@section Methods

We explore RAG models, which use the input sequence to retrieve text documents and use them as additional context when generating the target sequence . As shown in Figure , our models leverage two components: (i) a retriever MATH with parameters that returns (top-K truncated) distributions over text passages given a query and (ii) a generator MATH parametrized by that generates a current token based on a context of the previous MATH tokens MATH , the original input and a retrieved passage .

To train the retriever and generator end-to-end, we treat the retrieved document as a latent variable.

We propose two models that marginalize over the latent documents in different ways to produce a distribution over generated text. In one approach, , the model uses the same document to predict each target token. The second approach, , can predict each target token based on a different document. In the following, we formally introduce both models and then describe the MATH and MATH components, as well as the training and decoding procedure.

@src https://arxiv.org/abs/2005.11401
@title Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
@section Training

We jointly train the retriever and generator components without any direct supervision on what document should be retrieved.

Given a fine-tuning training corpus of input/output pairs MATH , we minimize the negative marginal log-likelihood of each target, MATH using stochastic gradient descent with Adam .

Updating the document encoder MATH during training is costly as it requires the document index to be periodically updated as REALM does during pre-training . We do not find this step necessary for strong performance, and keep the document encoder (and index) fixed, only fine-tuning the query encoder MATH and the BART generator.

@src https://arxiv.org/abs/2005.11401
@title Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
@section Implementation Details

For Open-domain QA we report test numbers using 15 retrieved documents for models. For models, we report test results using 50 retrieved documents, and we use the Thorough Decoding approach since answers are generally short. We use greedy decoding for QA as we did not find beam search improved results. For Open-MSMarco and Jeopardy question generation, we report test numbers using ten retrieved documents for both and , and we also train a BART-large model as a baseline. We use a beam size of four, and use the Fast Decoding approach for models, as Thorough Decoding did not improve performance.

@src https://arxiv.org/abs/2005.11401
@title Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
@section Training setup Details

We train all RAG models and BART baselines using Fairseq . (https://github.com/pytorch/fairseq

We train with mixed precision floating point arithmetic , distributing training across 8, 32GB NVIDIA V100 GPUs, though training and inference can be run on one GPU.

We find that doing Maximum Inner Product Search with FAISS is sufficiently fast on CPU, so we store document index vectors on CPU, requiring MATH GB of CPU memory for all of Wikipedia.

After submission, We have ported our code to HuggingFace Transformers (https://github.com/huggingface/transformers , which achieves equivalent performance to the previous version but is a cleaner and easier to use implementation. This version is also open-sourced. We also compress the document index using FAISS's compression tools, reducing the CPU memory requirement to 36GB. Scripts to run experiments with RAG can be found at https://github.com/huggingface/transformers/blob/master/examples/rag/README.md and an interactive demo of a RAG model can be found at https://huggingface.co/rag/

@src https://arxiv.org/abs/2005.12872
@title End-to-End Object Detection with Transformers
@section architecture

The overall architecture is surprisingly simple and depicted in Figure . It contains three main components, which we describe below: a CNN backbone to extract a compact feature representation, an encoder-decoder transformer, and a simple feed forward network (FFN) that makes the final detection prediction.

Unlike many modern detectors, can be implemented in any deep learning framework that provides a common CNN backbone and a transformer architecture implementation with just a few hundred lines. Inference code for can be implemented in less than 50 lines in PyTorch . We hope that the simplicity of our method will attract new researchers to the detection community.

@src https://arxiv.org/abs/2005.12872
@title End-to-End Object Detection with Transformers
@section Training details.

following the recipe for bounding box detection to predict boxes around stuff

During inference we collapse different mask predictions of the same stuff

category in one. The new mask head is trained for 25 epochs (see supplementary

for details). Similarly to , we remove small stuff

(resp. things) predictions that have area smaller than 256 pixels (resp 4

pixels) as they are likely to be spurious segments, and keep only the detections

with a confidence higher than 75%. The new mask head is trained for 25 epochs (see supplementary

for details). During inference we first filter out the detection with a confidence below 85%, then compute the per-pixel argmax to determine in which mask each pixel belongs. We then collapse different mask predictions of the same stuff

category in one, and filter the empty ones (less than 4 pixels).

@src https://arxiv.org/abs/2005.12872
@title End-to-End Object Detection with Transformers
@section Detailed architecture

The detailed description of the transformer used in , with positional encodings passed at every attention layer, is given in Fig. .

Image features from the CNN backbone are passed

through the transformer encoder, together with spatial positional encoding

that are added to queries and keys at every multi-head self-attention layer.

Then, the decoder receives queries (initially set to zero),

output positional encoding (object queries), and encoder memory, and produces the final

set of predicted class labels and bounding boxes through multiple

multi-head self-attention and decoder-encoder attention.

The first self-attention layer in the first decoder layer can be skipped.

We use -256 with 8 heads, and -512 with 16 heads.

@src https://arxiv.org/abs/2005.14165
@title Language Models are Few-Shot Learners
@section Approach

Our basic pre-training approach, including model, data, and training, is similar to the process described in , with relatively straightforward scaling up of the model size, dataset size and diversity, and length of training. Our use of in-context learning is also similar to , but in this work we systematically explore different settings for learning within the context. Therefore, we start this section by explicitly defining and contrasting the different settings that we will be evaluating GPT-3 on or could in principle evaluate GPT-3 on. These settings can be seen as lying on a spectrum of how much task-specific data they tend to rely on. Specifically, we can identify at least four points on this spectrum (see Figure for an illustration):

Fine-Tuning (FT) has been the most common approach in recent years, and involves updating the weights of a pre-trained model by training on a supervised dataset specific to the desired task. Typically thousands to hundreds of thousands of labeled examples are used. The main advantage of fine-tuning is strong performance on many benchmarks. The main disadvantages are the need for a new large dataset for every task, the potential for poor generalization out-of-distribution , and the potential to exploit spurious features of the training data , potentially resulting in an unfair comparison with human performance. In this work we do not fine-tune GPT-3 because our focus is on task-agnostic performance, but GPT-3 can be fine-tuned in principle and this is a promising direction for future work.

Few-Shot (FS) is the term we will use in this work to refer to the setting where the model is given a few demonstrations of the task at inference time as conditioning , but no weight updates are allowed. As shown in Figure , for a typical dataset an example has a context and a desired completion (for example an English sentence and the French translation), and few-shot works by giving MATH examples of context and completion, and then one final example of context, with the model expected to provide the completion. We typically set MATH in the range of 10 to 100 as this is how many examples can fit in the model’s context window ( MATH ). The main advantages of few-shot are a major reduction in the need for task-specific data and reduced potential to learn an overly narrow distribution from a large but narrow fine-tuning dataset. The main disadvantage is that results from this method have so far been much worse than state-of-the-art fine-tuned models. Also, a small amount of task specific data is still required. As indicated by the name, few-shot learning as described here for language models is related to few-shot learning as used in other contexts in ML – both involve learning based on a broad distribution of tasks (in this case implicit in the pre-training data) and then rapidly adapting to a new task.

One-Shot (1S) is the same as few-shot except that only one demonstration is allowed, in addition to a natural language description of the task, as shown in Figure 1. The reason to distinguish one-shot from few-shot and zero-shot (below) is that it most closely matches the way in which some tasks are communicated to humans. For example, when asking humans to generate a dataset on a human worker service (for example Mechanical Turk), it is common to give one demonstration of the task. By contrast it is sometimes difficult to communicate the content or format of a task if no examples are given.

Zero-Shot (0S) is the same as one-shot except that no demonstrations are allowed, and the model is only given a natural language instruction describing the task. This method provides maximum convenience, potential for robustness, and avoidance of spurious correlations (unless they occur very broadly across the large corpus of pre-training data), but is also the most challenging setting. In some cases it may even be difficult for humans to understand the format of the task without prior examples, so this setting is in some cases "unfairly hard". For example, if someone is asked to "make a table of world records for the 200m dash", this request can be ambiguous, as it may not be clear exactly what format the table should have or what should be included (and even with careful clarification, understanding precisely what is desired can be difficult). Nevertheless, for at least some settings zero-shot is closest to how humans perform tasks – for example, in the translation example in Figure , a human would likely know what to do from just the text instruction.

Figure shows the four methods using the example of translating English to French. In this paper we focus on zero-shot, one-shot and few-shot, with the aim of comparing them not as competing alternatives, but as different problem settings which offer a varying trade-off between performance on specific benchmarks and sample efficiency. We especially highlight the few-shot results as many of them are only slightly behind state-of-the-art fine-tuned models. Ultimately, however, one-shot, or even sometimes zero-shot, seem like the fairest comparisons to human performance, and are important targets for future work.

Sections - below give details on our models, training data, and training process respectively.

Section discusses the details of how we do few-shot, one-shot, and zero-shot evaluations.

@src https://arxiv.org/abs/2005.14165
@title Language Models are Few-Shot Learners
@section Model and Architectures

We use the same model and architecture as GPT-2 , including the modified initialization, pre-normalization, and reversible tokenization described therein, with the exception that we use alternating dense and locally banded sparse attention patterns in the layers of the transformer, similar to the Sparse Transformer . To study the dependence of ML performance on model size, we train 8 different sizes of model, ranging over three orders of magnitude from 125 million parameters to 175 billion parameters, with the last being the model we call GPT-3. Previous work suggests that with enough training data, scaling of validation loss should be approximately a smooth power law as a function of size; training models of many different sizes allows us to test this hypothesis both for validation loss and for downstream language tasks.

Table shows the sizes and architectures of our 8 models. Here MATH is the total number of trainable parameters, MATH is the total number of layers, MATH is the number of units in each bottleneck layer (we always have the feedforward layer four times the size of the bottleneck layer, MATH MATH ), and MATH is the dimension of each attention head. All models use a context window of MATH tokens. We partition the model across GPUs along both the depth and width dimension in order to minimize data-transfer between nodes. The precise architectural parameters for each model are chosen based on computational efficiency and load-balancing in the layout of models across GPU’s. Previous work suggests that validation loss is not strongly sensitive to these parameters within a reasonably broad range.

@src https://arxiv.org/abs/2005.14165
@title Language Models are Few-Shot Learners
@section Training Dataset

Datasets for language models have rapidly expanded, culminating in the Common Crawl dataset (https://commoncrawl.org/the-data/ constituting nearly a trillion words. This size of dataset is sufficient to train our largest models without ever updating on the same sequence twice. However, we have found that unfiltered or lightly filtered versions of Common Crawl tend to have lower quality than more curated datasets. Therefore, we took 3 steps to improve the average quality of our datasets: (1) we downloaded and filtered a version of CommonCrawl based on similarity to a range of high-quality reference corpora, (2) we performed fuzzy deduplication at the document level, within and across datasets, to prevent redundancy and preserve the integrity of our held-out validation set as an accurate measure of overfitting, and (3) we also added known high-quality reference corpora to the training mix to augment CommonCrawl and increase its diversity.

Details of the first two points (processing of Common Crawl) are described in Appendix . For the third, we added several curated high-quality datasets, including an expanded version of the WebText dataset , collected by scraping links over a longer period of time, and first described in , two internet-based books corpora (Books1 and Books2) and English-language Wikipedia.

Table shows the final mixture of datasets that we used in training. The CommonCrawl data was downloaded from 41 shards of monthly CommonCrawl covering 2016 to 2019, constituting 45TB of compressed plaintext before filtering and 570GB after filtering, roughly equivalent to 400 billion byte-pair-encoded tokens. Note that during training, datasets are not sampled in proportion to their size, but rather datasets we view as higher-quality are sampled more frequently, such that CommonCrawl and Books2 datasets are sampled less than once during training, but the other datasets are sampled 2-3 times. This essentially accepts a small amount of overfitting in exchange for higher quality training data.

A major methodological concern with language models pretrained on a broad swath of internet data, particularly large models with the capacity to memorize vast amounts of content, is potential contamination of downstream tasks by having their test or development sets inadvertently seen during pre-training. To reduce such contamination, we searched for and attempted to remove any overlaps with the development and test sets of all benchmarks studied in this paper. Unfortunately, a bug in the filtering caused us to ignore some overlaps, and due to the cost of training it was not feasible to retrain the model. In Section we characterize the impact of the remaining overlaps, and in future work we will more aggressively remove data contamination.

@src https://arxiv.org/abs/2005.14165
@title Language Models are Few-Shot Learners
@section Training Process

As found in , larger models can typically use a larger batch size, but require a smaller learning rate. We measure the gradient noise scale during training and use it to guide our choice of batch size . Table shows the parameter settings we used. To train the larger models without running out of memory, we use a mixture of model parallelism within each matrix multiply and model parallelism across the layers of the network. All models were trained on V100 GPU’s on part of a high-bandwidth cluster provided by Microsoft. Details of the training process and hyperparameter settings are described in Appendix .

@src https://arxiv.org/abs/2005.14165
@title Language Models are Few-Shot Learners
@section Details of Model Training

To train all versions of GPT-3, we use Adam with MATH , MATH , and MATH , we clip the global norm of the gradient at 1.0, and we use cosine decay for learning rate down to 10% of its value, over 260 billion tokens (after 260 billion tokens, training continues at 10% of the original learning rate). There is a linear LR warmup over the first 375 million tokens. We also gradually increase the batch size linearly from a small value (32k tokens) to the full value over the first 4-12 billion tokens of training, depending on the model size. Data are sampled without replacement during training (until an epoch boundary is reached) to minimize overfitting. All models use weight decay of 0.1 to provide a small amount of regularization .

During training we always train on sequences of the full MATH token context window, packing multiple documents into a single sequence when documents are shorter than 2048, in order to increase computational efficiency. Sequences with multiple documents are not masked in any special way but instead documents within a sequence are delimited with a special end of text token, giving the language model the information necessary to infer that context separated by the end of text token is unrelated. This allows for efficient training without need for any special sequence-specific masking.

@src https://arxiv.org/abs/2006.11239
@title Denoising Diffusion Probabilistic Models
@section Simplified training objective

With the reverse process and decoder defined above, the variational bound, consisting of terms derived from eq:vb_term_langevin_eps,eq:discrete_decoder , is clearly differentiable with respect to MATH and is ready to be employed for training. However, we found it beneficial to sample quality (and simpler to implement) to train on the following variant of the variational bound:

where MATH is uniform between MATH and MATH . The MATH case corresponds to MATH with the integral in the discrete decoder definition eq:discrete_decoder approximated by the Gaussian probability density function times the bin width, ignoring MATH and edge effects. The MATH cases correspond to an unweighted version of eq:vb_term_langevin_eps , analogous to the loss weighting used by the NCSN denoising score matching model . ( MATH does not appear because the forward process variances MATH are fixed.)

alg:training displays the complete training procedure with this simplified objective.

Since our simplified objective eq:training_objective_simple discards the weighting in eq:vb_term_langevin_eps , it is a weighted variational bound that emphasizes different aspects of reconstruction compared to the standard variational bound .

In particular, our diffusion process setup in sec:experiments causes the simplified objective to down-weight loss terms corresponding to small MATH . These terms train the network to denoise data with very small amounts of noise, so it is beneficial to down-weight them so that the network can focus on more difficult denoising tasks at larger MATH terms. We will see in our experiments that this reweighting leads to better sample quality.

@src https://arxiv.org/abs/2006.11239
@title Denoising Diffusion Probabilistic Models
@section Reverse process parameterization and training objective ablation

In table:loss_ablation , we show the sample quality effects of reverse process parameterizations and training objectives ( sec:revproc_dsm_diffusion_connection ). We find that the baseline option of predicting MATH works well only when trained on the true variational bound instead of unweighted mean squared error, a simplified objective akin to eq:training_objective_simple . We also see that learning reverse process variances (by incorporating a parameterized diagonal MATH into the variational bound) leads to unstable training and poorer sample quality compared to fixed variances. Predicting MATH , as we proposed, performs approximately as well as predicting MATH when trained on the variational bound with fixed variances, but much better when trained with our simplified objective.

@src https://arxiv.org/abs/2010.02502
@title Denoising Diffusion Implicit Models
@section Datasets and architectures

We consider 4 image datasets with various resolutions: CIFAR10 ( MATH , unconditional), CelebA ( MATH ), LSUN Bedroom ( MATH ) and LSUN Church ( MATH ). For all datasets, we set the hyperparameters MATH according to the heuristic in to make the results directly comparable. We use the same model for each dataset, and only compare the performance of different generative processes. For CIFAR10, Bedroom and Church, we obtain the pretrained checkpoints from the original DDPM implementation; for CelebA, we trained our own model using the denoising objective MATH .

Our architecture for MATH follows that in , which is a U-Net based on a Wide ResNet . We use the pretrained models from for CIFAR10, Bedroom and Church, and train our own model for the CelebA MATH model (since a pretrained model is not provided). Our CelebA model has five feature map resolutions from MATH to MATH , and we use the original CelebA dataset (not CelebA-HQ) using the https://github.com/NVlabs/stylegan/blob/master/dataset_tool.py#L484-L499 pre-processing technique from the StyleGAN repository.

@src https://arxiv.org/abs/2010.11929
@title An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale
@section Method

In model design we follow the original Transformer as closely as possible.

An advantage of this intentionally simple setup is that scalable NLP Transformer architectures – and their efficient implementations – can be used almost out of the box.

An overview of the model is depicted in Figure .

The standard Transformer receives as input a 1D sequence of token embeddings.

To handle 2D images, we reshape the image MATH into a sequence of flattened 2D patches MATH , where MATH is the resolution of the original image, MATH is the number of channels, MATH is the resolution of each image patch, and MATH is the resulting number of patches, which also serves as the effective input sequence length for the Transformer.

The Transformer uses constant latent vector size MATH through all of its layers, so we flatten the patches and map to MATH dimensions with a trainable linear projection (Eq. ).

We refer to the output of this projection as the patch embeddings.

Similar to BERT's |[class]| token, we prepend a learnable embedding to the sequence of embedded patches ( MATH ), whose state at the output of the Transformer encoder ( MATH ) serves as the image representation MATH (Eq. ).

Both during pre-training and fine-tuning, a classification head is attached to MATH .

The classification head is implemented by a MLP with one hidden layer at pre-training time and by a single linear layer at fine-tuning time.

Position embeddings are added to the patch embeddings to retain positional information.

We use standard learnable 1D position embeddings, since we have not observed significant performance gains from using more advanced 2D-aware position embeddings (Appendix ).

The resulting sequence of embedding vectors serves as input to the encoder.

The Transformer encoder consists of alternating layers of multiheaded self-attention (MSA, see Appendix ) and MLP blocks (Eq. , ).

Layernorm (LN) is applied before every block, and residual connections after every block .

The MLP contains two layers with a GELU non-linearity.

We note that Vision Transformer has much less image-specific inductive bias than CNNs.

In CNNs, locality, two-dimensional neighborhood structure, and translation equivariance are baked into each layer throughout the whole model.

In ViT, only MLP layers are local and translationally equivariant, while the self-attention layers are global.

The two-dimensional neighborhood structure is used very sparingly: in the beginning of the model by cutting the image into patches and at fine-tuning time for adjusting the position embeddings for images of different resolution (as described below).

Other than that, the position embeddings at initialization time carry no information about the 2D positions of the patches and all spatial relations between the patches have to be learned from scratch.

As an alternative to raw image patches, the input sequence can be formed from feature maps of a CNN .

In this hybrid model, the patch embedding projection MATH (Eq. ) is applied to patches extracted from a CNN feature map.

As a special case, the patches can have spatial size 1x1, which means that the input sequence is obtained by simply flattening the spatial dimensions of the feature map and projecting to the Transformer dimension.

The classification input embedding and position embeddings are added as described above.

@src https://arxiv.org/abs/2010.11929
@title An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale
@section Pre-training Data Requirements

The performs well when pre-trained on a large JFT-300M dataset.

With fewer inductive biases for vision than ResNets, how crucial is the dataset size?

First, we pre-train models on datasets of increasing size: , ImageNet-21k, and JFT-300M.

To boost the performance on the smaller datasets, we optimize three basic regularization parameters – weight decay, dropout, and label smoothing.

Figure shows the results after fine-tuning to (results on other datasets are shown in Table ) (Note that the pre-trained models are also fine-tuned, but again on . This is because the resolution increase during fine-tuning improves the performance. .

When pre-trained on the smallest dataset, , -Large models underperform compared to -Base models, despite (moderate) regularization.

With ImageNet-21k pre-training, their performances are similar.

Only with JFT-300M, do we see the full benefit of larger models.

Figure also shows the performance region spanned by BiT models of different sizes.

The BiT CNNs outperform on , but with the larger datasets, overtakes.

Second, we train our models on random subsets of 9M, 30M, and 90M as well as the full JFT-300M dataset.

We do not perform additional regularization on the smaller subsets and use the same hyper-parameters for all settings.

This way, we assess the intrinsic model properties, and not the effect of regularization.

We do, however, use early-stopping, and report the best validation accuracy achieved during training.

To save compute, we report few-shot linear accuracy instead of full fine-tuning accuracy.

s overfit more than ResNets with comparable computational cost on smaller datasets.

For example, -B/32 is slightly faster than ResNet50; it performs much worse on the 9M subset, but better on 90M+ subsets.

The same is true for ResNet152x2 and -L/16.

This result reinforces the intuition that the convolutional inductive bias is useful for smaller datasets, but for larger ones, learning the relevant patterns directly from data is sufficient, even beneficial.

Overall, the few-shot results on ImageNet (Figure ), as well as the low-data results on VTAB (Table ) seem promising for very low-data transfer. Further analysis of few-shot properties of is an exciting direction of future work.

@src https://arxiv.org/abs/2010.11929
@title An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale
@section Training

Table summarizes our training setups for our different models. We found strong regularization to be key when training models from scratch on . Dropout, when used, is applied after every dense layer except for the the qkv-projections and directly after adding positional- to patch embeddings. Hybrid models are trained with the exact setup as their counterparts. Finally, all training is done on resolution 224.

@src https://arxiv.org/abs/2011.13456
@title Score-Based Generative Modeling through Stochastic Differential Equations
@section Architecture improvements

We explore several new architecture designs for score-based models using both VE and VP SDEs (details in app:arch_search ), where we train models with the same discrete objectives as in SMLD/DDPM. We directly transfer the architectures for VP SDEs to sub-VP SDEs due to their similarity. Our optimal architecture for the VE SDE, named NCSN++, achieves an FID of 2.45 on CIFAR-10 with PC samplers, while our optimal architecture for the VP SDE, called DDPM++, achieves 2.78.

By switching to the continuous training objective in eqn:training , and increasing the network depth, we can further improve sample quality for all models. The resulting architectures are denoted as NCSN++ cont. and DDPM++ cont. in tab:fid for VE and VP/sub-VP SDEs respectively. Results reported in tab:fid are for the checkpoint with the smallest FID over the course of training, where samples are generated with PC samplers. In contrast, FID scores and NLL values in tab:bpd are reported for the last training checkpoint, and samples are obtained with black-box ODE solvers. As shown in tab:fid , VE SDEs typically provide better sample quality than VP/sub-VP SDEs, but we also empirically observe that their likelihoods are worse than VP/sub-VP SDE counterparts. This indicates that practitioners likely need to experiment with different SDEs for varying domains and architectures.

Our best model for sample quality, NCSN++ cont. (deep, VE), doubles the network depth and sets new records for both inception score and FID on unconditional generation for CIFAR-10. Surprisingly, we can achieve better FID than the previous best conditional generative model without requiring labeled data. With all improvements together, we also obtain the first set of high-fidelity samples on CelebA-HQ MATH from score-based models (see app:hq ). Our best model for likelihoods, DDPM++ cont. (deep, sub-VP), similarly doubles the network depth and achieves a log-likelihood of 2.99 bits/dim with the continuous objective in eqn:training . To our best knowledge, this is the highest likelihood on uniformly dequantized CIFAR-10.

@src https://arxiv.org/abs/2011.13456
@title Score-Based Generative Modeling through Stochastic Differential Equations
@section The framework for more general SDEs

In the main text, we introduced our framework based on a simplified SDE eqn:forward_sde where the diffusion coefficient is independent of MATH . It turns out that our framework can be extended to hold for more general diffusion coefficients. We can consider SDEs in the following form:

where MATH and MATH . We follow the It\^ o interpretation of SDEs throughout this paper.

According to , the reverse-time SDE is given by ( , eqn:backward_sde )

where we define MATH for a matrix-valued function MATH throughout the paper.

The probability flow ODE corresponding to eqn:forward_sde_2 has the following form ( , eqn:flow , see a detailed derivation in app:prob_flow_derive ):

Finally for conditional generation with the general SDE eqn:forward_sde_2 , we can solve the conditional reverse-time SDE below ( , eqn:cond_sde , details in app:cond_gen ):

When the drift and diffusion coefficient of an SDE are not affine, it can be difficult to compute the transition kernel MATH in closed form. This hinders the training of score-based models, because eqn:training requires knowing MATH . To overcome this difficulty, we can replace denoising score matching in eqn:training with other efficient variants of score matching that do not require computing MATH . For example, when using sliced score matching , our training objective eqn:training becomes

where MATH is a positive weighting function, MATH , MATH , and MATH . We can always simulate the SDE to sample from MATH , and solve eqn:training_ssm to train the time-dependent score-based model MATH .

@src https://arxiv.org/abs/2011.13456
@title Score-Based Generative Modeling through Stochastic Differential Equations
@section Architecture improvements

We explored several architecture designs to improve score-based models for both VE and VP SDEs. Our endeavor gives rise to new state-of-the-art sample quality on CIFAR-10, new state-of-the-art likelihood on uniformly dequantized CIFAR-10, and enables the first high-fidelity image samples of resolution MATH from score-based generative models. Code and checkpoints are open-sourced at https://github.com/yang-song/score_sde https://github.com/yang-song/score_sde .

@src https://arxiv.org/abs/2011.13456
@title Score-Based Generative Modeling through Stochastic Differential Equations
@section Settings for architecture exploration

Unless otherwise noted, all models are trained for 1.3M iterations, and we save one checkpoint per 50k iterations. For VE SDEs, we consider two datasets: MATH CIFAR-10 and MATH CelebA , pre-processed following . We compare different configurations based on their FID scores averaged over checkpoints after 0.5M iterations. For VP SDEs, we only consider the CIFAR-10 dataset to save computation, and compare models based on the average FID scores over checkpoints obtained between 0.25M and 0.5M iterations, because FIDs turn to increase after 0.5M iterations for VP SDEs.

All FIDs are computed on 50k samples with https://github.com/tensorflow/gan tensorflow_gan . For sampling, we use the PC sampler discretized at 1000 time steps. We choose reverse diffusion (see app:reverse_diffusion ) as the predictor. We use one corrector step per update of the predictor for VE SDEs with a signal-to-noise ratio of 0.16, but save the corrector step for VP SDEs since correctors there only give slightly better results but require double computation. We follow for optimization, including the learning rate, gradient clipping, and learning rate warm-up schedules. Unless otherwise noted, models are trained with the original discrete SMLD and DDPM objectives in eqn:ncsn_obj,eqn:ddpm_obj and use a batch size of 128. The optimal architectures found under these settings are subsequently transferred to continuous objectives and deeper models. We also directly transfer the best architecture for VP SDEs to sub-VP SDEs, given the similarity of these two SDEs.

Our architecture is mostly based on . We additionally introduce the following components to maximize the potential improvement of score-based models.

Upsampling and downsampling images with anti-aliasing based on Finite Impulse Response (FIR) . We follow the same implementation and hyper-parameters in StyleGAN-2 .

Rescaling all skip connections by MATH . This has been demonstrated effective in several best-in-class GAN models, including ProgressiveGAN , StyleGAN and StyleGAN-2 .

Replacing the original residual blocks in DDPM with residual blocks from BigGAN .

Increasing the number of residual blocks per resolution from MATH to MATH .

Incorporating progressive growing architectures. We consider two progressive architectures for input: "input skip" and "residual", and two progressive architectures for output: "output skip" and "residual". These progressive architectures are defined and implemented according to StyleGAN-2.

We also tested equalized learning rates, a trick used in very successful models like ProgressiveGAN and StyleGAN . However, we found it harmful at an early stage of our experiments, and therefore decided not to explore more on it.

The exponential moving average (EMA) rate has a significant impact on performance. For models trained with VE perturbations, we notice that 0.999 works better than 0.9999, whereas for models trained with VP perturbations it is the opposite. We therefore use an EMA rate of 0.999 and 0.9999 for VE and VP models respectively.

@src https://arxiv.org/abs/2101.03961
@title Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity
@section Improved Training and Fine-Tuning Techniques

Sparse expert models may introduce training difficulties over a vanilla Transformer.

Instability can result because of the hard-switching (routing) decisions at each of these layers.

Further, low precision formats like bfloat16 can exacerbate issues in the softmax computation for our router.

We describe training difficulties here and the methods we use to overcome them to achieve stable and scalable training.

Selective precision with large sparse models.

Model instability hinders the ability to train using efficient bfloat16 precision, and as a result, trains with float32 precision throughout their MoE Transformer.

However, we show that by instead selectively casting to float32 precision within a localized part of the model, stability may be achieved, without incurring expensive communication cost of float32 tensors. This technique is inline with modern mixed precision training strategies where certain parts of the model and gradient updates are done in higher precision .

Table shows that our approach permits nearly equal speed to bfloat16 training while conferring the training stability of float32.

To achieve this, we cast the router input to float32 precision.

The router function takes the tokens as input and produces the dispatch and combine tensors used for the selection and recombination of expert computation (refer to Code Block in the Appendix for details).

Importantly, the float32 precision is only used within the body of the router function—on computations local to that device.

Because the resulting dispatch and combine tensors are recast to bfloat16 precision at the end of the function, no expensive float32 tensors are broadcast through all-to-all communication operations, but we still benefit from the increased stability of float32.

Smaller parameter initialization for stability.

Appropriate initialization is critical to successful training in deep learning and we especially observe this to be true for Switch Transformer.

We initialize our weight matrices by drawing elements from a truncated normal distribution with mean MATH and standard deviation MATH where MATH is a scale hyper-parameter and MATH is the number of input units in the weight tensor (e.g. fan-in). (Values greater than two standard deviations from the mean are resampled.

As an additional remedy to the instability, we recommend reducing the default Transformer initialization scale MATH by a factor of 10.

This both improves quality and reduces the likelihood of destabilized training in our experiments.

Table measures the improvement of the model quality and reduction of the variance early in training.

We find that the average model quality, as measured by the Neg. Log Perp., is dramatically improved and there is a far reduced variance across runs.

Further, this same initialization scheme is broadly effective for models spanning several orders of magnitude.

We use the same approach to stably train models as small as our 223M parameter baseline to enormous models in excess of one trillion parameters.

Regularizing large sparse models. Our paper considers the common NLP approach of pre-training on a large corpus followed by fine-tuning on smaller downstream tasks such as summarization or question answering.

One issue that naturally arises is overfitting since many fine-tuning tasks have very few examples.

During fine-tuning of standard Transformers, use dropout at each layer to prevent overfitting.

Our Switch Transformers have significantly more parameters than the FLOP matched dense baseline, which can lead to more severe overfitting on these smaller downstream tasks.

We thus propose a simple way to alleviate this issue during fine-tuning: increase the dropout inside the experts, which we name as expert dropout.

During fine-tuning we simply increase the dropout rate by a significant amount only at the interim feed-forward computation at each expert layer.

Table has the results for our expert dropout protocol.

We observe that simply increasing the dropout across all layers leads to worse performance.

However, setting a smaller dropout rate (0.1) at non-expert layers and a much larger dropout rate (0.4) at expert layers leads to performance improvements on four smaller downstream tasks.

@src https://arxiv.org/abs/2102.12092
@title Zero-Shot Text-to-Image Generation
@section Method

Our goal is to train a transformer to autoregressively model the text and image tokens as a single stream of data. However, using pixels directly as image tokens would require an inordinate amount of memory for high-resolution images. Likelihood objectives tend to prioritize modeling short-range dependencies between pixels , so much of the modeling capacity would be spent capturing high-frequency details instead of the low-frequency structure that makes objects visually recognizable to us.

We address these issues by using a two-stage training procedure, similar to :

Stage 1. We train a discrete variational autoencoder (dVAE) (https://github.com/openai/DALL-E to compress each MATH RGB image into a MATH grid of image tokens, each element of which can assume 8192 possible values. This reduces the context size of the transformer by a factor of MATH without a large degradation in visual quality (see Figure ).

Stage 2. We concatenate up to 256 BPE-encoded text tokens with the MATH image tokens, and train an autoregressive transformer to model the joint distribution over the text and image tokens.

The overall procedure can be viewed as maximizing the evidence lower bound (ELB) on the joint likelihood of the model distribution over images MATH , captions MATH , and the tokens MATH for the encoded RGB image. We model this distribution using the factorization MATH , which yields the lower bound

MATH denotes the distribution over the MATH image tokens generated by the dVAE encoder given the RGB image MATH (We assume that MATH is conditionally independent of MATH given MATH . ;

MATH denotes the distribution over the RGB images generated by the dVAE decoder given the image tokens; and

MATH denotes the joint distribution over the text and image tokens modeled by the transformer.

Note that the bound only holds for MATH , while in practice we find it helpful to use larger values . The following subsections describe both stages in further detail. (In preliminary experiments on ImageNet , we attempted to maximize the ELB with respect to MATH , MATH , and MATH jointly, but were unable to improve on two-stage training.

@src https://arxiv.org/abs/2102.12092
@title Zero-Shot Text-to-Image Generation
@section Mixed-Precision Training

To save GPU memory and increase throughput, most parameters, Adam moments, and activations are stored in 16-bit precision. We also use activation checkpointing and recompute the activations within the resblocks during the backward pass. Getting the model to train in 16-bit precision past one billion parameters, without diverging, was the most challenging part of this project.

We believe the root cause of this instability to be underflow in the 16-bit gradients. Appendix presents a set of guidelines we developed to avoid underflow when training large-scale generative models. Here, we describe one of these guidelines: per-resblock gradient scaling.

Similar to prior work , we found that the norms of the activation gradients from the resblocks decrease monotonically as we move from the earlier resblocks to the later ones. (It is possible that better initialization schemes might be able to avoid this, but we did not have success with alternative schemes in our experiments. As the model is made deeper and wider, the true exponents of the activation gradients for later resblocks can fall below the minimum exponent of the 16-bit format. Consequently, they get rounded to zero, a phenomenon called underflow. We found that eliminating underflow allowed for stable training to convergence.

Standard loss scaling is able to avoid underflow when the range spanned by the smallest and largest activation gradients (in absolute value) fits within the exponent range of the 16-bit format. On NVIDIA V100 GPUs, this exponent range is specified by five bits. While this is sufficient for training vanilla language models of the same size, we found the range to be too small for the text-to-image model.

Our fix, which is shown in Figure , involves using a separate "gradient scale" for each resblock in the model. This can be seen as a practical alternative to a more general framework for mixed-precision training called Flexpoint , with the advantage that specialized GPU kernels are not required. We found that had independently developed similar procedure for training convolutional networks in 4-bit precision.

@src https://arxiv.org/abs/2102.12092
@title Zero-Shot Text-to-Image Generation
@section Architecture

The dVAE encoder and decoder are convolutional ResNets with bottleneck-style resblocks. The models primarily use MATH convolutions, with MATH convolutions along skip connections in which the number of feature maps changes between the input and output of a resblock. The first convolution of the encoder is MATH , and the last convolution of the encoder (which produces the MATH output used as the logits for the categorical distributions for the image tokens) is MATH . Both the first and last convolutions of the decoder are MATH . The encoder uses max-pooling (which we found to yield better ELB than average-pooling) to downsample the feature maps, and the decoder uses nearest-neighbor upsampling. The precise details for the architectures are given in the files dvae/encoder.py and dvae/decoder.py of the code release.

@src https://arxiv.org/abs/2102.12092
@title Zero-Shot Text-to-Image Generation
@section Training

The dVAE is trained on the same dataset as the transformer, using the data augmentation code given in Listing . Several quantities are decayed during training, all of which use a cosine schedule:

The KL weight MATH is increased from MATH to MATH over the first 5000 updates. use a similar schedule based on the sigmoid function.

The relaxation temperature MATH is annealed from MATH to MATH over the first 150000 updates. Using a linear annealing schedule for this typically led to divergence.

The step size is annealed from MATH to MATH over 1200000 updates.

The decay schedules for the relaxation temperature and the step size are especially important for stability and successful optimization.

We update the parameters using AdamW with MATH , MATH , MATH , and weight decay multiplier MATH . We use exponentially weighted iterate averaging for the parameters with decay coefficient MATH . The reconstruction term in the ELB is a joint distribution over the MATH values for the image pixels, and the KL term is a joint distribution over the MATH positions in the spatial grid output by the encoder. We divide the overall loss by MATH , so that the weight of the KL term becomes MATH , where MATH is the KL weight. The model is trained in mixed-precision using standard (i.e., global) loss scaling on MATH 16 GB NVIDIA V100 GPUs, with a per-GPU batch size of MATH , resulting in a total batch size of 512. It is trained for a total of 3000000 updates.

@src https://arxiv.org/abs/2102.12092
@title Zero-Shot Text-to-Image Generation
@section Architecture

Our model is a decoder-only sparse transformer of the same kind described in , with broadcasted row and column embeddings for the part of the context for the image tokens. A complete description of the embedding scheme used in our model is shown in Figure . We use 64 attention layers, each of which uses 62 attention heads with a per-head state size of 64.

The model uses three kinds of sparse attention masks, which we show in Figure . The convolutional attention mask (Figure (d)) is only used in the last self-attention layer. Otherwise, given the index MATH of a self-attention layer (with MATH ), we use the column attention mask (Figure (c)) if MATH , and row attention otherwise. E.g., the first four self-attention layers use "row, column, row, row", respectively. With the exception of the convolutional attention mask, which we found to provide a small boost in performance over the row and dense causal attention masks when used in the final self-attention layer, this is the same configuration used in .

@src https://arxiv.org/abs/2102.12092
@title Zero-Shot Text-to-Image Generation
@section Training

When training the transformer, we apply data augmentation to the images before encoding them using the dVAE encoder. We use slightly different augmentations from the ones used to train the dVAE; the code used for this is given in Listing . We also apply 10% BPE dropout when BPE-encoding the captions for training. The model is trained using per-resblock scaling (see Section ) and gradient compression (see Section ) with total compression rank 896 (so that each GPU uses a compression rank of 112 for its parameter shards). As shown in Table , this results in a compression rate of about 86%, which we analyze in Section .

We update the parameters using AdamW with MATH , MATH , MATH , and weight decay multiplier MATH . We clip the decompressed gradients by norm using a threshold of 4, prior to applying the Adam update. Gradient clipping is only triggered during the warm-up phase at the start of training. To conserve memory, most Adam moments (see Section for details) are stored in 16-bit formats, with a 1-6-9 format for the running mean (i.e., 1 bit for the sign, 6 bits for the exponent, and 9 bits for the significand), and a 0-6-10 format for the running variance. We clip the estimate for running variance by value to 5 before it is used to update the parameters or moments. Finally, we apply exponentially weighted iterate averaging by asynchronously copying the model parameters from the GPU to the CPU once every 25 updates, using a decay coefficient of 0.99.

We trained the model using 1024, 16 GB NVIDIA V100 GPUs and a total batch size of MATH , for a total of 430000 updates. At the start of training, we use a linear schedule to ramp up the step size to MATH over 5000 updates, and halved the step size each time the training loss appeared to plateau. We did this a total of five times, ending training with a final step size that was 32 times smaller than the initial one. We reserved about 606000 images for validation, and did not observe overfitting at any point during training.

@src https://arxiv.org/abs/2102.12092
@title Zero-Shot Text-to-Image Generation
@section Guidelines for Mixed-Precision Training

The most challenging part of this project was getting the model to train in 16-bit precision past one billion parameters. We were able to do this after detecting for underflow in various parts of training, and revising the code to eliminate it. We developed a set of guidelines as a result of this process that we present here. (Fewer of these guidelines may be necessary on hardware like the TPU that has native support for the bfloat16 format, since the larger 8-bit exponent range makes underflow less likely to occur.

Use per-resblock gradient scaling (Figure ) instead of standard loss scaling. Our model uses 128 gradient scales, one for each of its resblocks. All of the gradient scales are initialized to MATH , where MATH is the number of data-parallel replicas (i.e., the number of GPUs). In our setup, each grad scale is multiplied by MATH at every parameter update when there are no nonfinite values for any parameter gradient in that resblock. Otherwise, we divide the grad scale by MATH and skip the update. We also disallow consecutive divisions of the same grad scale within a window of MATH updates. All grad scales are clamped to the range MATH after being updated. Figure shows the gradient scales in the early phase of training for a 2.8-billion parameter model.

Only use 16-bit precision where it is really necessary for performance. In particular, store all gains, biases, embeddings, and unembeddings in 32-bit precision, with 32-bit gradients (including for remote communication) and 32-bit Adam moments. We disable gradient compression for these parameters (though PowerSGD would not make sense for 1D parameters like gains and biases). The logits for the text and image tokens are computed and stored in 32-bit precision. We found that storing the embeddings in 16-bit precision sometimes caused divergence early in optimization, and using 16-bit logits resulted in a small shift in the training curve, so we switched to use 32-bit precision out of an abundance of caution.

Avoid underflow when dividing the gradient. For data-parallel training, we need to divide the gradients by the total number of data-parallel workers MATH . One way to do this is to divide the loss by the per-machine batch size, and then divide the parameter gradients by MATH before summing them over the machines (using all-reduce). To save time and space, the gradients are usually computed and stored in 16-bit precision. When MATH is large, this division could result in underflow before the gradients are summed. On the other hand, if we attempt to sum the gradients first and then divide them later, we could encounter overflow in the all-reduce.

Our solution for this problem attempts to minimize the loss of information in the division prior to the all-reduce, without danger of overflow. To do this, we divide the loss by the overall batch size (which includes MATH as a factor) rather than the per-machine batch size, and multiply the gradient scales by MATH to compensate, as described in (1). Then, prior to the all-reduce operation, we divide the gradients by a constant that was tuned by hand to avoid both underflow and overflow. This was done by inspecting histograms of the exponents (i.e., base-2 logarithms) of the absolute values of the scalar components of the per-parameter gradients. Since the gradient scaling keeps the gradients close to right end of the exponent range of the 16-bit format, we found that the same constant worked well for all parameters in the model with 16-bit gradients. When using PowerSGD, we chose different constants for the MATH and MATH matrices.

@src https://arxiv.org/abs/2102.12092
@title Zero-Shot Text-to-Image Generation
@section Implementation Details

We describe the steps in our implementation of PowerSGD in detail, since these details were crucial in getting it to work efficiently and reliably at billion-parameter scale.

Our training setup uses a combination of parameter sharding and gradient compression, as described in Section . During backpropagation, while recomputing the activations and computing the gradients for the current resblock, we prefetch the parameters for the preceding resblock using all-gather. Once each GPU has computed the gradient with respect to a full parameter matrix, we compute the average of the slice of the gradient corresponding to the GPU's parameter shard, and discard the full gradient immediately to conserve memory. This average is taken over all of the GPUs on a machine using reduce-scatter.

If there are no nonfinite values in the result of the reduce-scatter (which could be caused by overflow in backpropagation or the reduce-scatter), we divide the result by the resblock's gradient scale, and add it to the error buffer (i.e., the buffer used for error correction). Otherwise, we do nothing and proceed with backpropagation; a single nonfinite value in the gradient means that the entire update will be skipped, which happens about 5% of the time. The error buffer uses the same 1-6-9 format used for the Adam mean, which we describe in Section ; the larger exponent range ensures that this division does not result in underflow. Adding the gradients directly to the error buffers avoids redundantly allocating another set of buffers of size equal to the parameter shard gradients.

Once the reduce-scatter operations for the resblock have finished, we schedule the operations to compute the MATH matrices from the errors buffers and the MATH matrices, whose values are fixed at the start of training (see Section ). Both the MATH and MATH matrices are stored in 1-6-9 format and have their values scaled by predetermined constants, as discussed in Section .

Once each GPU has computed the MATH matrices for the parameter shards in a resblock, they are averaged with the MATH matrices from the GPUs with the same ordinal on all other machines, using a single, grouped all-reduce operation. This all-reduce is carried out in the 1-6-9 format, using a custom kernel. The grouping results in better bandwidth utilization, since it avoids scheduling many all-reduce calls for smaller, individual parameters, each of which carries some overhead. We clamp any infinities in the results of the all-reduce to the maximum value of the 1-6-9 format (which is slightly less than 16), retaining the sign. With our choice of scaling factors for the MATH and MATH matrices, this clamping happens very rarely.

Once the all-reduce operation for the MATH matrices for a resblock have finished, we orthogonalize the columns of the resulting matrices. We use a custom Householder orthogonalization kernel rather than Gram-Schmidt, as we found the latter to be numerically unstable. We also add MATH to MATH in order to ensure that the result is not near rank-deficient, where MATH . Here, MATH is a rectangular matrix of the same size as the MATH matrix to which it is added; it contains the MATH identity matrix and has zeros elsewhere. The orthogonalizalied MATH matrices are stored in 1-6-9 format, but without scaling.

Once the MATH matrices for a resblock have been orthogonalized, we schedule the operations to compute the new MATH matrices from the error buffers and the MATH matrices.

Once the new MATH matrices for a resblock have been computed, we schedule another grouped all-reduce, similar to what we did for the MATH matrices. As in step (4), we clamp all infinities in the results of the all-reduce to the maximum value of the 1-6-9 format, retaining the sign. The error buffers for the resblock have now been decomposed into low-rank factors MATH and MATH .

The gradients for all parameters that are not compressed are grouped together into a single, 32-bit precision all-reduce. Section explains why we use 32-bit precision for these parameters and their gradients.

Once all GPUs on a machine have finished steps (7) and (8) for every resblock in the model, the values of the MATH and MATH matrices for the same parameter shard on all machines will be identical. We then compute the global gradient norm, which is the sum of two quantities: (a) the sum of the squared Frobenius norms of the MATH matrices over all of the parameter shards on a machine, and (b) the sum of the squared norms of the gradients for the parameter shards that do not use compression, taken over all such parameter shards on a machine. We need to compute this value for gradient clipping (see Section ).

While computing the global norm, we also synchronize the information from step (2) about which parameter shard gradients contained nonfinite values after the reduce-scatter. After doing this, we have two pieces of information for each parameter shard: (a) whether its error buffer from step (2) contains nonfinite values on the current GPU, and (b) whether MATH or MATH contains nonfinite values. We cannot rely on the values of the MATH and MATH matrices to determine (b), since we clamp infinities as described in step (4). If we find that the gradient with respect to any parameter shard on the machine contains nonfinite values, then we set the global norm to infinity.

Once all of the all-reduces have finished and the global norm has been computed, we can apply the parameter updates. Like backpropagation, the parameter updates proceed resblock-by-resblock. The first step is to compute the decompressed gradients by forming the product MATH for all parameters in a given resblock. To avoid overflow, these products are computed in 32-bit precision. We can then apply the Adam update to the parameters using the decompressed gradients and the global norm computed in step (9). If the global norm is not finite, then the update to the parameters and Adam moments is skipped. We note that the decompressed gradient must be divided by the scale of the MATH matrix (the MATH matrix is stored without scaling after orthogonalization).

The second step is the update to the error buffers. First, we use the results from step (10) to check if the MATH and MATH matrices for a given parameter shard contain only finite values. If this is the case, then we divide the decompressed gradient by the total number of machines, and subtract it from the current value for the error buffer. This sets the error buffer to the difference between the "local" gradient averaged over the GPUs on the machine using reduce-scatter, and the "remote" decompressed gradient (i.e., the "error"). If either MATH or MATH contains nonfinite values, then we check if the error buffer computed in step (2) contains only finite values. If it does, then we preserve its value and do nothing. If it does not, then we set it to zero. The purpose of this tedious logic is to set an error buffer to zero only when we must do so, because it has been contaminated with nonfinite values. We found that error buffers getting set to zero too frequently by gradient scaling events leads to performance regressions.

The parameter shards whose gradients are not compressed are updated separately.

We also note the following important optimizations:

There are several opportunities for overlap between compute and communication in the above steps. For example, while we are running step (2) for resblock MATH , we can proceed to steps (3)–(8) for all resblocks MATH . Exploiting opportunities for overlap is necessary to achieve good performance.

We throttle specific operations that are liable to exhaust all available memory. For example, we only prefetch the parameters from the preceding resblock when the reduce-scatter operations have finished for the current one. Otherwise, we risk running out of memory by holding on to the full parameters. We also throttle the Adam updates, so that we do not decompress all of the gradients at once.

There are two places in the implementation where the transposition matters: (a) the choice of shard axis for the MLP matrices and (b) whether we compute the low-rank factorization for a gradient or its transpose. The former influences the bandwidth analysis, which we present in Section . The latter influences the cost of the orthogonalization. Suppose that the gradient MATH is MATH and its low-rank factors MATH and MATH are MATH and MATH , respectively, with MATH . To make orthogonalization cheaper, we transpose MATH appropriately so that MATH .

At first glance, it may seem like a limitation that the NCCL all-gather and reduce-scatter primitives shard along axis 0 only. We may need to transpose some matrices before and after communication operations because of (a) and (b), which would require additional time and potentially special care to avoid out-of-memory errors. In fact, we never actually needed to do this. This is because we stored some of the parameters in their transposed formats and exploited the transpose_a and transpose_b parameters of the matrix multiplication kernels used in forward propagation, backpropagation, and steps (1)–(13) above. This allowed us to avoid explicit transposition while retaining the freedom to choose how to handle (a) and (b).

In step (12) above, we note that setting the error buffers to zero too often can cause performance regressions. We wanted to avoid doing this when resuming training from a checkpoint, which happens more frequently for larger jobs as it is likely that a machine will periodically fail. Naively, this would require uploading the error buffers from all of the machines along with the model checkpoints. Since we use a total of 128 machines for training, this would lead to 128 times greater storage usage, which is extremely wasteful.

Fortunately, this is unnecessary, as error correction depends only on the sum of the error buffers. This property follows from linearity and the sequence of operations used by PowerSGD. Hence, it suffices to store the sums of the errors buffers taken across all GPUs with the same ordinal. When resuming from a checkpoint, we can divide the error buffers by the total number of machines and broadcast them.

@src https://arxiv.org/abs/2103.00020
@title Learning Transferable Visual Models From Natural Language Supervision
@section Selecting an Efficient Pre-Training Method

State-of-the-art computer vision systems use very large amounts of compute. required 19 GPU years to train their ResNeXt101-32x48d and required 33 TPUv3 core-years to train their Noisy Student EfficientNet-L2. When considering that both these systems were trained to predict only 1000 ImageNet classes, the task of learning an open set of visual concepts from natural language seems daunting. In the course of our efforts, we found training efficiency was key to successfully scaling natural language supervision and we selected our final pre-training method based on this metric.

Our initial approach, similar to VirTex, jointly trained an image CNN and text transformer from scratch to predict the caption of an image. However, we encountered difficulties efficiently scaling this method. In Figure we show that a 63 million parameter transformer language model, which already uses twice the compute of its ResNet-50 image encoder, learns to recognize ImageNet classes three times slower than a much simpler baseline that predicts a bag-of-words encoding of the same text.

Both these approaches share a key similarity. They try to predict the exact words of the text accompanying each image. This is a difficult task due to the wide variety of descriptions, comments, and related text that co-occur with images. Recent work in contrastive representation learning for images has found that contrastive objectives can learn better representations than their equivalent predictive objective . Other work has found that although generative models of images can learn high quality image representations, they require over an order of magnitude more compute than contrastive models with the same performance . Noting these findings, we explored training a system to solve the potentially easier proxy task of predicting only which text as a whole is paired with which image and not the exact words of that text. Starting with the same bag-of-words encoding baseline, we swapped the predictive objective for a contrastive objective in Figure and observed a further 4x efficiency improvement in the rate of zero-shot transfer to ImageNet.

Given a batch of MATH (image, text) pairs, CLIP is trained to predict which of the MATH possible (image, text) pairings across a batch actually occurred. To do this, CLIP learns a multi-modal embedding space by jointly training an image encoder and text encoder to maximize the cosine similarity of the image and text embeddings of the MATH real pairs in the batch while minimizing the cosine similarity of the embeddings of the MATH incorrect pairings. We optimize a symmetric cross entropy loss over these similarity scores. In Figure we include pseudocode of the core of an implementation of CLIP. To our knowledge this batch construction technique and objective was first introduced in the area of deep metric learning as the multi-class N-pair loss , was popularized for contrastive representation learning by as the InfoNCE loss, and was recently adapted for contrastive (text, image) representation learning in the domain of medical imaging by .

Due to the large size of our pre-training dataset, over-fitting is not a major concern and the details of training CLIP are simplified compared to the implementation of . We train CLIP from scratch without initializing the image encoder with ImageNet weights or the text encoder with pre-trained weights. We do not use the non-linear projection between the representation and the contrastive embedding space, a change which was introduced by and popularized by . We instead use only a linear projection to map from each encoder's representation to the multi-modal embedding space. We did not notice a difference in training efficiency between the two versions and speculate that non-linear projections may be co-adapted with details of current image only in self-supervised representation learning methods. We also remove the text transformation function MATH from which samples a single sentence at uniform from the text since many of the (image, text) pairs in CLIP's pre-training dataset are only a single sentence. We also simplify the image transformation function MATH . A random square crop from resized images is the only data augmentation used during training. Finally, the temperature parameter which controls the range of the logits in the softmax, MATH , is directly optimized during training as a log-parameterized multiplicative scalar to avoid turning as a hyper-parameter.

@src https://arxiv.org/abs/2103.00020
@title Learning Transferable Visual Models From Natural Language Supervision
@section Training

We train a series of 5 ResNets and 3 Vision Transformers. For the ResNets we train a ResNet-50, a ResNet-101, and then 3 more which follow EfficientNet-style model scaling and use approximately 4x, 16x, and 64x the compute of a ResNet-50. They are denoted as RN50x4, RN50x16, and RN50x64 respectively. For the Vision Transformers we train a ViT-B/32, a ViT-B/16, and a ViT-L/14. We train all models for 32 epochs. We use the Adam optimizer with decoupled weight decay regularization applied to all weights that are not gains or biases, and decay the learning rate using a cosine schedule . Initial hyper-parameters were set using a combination of grid searches, random search, and manual tuning on the baseline ResNet-50 model when trained for 1 epoch. Hyper-parameters were then adapted heuristically for larger models due to computational constraints. The learnable temperature parameter MATH was initialized to the equivalent of 0.07 from and clipped to prevent scaling the logits by more than 100 which we found necessary to prevent training instability. We use a very large minibatch size of 32,768. Mixed-precision was used to accelerate training and save memory. To save additional memory, gradient checkpointing , half-precision Adam statistics , and half-precision stochastically rounded text encoder weights were used. The calculation of embedding similarities was also sharded with individual GPUs computing only the subset of the pairwise similarities necessary for their local batch of embeddings. The largest ResNet model, RN50x64, took 18 days to train on 592 V100 GPUs while the largest Vision Transformer took 12 days on 256 V100 GPUs. For the ViT-L/14 we also pre-train at a higher 336 pixel resolution for one additional epoch to boost performance similar to FixRes . We denote this model as ViT-L/14@336px. Unless otherwise specified, all results reported in this paper as "CLIP" use this model which we found to perform best.

@src https://arxiv.org/abs/2103.14030
@title Swin Transformer: Hierarchical Vision Transformer using Shifted Windows
@section Overall Architecture

An overview of the Swin Transformer architecture is presented in Figure , which illustrates the tiny version (Swin-T). It first

splits an input RGB image into non-overlapping patches by a patch splitting module, like ViT. Each patch is treated as a "token" and its feature is set as a concatenation of the raw pixel RGB values. In our implementation, we use a patch size of MATH and thus the feature dimension of each patch is MATH . A linear embedding layer is applied on this raw-valued feature to project it to an arbitrary dimension (denoted as MATH ).

Several Transformer blocks with modified self-attention computation ( Swin Transformer blocks ) are applied on these patch tokens. The Transformer blocks maintain the number of tokens ( MATH ), and together with the linear embedding are referred to as "Stage 1".

To produce a hierarchical representation, the number of tokens is reduced by patch merging layers as the network gets deeper. The first patch merging layer concatenates the features of each group of MATH neighboring patches, and applies a linear layer on the MATH -dimensional concatenated features. This reduces the number of tokens by a multiple of MATH ( MATH downsampling of resolution), and the output dimension is set to MATH . Swin Transformer blocks are applied afterwards for feature transformation, with the resolution kept at MATH . This first block of patch merging and feature transformation is denoted as "Stage 2". The procedure is repeated twice, as "Stage 3" and "Stage 4", with output resolutions of MATH and MATH , respectively. These stages jointly produce a hierarchical representation, with the same feature map resolutions as those of typical convolutional networks, e.g., VGG and ResNet . As a result, the proposed architecture can conveniently replace the backbone networks in existing methods for various vision tasks.

Swin Transformer block Swin Transformer is built by replacing the standard multi-head self attention (MSA) module in a Transformer block by a module based on shifted windows (described in Section ), with other layers kept the same. As illustrated in Figure (b), a Swin Transformer block consists of a shifted window based MSA module, followed by a 2-layer MLP with GELU non-linearity in between. A LayerNorm (LN) layer is applied before each MSA module and each MLP, and a residual connection is applied after each module.

@src https://arxiv.org/abs/2103.14030
@title Swin Transformer: Hierarchical Vision Transformer using Shifted Windows
@section Architecture Variants

We build our base model, called Swin-B, to have of model size and computation complexity similar to ViT-B/DeiT-B. We also introduce Swin-T, Swin-S and Swin-L, which are versions of about MATH , MATH and MATH the model size and computational complexity, respectively. Note that the complexity of Swin-T and Swin-S are similar to those of ResNet-50 (DeiT-S) and ResNet-101, respectively. The window size is set to MATH by default. The query dimension of each head is MATH , and the expansion layer of each MLP is MATH , for all experiments. The architecture hyper-parameters of these model variants are:

where MATH is the channel number of the hidden layers in the first stage. The model size, theoretical computational complexity (FLOPs), and throughput of the model variants for ImageNet image classification are listed in Table .

@src https://arxiv.org/abs/2103.14030
@title Swin Transformer: Hierarchical Vision Transformer using Shifted Windows
@section Detailed Architectures

The detailed architecture specifications are shown in Table , where an input image size of 224 MATH 224 is assumed for all architectures.

"Concat MATH " indicates a concatenation of MATH neighboring features in a patch. This operation results in a downsampling of the feature map by a rate of MATH . "96-d" denotes a linear layer with an output dimension of 96. "win. sz. MATH " indicates a multi-head self-attention module with window size of MATH .

@src https://arxiv.org/abs/2105.05233
@title Diffusion Models Beat GANs on Image Synthesis
@section Architecture Improvements

In this section we conduct several architecture ablations to find the model architecture that provides the best sample quality for diffusion models.

ddpm introduced the UNet architecture for diffusion models, which adversarial found to substantially improve sample quality over the previous architectures improvedscore,refinenet used for denoising score matching. The UNet model uses a stack of residual layers and downsampling convolutions, followed by a stack of residual layers with upsampling colvolutions, with skip connections connecting the layers with the same spatial size. In addition, they use a global attention layer at the 16 MATH 16 resolution with a single head, and add a projection of the timestep embedding into each residual block. sde found that further changes to the UNet architecture improved performance on the CIFAR-10 cifar10 and CelebA-64 celeba datasets. We show the same result on ImageNet 128 MATH 128, finding that architecture can indeed give a substantial boost to sample quality on much larger and more diverse datasets at a higher resolution.

We explore the following architectural changes:

Increasing depth versus width, holding model size relatively constant.

Increasing the number of attention heads.

Using attention at 32 MATH 32, 16 MATH 16, and 8 MATH 8 resolutions rather than only at 16 MATH 16.

Using the BigGAN biggan residual block for upsampling and downsampling the activations, following sde .

Rescaling residual connections with MATH , following sde,stylegan,stylegan2 .

For all comparisons in this section, we train models on ImageNet 128 MATH 128 with batch size 256, and sample using 250 sampling steps. We train models with the above architecture changes and compare them on FID, evaluated at two different points of training, in Table . Aside from rescaling residual connections, all of the other modifications improve performance and have a positive compounding effect. We observe in Figure that while increased depth helps performance, it increases training time and takes longer to reach the same performance as a wider model, so we opt not to use this change in further experiments.

We also study other attention configurations that better match the Transformer architecture transformer . To this end, we experimented with either fixing attention heads to a constant, or fixing the number of channels per head. For the rest of the architecture, we use 128 base channels, 2 residual blocks per resolution, multi-resolution attention, and BigGAN up/downsampling, and we train the models for 700K iterations. Table shows our results, indicating that more heads or fewer channels per head improves FID. In Figure , we see 64 channels is best for wall-clock time, so we opt to use 64 channels per head as our default. We note that this choice also better matches modern transformer architectures, and is on par with our other configurations in terms of final FID.

@src https://arxiv.org/abs/2112.10741
@title GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models
@section Training Hyperparameters

Our noised CLIP models process MATH images using a ViT with patch size MATH . We trained our CLIP models for 390K iterations with batch size 32K on a 50%-50% mixture of the datasets used by and . For our final CLIP model, we trained a ViT-L with weight decay 0.0125. After training, we fine-tuned the final ViT-L for 30K iterations on an even broader dataset of internet images.

We pre-trained (filtered) for 1.1M iterations before fine-tuning for another 500K iterations for classifier-free guidance and inpainting. Additionally, we trained a small filtered upsampler model with 192 base channels and 512 text encoder channels for 400K iterations.

@src https://arxiv.org/abs/2112.10752
@title High-Resolution Image Synthesis with Latent Diffusion Models
@section Method

To lower the computational demands of training diffusion models towards high-resolution image synthesis,

to ignore perceptually irrelevant details by undersampling the corresponding loss terms ,

they still require costly function evaluations in pixel space,

huge demands in computation time and energy resources.

We propose to circumvent this drawback by introducing an explicit separation

of the compressive from the generative learning phase (see

To achieve this, we utilize an autoencoding model which learns a space that is perceptually equivalent to the image space,

but offers significantly reduced computational complexity.

Such an approach offers several advantages: (i)

By leaving the high-dimensional image space, we

obtain DMs which are computationally much more efficient

because sampling is performed on a low-dimensional space.

We exploit the inductive bias of DMs inherited from their UNet architecture

, which makes them particularly effective for data with spatial

alleviates the need for aggressive, quality-reducing compression levels as required by previous

Finally, we obtain general-purpose compression models whose latent space

can be used to train multiple generative models

for other downstream applications such as single-image CLIP-guided synthesis .

@src https://arxiv.org/abs/2112.10752
@title High-Resolution Image Synthesis with Latent Diffusion Models
@section Implementations of MATH for conditional LDMs

For the experiments on text-to-image and layout-to-image (Sec. ) synthesis,

we implement the conditioner MATH as an unmasked transformer which processes

a tokenized version of the input MATH and produces an output MATH ,

More specifically, the transformer is implemented from MATH transformer blocks consisting of

global self-attention layers, layer-normalization and

position-wise MLPs as follows (adapted from https://github.com/lucidrains/x-transformers :

With MATH available, the conditioning is mapped into the UNet via the cross-attention mechanism

as depicted in Fig. . We modify the "ablated UNet" architecture

and replace the self-attention layer with a shallow (unmasked) transformer consisting

of MATH blocks with alternating layers of (i) self-attention, (ii) a position-wise MLP and

(iii) a cross-attention layer; see Tab. . Note that without (ii) and (iii), this

architecture is equivalent to the "ablated UNet".

While it would be possible to increase the representational power of MATH

by additionally conditioning on the time step MATH , we do not pursue this choice as it reduces the speed of inference.

We leave a more detailed analysis of this modification to future work.

For the text-to-image model, we rely on a publicly available (https://huggingface.co/transformers/model_doc/bert.html#berttokenizerfast tokenizer

The layout-to-image model discretizes the spatial locations of the bounding boxes

and encodes each box as a MATH -tuple, where MATH denotes the (discrete) top-left and MATH the

bottom-right position. Class information is contained in MATH .

See Tab. for the hyperparameters of MATH and Tab. for those of the UNet for both of the above tasks.

Note that the class-conditional model as described in Sec.

is also implemented via cross-attention, where MATH is a single learnable

embedding layer with a dimensionality of 512, mapping classes MATH to

@src https://arxiv.org/abs/2201.03545
@title A ConvNet for the 2020s
@section Training Techniques

Apart from the design of the network architecture, the training procedure also affects the ultimate performance.

Not only did vision Transformers bring a new set of modules and architectural design decisions, but they also introduced different training techniques ( AdamW optimizer) to vision.

This pertains mostly to the optimization strategy and associated hyper-parameter settings.

Thus, the first step of our exploration is to train a baseline model with the vision Transformer training procedure, in this case, ResNet-50/200.

Recent studies demonstrate that a set of modern training techniques can significantly enhance the performance of a simple ResNet-50 model. In our study, we use a training recipe that is close to DeiT's and Swin Transformer's . The training is extended to 300 epochs from the original 90 epochs for ResNets. We use the AdamW optimizer , data augmentation techniques such as Mixup , Cutmix , RandAugment , Random Erasing , and regularization schemes including Stochastic Depth and Label Smoothing . The complete set of hyper-parameters we use can be found in Appendix . By itself, this enhanced training recipe increased the performance of the ResNet-50 model from 76.1% to 78.8% (+2.7%), implying that a significant portion of the performance difference between traditional ConvNets and vision Transformers may be due to the training techniques. We will use this fixed training recipe with the same hyperparameters throughout the "modernization" process. Each reported accuracy on the ResNet-50 regime is an average obtained from training with three different random seeds.

@src https://arxiv.org/abs/2201.03545
@title A ConvNet for the 2020s
@section ImageNet (Pre-)training

We provide s ' ImageNet-1K training and ImageNet-22K pre-training settings in Table . The settings are used for our main results in Table (Section ). All variants use the same setting, except the stochastic depth rate is customized for model variants.

For experiments in "modernizing a ConvNet" (Section ), we also use Table 's setting for ImageNet-1K, except EMA is disabled, as we find using EMA severely hurts models with BatchNorm layers.

For isotropic s (Section ), the setting for ImageNet-1K in Table is also adopted, but warmup is extended to 50 epochs, and layer scale is disabled for isotropic -S/B. The stochastic depth rates are 0.1/0.2/0.5 for isotropic -S/B/L.

@src https://arxiv.org/abs/2201.12086
@title BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation
@section Vision-language Pre-training

Vision-language pre-training (VLP) aims to improve performance of downstream vision and language tasks

by pre-training the model on large-scale image-text pairs.

Due to the prohibitive expense of acquiring human-annotated texts,

most methods use image and alt-text pairs crawled from the web ,

Despite the use of simple rule-based filters,

noise is still prevalent in the web texts.

However, the negative impact of the noise has been largely overlooked, shadowed by the performance gain

Our paper shows that the noisy web texts are suboptimal for vision-language learning,

and proposes CapFilt that utilizes web datasets in a more effective way.

There have been many attempts to unify various vision and language tasks into a single framework .

The biggest challenge is to design model architectures that can perform both understanding-based tasks ( image-text retrieval) and generation-based tasks ( image captioning).

Neither encoder-based models nor encoder-decoder models can excel at both types of tasks,

whereas a single unified encoder-decoder also limits the model's capability.

Our proposed multimodal mixture of encoder-decoder model offers more flexibility and better performance on a wide range of downstream tasks,

in the meantime keeping the pre-training simple and efficient.

@src https://arxiv.org/abs/2201.12086
@title BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation
@section Model Architecture

We employ a visual transformer as our image encoder,

which divides an input image into patches and encodes them as a sequence of embeddings, with an additional [CLS] token to represent the global image feature.

Compared to using pre-trained object detectors for visual feature extraction ,

using a ViT is more computation-friendly and has been adopted by the more recent methods .

In order to pre-train a unified model with both understanding and generation capabilities,

we propose multimodal mixture of encoder-decoder (MED),

a multi-task model which can operate in one of the three functionalities:

(1) Unimodal encoder, which separately encodes image and text. The text encoder is the same as BERT , where a [CLS] token is appended to the beginning of the text input to summarize the sentence.

(2) Image-grounded text encoder, which injects visual information by inserting one additional cross-attention (CA) layer between the self-attention (SA) layer and the feed forward network (FFN) for each transformer block of the text encoder. A task-specific [Encode] token is appended to the text, and the output embedding of [Encode] is used as the multimodal representation of the image-text pair.

(3) Image-grounded text decoder, which replaces the bi-directional self-attention layers in the image-grounded text encoder with causal self-attention layers. A [Decode] token is used to signal the beginning of a sequence, and an end-of-sequence token is used to signal its end.

@src https://arxiv.org/abs/2201.12086
@title BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation
@section Pre-training Objectives

We jointly optimize three objectives during pre-training,

with two understanding-based objectives and one generation-based objective.

Each image-text pair only requires one forward pass through the computational-heavier visual transformer,

and three forward passes through the text transformer,

where different functionalities are activated to compute the three losses as delineated below.

-Text Contrastive Loss (ITC) activates the unimodal encoder. It aims to align the feature space of the visual transformer and the text transformer by encouraging positive image-text pairs to have similar representations in contrast to the negative pairs.

It has been shown to be an effective objective for improving vision and language understanding .

where a momentum encoder is introduced to produce features,

and soft labels are created from the momentum encoder as training targets to account for the potential positives in the negative pairs.

-Text Matching Loss (ITM) activates the image-grounded text encoder.

It aims to learn image-text multimodal representation that captures the fine-grained alignment between vision and language.

where the model uses an ITM head (a linear layer) to predict whether an image-text pair is positive (matched) or negative (unmatched) given their multimodal feature.

In order to find more informative negatives,

we adopt the hard negative mining strategy by ,

where negatives pairs with higher contrastive similarity in a batch are more likely to be selected to compute the loss.

Modeling Loss (LM) activates the image-grounded text decoder,

which aims to generate textual descriptions given an image.

It optimizes a cross entropy loss which trains the model to maximize the likelihood of the text in an autoregressive manner.

We apply a label smoothing of 0.1 when computing the loss.

Compared to the MLM loss that has been widely-used for VLP,

LM enables the model with the generalization capability to convert visual information into coherent captions.

In order to perform efficient pre-training while leveraging multi-task learning,

the text encoder and text decoder share all parameters except for the SA layers.

The reason is that the differences between the encoding and decoding tasks are best captured by the SA layers. In particular, the encoder employs bi-directional self-attention to build representations for the current input tokens, while the decoder employs causal self-attention to predict next tokens.

On the other hand, the embedding layers, CA layers and FFN function similarly between encoding and decoding tasks,

therefore sharing these layers can improve training efficiency while benefiting from multi-task learning,

@src https://arxiv.org/abs/2201.12086
@title BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation
@section Pre-training Details

Our models are implemented in PyTorch and pre-trained on two 16-GPU nodes.

The image transformer is initialized from ViT pre-trained on ImageNet ,

and the text transformer is initialized from BERT MATH .

We explore two variants of ViTs: ViT-B/16 and ViT-L/16.

Unless otherwise specified, all results reported in this paper as " " uses ViT-B.

We pre-train the model for 20 epochs using a batch size of 2880 (ViT-B) / 2400 (ViT-L).

We use AdamW optimizer with a weight decay of 0.05.

The learning rate is warmed-up to MATH -4 (ViT-B) / MATH -4 (ViT-L) and decayed linearly with a rate of 0.85.

We take random image crops of resolution MATH during pre-training, and increase the image resolution to MATH during finetuning.

We use the same pre-training dataset as with 14M images in total,

including two human-annotated datasets (COCO and Visual Genome ),

and three web datasets (Conceptual Captions , Conceptual 12M , SBU captions ).

We also experimented with an additional web dataset, LAION , which contains 115M images with more noisy texts (We only download images whose shorter edge is larger than 256 pixels from the original LAION400M. Due to the large size of LAION, we only use MATH of it each epoch during pre-training. .

More details about the datasets can be found in the appendix.

@src https://arxiv.org/abs/2203.02155
@title Training language models to follow instructions with human feedback
@section High-level methodology

Our methodology follows that of and , who applied it in the stylistic continuation and summarization domains. We start with a pretrained language model , a distribution of prompts on which we want our model to produce aligned outputs, and a team of trained human labelers (see Sections for details). We then apply the following three steps (Figure ).

Step 1: Collect demonstration data, and train a supervised policy. Our labelers provide demonstrations of the desired behavior on the input prompt distribution (see Section for details on this distribution). We then fine-tune a pretrained GPT-3 model on this data using supervised learning.

Step 2: Collect comparison data, and train a reward model. We collect a dataset of comparisons between model outputs, where labelers indicate which output they prefer for a given input. We then train a reward model to predict the human-preferred output.

Step 3: Optimize a policy against the reward model using PPO. We use the output of the RM as a scalar reward. We fine-tune the supervised policy to optimize this reward using the PPO algorithm .

Steps 2 and 3 can be iterated continuously; more comparison data is collected on the current best policy, which is used to train a new RM and then a new policy. In practice, most of our comparison data comes from our supervised policies, with some coming from our PPO policies.

@src https://arxiv.org/abs/2203.02155
@title Training language models to follow instructions with human feedback
@section Implications for alignment research

This research is part of our broader research program to align AI systems with human intentions . Even though this work focuses on our current language model systems, we seek general and scalable methods that work for future AI systems . The systems we work with here are still fairly limited, but they are among the largest language models today and we apply them on a wide range of language tasks, including classification, summarization, question-answering, creative writing, dialogue, and others.

Our approach to alignment research in this work is iterative: we are improving the alignment of current AI systems instead of focusing abstractly on aligning AI systems that don't yet exist. A disadvantage of this approach is that we are not directly facing alignment problems that occur only when aligning superhuman systems . However, our approach does provides us with a clear empirical feedback loop of what works and what does not. We believe that this feedback loop is essential to refine our alignment techniques, and it forces us to keep pace with progress in machine learning. Moreover, the alignment technique we use here, RLHF, is an important building block in several proposals to align superhuman systems . For example, RLHF was a central method in recent work on summarizing books, a task that exhibits some of the difficulties of aligning superhuman AI systems as it is difficult for humans to evaluate directly .

From this work, we can draw lessons for alignment research more generally:

The cost of increasing model alignment is modest relative to pretraining. The cost of collecting our data and the compute for training runs, including experimental runs is a fraction of what was spent to train GPT-3: training our 175B SFT model requires 4.9 petaflops/s-days and training our 175B PPO-ptx model requires 60 petaflops/s-days, compared to 3,640 petaflops/s-days for GPT-3 . At the same time, our results show that RLHF is very effective at making language models more helpful to users, more so than a 100x model size increase. This suggests that right now increasing investments in alignment of existing language models is more cost-effective than training larger models—at least for our customers' natural language task distribution.

We've seen some evidence that InstructGPT generalizes 'following instructions' to settings that we don't supervise it in, for example on non-English language tasks and code-related tasks. This is an important property because it's prohibitively expensive to have humans supervise models on every task they perform. More research is needed to study how well this generalization scales with increased capabilities; see for recent research in this direction.

We were able to mitigate most of the performance degradations introduced by our fine-tuning. If this was not the case, these performance degradations would constitute an alignment tax—an additional cost for aligning the model. Any technique with a high tax might not see adoption. To avoid incentives for future highly capable AI systems to remain unaligned with human intent, there is a need for alignment techniques that have low alignment tax. To this end, our results are good news for RLHF as a low-tax alignment technique.

We've validated alignment techniques from research in the real world. Alignment research has historically been rather abstract, focusing on either theoretical results , small synthetic domains , or training ML models on public NLP datasets . Our work provides grounding for alignment research in AI systems that are being used in production in the real world with customers. (Note that while fine-tuning models using human data is common practice when deploying ML systems, the purpose of these efforts is to obtain a model that performs well on a company's specific use case, rather than advancing the alignment of general-purpose ML models. This enables an important feedback loop on the techniques' effectiveness and limitations.

@src https://arxiv.org/abs/2203.02155
@title Training language models to follow instructions with human feedback
@section Details of SFT training

We train our SFT models for 16 epochs with residual dropout of 0.2. We use a cosine LR schedule down to 10% of the original learning rate, with no learning rate warmup. For our 1.3B and 6B models, we use an LR of 9.65e-6 and a batch size of 32. For 175B, we use a LR of 5.03e-6 and a batch size of 8. To select learning rates, we did a geometric search over 7 LRs for 1.3B and 6B, and 5 LRs for 175B. We also tuned the number of epochs using geometric search. Our final models were selected based on the RM score, which we've found to be more predictive of human preference results compared to validation loss.

@src https://arxiv.org/abs/2203.02155
@title Training language models to follow instructions with human feedback
@section Details of RM training

We trained a single 6B reward model which we used for all PPO models of all sizes. Larger 175B RMs had the potential to achieve lower validation loss, but (1) their training was more unstable which made them less suitable for use as initializations for the PPO value functions, and (2) using a 175B RM and value function greatly increase the compute requirements of PPO. In preliminary experiments, we found that 6B RMs were stable across a wide range of learning rates, and led to equally strong PPO models.

The final reward model was initialized from a 6B GPT-3 model that was fine-tuned on a variety of public NLP datasets (ARC, BoolQ, CoQA, DROP, MultiNLI, OpenBookQA, QuAC, RACE, and Winogrande). This was mostly for historical reasons; we find similar results when initializing the RM from the GPT-3 or SFT models. We trained for a single epoch over the full reward model training set (see Table ) at a learning rate of lr = 9e-6, a cosine learning rate schedule (dropping to 10% of its initial value by the end of training), and a batch size of 64. Training did not appear to be very sensitive to the learning rate or schedule; changes of up to 50% in the learning rate resulted in similar performance. Training was quite sensitive to the number of epochs: multiple epochs quickly overfit the model to the training data with obvious deterioration in the validation loss. The batch size here represents the distinct number of prompts per batch. Each prompt had between MATH and MATH labeled completions, from which there were up to MATH possible comparisons. Ties were dropped. Therefore, a single batch could contain up to MATH 2,304 comparisons.

@src https://arxiv.org/abs/2203.02155
@title Training language models to follow instructions with human feedback
@section Details of RLHF training

We then initialize the RL policies from the above supervised fine-tuned models with pretraining mix. These models are also used to compute the KL reward, in the same way as , with MATH (see Equation ). We train all the RL models for 256k episodes. These episodes include about 31k unique prompts, after filtering out prompts with PII and deduplication based on common prefixes.

The batch size for each iteration is 512, with a minibatch size of 64. In other words, each batch is randomly split into 8 minibatches and is trained on for only a single inner epoch . A constant learning rate is applied with a warmup over the first 10 iterations, starting with one tenth of the peak learning rate. Exponential moving averages of the weights are applied, with a decay rate of 0.992. No discount is applied when estimating the generalized advantage . The PPO clip ratio is set to 0.2, and the sampling temperature is 1 for rollouts.

As previously mentioned, for all PPO models we use a 6B RM and a 6B value function, and the latter is initialized from the former.

By using the same 6B reward model and value function on policies of all model sizes, it's easier to compare the effect of policy model size on policy performance. A fixed learning rate of 9e-6 for the value function is used for 1.3B and the 6B policies and 5e-6 for the 175B policy.

Our initial RLHF experiments showed regressions on public NLP datasets, such as SQuADv2 and DROP, and we mitigate the regressions by mixing in pretraining gradients during PPO training. We use 8 times more pretraining examples than the number of the RL training episodes. The pretraining data is randomly drawn from the dataset used to train the GPT-3 models. For each minibatch, we compute the PPO gradients and pretraining gradients in consecutive steps and accumulate them both into the gradient buffers. We multiply the pretraining gradients by a coefficient, MATH (see Equation ), to control the relative strength of gradients from PPO and pretraining distributions.

@src https://arxiv.org/abs/2203.11171
@title Self-Consistency Improves Chain of Thought Reasoning in Language Models
@section Compare to other existing approaches

We conduct a set of additional studies and show that self-consistency significantly outperforms existing methods including sample-and-rank, beam search, and ensemble-based approaches.

One commonly used approach to improve generation quality is sample-and-rank, where multiple sequences are sampled from the decoder and then ranked according to each sequence's log probability .

We compare self-consistency with sample-and-rank on GPT-3 code-davinci-001, by sampling the same number of sequences from the decoder as self-consistency and taking the final answer from the top-ranked sequence.

While sample-and-rank does improve the accuracy with additionally sampled sequences and ranking, the gain is much smaller compared to self-consistency.

In Table , we compare self-consistency with beam search decoding on the UL2-20B model. For a fair comparison we report the accuracy under the same number of beams and reasoning paths. On both tasks self-consistency outperforms beam search significantly.

Note self-consistency can also adopt beam search to decode each reasoning path (results are shown as "Self-consistency using beam search"), but its performance is worse compared to self-consistency with sampling.

The reason is that beam search yields a lower diversity in the outputs , while in self-consistency the diversity of the reasoning paths is the key to a better performance.

We further compare self-consistency to ensemble-based methods for few-shot learning.

In particular, we consider ensembling by:

(1) prompt order permutation: we randomly permute the exemplars in the prompt 40 times to mitigate model's sensitivity to prompt order ;

and (2) multiple sets of prompts : we manually write MATH different sets of prompts.

We took majority vote of the answers from greedy decoding in both approaches as an ensemble.

Table shows that compared to self-consistency, existing ensemble-based approaches achieve a much smaller gain. (Self-consistency is compatible with both ensemble approaches and we show the results in Appendix .

In addition, note that self-consistency is different from a typical model-ensemble approach, where multiple models are trained and their outputs are aggregated. Self-consistency acts more like a "self-ensemble" on top of a single language model. We additionally show the results of ensembling multiple models in Appendix where the model-ensembles perform much worse compared to self-consistency.

@src https://arxiv.org/abs/2204.14198
@title Flamingo: a Visual Language Model for Few-Shot Learning
@section Approach

This section describes Flamingo: a visual language model that accepts text interleaved with images/videos as input and outputs free-form text.

The key architectural components shown in Figure

are chosen to leverage pretrained vision and language models and bridge them effectively.

First, the Perceiver Resampler (Section ) receives spatio-temporal features from the Vision Encoder (obtained from either an image or a video) and outputs a fixed number of visual tokens.

Second, these visual tokens are used to condition the frozen LM using freshly initialised cross-attention layers (Section ) that are interleaved between the pretrained LM layers.

These new layers offer an expressive way for the LM to incorporate visual information for the next-token prediction task.

Flamingo models the likelihood of text MATH conditioned on interleaved images and videos MATH as follows:

where MATH is the MATH -th language token of the input text, MATH is the set of preceding tokens, MATH is the set of images/videos preceding token MATH in the interleaved sequence and MATH is parametrized by a model.

The ability to handle interleaved text and visual sequences (Section ) makes it natural to use models for in-context few-shot learning, analogously to GPT-3 with few-shot text prompting.

The model is trained on a diverse mixture of datasets as described in Section .

@src https://arxiv.org/abs/2204.14198
@title Flamingo: a Visual Language Model for Few-Shot Learning
@section Training on a mixture of vision and language datasets

We train the models on a mixture of three kinds of datasets, all scraped from the web: an interleaved image and text dataset derived from webpages, image-text pairs, and video-text pairs.

M3W: Interleaved image and text dataset.

The few-shot capabilities of Flamingo models rely on training on interleaved text and image data.

For this purpose, we collect the MultiModal MassiveWeb ( ) dataset.

We extract both text and images from the HTML of approximately 43 million webpages, determining the positions of images relative to the text based on the relative positions of the text and image elements in the Document Object Model (DOM).

An example is then constructed by inserting <image> tags in plain text at the locations of the images on the page, and inserting a special <EOC> (end of chunk) token (added to the vocabulary and learnt) prior to any image and at the end of the document.

From each document, we sample a random subsequence of MATH tokens and take up to the first MATH images included in the sampled sequence.

Further images are discarded in order to save compute.

More details are provided in Appendix app:datasets .

For our image and text pairs we first leverage the ALIGN dataset, composed of 1.8 billion images paired with alt-text.

To complement this dataset, we collect our own dataset of image and text pairs targeting better quality and longer descriptions: ( ) which consists of 312 million image and text pairs.

We also collect a similar dataset but with videos instead of still images: ( ) consists of 27 million short videos (approximately 22 seconds on average) paired with sentence descriptions.

We align the syntax of paired datasets with the syntax of M3W by prepending <image> and appending <EOC> to each training caption (see Appendix app:vtp_and_itp for details).

Multi-objective training and optimisation strategy.

We train our models by minimizing a weighted sum of per-dataset expected negative log-likelihoods of text, given the visual inputs:

where MATH and MATH are the MATH -th dataset and

Tuning the per-dataset weights MATH is key to performance.

We accumulate gradients over all datasets, which we found outperforms a "round-robin" approach .

We provide further training details and ablations in Appendix app:large_scale_training .

@src https://arxiv.org/abs/2204.14198
@title Flamingo: a Visual Language Model for Few-Shot Learning
@section Transformer architecture

We list in Table the number of layers ( MATH ), the hidden dimension ( MATH ), the number of heads ( MATH ), and the FFW activation (Act.) used for each transformer component of our models.

The dimension of keys and values in each configuration is given by MATH (96 for the Perceiver Resampler; 128 for gated xattn-dense and the frozen LM),

and the hidden dimension of each feed-forward MLP is MATH .

Note that the frozen LM was trained with the GeLU activation , while the remaining trainable transformer layers use the Squared ReLU activation , which we found to outperform GeLU.

@src https://arxiv.org/abs/2204.14198
@title Flamingo: a Visual Language Model for Few-Shot Learning
@section Training dataset details

We train the Flamingo models on a carefully chosen mixture of datasets illustrated in Figure and described next.

The selection and scraping of web pages for follows a similar process to the one used for collecting the MassiveWeb dataset . We start by filtering out non-English documents.

We also remove those that do not pass internal filters,

which identify explicit content across images, videos, and text. We use a custom scraper to extract salient content from the remaining documents, in the form of plain text interleaved with images, as described in Section sec:interleaved_datasets .

The text in is collected in a similar fashion to that of MassiveWeb,

but we also collect any images present at the same level in the HTML tree. We discard documents for which the scraping process does not yield any images.

We then apply similar text filtering heuristics, to remove low quality documents and reduce repetition, as well as some image filters to remove images that are too small (either width or height less than 64 pixels), too wide or narrow (aspect ratio greater than 3 in either direction), or unambiguously low quality (e.g. single-colour images). We discard documents that no longer contain any images following this filtering step.

During evaluation of , we prompt the model with an image and ask it to generate text for that image.

This lends itself to a natural sequencing at inference time in which the image comes before the corresponding text output.

However, the correspondence between images and text in our interleaved M3W dataset (Section sec:interleaved_datasets ) is in general unknown (and potentially not well-defined in certain cases).

As a motivating example, a simple webpage might be structured in either of the following ways:

This is my dog! <dog image> This is my cat! <cat image>

<dog image> That was my dog! <cat image> That was my cat!

The text-aligned image indices (indices) might "ideally" be chosen such that at each point in the text, the index points to the most semantically relevant image for that text – i.e., the next image in example (a), and the previous image in example (b).

In the absence of a general way to determine semantic correspondence between text and images on webpages "in the wild", we make a simplifying assumption that the most relevant image at any given point in the text is either the last image appearing before the text token, or the image immediately following it (as in the simple examples above), and choose indices accordingly.

During training, for each webpage sampled, we sample with probability MATH whether indices are chosen to map text to the previous or next image.

This inevitably means we make the semantically "unnatural" choice – e.g., associating the text "This is my cat!" with the dog image in (a) above – around half of the time.

We ablate this choice in Section sec:ablations , finding a small advantage to setting MATH over either MATH (always the previous image index) or MATH (always the next image index).

This suggests that there may be a beneficial "data augmentation" effect to this randomisation.

Along with our interleaved image and text dataset, we use several paired vision and text web datasets for training.

One dataset is ALIGN , composed of 1.8 billion images paired with alt-text.

ALIGN is large, but noisy and limited to images.

The images are often poorly described by the corresponding alt-text annotation.

For this reason, we augment it with two datasets: ( ) consists of 312 million images, and ( ) consists of 27 million short videos (approximately 22 seconds on average). Both datasets are paired with more descriptive captions.

For instance, the average number of tokens of an ALIGN text description is 12.4 per image, while it is 20.5 for the dataset.

The and datasets were collected by crawling fewer than ten websites targeting high-quality and rich image descriptions.

These single-image and single-video datasets are preprocessed analogously to the data preprocessing described previously, adding the <image> tag at the beginning of the sequence (immediately after <BOS>), and the <EOC> token after the text (before <EOS>).

We deduplicated these datasets against all our benchmarks (against both the training and the evaluation sets) using image similarity, as detailed in Appendix .

Datasheets for and are respectively given in Appendix and Appendix .

@src https://arxiv.org/abs/2204.14198
@title Flamingo: a Visual Language Model for Few-Shot Learning
@section Dataset mixing strategies for the contrastive pretraining

One key to achieving strong results was the inclusion of our new dataset alongside ALIGN for training. Despite being a smaller dataset ALIGN by a factor of 6, a contrastive model trained on only outperforms one trained only on ALIGN on our evaluation metrics, suggesting that dataset quality may be more important than scale in the regimes in which we operate. We also find that a model trained on both ALIGN and outperforms those trained on the two datasets individually and that how the datasets are combined is important.

To demonstrate this, we train a small model with an NFNet-F0 vision encoder, BERT-mini language encoder and batch size 2048 for 1 million gradient-calculation steps on ALIGN, and a mixture of the two. The results are presented in Table . It shows the results of training models on the combined datasets using three different merging regimes:

Data merged: Batches are constructed by merging examples from each dataset into one batch.

Round-robin: We alternate batches of each dataset, updating the parameters on each batch.

Accumulation: We compute a gradient on a batch from each dataset. These gradients are then weighted and summed and use to update the parameters.

Across all evaluation metrics, we find that the Accumulation method outperforms other methods of combining the datasets.

Although the dataset is 5 MATH smaller than the ALIGN dataset, this ablation study suggests that the quality of the training data can be more important than its abundance.

@src https://arxiv.org/abs/2205.11487
@title Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding
@section Neural network architecture

Base model: We adapt the U-Net architecture from for our base MATH text-to-image diffusion model. The network is conditioned on text embeddings via a pooled embedding vector, added to the diffusion timestep embedding similar to the class embedding conditioning method used in . We further condition on the entire sequence of text embeddings by adding cross attention over the text embeddings at multiple resolutions. We study various methods of text conditioning in sec:text_conditioning_ablation . Furthermore, we found Layer Normalization for text embeddings in the attention and pooling layers to help considerably improve performance.

Super-resolution models: For MATH super-resolution, we use the U-Net model adapted from . We make several modifications to this U-Net model for improving memory efficiency, inference time and convergence speed (our variant is 2-3x faster in steps/second over the U-Net used in ). We call this variant Efficient U-Net (See Appendix for more details and comparisons). Our MATH super-resolution model trains on MATH crops of the MATH image. To facilitate this, we remove the self-attention layers, however we keep the text cross-attention layers which we found to be critical. During inference, the model receives the full MATH low-resolution images as inputs, and returns upsampled MATH images as outputs. Note that we use text cross attention for both our super-resolution models.

@src https://arxiv.org/abs/2205.11487
@title Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding
@section Training details

Unless specified, we train a 2B parameter model for the MATH text-to-image synthesis, and 600M and 400M parameter models for MATH and MATH for super-resolution respectively. We use a batch size of 2048 and 2.5M training steps for all models. We use 256 TPU-v4 chips for our base MATH model, and 128 TPU-v4 chips for both super-resolution models. We do not find over-fitting to be an issue, and we believe further training might improve overall performance. We use Adafactor for our base MATH model, because initial comparisons with Adam suggested similar performance with much smaller memory footprint for Adafactor. For super-resolution models, we use Adam as we found Adafactor to hurt model quality in our initial ablations. For classifier-free guidance, we joint-train unconditionally via zeroing out the text embeddings with 10% probability for all three models. We train on a combination of internal datasets, with MATH 460M image-text pairs, and the publicly available Laion dataset , with MATH 400M image-text pairs. There are limitations in our training data, and we refer the reader to sec:limitations for details. See sec:impl_details_appendix for more implementation details.

@src https://arxiv.org/abs/2205.11487
@title Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding
@section Classifier-free Guidance and the Alignment-Fidelity Trade-off

We observe that classifier-free guidance is a key contributor to generating samples with strong image-text alignment, this is also consistent with the observations of . There is typically a trade-off between image fidelity and image-text alignment, as we iterate over the guidance weight.

While previous work has typically used relatively small guidance weights, uses relatively large guidance weights for all three diffusion models. We found this to yield a good balance of sample quality and alignment.

However, naive use of large guidance weights often produces relatively poor results. To enable the effective use of larger guidance we introduce several innovations, as described below.

Thresholding Techniques: First, we compare various thresholding methods used with classifier-free guidance. Fig. compares the CLIP vs.\ FID-10K score pareto frontiers for various thresholding methods of the base text-to-image MATH model. We observe that our dynamic thresholding technique results in significantly better CLIP scores, and comparable or better FID scores than the static thresholding technique for a wide range of guidance weights. fig:clip_noclip_scaledclip shows qualitative samples for thresholding techniques.

Guidance for Super-Resolution: We further analyze the impact of classifier-free guidance for our MATH model. fig:256x256_t_eval_and_gw shows the pareto frontiers for CLIP vs. FID-10K score for the MATH super-resolution model. MATH specifies the level of noise augmentation applied to the input low-resolution image during inference ( MATH means no noise). We observe that MATH gives the best FID score for all values of guidance weight. Furthermore, for all values of MATH , we observe that FID improves considerably with increasing guidance weight upto around MATH . While generation using larger values of MATH gives slightly worse FID, it allows more varied range of CLIP scores, suggesting more diverse generations by the super-resolution model. In practice, for our best samples, we generally use MATH in MATH . Using large values of MATH and high guidance weights for the super-resolution models, can create different variations of a given MATH image by altering the prompts to the super-resolution models (See fig:super_res_variations for examples).

Impact of Conditioning Augmentation: fig:super_res_ablation shows the impact of training super-resolution models with noise conditioning augmentation. Training with no noise augmentation generally results in worse CLIP and FID scores, suggesting noise conditioning augmentation is critical to attaining best sample quality similar to prior work . Interestingly, the model trained without noise augmentation has much less variations in CLIP and FID scores across different guidance weights compared to the model trained with conditioning augmentation. We hypothesize that this is primarily because strong noise augmented training reduces the low-resolution image conditioning signal considerably, encouraging higher degree of dependence on conditioned text for the model.

@src https://arxiv.org/abs/2205.11916
@title Large Language Models are Zero-Shot Reasoners
@section Implementation details

For Original GPT-3 and Instruct-GPT3, we used OpenAI API.

For OPT, T0, GPT-J, GPT-Neo, and GPT-2, we used Hugging Face Transformer Library .

We set max_tokens = 128 and used greedy decoding (temperature = 0 in the case of OpenAI API) across all the methods and models except PaLM.

For PaLM, we used 'TopK=1' for greedy deterministic decoding and max_tokens = 256.

"Q:" is set as a customized stop sequence for all the models except for Instruct-GPT3 to stop the models from repeating questions and answers by themselves.

We run our experiments on cloud V100 instances without GPU for GPT-3 models, on cloud A100x8 GPU(60GB) instances for T0 and OTP, and on cloud A100x1 GPU(60GB) instances for GPT-J, GPT-Neo, and GPT-2. Our implementation is in PyTorch .

@src https://arxiv.org/abs/2205.14135
@title FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness
@section Standard Attention Implementation

Given input sequences MATH where MATH is the sequence length and

MATH is the head dimension, we want to compute the attention output MATH :

Standard attention implementations materialize the matrices MATH and MATH to HBM, which takes MATH memory.

Often MATH (e.g., for GPT2, MATH and MATH ).

We describe the standard attention implementation in alg:standard_attn .

As some or most of the operations are memory-bound (e.g., softmax), the large number of

memory accesses translates to slow wall-clock time.

This problem is exacerbated by other elementwise operations applied

to the attention matrix, such as masking applied to MATH or dropout applied to MATH .

As a result, there have been many attempts to fuse several elementwise

operations, such as fusing masking with softmax .

In sec:theory , we will show that the standard attention implementation

performs HBM accesses quadratic in the sequence length MATH .

We also compare the number of FLOPs and number of HBM accesses of standard

@src https://arxiv.org/abs/2209.14988
@title DreamFusion: Text-to-3D using 2D Diffusion
@section NeRF Details and Training Hyperparameters

Our model builds upon mip-NeRF 360 (starting from the publicly available implementation ), which is an improved version of NeRF . The main modification this model makes to NeRF is in how 3D point information is passed to the NeRF MLP. In NeRF, each 3D input point is mapped to a higher dimensional space using a sinusoidal positional encoding function . In mip-NeRF, this is replaced by an integrated positional encoding that accounts for the "width" of the ray being rendered (based on its pixel footprint in the image plane) and the length of each interval MATH sampled along the ray . This allows each interval along a ray to be represented as a Gaussian distribution with mean MATH and covariance matrix MATH that approximates the interval's 3D volume.

Mip-NeRF covariance annealing. As in mip-NeRF, each mean MATH is the 3D coordinate of the center of the ray interval, but unlike mip-NeRF we do not use a covariance derived from camera geometry, but instead define each MATH as:

Where MATH is a scale parameter that is linearly annealed from a large value to a small value during training. Representative settings are MATH and MATH for the initial and final values of MATH , linearly annealed for the first 5k steps of optimization (out of 15k total).

This "coarse to fine" annealing of a scale parameter has a similar effect as the annealing used by but uses integrated positional encoding instead of traditional positional encoding. The underlying sinusoidal positional encoding function uses frequencies MATH , where we set MATH .

MLP architecture changes. Our NeRF MLP consists of 5 ResNet blocks with 128 hidden units, Swish/SiLU activation , and layer normalization between blocks. We use an MATH activation to produce density MATH and a sigmoid activation to produce RGB albedo MATH .

Shading hyperparameters. For the first 1k steps of optimization we set the ambient light color MATH to MATH and the diffuse light color MATH to MATH , which effectively disables diffuse shading. For the remaining steps we set MATH and MATH with probability MATH , otherwise MATH , MATH , i.e. we use diffuse shading 75% of the time. When shading is on ( MATH ), we choose textureless shading ( MATH ) with probability MATH .

Spatial density bias. To aid in the early stages of optimization, we add a small "blob" of density around the origin to the output of the MLP. This helps focus scene content at the center of the 3D coordinate space, rather than directly next to the sampled cameras. We use a Gaussian PDF to parameterize the added density:

Representative settings are MATH for the scale parameter and MATH for the width parameter. This density is added to the MATH output of the NeRF MLP.

Additional camera and light sampling details.

Uniformly sampling camera elevation MATH in angular space does not produce uniform samples over the surface of the sphere — the area around the pole is oversampled. We found this bias to be helpful in practice, so we sample MATH from this biased distribution with probability 0.5, otherwise we sample from a true uniform-in-area distribution on a half-sphere.

The sampled camera position is perturbed by a small uniform offset MATH . The "look-at" point is sampled from MATH and the default "up" vector is perturbed by noise sampled from MATH . This noise acts as an additional augmentation, and ensures a wider diversity of viewpoints are seen during training.

We separately sample the direction and norm of the light position vector MATH . To sample the direction, we sample from MATH where MATH is the camera position (this ensures that the point light usually ends up on the same side of the object as the camera). The norm MATH is sampled from MATH , while MATH .

We use the orientation loss proposed by Ref-NeRF to encourage normal vectors of the density field to face toward the camera when they are visible (so that the camera does not observe geometry that appears to face "backwards" when shaded). We place a stop-gradient on the rendering weights MATH , which helps prevent unintended local minima where the generated object shrinks or disappears:

where MATH is the direction of the ray (the viewing direction).

We also apply a small regularization to the accumulated alpha value (opacity) along each ray: MATH . This discourages optimization from unnecessarily filling in empty space, and improves foreground/background separation.

For orientation loss MATH , we find reasonable weights to lie in MATH . If orientation loss is too high, surfaces become oversmoothed. In most experiments, we set the weight to MATH . This weight is annealed in starting from MATH over the first 5k (out of 15k) steps.

For accumulated alpha loss MATH , we find reasonable weights to lie in MATH .

View-dependent prompting. We interpolate between front/side/back view prompt augmentations based on which quadrant contains the sampled azimuth MATH . We experimented with different ways of interpolating the text embeddings, but found that simply taking the text embedding closest to the sampled azimuth worked well.

with MATH , MATH , MATH , MATH , MATH , MATH , and a linear warmup of learning rate over 3000 steps from MATH to MATH followed by cosine decay down to MATH . We found this long warmup period to be helpful for improving the coherence of generated geometry.

@src https://arxiv.org/abs/2210.03629
@title ReAct: Synergizing Reasoning and Acting in Language Models
@section Methods

Prompting For HotpotQA and Fever, we randomly select 6 and 3 cases (We find more examples do not improve performance. from the training set and manually compose -format trajectories to use as few-shot exemplars in the prompts. Similar to Figure (d), each trajectory consists of multiple thought-action-observation steps (i.e.\,dense thought), where free-form thoughts are used for various purposes. Specifically, we use a combination of thoughts that decompose questions ("I need to search x, find y, then find z"), extract information from Wikipedia observations ("x was started in 1844", "The paragraph does not tell x"), perform commonsense ("x is not y, so z must instead be...") or arithmetic reasoning ("1844 < 1989"), guide search reformulation ("maybe I can search/look up x instead"), and synthesize the final answer ("...so the answer is x"). See Appendix for more details.

Baselines We systematically ablate trajectories to build prompts for multiple baselines (with formats as Figure (1a-1c)):

(a) Standard prompting ( ), which removes all thoughts, actions, observations in trajectories.

(b) Chain-of-thought prompting ( ) , which removes actions and observations and serve as a reasoning-only baseline. We also build a self-consistency baseline ( ) by sampling 21 trajectories with decoding temperature 0.7 during inference and adopting the majority answer, which is found to consistently boost performance over .

(c) Acting-only prompt ( ), which removes thoughts in trajectories, loosely resembling how WebGPT interacts with the Internet to answer questions, though it operates on a different task and action space, and uses imitation and reinforcement learning instead of prompting.

Combining Internal and External Knowledge As will be detail in Section , we observe that the problem solving process demonstrated by is more factual and grounded, whereas is more accurate in formulating reasoning structure but can easily suffer from hallucinated facts or thoughts. We therefore propose to incorporate and , and let the model decide when to switch to the other method based on the following heuristics:

MATH : when fails to return an answer within given steps, back off to . We set 7 and 5 steps for HotpotQA and FEVER respectively as we find more steps will not improve performance ( Of all trajectories with correct final answers, those with 7 steps on HotpotQA and 5 steps on FEVER only take up 0.84% and 1.33% respectively. .

MATH : when the majority answer among MATH samples occurs less than MATH times (i.e.\,internal knowledge might not support the task confidently), back off to .

Finetuning Due to the challenge of manually annotating reasoning traces and actions at scale, we consider a bootstraping approach similar to , using 3,000 trajectories with correct answers generated by (also for other baselines) to finetune smaller language models (PaLM-8/62B) to decode trajectories (all thoughts, actions, observations) conditioned on input questions/claims. More details are in Appendix .

@src https://arxiv.org/abs/2210.08402
@title LAION-5B: An open large-scale dataset for training next generation image-text models
@section Collection Methodology

We constructed LAION-5B starting from Common Crawl, a public web archive .

The Common Crawl organization crawls the web since 2008 and publishes the results in snapshots approximately every month.

Recent snapshots each contain about 300 TiB of data for around 3 billion web pages.

In the following, we introduce our pipeline to assemble and filter a vision-language dataset from images in Common Crawl and their associated HTML alt-text.

@src https://arxiv.org/abs/2210.08402
@title LAION-5B: An open large-scale dataset for training next generation image-text models
@section Training Details

We used distributed data parallel training (using PyTorch DDP) to train models on multiple NVIDIA A100 GPUs. Training was done using the InfoNCE loss like in . We used Adam with decoupled weight regularization (i.e., AdamW) as an optimizer, with MATH and MATH for all models. We used a linear warmup followed by a cosine decay schedule. For regularization we used the same weight decay of MATH for all the models.

Details about different architectures that were used are provided in Tab. .

Training hyper-parameters and resources used are provided in Tab. .

@src https://arxiv.org/abs/2210.08402
@title LAION-5B: An open large-scale dataset for training next generation image-text models
@section Distributed Training and InfoNCE Loss

To properly deal with global batch for contrastive InfoNCE loss in distributed setting, we need additional communication between GPU workers to compute the loss and the gradients for all positive and negative sample pairs correctly. In each worker, we gather all image and text embeddings from the other workers, and use them as negative examples for each image-text pair in the mini-batch.

A naive implementation of InfoNCE involves materializing a very large MATH matrix, MATH being the global batch size. For MATH , the matrix occupies a hefty 8 GB in float32. To remedy this, we use a formulation of the loss like OpenAI where redundant operations are sharded to local devices while maintaining correct global gradients. This successfully overcomes a significant scaling issue and achieves a memory complexity that scales linearly with global batch size by only materializing 2 matrices of size MATH , MATH being local batch size per GPU. By turning memory complexity from MATH into MATH , we slash memory overhead due to scaling from GBs down to MBs.

@src https://arxiv.org/abs/2210.08402
@title LAION-5B: An open large-scale dataset for training next generation image-text models
@section Training Details

We used distributed data parallel training (using PyTorch DDP) to train models on multiple NVIDIA A100 GPUs. Training was done using the InfoNCE loss like in . We used Adam with decoupled weight regularization (i.e., AdamW) as an optimizer, with MATH and MATH for all models. We used a linear warmup followed by a cosine decay schedule. For regularization we used the same weight decay of MATH for all the models.

Details about different architectures that were used are provided in Tab. .

Training hyper-parameters and resources used are provided in Tab. .

@src https://arxiv.org/abs/2210.08402
@title LAION-5B: An open large-scale dataset for training next generation image-text models
@section Distributed Training and InfoNCE Loss

To properly deal with global batch for contrastive InfoNCE loss in distributed setting, we need additional communication between GPU workers to compute the loss and the gradients for all positive and negative sample pairs correctly. In each worker, we gather all image and text embeddings from the other workers, and use them as negative examples for each image-text pair in the mini-batch.

A naive implementation of InfoNCE involves materializing a very large MATH matrix, MATH being the global batch size. For MATH , the matrix occupies a hefty 8 GB in float32. To remedy this, we use a formulation of the loss like OpenAI where redundant operations are sharded to local devices while maintaining correct global gradients. This successfully overcomes a significant scaling issue and achieves a memory complexity that scales linearly with global batch size by only materializing 2 matrices of size MATH , MATH being local batch size per GPU. By turning memory complexity from MATH into MATH , we slash memory overhead due to scaling from GBs down to MBs.

@src https://arxiv.org/abs/2212.06817
@title RT-1: Robotics Transformer for Real-World Control at Scale
@section How do various methods generalize long-horizon robotic scenarios?

In the next set of experiments we evaluate whether our method generalizes enough to be used in long-horizon realistic kitchen settings.

To answer this question, we execute and various baselines within the SayCan framework in two different real kitchens.

Since SayCan combines many low-level instructions to perform high-level instructions, the number of possible high-level instructions increases combinatorially with skills, so the skill-breadth of can be fully seen (for more details on the SayCan algorithm please refer to ).

The success rate of long-horizon tasks also decreases exponentially with the length of the task, so high success rates in manipulation skills are particularly important. Furthermore, as mobile manipulation tasks require both navigation and manipulation, the policies ability to be robust to base position is crucial.

Table shows our results (on instructions in Appendix Table ). Except for original SayCan, all methods get 87% as planning success rate, and RT-1 performs the best, with 67% execution success rate in Kitchen1. Kitchen2 constitutes a much more challenging generalization scene, since the Robot Classroom training scenes are modeled after Kitchen1 (see the pictures of the kitchens in Fig. ). Due to this generalization difficulty, SayCan with Gato is not able to finish any long horizon task, and SayCan with BC-Z is able to achieve a success rate of 13%. The original SayCan paper did not evaluate performance in a new kitchen.

Surprisingly, the manipulation performance does not see a visible drop from Kitchen1 to Kitchen2 for our method. In the supplementary video, we show that this enables us to operate unseen drawers in Kitchen2, and that we can use SayCan-RT1 to plan and execute ultra-long horizon tasks, with as many as 50 steps.

@src https://arxiv.org/abs/2301.12597
@title BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models
@section End-to-end Vision-Language Pre-training

Vision-language pre-training aims to learn multimodal foundation models with improved performance on various vision-and-language tasks.

Depending on the downstream task, different model architectures have been proposed, including the dual-encoder architecture , the fusion-encoder architecture , the encoder-decoder architecture ,

and more recently, the unified transformer architecture .

Various pre-training objectives have also been proposed over the years,

and have progressively converged to a few time-tested ones: image-text contrastive learning ,

Most VLP methods perform end-to-end pre-training using large-scale image-text pair datasets.

As the model size keeps increasing, the pre-training can incur an extremely high computation cost.

Moreover, it is inflexible for end-to-end pre-trained models to leverage readily-available unimodal pre-trained models,

@src https://arxiv.org/abs/2301.12597
@title BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models
@section Modular Vision-Language Pre-training

More similar to us are methods that leverage off-the-shelf pre-trained models and keep them frozen during VLP.

Some methods freeze the image encoder, including the early work which adopts a frozen object detector to extract visual features ,

and the recent LiT which uses a frozen pre-trained image encoder for CLIP pre-training.

Some methods freeze the language model to use the knowledge from LLMs for vision-to-language generation tasks .

The key challenge in using a frozen LLM is to align visual features to the text space.

To achieve this, Frozen finetunes an image encoder whose outputs are directly used as soft prompts for the LLM.

Flamingo inserts new cross-attention layers into the LLM to inject visual features,

and pre-trains the new layers on billions of image-text pairs.

Both methods adopt the language modeling loss,

where the language model generates texts conditioned on the image.

BLIP-2 can effectively and efficiently leverage both frozen image encoders and frozen LLMs for various vision-language tasks,

achieving stronger performance at a lower computation cost.

@src https://arxiv.org/abs/2301.12597
@title BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models
@section Method

We propose BLIP-2, a new vision-language pre-training method that bootstraps from frozen pre-trained unimodal models.

we propose a Querying Transformer ( ) pre-trained in two stages:

(1) vision-language representation learning stage with a frozen image encoder and (2) vision-to-language generative learning stage with a frozen LLM.

This section first introduces the model architecture of ,

and then delineates the two-stage pre-training procedures.

@src https://arxiv.org/abs/2301.12597
@title BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models
@section Model Architecture

We propose as the trainable module to bridge the gap between a frozen image encoder and a frozen LLM.

It extracts a fixed number of output features from the image encoder,

consists of two transformer submodules that share the same self-attention layers: (1) an image transformer that interacts with the frozen image encoder for visual feature extraction, (2) a text transformer that can function as both a text encoder and a text decoder.

We create a set number of learnable query embeddings as input to the image transformer.

The queries interact with each other through self-attention layers, and interact with frozen image features through cross-attention layers (inserted every other transformer block).

The queries can additionally interact with the text through the same self-attention layers.

we apply different self-attention masks to control query-text interaction.

We initialize with the pre-trained weights of BERT MATH , whereas the cross-attention layers are randomly initialized.

Note that the queries are considered as model parameters.

we use 32 queries where each query has a dimension of 768 (same as the hidden dimension of the ).

We use MATH to denote the output query representation.

The size of MATH ( MATH ) is much smaller than the size of frozen image features ( MATH for ViT-L/14).

This bottleneck architecture works together with our pre-training objectives into forcing the queries to extract visual information that is most relevant to the text.

@src https://arxiv.org/abs/2301.12597
@title BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models
@section Model Pre-training

We use the same pre-training dataset as BLIP with 129M images in total,

including COCO , Visual Genome , CC3M , CC12M , SBU , and 115M images from the LAION400M dataset .

We adopt the CapFilt method to create synthetic captions for the web images.

Specifically, we generate 10 captions using the BLIP MATH captioning model, and rank the synthetic captions along with the original web caption based on the image-text similarity produced by a CLIP ViT-L/14 model.

We keep top-two captions per image as training data and randomly sample one at each pre-training step.

For the frozen image encoder, we explore two state-of-the-art pre-trained vision transformer models: (1) ViT-L/14 from CLIP and (2) ViT-g/14 from EVA-CLIP .

We remove the last layer of the ViT and uses the second last layer's output features,

which leads to slightly better performance.

we explore the unsupervised-trained OPT model family for decoder-based LLMs,

and the instruction-trained FlanT5 model family for encoder-decoder-based LLMs.

We pre-train for 250k steps in the first stage and 80k steps in the second stage.

We use a batch size of 2320/1680 for ViT-L/ViT-g in the first stage and a batch size of 1920/1520 for OPT/FlanT5 in the second stage.

During pre-training, we convert the frozen ViTs' and LLMs' parameters into FP16, except for FlanT5 where we use BFloat16.

We found no performance degradation compared to using 32-bit models.

our pre-training is more computational friendly than existing large-scale VLP methods.

our largest model with ViT-g and FlanT5-XXL requires less than 6 days for the first stage and less than 3 days for the second stage.

The same set of pre-training hyper-parameters are used for all models.

We use the AdamW optimizer with MATH , MATH , and a weight decay of 0.05.

We use a cosine learning rate decay with a peak learning rate of 1e-4 and a linear warmup of 2k steps.

The minimum learning rate at the second stage is 5e-5.

We use images of size 224 MATH 224, augmented with random resized cropping and horizontal flipping.

@src https://arxiv.org/abs/2304.07193
@title DINOv2: Learning Robust Visual Features without Supervision
@section Discriminative Self-supervised Pre-training

We learn our features with a discriminative self-supervised method that can be seen as a combination of DINO and iBOT losses with the centering of SwAV .

We also add a regularizer to spread features and a short high-resolution training phase.

We rapidly introduce each of these approaches, but more details can be found in the related papers, or in our open-sourced code.

We consider the cross-entropy loss between the features extracted from a student and a teacher network.

Both features are coming from the class token of a ViT, obtained from different crops of the same image.

We pass the student class token through the student DINO head.

This head is an MLP model outputting a vector of scores, that we call "prototype scores".

We then apply a softmax to obtain MATH .

Similarly, we apply the teacher DINO head to the teacher class token to obtain teacher prototype scores.

We then apply a softmax followed by a centering with moving average (or a Sinkhorn-Knopp centering as detailed thereafter) to obtain MATH .

We learn the parameters of the student and build the teacher head with an exponential moving average of past iterates .

We randomly mask some of the input patches given to the student, but not to the teacher.

We then apply the student iBOT head to the student mask tokens.

Similarly, we apply the teacher iBOT head to the (visible) teacher patch tokens corresponding to the ones masked in the student.

We then apply the softmax and centering steps as above, and obtain the iBOT loss term:

where MATH are patch indices for masked tokens.

Similarly to above, we learn the parameters of the student, and build the teacher head through exponential moving average.

Untying head weights between both objectives.

Both the DINO and the iBOT loss use a learnable MLP projection head.

It is applied to the output tokens and the loss is compute atop.

In , an ablation study shows that sharing parameters between the DINO and iBOT heads leads to better performance.

At scale, we observed that the opposite is true, and we therefore use two separate heads in all our experiments.

recommend to replace the teacher softmax-centering step of DINO and iBot by the Sinkhorn-Knopp (SK) batch normalization of SwAV .

We run the Sinkhorn-Knopp algorithm steps for 3 iterations.

For the student, we apply the softmax normalization.

The KoLeo regularizer derives from the Kozachenko-Leonenko differential entropy estimator (see ) and encourages a uniform span of the features within a batch.

Given a set of MATH vectors MATH , it is defined as where MATH is the minimum distance between MATH and any other point within the batch.

We also MATH -normalize the features before computing this regularizer.

Increasing image resolution is key to pixel-level downstream tasks such as segmentation or detection, where small objects disappear at low resolutions.

However, training at high resolution is time and memory demanding, and instead, we increase the resolution of images to MATH during a short period at the end of pretraining. This is also similar to UniViT training from and FlexiViT training from .

@src https://arxiv.org/abs/2304.07193
@title DINOv2: Learning Robust Visual Features without Supervision
@section Efficient implementation

We consider several improvements to train models at a larger scale.

We train models on A100 GPUs using PyTorch 2.0.

The code and pretrained models are made available under Apache 2.0 license (https://github.com/facebookresearch/dinov2 .

The details of our models are in the appendix, Table . With the same hardware, compared to the iBOT implementation, the code runs around MATH faster using only MATH of the memory.

We implemented our own version of FlashAttention to improve memory usage and speed on the self-attention layers.

Our version is on par with or better than the original on all cases considered, while covering more use-cases and hardware.

Due to the GPU hardware specifics, the efficiency is best when the embedding dimension per head is a multiple of 64, and the matrix operations are even better when the full embedding dimension is a multiple of 256.

As a consequence, our ViT-g architecture slightly differs from the architecture proposed by in order to maximize compute efficiency, and we use an embedding dimension of 1536 with 24 heads (64 dim/head), rather than 1408 with 16 heads (88 dim/head). Our experiments did not show significant differences in final accuracy, and our ViT-g backbone counts 1.1B parameters.

Sequence packing. The DINO algorithm requires forwarding both large crops (at resolution 224) and small crops (resolution 98).

When split into patches, these two groups are represented by token sequences of different lengths and cannot be forwarded together.

In order to accelerate training, we use a trick called "sequence packing," which originates from NLP .

The idea is simple: we concatenate the sequences we must forward through the transformers into a single long sequence.

We pass this sequence through the transformer blocks as usual.

However, a block-diagonal mask is applied to the self-attention matrix in attention layers, preventing attention between different sequences.

This way, the forward is strictly equivalent to forwarding each sequence separately.

This trick gives us significant compute efficiency gains compared to using separate forward and backward passes, as in prior implementations.

The lower-level components of our setup are available in the xFormers library (https://github.com/facebookresearch/xformers ( ).

We implement an improved version of stochastic depth that skips the computation of the dropped residuals rather than masking the result.

This saves memory and compute in proportion approximately equal to the drop rate, thanks to specific fused kernels.

With high drop rates ( MATH in this work), this allows a drastic improvement in compute efficiency and memory usage.

The implementation consists of randomly shuffling the MATH samples over the batch dimension, and slicing the first MATH samples for the computations in the block.

Minimizing our objective with the AdamW optimizer requires 4 model replicas in float32 precision – student, teacher, optimizer first moments, optimizer second moments.

This sums to MATH of memory for a billion-parameter model such as our ViT-g.

In order to reduce this memory footprint per GPU, we split the model replicas across GPUs, i.e., sharding MATH across GPUs using the PyTorch implementation of FSDP.

Consequently, the model size is not bounded by the memory of a single GPU but by the total sum of GPU memory across compute nodes.

The Pytorch implementation of FSDP brings a second advantage, which is to save on the cross-GPU communication costs: the weight shards are stored in float32 precision as required by the optimizer, but broadcasting weights and reducing gradients is done in float16 precision for the backbone (MLP heads gradients are reduced in float32 to avoid training instabilities).

This leads to approximately 50% reduction in communication costs compared to the float32 gradient all-reduce operation used in DistributedDataParallel (DDP), which is used in other self-supervised pretraining methods .

As a consequence, the training procedure scales more efficiently than DDP with float16 autocast when scaling the number of GPU nodes.

Overall, Pytorch-FSDP mixed-precision is superior to DDP with autocast in virtually all cases we encountered.

Most of our technical improvements to the training loop aim at improving the training of large models over large quantities of data.

For smaller models, we distill them from our largest model, the ViT-g, instead of training them from scratch.

Knowledge distillation aims at reproducing the output of a large model with a smaller model by minimizing some distance between both outputs for a set of given inputs.

Since our objective function is a form of distillation from the teacher network to the student network, we leverage the same training loop with a few exceptions:

we use a larger model as a frozen teacher, keep a spare EMA of the student that we use as our final model, remove the masking and stochastic depth, and, apply the iBOT loss on the two global crops.

In our ablations, we observe that this approach achieves better performance than training from scratch, even for a ViT-L.

Our distillation method ends up close to the one described by , except we do not modify the loss terms for distillation and evaluate the EMA of the student.

@src https://arxiv.org/abs/2304.07193
@title DINOv2: Learning Robust Visual Features without Supervision
@section Improved Training Recipe

Our approach improves over the iBOT method by combining it with several existing components described in Sec. .

To evaluate their importance, we train multiple models where we successively add components to a baseline iBOT model.

We report the Top-1 accuracy on the validation set of ImageNet-1k with a k-NN and a linear probe in Table .

Generally, we observe that each component improves the performance on either k-NN or linear probing and even both in most cases.

Only LayerScale and Stochastic Depth incur a performance drop in linear probing but significantly improve the training stability in our experience.

@src https://arxiv.org/abs/2304.07193
@title DINOv2: Learning Robust Visual Features without Supervision
@section Pretraining Data Source

The quality of features is directly related to the quality of the pretraining data.

In this experiment, we probe the impact of compared to ImageNet-22k, a commonly used pretraining dataset, or using directly raw and uncurated data.

For the uncurated dataset, we randomly sample MATH million images from the same data source as .

We train a ViT-g/14 on each dataset for the same number of iterations.

We also include a variant of ImageNet-22k obtained by removing the synsets of ImageNet-1k (INet-22k MATH INet-1k) for completeness.

The most salient observation is that training on a curated set of images works better on most benchmarks than training on uncurated data.

This confirms the benefit of curating data, even in the case of self-supervised pretraining.

When compared with models trained on ImageNet-22k, training on is also superior on all the benchmarks but ImageNet-1k.

This confirms that training on a more diverse set of images improves the quality of the features in domains that are not covered by ImageNet-22k .

We also see that training on our curated data increases the performances on domains that are not used for the curation process (INaturalist 2018, 2021 and Places205), proving that scale and diversity can benefit unseen domains.

Overall, the conclusion of this ablation is that our dataset provides a good balance of different types of images that leads to the best performance overall.

@src https://arxiv.org/abs/2304.07193
@title DINOv2: Learning Robust Visual Features without Supervision
@section Estimating the Environmental Impact of Training our Models

Training foundation models consumes a significant amount of energy, resulting in carbon dioxide emissions.

propose a methodology to report an estimation of the carbon emitted during the training of a model based on the specifics of the data center and its power grid.

This computation informs the design of the data center used for the training of models and the choice of location for data centers.

This methodology requires to know the specifics of the data center used for training, which can be complex when multiple data centers are involved over time.

Additionally, these specifics are most often not in the control of the AI practitioner, and hence, this methodology is less helpful when practioners make technical decisions about future trainings.

Instead, in this section, we follow an alternative that reports the potential carbon emission of retraining a similar model in an average data center located in the US.

This methodology was used in previous work in natural language processing to establish an apple-to-apple comparison between pretraining schemes.

More precisely, we fix the value of all exogenous variables, i.e., the Power Usage Effectiveness (PUE) and carbon intensity factor of a power grid to the same values as in , that is, a PUE of 1.1 and the carbon intensity factor to the US average of 0.385 kg CO MATH eq/KWh.

We use the same formula as in to estimate the potential energy consumption and the carbon emission.

For the power consumption of an A100-80GB, we take the thermal design power for NVLink systems, which is 400W.

We report the potential carbon emission of retraining a ViT-g in Table .

For comparison, retraining an OpenCLIP ViT-L or OpenCLIP ViT-G would require 22.4 MWh and 118.9 MWh, respectively, if run in the same data center.

Note that this comparison is not fair to them, since they also train a text encoder in parallel, and we thus do not report them in the table.

However, it gives a reasonable guideline for those who are interested in training only visual features: in this context, training a self-supervised model is preferable in terms of carbon emission.

Training a text-guided model still makes sense when planning to reuse the text encoder.

Additionally, we estimate the footprint of the whole project to be between MATH k and MATH k tCO MATH eq using the same grid as presented above ( For context, a full Boeing 777 return flight between London and New York corresponds to approximately 560 tCO MATH eq. .

This carbon footprint represents in the order of MATH k GPU-days.

The primary sources of emissions are the self-supervised pre-trainings of the models.

For example, a single pre-training of a ViT-g model (22k GPU-hours) emits 3.7 tons of CO MATH eq, while a finetuning on ImageNet-1k (1k GPU-hours) emits 0.2 tons.

This estimate only considers the GPUs' electricity consumption and ignores other emissions, such as their manufacturing and disposal.

@src https://arxiv.org/abs/2304.07193
@title DINOv2: Learning Robust Visual Features without Supervision
@section Unsupervised pre-training

For unsupervised pre-training we build on the DINO and iBOT codebases. We use hyperparameters shown in

Table , ViT architectures described in Table .

We apply the KoLeo regularizer with a weight of 0.1 between the class tokens of the first global crop, for all samples within a GPU without cross-communication for this step.

The teacher is initialized with the same state as the student, and is an exponential moving average of the student network, with a momentum value in [0.994, 1.0] following a cosine schedule. It is updated at the end of every training step.

@src https://arxiv.org/abs/2304.08485
@title Visual Instruction Tuning
@section Architecture

The primary goal is to effectively leverage the capabilities of both the pre-trained LLM and visual model. The network archtecture is illustrated in Figure . We choose Vicuna as our LLM MATH parameterized by MATH , as it has the best instruction following capabilities in language tasks among publicly available checkpoints .

For an input image MATH , we consider the pre-trained CLIP visual encoder ViT-L/14 , which provides the visual feature MATH . The grid features before and after the last Transformer layer are considered in our experiments.

We consider a simple linear layer to connect image features into the word embedding space. Specifically, we apply a trainable projection

into language embedding tokens MATH , which have the same dimensionality as the word embedding space in the language model:

Thus, we have a sequence of visual tokens MATH .

Note that our simple projection scheme is lightweight, which allows us to iterate data centric experiments quickly. More sophisticated schemes to connect the image and language representations can also be considered, such as gated cross-attention in Flamingo and Q-former in BLIP-2 . We leave exploring possibly more effective and sophisticated architecture designs for as future work.

@src https://arxiv.org/abs/2304.08485
@title Visual Instruction Tuning
@section Training

For each image MATH , we generate multi-turn conversation data

MATH , where MATH is the total number of turns.

We organize them as a sequence, by treating all answers as the assistant's response, and the instruction MATH at the MATH -th turn as:

This leads to the unified format for the multimodal instruction-following sequence illustrated in Table . We perform instruction-tuning of the LLM on the prediction tokens, using its original auto-regressive training objective.

Specifically, for a sequence of length MATH , we compute the probability of the target answers MATH by:

where MATH is the trainable parameters, MATH and MATH are the instruction and answer tokens in all turns before the current prediction token MATH , respectively. Please see Table for an illustration of the prediction tokens. For the conditionals in , we explicitly add MATH to emphasize the fact that the image is grounded for all answers, and we omit MATH and all previous <STOP> for better readability.

For model training, we consider a two-stage instruction-tuning procedure.

Stage 1: Pre-training for Feature Alignment. To strike a balance between concept coverage and training efficiency, we filter CC3M to 595K image-text pairs. Please see Appendix for details of the filtering process. These pairs are converted to the instruction-following data using the naive expansion method describe in Section .

Each sample can be treated as a single-turn conversation. To construct the input MATH in , for an image MATH , a question MATH is randomly sampled, which is a language instruction to request the assistant to describe the image briefly. The ground-truth prediction answer MATH is the original caption. In training, we keep both the visual encoder and LLM weights frozen, and maximize the likelihood of with trainable parameters MATH (the projection matrix) only. In this way, the image features MATH can be aligned with the pre-trained LLM word embedding. This stage can be understood as training a compatible visual tokenizer for the frozen LLM.

We always keep the visual encoder weights frozen, and continue to update both the pre-trained weights of the projection layer and LLM in ; i.e., the trainable parameters are MATH in . We consider two specific use case scenarios:

Multimodal Chatbot . We develop a Chatbot by fine-tuning on the 158K language-image instruction-following data in Section . Among the three types of responses, conversation is multi-turn while the other two are single-turn. They are uniformly sampled in training.

Science QA . We study our method on the ScienceQA benchmark , the first large-scale multimodal science question dataset that annotates the answers with detailed lectures and explanations. Each question is provided a context in the form of natural language or an image. The assistant provides the reasoning process in natural language and selects the answer among multiple choices.

For training in , we organize the data as a single turn conversation, the question & context as MATH , and reasoning & answer as MATH .

@src https://arxiv.org/abs/2304.08485
@title Visual Instruction Tuning
@section Training Details

We pre-train our model on the filtered CC-595K subset for 1 epoch with a learning rate of 2e-3 and a batch size of 128, and fine-tune on the proposed LLaVA-Instruct-158K dataset for 3 epochs, with a learning rate of 2e-5 and a batch size of 32. Following Vicuna, we use the Adam optimizer with no weight decay and a cosine learning rate with a warmup ratio of 3%. During finetuning, FSDP (Full Shard Data Parallel) and gradient checkpointing is used to save GPU memory, and offloading is not used. BF16 and TF32 are enabled to achieve a balance between speed and precision.

We train all models with 8 MATH A100s. Pretraining on CC-595K completes within 4 hours. Finetuning on Instruct-158K completes within 10 hours. Finetuning on ScienceQA completes within 4 hours.

@src https://arxiv.org/abs/2304.10592
@title MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models
@section Method

MiniGPT-4 aims to align visual information from a pretrained vision encoder with an advanced large language model (LLM). Specifically, we utilize the Vicuna as our language decoder, which is constructed upon LLaMA and can perform a wide range of complex linguistic tasks. For visual perception, we employ the same visual encoder as used in BLIP-2 , a ViT backbone coupled with their pre-trained Q-Former. Both language and vision models are open-sourced. We target to bridge the gap between the visual encoder and LLM using a linear projection layer, with an overview of our model displayed in Fig. .

To achieve an effective MiniGPT-4, we propose a two-stage training approach. The initial stage involves pretraining the model on a large collection of aligned image-text pairs to acquire vision-language knowledge. In the second stage, we finetune the pretrained model with a smaller but high-quality image-text dataset with a designed conversational template to enhance generation reliability and usability.

@src https://arxiv.org/abs/2304.10592
@title MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models
@section First pretraining stage

During the initial pretraining stage, the model is designed to acquire vision-language knowledge from a large collection of aligned image-text pairs. We regard the output from the injected projection layer as a soft prompt for the LLM, prompting it to generate the corresponding ground-truth texts.

Throughout the entire pretraining process, both the pretrained vision encoder and the LLM remain frozen, with only the linear projection layer being pretrained. We use a combined dataset of Conceptual Caption , SBU and LAION to train our model. Our model undergoes 20,000 training steps with a batch size of 256, covering approximately 5 million image-text pairs. The entire process takes about 10 hours to complete, utilizing 4 A100 (80GB) GPUs.

Following the first pretraining stage, our MiniGPT-4 demonstrates the capacity to possess a wealth of knowledge and offer reasonable responses to human inquiries. However, we have observed instances where it produces incoherent linguistic outputs, such as repetitive words or sentences, fragmented sentences, or irrelevant content. These issues hinder MiniGPT-4's ability to engage in a fluent visual conversation with humans.

We also observed similar challenges encountered in GPT-3. Despite its pretraining on a extensive language dataset, GPT-3 struggles to generate language outputs that are accurately aligned with users' intentions.

Through a process of instruction fine-tuning and reinforcement learning from human feedback, GPT-3 evolves into GPT-3.5 and becomes capable of producing more human-friendly outputs.

This phenomenon bears a resemblance to the current state of MiniGPT-4 following its initial pretraining stage. As such, it is not surprising that our model may struggle to generate fluent and natural human language outputs at this stage.

@src https://arxiv.org/abs/2304.10592
@title MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models
@section Curating a high-quality alignment dataset for vision-language domain.

To achieve greater naturalness in the generated language and enhance the model's usability, a second-stage alignment process is essential. While in the realm of NLP, instruction fine-tuning datasets and conversations are easily accessible, no equivalent datasets exist for the vision-language domain. To address this deficiency, we carefully curated a detailed image description dataset, specifically tailored for vision-language alignment purposes. This dataset is subsequently utilized to fine-tune our MiniGPT-4 during the second-stage alignment process.

In the initial phase, we employ the model derived from the first pretraining stage to generate comprehensive descriptions of input images. To enable our model to produce more detailed image descriptions, we designed a prompt that adheres to the conversational format of the Vicuna language model, as shown below. In this prompt, ImageFeature represents the visual features produced by the linear projection layer.

###Human: Img ImageFeature /Img Describe this image in detail. Give as many details as possible. Say everything you see. ###Assistant:

To identify incomplete sentences, we examine whether the generated sentence exceeds 80 tokens. If it does not, we incorporate an additional prompt, ###Human: Continue ###Assistant: , prompting our MiniGPT-4 to extend the generation process. By concatenating the outputs from both steps, we can create a more comprehensive image description. This approach enables us to generate image-text pairs with detailed and informative image descriptions. We randomly select 5,000 images from the Conceptual Caption dataset and use the pretrained model to generate corresponding language descriptions for each image.

The above automatically generated image descriptions contain noisy or incoherent descriptions, such as repetition of words or sentences, fragmented sentences, or irrelevant content.

In order to fix these issues, we employ ChatGPT to mend the descriptions by utilizing the following prompt:

Fix the error in the given paragraph. Remove any repeating sentences, meaningless characters, not English sentences, and so on. Remove unnecessary repetition. Rewrite any incomplete sentences. Return directly the results without explanation. Return directly the input paragraph if it is already correct without explanation.

Upon completing the post-processing stage, we manually verify the correctness of each image description to guarantee its high quality. Specifically, we first identified several frequently shown errors ("I'm sorry I made a mistake...", or "I apologize for that ...") and then hard-coded rules to automatically filter them out. We also manually refine the generated captions by eliminating redundant words or sentences that ChatGPT fails to detect. Finally, only approximately 3,500 out of 5,000 image-text pairs satisfy our requirement, and these pairs are subsequently utilized for the second-stage alignment process.

@src https://arxiv.org/abs/2304.10592
@title MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models
@section Ablation on the architecture designs

To further demonstrate the effectiveness of using one single linear layer to align visual features with LLM, we conduct experiments with different architecture designs, including (a) removing the Q-Former and directly mapping the VIT’s output to Vicuna’s embedding space (i.e., without Q-former), (b) using three linear layers instead of one layer, and (c) additionally finetuning the Q-Former in the vision module.

All the variants are trained in the same way as the original design. Results on AOK-VQA and GQA datasets in Tab. show that the variant (a) MiniGPT-4 w/o Q-Former has a similar performance to the original design.

Qualitative results of this variant in Fig. , , and also show similar advanced skills.

This reveals that the Q-Former from BLIP-2 doesn't plays a critical roles for advanced skills.

Besides, both variants (b) MiniGPT-4+ 3 Layers and (c) MiniGPT-4 + finetuning Q-Former, perform slightly worse than the original MiniGPT-4.

This indicates a single projection layer is sufficient to align the vision encoder and the large language model in our limited training data setting.

@src https://arxiv.org/abs/2305.20050
@title Let's Verify Step by Step
@section Methods

We perform a comparison of outcome and process supervision, following a similar methodology to . Outcome supervision can be provided without humans, since all problems in the MATH dataset have automatically checkable answers. In contrast, there is no simple way to automate process supervision. We therefore rely on human data-labelers to provide process supervision, specifically by labelling the correctness of each step in model-generated solutions.

We conduct experiments in two separate regimes: large-scale and small-scale. Each has its own advantages, and they offer complimentary perspectives. At large-scale, we finetune all models from GPT-4 . We focus on advancing the state-of-the-art by training the most reliable ORM and PRM possible. Unfortunately the training sets for these reward models are not directly comparable, for reasons we will discuss in section:large_scale . These models are therefore not ideal for making an apples-to-apples comparison of outcome and process supervision. To address this flaw, we also train models at small-scale, where we can conduct a more direct comparison. In order to remove our dependence on costly human feedback, we use a large-scale model to supervise small-scale model training. This setup enables us to conduct several important ablations that would otherwise be infeasible.

@src https://arxiv.org/abs/2305.20050
@title Let's Verify Step by Step
@section Alignment Impact

Process supervision has several advantages over outcome supervision related to AI alignment. Process supervision is more likely to produce interpretable reasoning, since it encourages models to follow a process endorsed by humans. Process supervision is also inherently safer: it directly rewards an aligned chain-of-thought rather than relying on outcomes as a proxy for aligned behavior . In contrast, outcome supervision is harder to scrutinize, and the preferences conveyed are less precise. In the worst case, the use of outcomes as an imperfect proxy could lead to models that become misaligned after learning to exploit the reward signal .

In some cases, safer methods for AI systems can lead to reduced performance , a cost which is known as an alignment tax. In general, any alignment tax may hinder the adoption of alignment methods, due to pressure to deploy the most capable model. Our results show that process supervision in fact incurs a negative alignment tax. This could lead to increased adoption of process supervision, which we believe would have positive alignment side-effects. It is unknown how broadly these results will generalize beyond the domain of math, and we consider it important for future work to explore the impact of process supervision in other domains.

@src https://arxiv.org/abs/2305.20050
@title Let's Verify Step by Step
@section ORM Training Details

We train outcome-supervised reward models in the same manner as token-level verifiers from , with a few subtle differences to hyperparameters. In particular, we only train for a single epoch on each dataset of model samples and reward model labels, without dropout, and without jointly learning a language modeling objective. We find that performance is not sensitive to most other hyperparameters, within a reasonable range.

To collect model samples, we simply sample uniformly from the generator at a temperature of 1.0 without applying any rebalancing of positives or negatives. At training time, the reward model makes predictions for every token in the context. The target for each token in a solution is the same, based on whether the solution is labelled correct or incorrect. At test time, we simply use the score of the final token in the completion as the overall score of the solution. We note that this setup is identical to the way token-level verifiers were trained in .

@src https://arxiv.org/abs/2305.20050
@title Let's Verify Step by Step
@section Training

We train our PRMs by fine-tuning the MathMix model to predict the probability of positive, negative, and neutral labels given a solution prefix ending in one of our labeled steps. We sweep over hyperparameters using a dataset containing the first MATH of PRM800K. Fine-tuning an LLM from its ordinary language modeling task to a classification task like this is a large distribution shift, and we found low learning rates were important to stable PRM training.

All of our PRMs are trained for 2 epochs. On smaller datasets (such as in phase 1 and the first few generations of phase 2) this improves the final performance over training for just 1 epoch. Additional epochs, up to some point, don't noticeably help or hurt performance. On larger datasets, the benefits of 2 epoch training diminishes, but we continue doing it for consistency.

@src https://arxiv.org/abs/2307.01952
@title SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis
@section Architecture & Scale

Starting with the seminal works and , which demonstrated that DMs are powerful generative models for image synthesis, the convolutional UNet architecture has been the dominant architecture for diffusion-based image synthesis. However, with the development of foundational DMs , the underlying architecture has constantly evolved: from adding self-attention and improved upscaling layers , over cross-attention for text-to-image synthesis , to pure transformer-based architectures .

We follow this trend and, following , shift the bulk of the transformer computation to lower-level features in the UNet. In particular, and in contrast to the original architecture, we use a heterogeneous distribution of transformer blocks within the UNet: For efficiency reasons, we omit the transformer block at the highest feature level, use 2 and 10 blocks at the lower levels, and remove the lowest level ( MATH downsampling) in the UNet altogether — see tab:modelarchcomp for a comparison between the architectures of 1.x & 2.x and . We opt for a more powerful pre-trained text encoder that we use for text conditioning. Specifically, we use OpenCLIP ViT-bigG in combination with CLIP ViT-L , where we concatenate the penultimate text encoder outputs along the channel-axis . Besides using cross-attention layers to condition the model on the text-input, we follow and additionally condition the model on the pooled text embedding from the OpenCLIP model. These changes result in a model size of 2.6B parameters in the UNet, see Tab. . The text encoders have a total size of 817M parameters.

@src https://arxiv.org/abs/2307.01952
@title SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis
@section Multi-Aspect Training

Real-world datasets include images of widely varying sizes and aspect-ratios (c.f. fig:size_dist ) While the common output resolutions for text-to-image models are square images of MATH or MATH pixels, we argue that this is a rather unnatural choice, given the widespread distribution and use of landscape (e.g., 16:9) or portrait format screens.

Motivated by this, we finetune our model to handle multiple aspect-ratios simultaneously: We follow common practice and partition the data into buckets of different aspect ratios, where we keep the pixel count as close to MATH pixels as possibly, varying height and width accordingly in multiples of 64. A full list of all aspect ratios used for training is provided in supsubsec:marlist . During optimization, a training batch is composed of images from the same bucket, and we alternate between bucket sizes for each training step. Additionally, the model receives the bucket size (or, target size) as a conditioning, represented as a tuple of integers MATH which are embedded into a Fourier space in analogy to the size- and crop-conditionings described above.

In practice, we apply multi-aspect training as a finetuning stage after pretraining the model at a fixed aspect-ratio and resolution and combine it with the conditioning techniques introduced in subsec:condtricks via concatenation along the channel axis. fig:cond_cat_code in supsec:cond_pseudo_code provides |python|-code for this operation. Note that crop-conditioning and multi-aspect training are complementary operations, and crop-conditioning then only works within the bucket boundaries (usually 64 pixels). For ease of implementation, however, we opt to keep this control parameter for multi-aspect models.

@src https://arxiv.org/abs/2307.08691
@title FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning
@section Standard Attention Implementation

Given input sequences MATH where MATH is the sequence length and

MATH is the head dimension, we want to compute the attention output MATH :

where MATH is applied row-wise. (For clarity of exposition, we

omit the scaling of MATH (typically by MATH ), and optionally

elementwise masking on MATH and/or dropout applied to MATH For multi-head

attention (MHA), this same computation is performed in parallel across many

heads, and parallel over the batch dimension (number of input sequences in a

The backward pass of attention proceeds as follows.

Let MATH be the gradient of MATH with respect to some loss

function. Then by the chain rule (aka backpropagation):

where MATH is the gradient (backward pass) of softmax applied row-wise.

One can work out that if MATH for some vector MATH and MATH , then

with output gradient MATH , the input gradient MATH .

Standard attention implementations materialize the matrices MATH and MATH to

Often MATH (typically MATH is on the order of 1k–8k and MATH is around 64–128).

The standard attention implementation (1) calls the matrix multiply (GEMM)

subroutine to multiply MATH , writes the result to HBM, then (2)

loads MATH from HBM to compute softmax and write the result MATH to HBM, and

As most of the operations are bounded by memory bandwidth, the large number of

memory accesses translates to slow wall-clock time.

Moreover, the required memory is MATH due to having to materialize MATH and

Moreover, one has to save MATH for the backward pass to compute the

@src https://arxiv.org/abs/2307.15818
@title RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control
@section Training Details

We perform co-fine-tuning on pre-trained models from the PaLI-X 5B & 55B model, PaLI 3B model and the PaLM-E 12B model. For -PaLI-X-55B, we use learning rate 1e-3 and batch size 2048 and co-fine-tune the model for 80K gradient steps whereas for -PaLI-X-5B, we use the same learning rate and batch size and co-fine-tune the model for 270K gradient steps. For -PaLM-E-12B, we use learning rate 4e-4 and batch size 512 to co-fine-tune the model for 1M gradient steps. Both models are trained with the next token prediction objective, which corresponds to the behavior cloning loss in robot learning. For RT-2-PaLI-3B model used for Language-Table results in Table , we use learning rate 1e-3 and batch size 128 to co-fine-tune the model for 300K gradient steps.

@src https://arxiv.org/abs/2310.06770
@title SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
@section Retrieval-Based Approach

instances provide an issue description and a codebase as input to the model.

While issues descriptions are usually short ( MATH words on average as shown in Table ), codebases consist of many more tokens ( MATH K lines on average) than can typically be fit into an LMs context window.

Then the question remains of exactly how to choose the relevant context to provide to the model?

To address this issue for our baselines, we simply use a generic retrieval system to select the files to insert as context.

In particular, we evaluate models under two relevant context settings: 1) sparse retrieval and 2) an oracle retrieval.

Dense retrieval methods are ill-suited to our setting due to very long key and query lengths, and especially the unusual setting of retrieving code documents with natural language queries.

Therefore, we choose to use BM25 retrieval to retrieve relevant files to provide as context for each task instance.

We experiment with three different maximum context limits, and simply retrieve as many files as fits within the specified limit.

We evaluate each model on all limits that fit within its context window and report the best performance.

From observation, models perform best on the shortest context window, as shown in Table .

For analysis purposes we also consider a setting where we "retrieve" the files edited by the reference patch that solved the issue on GitHub.

This "oracle" setting is less realistic, since an engineer working on addressing an issue may not know a priori which files need to be modified.

In addition, this setting is also not necessarily comprehensive since edited files alone may not include all the required context to understand exactly how software will behave when interacting with unseen parts of the code.

We compare the BM25 retrieval results with those of the "oracle" retrieval setting, as shown in Table .

We observe that in approximately MATH of instances, BM25 retrieves a superset of the oracle files for the MATH -token context limit. However, in almost half of the instances with the MATH -token limit, it retrieves none of the files from the "oracle" context.

@src https://arxiv.org/abs/2310.06770
@title SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
@section Training Details

Optimization. We finetune using LoRA with MATH , MATH , MATH , on the query, key, value, and output projection matrices of every attention sublayer.

We train with a learning rate of MATH and a batch size of MATH sequences per gradient step for a maximum of MATH epochs.

During training, we save checkpoints every MATH steps, and after training, select the best checkpoint based on the validation loss on a held-out MATH instances.

7b was initialized with CodeLlama-Python 7b and trained in MATH hours on MATH NVIDIA A100s.

13b was initialized with CodeLlama-Python 13b and trained in MATH hours on MATH NVIDIA A100s.

We used DeepSpeed Ulysses and Flash Attention to enable long context training.

@src https://arxiv.org/abs/2310.11511
@title Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection
@section Training the Critic Model

Manual annotation of reflection tokens for each segment is expensive .

A state-of-the-art LLM like GPT-4 can be effectively used to generate such feedback .

However, depending on such proprietary LMs can raise API costs and diminish reproducibility

We create supervised data by prompting GPT-4 to generate reflection tokens and then distill their knowledge into an in-house .

For each group of reflection tokens, we randomly sample instances from the original training data: MATH .

As different reflection token groups have their own definitions and input, as shown in Table , we use different instruction prompts for them. Here, we use as an example. We prompt GPT-4 with a type-specific instruction ("Given an instruction, make a judgment on whether finding some external documents from the web helps to generate a better response.") followed by few-shot demonstrations MATH the original task input MATH and output MATH to predict an appropriate reflection token as text: MATH .

Manual assessment reveals that GPT-4 reflection token predictions show high agreement with human evaluations.

We collect 4k-20k supervised training data for each type and combine them to form training data for .

Appendix Section shows the full list of instructions, and contains more details and our analysis.

After we collect training data MATH , we initialize with a pre-trained LM

and train it on MATH using a standard conditional language modeling objective, maximizing likelihood:

Though the initial model can be any pre-trained LM, we use the same one as the generator LM (i.e., Llama 2-7B; ) for initialization.

The critic achieves a higher than 90% agreement with GPT-4-based predictions on most reflection token categories (Appendix Table ).

@src https://arxiv.org/abs/2310.11511
@title Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection
@section Training the Generator Model

Given an input-output pair MATH , we augment the original output MATH using the retrieval and critic models to create supervised data that precisely mimics the inference-time process (Section ).

For each segment MATH , we run to assess whether additional passages could help to enhance generation.

If retrieval is required, the retrieval special token =Yes is added, and retrieves the top MATH passages, MATH .

For each passage, further evaluates whether the passage is relevant and predicts .

If a passage is relevant, further evaluates whether the passage supports the model generation and predicts .

Critique tokens and are appended after the retrieved passage or generations.

At the end of the output, MATH (or MATH ), predicts the overall utility token , and an augmented output with reflection tokens and the original input pair is added to MATH .

See the example training data in Figure .

We train the generator model by training on the curated corpus augmented with reflection tokens MATH using the standard next token objective:

Unlike training (Eq. ), learns to predict the target output as well as the reflection tokens.

During training, we mask out the retrieved text chunks (surrounded by <p> and </p> in Figure ) for loss calculation and

expand the original vocabulary MATH with a set of reflection tokens MATH .

Connections to prior work on learning with critique.

incorporates additional critique (feedback) during training, e.g., RLHF ( ) via PPO.

While PPO relies on separate reward models during training, we compute critique offline and directly insert them into the training corpus, where the generator LM is trained with a standard LM objective. This significantly reduces training costs compared to PPO.

Our work also relates to prior work that incorporates special tokens to control generation . Our learns to generate special tokens to evaluate its own prediction after each generated segment,

enabling the use of a soft re-ranking mechanism or hard constraints at inference (discussed next).

@src https://arxiv.org/abs/2310.11511
@title Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection
@section Training

Algorithm provides a high-level overview of our training.

To sample diverse input-output pairs, we sample instances of the Open-Instruct dataset. In particular, we use their ShareGPT, GPT-4 Alpaca, Alpaca, OpenAssistant, and FLAN subsets subsets.

We also sample instances from a couple of knowledge-intensive datasets, Natural Questions , Wizard of Wikipedia and FEVER from the KILT benchmark , ASQA and multiple QA datasets including ARC-Easy and OpenBookQA .

Table shows the full list of training instances, and in total, we use 145,619 instances.

We evaluate the accuracy of reward predictions by splitting GPT-4 generated feedback into training, development, and test sets.

The accuracy of the reward model is as follows. Table shows the model performance of predicting GPT-4 judgments.

As you can see, overall our fine-tuned reward model shows high prediction matching with GPT-4 predicted feedback.

While our final model uses Llama2-7B as a base LM, we also train and compare FLAN-3B model on the same data, to investigate the effectiveness of different data sizes affect final reward predictions.

In most aspects, our reward model shows higher than 80% accuracy, indicating the powerful ability of fine-tuned specialized LMs to evaluate text. While both models show relatively lower performance on , this is because both models often confuse between the two highest cases (5 and 4), where human annotators can also disagree.

Here, we provide detailed data creation procedures.

Here we set MATH to MATH for simplification.

Once we train the critic model, we first run it on input data from the aforementioned datasets, to predict whether retrieval is needed or not. For the instances where the critic predicts =No, we only predict the given input and output. For the instances where the critic predicts =Yes, we first retrieve passages using the input and the entire output as queries, to find passages that are relevant to the entire output. We then split output sentences using Spacy. (https://spacy.io/

For each sentence, we run to predict whether the retrieval is necessary or not, given the input, preceding segments, and the initial retrieved passage.

If predicts =No, then do not insert any paragraph at the MATH th segment.

If predicts =Yes, then we use the original input and the MATH th segment as a retrieval query to find relevant passages for the MATH -th segment. For each retrieved passage, we predict and .

If there is any passage and continuation with =Relevant and =Fully Supported / =Partially Supported, then we sample it as the continuation. If there is more than one passage satisfying this criterion, we use the one with the highest retrieval score.

If there are only =Irrelevant or =No Support passages, we randomly sample one passage.

Table show several training examples used for training.

@src https://arxiv.org/abs/2310.11511
@title Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection
@section More Details of Training

More details of training and computations.

We use 4 Nvidia A100 with 80GB memory to train our models. All models are trained for 3 epochs with a batch size of 128, a peak learning rate of 2e-5 with 3% warmup steps, and linear decay afterward. We set the maximum token length to be 2,048 for the 7B model, and 1,524 for the 13B model due to the memory constraint. We use Deepspeed stage 3 to conduct multi-GPU distributed training, with training precision Bfloat16 enabled. FlashAttention is used to make the long-context training more efficient.

We run inference of our trained models using 1-2 Quadro RTX 6000 GPUs with 24GB memory.

@src https://arxiv.org/abs/2407.10671
@title Qwen2 Technical Report
@section Pre-training Data

The pre-training of the Qwen2 models involves the development of a new, large-scale, high-quality multilingual dataset.

This dataset represents an improvement over the corpora used in previous Qwen and Qwen1.5 models , enhancing the scale, quality, and diversity of the pre-training data in several key areas:

The filtering algorithm has been refined with additional heuristic and model-based methods, including the use of the Qwen models to filter out low-quality data.

Moreover, these models are utilized to synthesize high-quality pre-training data.

Compared to Qwen1.5 , we have collected a significantly larger volume of high-quality code, mathematics, and multilingual data, enhancing the model's capabilities in respective areas.

This new dataset supports approximately 30 languages, such as English, Chinese, Spanish, French, German, Arabic, Russian, Korean, Japanese, Thai, and Vietnamese.

To ensure the model learns the distribution akin to human-like learning, we conduct experiments on scaled-down models to optimize the mixing of data from various sources and domains.

Based on these enhancements, the pre-training data was expanded from 3 trillion tokens in Qwen1.5 to 7 trillion tokens.

An attempt to further relax the quality threshold resulted in a 12 trillion token dataset.

However, the model trained on this dataset did not show a significant performance improvement over the 7 trillion token model.

It is suspected that increasing the volume of data does not necessarily benefit model pre-training.

Considering training costs, we opted to use the higher-quality 7 trillion token dataset for training larger models, leaving further exploration for future model iterations.

All Qwen2 dense models, excluding Qwen2-0.5B, were pre-trained on this large-scale dataset of over 7 trillion tokens.

Qwen2-0.5B were pre-trained using the 12 trillion token dataset.

The MoE model received an additional 4.5 trillion tokens of pre-training, in line with the principle of upcycling.

Similar to previous Qwen models, high-quality multi-task instruction data is integrated into the Qwen2 pre-training process to enhance in-context learning and instruction-following abilities.

@src https://arxiv.org/abs/2407.10671
@title Qwen2 Technical Report
@section Long-context Training

To enhance the long-context capability of Qwen2, we augmented the context length from 4,096 tokens to 32,768 tokens during the concluding phase of pre-training.

This expansion was complemented by the introduction of a significantly increased volume of high-quality, lengthy data.

In conjunction with these enhancements, we modified the base frequency of RoPE from 10,000 to 1,000,000 to optimize performance in long-context scenarios .

To fully leverage the model's length extrapolation potential, we adopted the YARN mechanism and the Dual Chunk Attention mechanism .

These strategies enable the model to process sequences of up to 131,072 tokens while maintaining high performance, as evidenced by minimal perplexity degradation in preliminary experiments.

@src https://arxiv.org/abs/2407.10671
@title Qwen2 Technical Report
@section Post-training

Following extensive large-scale pre-training, we engage in a post-training phase for Qwen2.

This process is pivotal in enhancing its proficiency across a broad spectrum of domains, including coding, mathematics, logical reasoning, instruction following, and multilingual comprehension.

Moreover, it ensures that the generation from the models is in harmony with human values, making it helpful, honest, and harmless.

Unlike traditional methods that heavily rely on extensive human supervision, our approach focuses on scalable alignment with minimal human annotation .

Specifically, we investigate methods to acquire high-quality demonstration and preference data for Supervised Fine-Tuning (SFT) and Reinforcement Learning from Human Feedback (RLHF), aiming to minimize the need for human labeling while maximizing the quality and reliability of the data.

@src https://arxiv.org/abs/2407.10671
@title Qwen2 Technical Report
@section Post-training Data

The post-training data primarily consists of two components: demonstration data MATH and preference data MATH , where MATH represents the instruction, MATH represents a satisfactory response, and MATH and MATH are two responses to MATH , with MATH being the preferred choice over MATH .

The set MATH is utilized in SFT, whereas MATH is employed in RLHF.

The construction of training data entails a two-step process: collaborative data annotation and automated data synthesis.

First, we extract the data ontology from large-scale instruction corpora, leading to a broad and diverse set of high-quality instructions.

These instructions are systematically enhanced to incorporate greater complexity.

Through human annotation, we obtain the target response MATH and their positive and negative counterparts MATH .

Subsequently, a variety of automated alignment strategies are employed to synthesize a substantial volume of artificially annotated data across the domains of code, mathematics, instruction-following, creation, role-playing, and safety.

@src https://arxiv.org/abs/2408.00714
@title SAM 2: Segment Anything in Images and Videos
@section Model architecture ablations

In this section, we present model ablations that guided design decisions, conducted under a smaller model setup with 512 input resolution by default. For each ablation setting, we report segmentation accuracy for video ( ) and image (mIoU) tasks, and its relative video segmentation speed (the maximum inference throughput relative to the ablation default setup in lightgray gray ).

We find design choices for image and video components to be largely decoupled – this can be attributed to our modular design and training strategy.

@src https://arxiv.org/abs/2408.00714
@title SAM 2: Segment Anything in Images and Videos
@section Memory architecture ablations

Recurrent memory. We investigate the effectiveness of feeding the memory features to a GRU before adding them to the memory bank. Similar to sec:ablation_pos_enc , we also evaluate on LVOSv2 as an additional benchmark for long-term object segmentation. While prior works have commonly employed GRU states as a means of incorporating memory into the tracking process, our findings in tab:mem_enhance_ablation suggest that this approach does not provide an improvement (except slightly on LVOSv2). Instead, we find it sufficient to directly store the memory features in the memory bank, which is both simpler and more efficient.

Object pointers. We ablate the impact of cross-attending to the object pointer vectors from the mask decoder output in other frames (see sec:model ). The results presented in tab:mem_enhance_ablation show that while cross-attending to object pointers does not enhance average performance across the 9 zero-shot datasets, it significantly boosts performance on SA-V val dataset as well as on the challenging LVOSv2 benchmark (validation split). Hence, we default to cross-attending to object pointers together with the memory bank embeddings from the memory encoder.

@src https://arxiv.org/abs/2408.00714
@title SAM 2: Segment Anything in Images and Videos
@section Architecture

Here we discuss further architecture details, expanding on the model description in sec:model .

Image encoder. We use a feature pyramid network to fuse the stride 16 and 32 features from Stages 3 and 4 of the Hiera image encoder respectively to produce the image embeddings for each frame. In addition, the stride 4 and 8 features from Stages 1 and 2 are not used in the memory attention but are added to the upsampling layers in the mask decoder as shown in Figure , which helps produce high-resolution segmentation details. We follow in using windowed absolute positional embeddings in the Hiera image encoder. In , RPB provided positional information spanning across windows in the image encoder, in lieu of which we adopt a simpler approach of interpolating the global positional embedding instead to span across windows. We do not use any relative positional encoding. We train models with varying image encoder sizes – T, S, B+ and L. We follow and use global attention in only a subset of the image encoder layers (see tab:hyperparams ).

Memory attention. In addition to sinusoidal absolute positional embeddings, we use 2d spatial Rotary Positional Embedding (RoPE) in self-attention and cross-attention layers. The object pointer tokens are excluded from RoPE as they do not have specific spatial correspondence. By default, the memory attention uses MATH layers.

Prompt encoder and mask decoder. The prompt encoder design follows SAM, and we next discuss additional details on design changes in the mask decoder. We use the mask token corresponding to the output mask as the object pointer token for the frame, which is placed in the memory bank. As discussed in sec:model , we also introduce an occlusion prediction head. This is accomplished by including an additional token along with the mask and IoU output tokens. An additional MLP head is applied to this new token to produce a score indicating the likelihood of the object of interest being visible in the current frame (as shown in Figure ). In the memory bank, we also add a learned occlusion embedding to the memory features of those frames that are predicted to be occluded (invisible) by the occlusion prediction head.

SAM introduced the ability to output multiple valid masks when faced with ambiguity about the object being segmented in an image. For example, when a person clicks on the tire of a bike, the model can interpret this click as referring to only the tire or the entire bike and output multiple predictions. In videos, this ambiguity can extend across video frames. For example, if in one frame only the tire is visible, a click on the tire might relate to just the tire, or as more of the bike becomes visible in subsequent frames, this click could have been intended for the entire bike. To handle this ambiguity, SAM 2 predicts multiple masks at each step of the video. If further prompts do not resolve the ambiguity, the model selects the mask with the highest predicted IoU for the current frame for further propagation in the video.

Our memory encoder does not use an additional image encoder and instead reuses the image embeddings produced by the Hiera encoder, which are fused with the predicted mask information to produce memory features (as discussed in sec:model ). This design allows the memory features to benefit from the strong representations produced by the image encoder (especially when we scale the image encoder to a larger size). Further, we project the memory features in our memory bank to a dimension of 64, and split the 256-dim object pointer into 4 tokens of 64-dim for cross-attention to the memory bank.

When applying SAM 2 to segment multiple objects in the same video (such as multi-object tracking in the semi-supervised VOS evaluation), we perform inference on each object independently. More specifically, we share the visual features from the image encoder between all the objects in the video but run all the other model components (such as the memory bank and the mask decoder) separately for each object.

@src https://arxiv.org/abs/2408.00714
@title SAM 2: Segment Anything in Images and Videos
@section Pre-training

We first pre-train SAM 2 on static images on the SA-1B dataset. tab:pre-training-hparam details the settings used during pre-training on SA-1B – other settings not mentioned here follow . The image encoder is initialized from MAE pre-trained Hiera . Similar to SAM, we filter masks covering more than 90% of the image and restricted training to 64 randomly sampled masks per image.

Unlike SAM, we found it beneficial to use an MATH loss to more aggressively supervise the IoU predictions and to apply a sigmoid activation to the IoU logits to restrict the output into the range between 0 and 1. For multi-mask predictions (on the first click), we supervise the IoU predictions of all masks to encourage better learning of when a mask might be bad, but only supervise the mask logits with the lowest segmentation loss (linear combination of focal and dice loss). In SAM, during iterative sampling of points, two iterations were inserted with no additional prompts (only feeding the previous mask logits) – we do not add such iterations during our training and use 7 correction clicks (instead of 8 in SAM). We also employ horizontal flip augmentation during training and resize the image to a square size of 1024 MATH 1024.

We use AdamW and apply layer decay on the image encoder and follow a reciprocal square-root schedule . See tab:hyperparams (a) for the hyperparameters in our pre-training stage.

@src https://arxiv.org/abs/2408.00714
@title SAM 2: Segment Anything in Images and Videos
@section Full training

After pre-training, we train SAM 2 on our introduced datasets SA-V + Internal (section sec:dataset ), a 10% subset of SA-1B, and a mixture of open-source video datasets including DAVIS , MOSE , and YouTubeVOS .

Our released model is trained on SA-V manual + Internal and SA-1B.

SAM 2 is designed for two tasks; the PVS task (on videos) and the SA task (on images).

Training is done jointly on image and video data. To optimize our data usage and computational resources during training, we adopt an alternating training strategy between video data (multiple frames) and static images (one single frame). Specifically, in each training iteration, we sample a full batch either from the image or video dataset, with their sampling probabilities proportional to the size of each data source. This approach allows for a balanced exposure to both tasks and a different batch size for each data source to maximize compute utilization. Settings not explicitly mentioned here for the image task follow settings from the pre-training phase. See tab:hyperparams (b) for the hyperparameters in our full training stage. The training data mixture consists of MATH 15.2% SA-1B, MATH 70% SA-V and MATH 14.8% Internal. The same settings are used when open-source datasets are included, with the change that the additional data is included ( MATH 1.3% DAVIS, MATH 9.4% MOSE, MATH 9.2% YouTubeVOS, MATH 15.5% SA-1B, MATH 49.5% SA-V, MATH 15.1% Internal). When training on SA-V and other video datasets, we only use those manually annotated masklets (without adding automatically generated ones), which are sufficient to achieve strong performance based on our analyses.

We apply a series of data augmentations to the training videos (detailed in tab:hyperparams ), including random horizontal flips, random affine transforms, random color jittering, and random grayscale transforms, as listed in tab:hyperparams . We also adopt a mosaic transform to simulate challenging scenarios with multiple similar-looking objects – with 10% probability, we tile the same training video into a 2 MATH 2 grid and select a masklet from one of the 4 quadrants as the target object to segment. In this case, the model must focus on other cues like motion or temporal continuity to distinguish the target object from their identical-looking counterparts in other quadrants. In addition, the videos and objects in each quadrant are smaller in size (only half the original width and height) after this mosaic transform, which also facilitates learning to segment small objects.

We train by simulating an interactive setting, sampling 8-frame sequences and randomly selecting up to 2 frames (including the first) for corrective clicks. During training, we use ground-truth masklets and model predictions to sample prompts, with initial prompts being the ground-truth mask (50% probability), a positive click from the ground-truth mask (25%), or a bounding box input (25%).

We restrict the maximum number of masklets for each sequence of 8 frames to 3 randomly chosen ones. We reverse the temporal order with a probability of 50% to help generalization to bi-directional propagation. When we sample corrective clicks, with a small probability of 10%, we randomly sample clicks from the ground truth mask, irrespective of the model prediction, to allow additional flexibility in mask refinement.

Fine-tuning using 16-frame sequences. A potential shortcoming of the procedure above is that the model only sees sampled 8-frame sequences during training, which is relatively short compared to the full video length during inference. To alleviate this issue and further boost the segmentation quality on long videos, we introduce an extra fine-tuning stage where we sample 16-frame sequences on challenging videos (those videos with the highest number of edited frames, as described in app:sec:ann_guidelines ). More specifically, we sort our masklets by number of edited frames and only consider the top 50% most edited masklets for training, for both SA-V and Internal datasets. We still keep the complete versions of the OSS datasets (DAVIS, MOSE, and YouTubeVOS) in the training mix. We fine-tune for 50k iterations (1/3 of the original schedule) using half of the original learning rate and freeze the image encoder to fit the 16-frame sequence into the 80 GB memory of A100 GPUs.

Losses and optimization. We supervise the model's predictions using a linear combination of focal and dice losses for the mask prediction, mean-absolute-error (MAE) loss for the IoU prediction, and cross-entropy loss for object prediction with a ratio of 20:1:1:1 respectively. As during pre-training, for multi-mask predictions, we only supervise the mask with the lowest segmentation loss. If the ground-truth does not contain a mask for a frame, we do not supervise any of the mask outputs (but always supervise the occlusion prediction head that predicts whether there should exist a mask in the frame).

@src https://arxiv.org/abs/2408.06072
@title CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer
@section The Architecture

Figure illustrates the overall architecture.

Given a pair of video and text input, we design a 3D causal VAE to compress the video into the latent space, and the latents are then patchified and unfolded into a long sequence denoted as MATH .

Simultaneously, we encode the textual input into text embeddings MATH using T5 .

Subsequently, MATH and MATH are concatenated along the sequence dimension.

The concatenated embeddings are then fed into a stack of expert transformer blocks.

Finally, the model output are unpatchified to restore the original latent shape, which is then decoded using a 3D causal VAE decoder to reconstruct the video.

We illustrate the technical design of the 3D causal VAE and expert transfomer in detail.

@src https://arxiv.org/abs/2408.06072
@title CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer
@section Progressive Training

Videos from the Internet usually include a significant amount of low-resolution ones. And directly training on high-resolution videos is extremely expensive. To fully utilize data and save costs, the model is first trained on 256px videos to learn semantic and low-frequency knowledge. Then it is trained on gradually increased resolutions, from 256px to 512px, 768px, to learn high-frequency knowledge. To maintain the ability of generating videos with different aspect ratios, we keep the aspect ratio unchanged and resize the short side to above resolutions. Finally, we do a high-quality fine-tuning, See Appendix

Moreover, we trained an image-to-video model based on above model. See Appendix for details.

@src https://arxiv.org/abs/2408.06072
@title CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer
@section Training Details

Since the filtered pre-training data still contains a certain proportion of dirty data, such as subtitles, watermarks, and low-bitrate videos, we selected a subset of higher quality video data, accounting for 20% of the total dataset, for fine-tuning in the final stage. This step effectively removed generated subtitles and watermarks and slightly improved the visual quality. However, we also observed a slight degradation in the model's semantic ability.

Visualizing different rope interpolation methods

When adapting low-resolution position encoding to high-resolution, we consider two different methods: interpolation and extrapolation. We show the effects of two methods in Figure . Interpolation tends to preserve global information more effectively, whereas the extrapolation better retains local details. Given that RoPE is a relative position encoding, We chose the extrapolation to maintain the relative position between pixels.

We present the model and training hyperparameters in tab:hyper2 and tab:hyper .

@src https://arxiv.org/abs/2408.12528
@title Show-o: One Single Transformer to Unify Multimodal Understanding and Generation
@section Architecture

Show-o inherits the architecture of existing LLM without any architecture modifications except for prepending a QK-Norm operation to each attention layer. We initialize Show-o with the weights of a pre-trained LLM and expand the size of the embedding layer by incorporating 8,192 new learnable embeddings for discrete image tokens. Unlike state-of-the-art diffusion models that require an additional text encoder, Show-o inherently encodes text conditional information by itself for text-to-image generation.

Unified Prompting. To perform unified learning on multimodal understanding and generation, we design a unified prompting strategy to format various kinds of input data. Given an image-text pair MATH , it is first tokenized into MATH image tokens MATH and MATH text tokens MATH by the image and text tokenizer, respectively. We form them into an input sequence according to the type of task in the format illustrated in Fig. . Specifically, MATH and MATH are pre-defined task tokens that indicate the learning task for the input sequence. MATH and MATH serve as special tokens denoting the start and end of text tokens, respectively. Similarly, MATH and MATH are pre-defined special tokens marking the start and end of image tokens.

By employing this prompt design, we can effectively encode various input data for multi-modal understanding, text-to-image generation, and mixed-modality generation as sequential data. This setup enables unified learning to operate seamlessly within sequences across these various tasks. Once trained, we can accordingly prompt Show-o to handle various vision-language tasks including visual question answering and text-to-image generation (as shown in Fig. ).

Omni-Attention Mechanism. Different from existing works that model sequence auto-regressively only, we propose an omni-attention mechanism to enable Show-o to model various types of signals in distinct ways. It is a comprehensive attention mechanism with causal and full attention that adaptively mixes and changes according to the format of the input sequence. We illustrate omni-attention examples for different input sequences in Fig. . Specifically, Show-o model text tokens MATH within the sequence via causal attention. For image tokens MATH , Show-o processes them via full attention, allowing each token to comprehensively interact with all others. Given a formatted input sequence, it is apparent that in multimodal understanding (Fig. (a)), text tokens in a sequence can attend to all previous image tokens, and in text-to-image generation (Fig. (b)), image tokens are able to interact with all preceding text tokens. When given only text tokens, it degrades to causal attention (Fig. (c)).

Training Objectives. To perform both auto-regressive and (discrete) diffusion modeling, we employ two learning objectives: i) Next Token Prediction (NTP) and ii) Mask Token Prediction (MTP). Given a sequence with MATH image tokens MATH and MATH text tokens MATH for multimodal understanding, we maximize the likelihood of text tokens by employing the standard language modeling objective:

where MATH indicates the conditional probability which is modeled by the weights MATH of Show-o and stochastic gradient descent is used to train the model. Note that, if the input sequence involves only text tokens, there are no conditional terms on image tokens MATH .

With the proof in Appendix , we seamlessly integrate the simplified discrete diffusion modeling within Show-o by employing the mask token prediction as a learning objective. Hence, for modeling image tokens MATH within the input sequence, we first randomly replace the image tokens with the MATH token, notated as MATH , at a random ratio (controlling by a time step) to create a masked sequence MATH . An illustration can be found in Fig. . Next, we aim to reconstruct the original image token from the masked tokens conditioning on unmasked regions and preceding text tokens by maximizing the following likelihood:

Note that the loss is only applied to the masked tokens. Specifically, we follow the sampling strategy used by MaskGIT to mask image tokens and reconstruct them via the information from all text and unmasked image tokens within the input sequence. Following the classifier-free guidance introduced by , we randomly replace the conditioned text tokens using a null text "" with some probability.

Given a batch size of input sequences, the overall training loss is the combination of MATH and MATH :

where MATH is the hyper-parameter weighting the loss term MATH . The training schedule mainly involves three stages, and we provide more details in Appendix .

Inference Stage. In multimodal understanding, given an image accompanying visual questions, Show-o autoregressively predicts textual answers. In visual generation, we use all MATH tokens as initial input for Show-o, in which MATH tokens will be iteratively replaced by the predicted image tokens within MATH steps. More inference details are provided in Appendix .

@src https://arxiv.org/abs/2408.12528
@title Show-o: One Single Transformer to Unify Multimodal Understanding and Generation
@section Training Pipeline

Given that the embedding of image tokens is newly initialized, it necessitates large-scale pre-training to align for multimodal understanding and generation. Besides, Show-o eliminates the text encoder to extract text embeddings for text-to-image generation, which poses a significant challenge for achieving effective alignment between text and image content within one single transformer. To this end, we employ a three-stage approach to progressively and effectively train Show-o:

i) Image Token Embedding and Pixel Dependency Learning: We employ RefinedWeb dataset to train Show-o to maintain the language modeling ability. Meanwhile, ImageNet-1K dataset and large-scale image-text pairs are adopted to train Show-o for class-conditional image generation and image captioning, respectively. Here, we directly leverage the class names from ImageNet-1K as textual inputs for learning class-conditional image generation. This stage primarily involves the learning of new learnable embeddings for discrete image tokens, pixel dependency for image generation, and alignment between image and text for image captioning.

ii) Image-Text Alignment for Multimodal Understanding and Generation: Building upon the pre-trained weights, we proceed to involve training of text-to-image generation on the image-text data instead of the ImageNet-1K. This stage mainly focuses on image and text alignment for both image captioning and text-to-image generation.

iii) High-Quality Data Fine-tuning: Lastly, we further refine the pre-trained Show-o model by incorporating filtered high-quality image-text pairs for text-to-image generation and instructional data for multimodal understanding and mixed-modality generation.

@src https://arxiv.org/abs/2408.12528
@title Show-o: One Single Transformer to Unify Multimodal Understanding and Generation
@section Implementation Details

We initially conduct joint training of Show-o using the RefinedWeb, a collection of image-text pairs, and the ImageNet-1K for language modeling, image captioning, and class-conditional image generation, respectively, over 500K steps. Subsequently, we replace the class-conditional generation with the training for text-to-image generation using the around 35M image-text pairs for an additional 1,000K steps. The base model is trained on 48 A100 (80GB) GPUs with a total batch size of 1,152. We employ the AdamW optimizer with a weight decay of 0.01, 5,000 steps of warm-up, and an initial learning rate of 1e-4 with a cosine scheduling. Finally, we fine-tune Show-o with around 1M internal high-quality image-text pairs and adhere to the configuration of LLaVA-v1.5 for instruction data tuning. Note that, the current version of Show-o is based on Phi-1.5 . In the following experiment sections, the default Show-o employs discrete image tokens as input for both multimodal understanding and generation. Show-o MATH and Show-o MATH indicate the use of continuous image representations from the pre-trained MAGVIT-v2 and CLIP-ViT (corresponding to options (b) and (c) in Fig. ), respectively, for multimodal understanding and we discuss this exploration in Section .

Based on the pre-trained Show-o, we continue to train it on the 2.0B image-text pairs for 500K steps and then we increase the image resolution to MATH and train Show-o for an additional 500K steps. Finally, we fine-tune Show-o with around 1M internal high-quality image-text pairs and adhere to the configuration of LLaVA-v1.5 for instruction data tuning.

@src https://arxiv.org/abs/2410.18072
@title WorldSimBench: Towards Video Generation Models as World Simulators
@section Experiments on We demonstrate the strong capabilities and generalization of by comparing it with GPT-4o , showcasing its applicability for , as shown in Tab. . We use accuracy (Acc) in to assess the alignment of the model with human preferences, given the scoring range of 1-2. In contrast, we employ Pearson linear correlation coefficient (PLCC) for and as their scores range from 1-5.

After fine-tuning on , our evaluator consistently surpasses the performance of GPT-4o in terms of alignment with human preferences across all scenarios. Additionally, we conducted zero-shot experiments with two challenging models, OpenSora and Lavie. GPT-4o exhibits a negative correlation with human preferences in evaluating OpenSora in under zero-shot setting, as well as evaluating Lavie in under zero-shot setting. Our evaluator's zero-shot performance shows a high correlation with human preferences, further demonstrating its robust generalization capabilities. is suitable for , and the can be leveraged to train even more aligned models for assessing video generation models towards World Simulators. More details in Sup. .

@src https://arxiv.org/abs/2410.18072
@title WorldSimBench: Towards Video Generation Models as World Simulators
@section Detaild Implementation of

Tab. provides an analysis of the . In scenario, there are only five instructions: move forward, move backward, turn left, turn right, and stop. The other two scenarios include a variety of instructions that combine actions with target objects. Given the diverse instructions, different video generation models generate multiple videos after finetuning on specific datasets. To enhance the understanding of the autonomous driving context, we also supplement the scenario with videos from real-world scenes. Additionally, we list the quantities of positive and negative samples across all dimensions. Samples with human annotated scores of 3 or higher in and are considered positive. Leveraging with comprehensive embodied dimensions, we train the to enable efficient assessment in .

@src https://arxiv.org/abs/2412.08821
@title Large Concept Models: Language Modeling in a Sentence Representation Space
@section Our baseline architecture for next-concept prediction is a standard decoder-only Transformer that transduces a sequence of preceding concepts (read sentence embeddings) into a sequence of future ones.

As illustrated in fig:archi:baselcm , the is equipped with a " MATH " and a " MATH ". The MATH normalizes the input embeddings and maps them to the model's hidden dimension MATH .

In order to learn the maps " MATH " and its inverse " MATH " we fit a robust scaler to a set of randomly sampled vectors from different corpora and domains of text data. This scaler removes the median statistics and scales the data according to the interquartile range (IQR).

The is trained on the semi-supervised task of next concept prediction, that is, the model predicts the next concept MATH and its parameters MATH are optimized to regress the ground truth next concept ( MATH ).

Given a data distribution MATH of documents (sequences of concepts), the training loss is evaluated as:

In order to enable the generation of variable length documents at inference time, we suffix training documents with the sentence "End of text.". Similar to any sentence in the document, this special suffix will be encoded with . This means that MATH . During inference, we implement two main early stopping mechanisms: the first one measures the similarity of the generated embedding MATH to MATH and stops if the cosine similarity exceeds a threshold MATH . The second mechanism compares the newly generated embedding MATH to the previous generation MATH and stops if their cosine similarity is higher than a threshold MATH . We set both MATH and MATH to 0.9.

@src https://arxiv.org/abs/2412.08821
@title Large Concept Models: Language Modeling in a Sentence Representation Space
@section Quantized Two major approaches currently stand to deal with continuous data generation in the image or speech generation fields: one is diffusion modeling, the other is learning quantization of the data before modeling on top of these discrete units.

In addition, the text modality remains discrete, and despite dealing with continuous representations in the SONAR space, all possible text sentences (of less than a given number of characters) are a cloud of points rather than a real continuous distribution in the SONAR space.

These considerations motivate the exploration of quantization of SONAR representations and then modeling on these discrete units to address the next sentence prediction task. Finally, following such an approach enables the natural use of temperature, top-p or top-k sampling, to control the level of randomness and diversity in the sampling of the next sentence representation.

In this section, we learn residual quantizers for the SONAR space, and then build a Quantized based on these discrete units. We tried to come up with an architecture as close as the diffusion models, to be able to compare approaches.

Quantization of SONAR space. We use Residual Vector Quantization (RVQ; ) as a coarse-to-fine quantization technique to discretize SONAR representations. Vector quantization maps continuous input embeddings to the nearest entry in a learnt codebook. RVQ iteratively quantize residual errors from previous quantizations using additional codebook for each iteration. We use FAISS implementation

which performs iterative k-means clustering of residuals. We use the Improved Residual Vector Quantization (IRVQ) method from , with a beam size of 1 for memory efficiency. We trained the RVQ codebooks on 15 million English sentences extracted from Common Crawl using MATH number of quantizers with MATH units per codebook.

One property of RVQ is that the cumulative sum of centroid embeddings of the first codebooks are an intermediate coarse approximation of input SONAR vectors. In that way, we can report the evolution of auto-encoding BLEU scores with the increasing number of codebooks used to quantize SONAR embeddings, before using the SONAR text decoder to decode quantized embeddings. We notice in fig:auto_bleu_quant that auto-encoding BLEU consistently improves as the number of codebooks increases , reaching around 70% of the auto-encoding BLEU score achieved with continuous SONAR embeddings, when using all 64 codebooks.

Finetuning the SONAR decoder on quantized representations.

We fine-tuned SONAR decoder on quantized representations to adjust it for the space created by the quantizers on 1.2M English sentences.

To make the decoder more robust against residual representations from intermediate codebooks, we randomly select a codebook number MATH during fine-tuning, with probability MATH , and use the quantized representation with codebooks up to MATH .

fig:auto_bleu_quant shows the improvement in auto-encoding performance when the decoder is adapted to quantized representations.

In the same spirit of diffusion , we aim at coarse-to-fine generation of embeddings conditioned on left-context sentences. However, we do not follow a denoising task as in diffusion modeling, but an iterative generation of embeddings based on intermediate quantized representations instead. In order to generate a embedding conditioned on left-context sentences, the model starts with the intermediate representation as a vector filled with zeros. We iteratively add to this intermediate representation the predicted residual centroid embeddings. In that way, the predicted embeddings are iteratively refined based on the growing cumulative sum of centroid embeddings of first codebooks, until all codebooks have been seen. We used the architecture for experiments even though it could be trained with architecture too. Compared to the diffusion , noisy input representations are replaced with intermediate quantized representations and diffusion timestep embeddings as input are replaced by codebook index embeddings.

Following previous work on modeling discrete units from residual quantizers , a Quant-LCM can be trained to predict the unit from the next codebook, parameterized with a softmax output layer. For parameter efficiency, we do not use MATH unique indices as discrete targets which would imply MATH output dimensions, but only MATH output dimensions while inputting the information of the codebook index to the model. At training time, similarly to diffusion training, we randomly sample codebook index MATH between 1 and MATH , and compute the cumulative sum of centroid embeddings of the first MATH codebooks as input. We use the unit from codebook MATH of the target embedding as target index for cross entropy loss computation. At inference time, we iteratively predict the unit from the next codebook, get the corresponding centroid embedding and add it to the current intermediate representation as additional predicted residual embedding. Finally, we also enable classifier-free guidance on logits at inference time

by randomly dropping left-context conditioning during training as previously described in sec:arch:interleaved . This modeling approach with discrete targets is dubbed in the following sections. The improved SONAR decoder for quantized representations is used to bridge the compression gap coming from SONAR quantization in following ablation studies when using .

We also explored a modeling approach that predicts continuous target SONAR vectors based on left-context sentences and intermediate quantized representation of the target vector, minimizing the Mean Squared Error between prediction and target embeddings. At inference time, we can either iteratively add the closest centroid embedding based on the predicted residual MATH or sample a centroid MATH from the following distribution:

where MATH is a temperature hyper-parameter. This modeling approach with continuous targets is denoted with in the following sections.

@src https://arxiv.org/abs/2412.08821
@title Large Concept Models: Language Modeling in a Sentence Representation Space
@section Inference efficiency of We compare in this section the inference computational cost of the to that of a vanilla LLM as a function of the total length in tokens of the prompt and output combined. We chose the theoretical number of FLOPs, independent of any specific optimization. These optimizations are generic to the transformer architecture and also apply to our .

We include in this comparison two configurations of ; the 1.6B used in the previous ablation studies and a 7B model we scale up to in the following sections. For both , we estimate the inference cost with inference sample steps MATH .

Given the quadratic complexity of the attention mechanism in transformers, the complexity sharply increases with the context size (see upper right corner of fig:ablation:flops 's left panel).

The complexity of the depends on how the context is sentencized: a context length of 200 tokens split into 10 sentences (20 tokens each) will incur a higher cost than the same 200 tokens split into 5 sentences (40 tokens each). We account for this by computing the cost on a range of sentence lengths but report the total context size on the x-axis (context size = sentence length MATH number of sentences).

The shows substantially better scalability with respect to increasing context size. The inference computational cost of the includes the three steps of (1) encoding into , (2) prediction in the sentence space then (3) decoding with a decoder. The inference cost of varies significantly depending on the average length in tokens per sentence.

For extremely short sentences (less than 10 tokens), an is more computationally efficient (see lower left corner of fig:ablation:flops 's right panel).

@src https://arxiv.org/abs/2412.08821
@title Large Concept Models: Language Modeling in a Sentence Representation Space
@section Methodology

In order to evaluate this single-model approach, we perform an ablation study. As a baseline method, we train a (cf. sec:arch:interleaved ) without any visibility to break or plan concepts. We then subsequently train a with the same number of parameters as the baseline. Both models were trained on the same data (Compared to previous experiments, we use a different data mixture more favorable for long-form generation. for the same number of steps.

In order to represent break concepts, we begin by first segmenting the data into paragraphs.

Given that most real world datasets are absent of paragraph structure (or it is not easy to recover),

we apply the Segment Any Text paragraph splitting API (https://github.com/segment-any-text/wtpsplit .

We additionally force each paragraph to be less than 10 sentences, and merge small (e.g. one sentence) consecutive paragraphs together.

In order to represent plan concepts, we generate synthetic high-level topic description for each preceding segmented paragraph using an existing open-sourced , namely Llama-3.1-8B-IT,

which offers a good trade-off between the generated topic quality and the generation speed.

The system prompt used to generate these topic descriptions is listed in sec:prompt_generation_of_topic_descriptions .

paragraphs with topic descriptions, spanning MATH segmented concepts (i.e. approximately MATH tokens).

Metrics. We focus on coherence as our main measure of evaluation. Previous ablations (cf. sec:archi:lcm:ablations ) used the coherence metric introduced by . However, we explore here -as-a-judge as an alternative. Specifically, we use Llama-3.1-8B-IT in order to evaluate the coherence of the generated model outputs, which is prompted to return an overall coherence score between MATH .

The prompt used is listed in sec:prompt_llm_as_a_judge_coherence .

In order to validate this prompt, we evaluate it against a dataset of human judgements introduced by , and observed it reported an agreement (Krippendorff's MATH = 0.48 with human annotators which improves upon their coherence model. We therefore choose this metric for our evaluation.

To be consistent across both model results, we do not include the special break or plan concepts generated by the when calculating coherence scores.

@src https://arxiv.org/abs/2412.08821
@title Large Concept Models: Language Modeling in a Sentence Representation Space
@section Multilingual Most of the leading have been trained on texts in several languages. fig:archi:langs summarizes the coverage of several of them. Nevertheless, the pretraining data of these seems to be mainly English texts. For example, mentions that pretraining data contains significantly more English texts, requiring continued pre-training with multilingual data, out of which 34.6% is translated reasoning data.

There are also several efforts to train optimized on specific languages, e.g. LeoLM for German, (https://laion.ai/blog/leo-lm/ Fuano

for Italian , ALLaM for Arabic , and several models for Chinese: ErniBot, (http://research.baidu.com/Blog/index-view?id=183 Tongyi Qianwen, (https://www.alibabacloud.com/en/solutions/generative-ai or ChatGLM . Some adaptations of LLMs to a massive number of languages also exist. LOLA is a recent mixture-of-experts LLM supporting 160 languages, MALA-500 adapts LLaMA2 to 546 languages. However, such models typically face a trade-off between language coverage and other capabilities. For example, the Aya model , following instructions in 101 languages, was superseded by Aya-23 that exchanged some breadth for depth, focusing on 23 languages only. The LCM architecture, combining a language-agnostic model for knowledge and reasoning with potentially language-specialized encoders and decoders, is expected to exhibit this trade-off to a lesser extent.

@src https://arxiv.org/abs/2412.08821
@title Large Concept Models: Language Modeling in a Sentence Representation Space
@section Alternative architectures

Predicting the next state in the embedding space is a core idea of the Joint Embedding Predictive Architecture ( ) proposed by . This idea has been implemented for images (I-JEPA by ) and video (V-JEPA by ) as a self-supervised approach to learning representations. For language, equivalent models have not yet been explored.

Sentence embeddings for language modeling. For text completion, proposed a sentence-level language model operating by choosing the next sentence from a finite set of candidates. Their model demonstrated success in selecting appropriate continuations for short stories, but it has not been scaled to longer inputs or to fully generative outputs. studied a similar problem in the even more restrictive sentence ordered setting, but with a more thorough study of architectural choices. The INSET architecture solves the sentence infilling task by combining a denoising autoencoder that encodes sentences into fixed-size vectors and decodes them back and a bidirectional transformer that predicts the embedding of a missing sentence.

and used predicted next sentence embeddings in a fully generative setting, for summarization and generic language modeling, respectively. However, their architectures considered sentence-level connections only as an addition to the token-level connections across sentences, not as their replacement.

In a recent work of , the SentenceVAE architecture performs language modeling on the sentence level using a sentence encoder to prepare the inputs and a sentence decoder to produce the outputs. However, its input and output embedding spaces are not tied, so the inference is only possible by decoding each predicted sentence into text and then re-encoding it for adding it to the context.

Language modeling with diffusion. A series of more recent works tried adapting diffusion modeling, originally developed for continuous data, to the discrete text domain. The PLANNER architecture consists of a variational autoencoder for paragraphs and a diffusion model trained to predict latent autoencoder representations conditional on the textual context or on the class label. augmented a decoder-only language model with an encoded semantic proposal of the continuation text, with an easily guidable diffusion model predicting the embedding of the next proposal. A TEncDM model performs diffusion in the space of contextual token embeddings which are then decoded non-autoregressively.

Some applications of diffusion to sequence modeling have targeted the planning capabilities of the sequence models. Semformer proposed training transformers language models to plan several steps ahead by including special planning tokens, the representations of which are trained to be informative about the future tokens. applied discrete diffusion to language models as an alternative to autoregressive generation, more suitable for tasks that require multi-step planning. give an overview of applications of diffusion for planning tasks, but most of them are not concerned with the language domain.

Overall, while many of the previous works used hidden representations for language modeling or related tasks, all of them either relied on token-level inputs or outputs, or were not intented for generating texts of arbitrary length. The seems to be the first fully generative language model implemented fully in a highly semantic, reconstructable sentence representation space.

@src https://arxiv.org/abs/2412.13663
@title Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference
@section Training Settings

MLM We follow the Masked Language Modeling (MLM) setup used by MosaicBERT . We remove the Next-Sentence Prediction objective which introduces noticeable overhead for no performance improvement , and use a masking rate of 30 percent, as the original rate of 15 percent has since been shown to be sub-optimal .

Optimizer We use the StableAdamW optimizer , which improves upon AdamW by adding Adafactor-style update clipping as a per-parameter learning rate adjustment. StableAdamW's learning rate clipping outperformed standard gradient clipping on downstream tasks and led to more stable training. Hyperparameters details are given in Appendix .

Learning Rate Schedule During pretraining, we use a modified trapezoidal Learning Rate (LR) schedule , also known as Warmup-Stable-Decay (WSD) . After a short LR warmup, the trapezoidal schedule holds the LR constant for the majority of training, followed by a short LR decay. This schedule has been shown to match the performance of cosine scheduling with the benefit of enabling continual training on any checkpoint without cold restart issues . Unlike most trapezoidal schedules, we use a MATH LR decay , as we found it to outperform linear and cosine decay.

We trained ModernBERT-base at a constant LR of 8e-4 for 1.7 trillion tokens following a 3 billion token warmup. After a 2 billion token warmup, we trained ModernBERT-large at a LR of 5e-4 for 900 billion tokens. We rolled back and restarted training at 5e-5 for the remaining 800 billion tokens after large’s loss plateaued for a few hundred billion tokens at 5e-4.

Batch Size Schedule Batch size scheduling starts with smaller gradient accumulated batches, increasing over time to the full batch size. In ablations, this schedule accelerated training progress. We warmup the batch size from 768 to 4,608 over 50 billion tokens and from 448 to 4,928 over 10 billion tokens, for ModernBERT-base and -large, respectively, with an uneven token schedule so each batch size has the same number of update steps. Details are provided in Appendix .

We initialize ModernBERT-base with random weights following the Megatron initialization . For ModernBERT-large, we follow the Phi model family (As detailed in their 2023 NeurIPS presentation. and initialize -large’s weights from ModernBERT-base. In ablation runs, this consistently matched Phi's improved training results and greatly speed up the initial loss decrease of our model training (This initialization reduced the amount of batch size and LR warmup needed for ModernBERT-large . Details are provided in Appendix .

After training on 1.7 trillion tokens at a 1024 sequence length and RoPE theta of 10,000, we extend the native context length of ModernBERT to 8192 tokens by increasing the global attention layer’s RoPE theta to 160,000 and train for an additional 300 billion tokens. We first train at a constant lower learning rate (We only lowered the LR for ModernBERT-base, as large already decreased LR during the 1024 token training phase. of 3e-4 for 250 billion tokens on an 8192 token mixture of the original pretraining dataset sampled following . Next, we upsample higher-quality sources following and conduct the decay phase with a MATH LR schedule over 50 billion tokens. This context extension process yielded the most balanced model on downstream tasks, as most of our ablations using only one of these strategies resulted in a performance loss on either retrieval or classification tasks.

@src https://arxiv.org/abs/2412.13663
@title Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference
@section Training Settings

Detailed training settings can be found in Table .

During training we used MNLI as a live evaluation, along with validation loss and token accuracy metrics on a 500 million randomly sampled sequences from the source datasets.

We use https://github.com/composer/composer Composer as our training framework and

https://github.com/search?q=optimi&type=repositories optimī for our optimizer implementations.

@src https://arxiv.org/abs/2412.13663
@title Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference
@section Architecture ablations

To select the updates to add in the ModernBERT architecture, we performed different ablations, except where stated, most ablations where ran at the 8-20 billion token scale:

We compared two GLU layers, GeGLU and SwiGLU. We find close to no difference between the two and choose to use GeGLU layers.

Using different percentage of the head dimension for the RoPE dimension (50, 75, 100). Lower percentages gave slightly better results. However, the observed difference was minimal. As the ablations were conducted at a considerably smaller scale than the final training, we choose to err on the side of caution and opt to keep the dimension at 100 % to avoid potentially hindering the capabilities of the fully trained models.

Both LayerNorm and RMSNorm yielded very similar results. While RMSNorm is theoretically faster, at the time this work was conducted, PyTorch did not have a native RMSNorm implementation, leading to eager-mode RMSNorm being the default implementation used for many users. To ensure ModernBERT has the highest possible out-of-the-box efficiency, we choose to use LayerNorm in the final models.

We investigated using parallel attention to compute the MLP and attention matrices at the same time, which has been shown to increase processing speeds for larger model sizes . However, for models within our targe sizes and pre-training sequence length, the speed-up we observed was minimal while we encountered significant degradation in downstream performance. As such, we do not use parallel attention. It is however possible that larger encoders and/or larger sequence lengths might see a different trade-off.

We explored the use of alternating global/local attention, with global attention every 3 layers and local attention over a 128 token sliding window otherwise. This setup yielded identical downstream performance when compared to the use of global attention in every layer, even at 100 billion tokens, while resulting in major speedups.

We experimented with multiple tokenizers, before selecting our final one, based on a modified OLMo tokenizer, which performed the best out of the recent tokenizers evaluated. Tokenizers from the BERT and RoBERTa generation of encoder models had competitive downstream performance on MNLI, but we theorized that their lack of recent training data and lack of code support would hinder downstream applications. Interestingly, we observed significant downstream performance degradation when using the Llama 2 tokenizer.

@src https://arxiv.org/abs/2501.12948
@title DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
@section Training Details of the First RL Stage

In the first stage of RL, we set the learning rate to 3e-6, the KL coefficient to 0.001, the GRPO clip ratio MATH to 10, and the sampling temperature to 1 for rollout. For each question, we sample 16 outputs with a maximum length of 32,768. Each training step consists of 32 unique questions, resulting in a training batch size of 512 per step. Every 400 steps, we replace the reference model with the latest policy model. To accelerate training, each rollout generates 8,192 outputs, which are randomly split into 16 minibatches and trained for only a single inner epoch. However, to mitigate the issue of language mixing, we introduce a language consistency reward during RL training, which is calculated as the proportion of target language words in the CoT.

Although ablation experiments in Supplementary show that such alignment results in a slight degradation in the model's performance, this reward aligns with human preferences, making it more readable. We apply the language consistency reward to both reasoning and non-reasoning data by directly adding it to the final reward.

Note that the clip ratio plays a crucial role in training. A lower value can lead to the truncation of gradients for a significant number of tokens, thereby degrading the model's performance, while a higher value may cause instability during training.

@src https://arxiv.org/abs/2501.12948
@title DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
@section Training Details of the Second RL Stage

Specifically, we train the model using a combination of reward signals and diverse prompt distributions. For reasoning data, we follow the methodology outlined in DeepSeek-R1-Zero, which employs rule-based rewards to guide learning in mathematical, coding, and logical reasoning domains. During the training process, we observe that CoT often exhibits language mixing, particularly when RL prompts involve multiple languages.

For general data, we utilize reward models to guide training. Ultimately, the integration of reward signals with diverse data distributions enables us to develop a model that not only excels in reasoning but also prioritizes helpfulness and harmlessness. Given a batch of data, the reward can be formulated as

The second stage of RL retains most of the parameters from the first stage, with the key difference being a reduced temperature of 0.7, as we find that higher temperatures in this stage lead to incoherent generation. The stage comprises a total of 1,700 training steps, during which general instruction data and preference-based rewards are incorporated exclusively in the final 400 steps. We find that more training steps with the model based preference reward signal may lead to reward hacking, which is documented in Supplementary . The total training cost is listed in Supplementary .

@src https://arxiv.org/abs/2501.12948
@title DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
@section Conventional Post-Training Paradigm

Post-training has emerged as an essential step in refining pre-trained LLMs to meet specific performance goals and align with human expectations. A widely adopted two-stage post-training framework is SFT followed by RL .

Supervised Fine-Tuning refines a pre-trained LLM by training it on a curated dataset of input-output pairs tailored to specific tasks. The process employs a supervised learning objective, typically minimizing cross-entropy loss between the model’s predictions and labeled ground truth . For instance, in conversational applications, SFT might utilize dialogue datasets where desired responses are explicitly provided, enabling the model to adapt its outputs to predefined standards . SFT offers several compelling benefits. First, it achieves precise task alignment by leveraging high-quality examples, allowing the model to excel in domains such as customer support or technical documentation . Second, its reliance on pre-trained weights ensures computational efficiency, requiring fewer resources than training from scratch. Finally, the use of explicit input-output mappings enhances interpretability, as the model’s learning process is directly tied to observable data, minimizing the risk of erratic behavior . Despite its strengths, the performance of SFT hinges on the quality and diversity of the training dataset; narrow or biased data can impair the model’s ability to generalize to novel contexts . Additionally, SFT’s static nature—optimizing for fixed outputs—may fail to capture evolving human preferences or nuanced objectives. The labor-intensive process of curating high-quality datasets further complicates its scalability, as errors or inconsistencies in the data can propagate into the model’s behavior .

Following SFT, Reinforcement Learning further refines the LLM by optimizing its outputs against a reward signal. In this stage, the model interacts with an environment—often a reward model trained on human feedback—and adjusts its behavior to maximize cumulative rewards. A prominent instantiation of this approach is Reinforcement Learning from Human Feedback (RLHF), where the reward function encodes human preferences . RL thus shifts the focus from static supervision to dynamic optimization. Notably, RL reduces the need for extensive annotated resources; while SFT demands a fully labeled dataset for every input-output pair, RL can operate with a smaller set of human evaluations or a trained reward model, even rule-based reward model, significantly lowering the annotation burden.

The sequential application of SFT and RL combines their complementary strengths. SFT establishes a robust, task-specific baseline by grounding the model in curated examples, while RL refines this foundation to align with broader, human-centric objectives . For example, SFT might ensure grammatical accuracy in a dialogue system, while RL optimizes for engagement and brevity, as demonstrated in the development of InstructGPT . This hybrid approach has proven effective in producing models that are both precise and adaptable.

In this study, we demonstrate that the SFT stage may impede a model’s ability to explore and develop effective reasoning strategies. This limitation arises because human-provided responses, which serve as targets during SFT, are not always optimal for model learning; they often omit critical reasoning components such as explicit reflection and verification steps. To address this, enables direct exploration of reasoning patterns by the model itself, independent of human priors. The reasoning trajectories discovered through this self-exploration are subsequently distilled and used to train other models, thereby promoting the acquisition of more robust and generalizable reasoning capabilities.

@src https://arxiv.org/abs/2501.12948
@title DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
@section Training Cost

Regarding our research on , we utilized the A100 GPUs to prepare for the experiments with a smaller model (30B parameters). The results from this smaller model have been promising, which has allowed us to confidently scale up to 660B R1-Zero and R1.

For the training of , we employed 64*8 H800 GPUs, and the process required approximately 198 hours. Additionally, during the training phase of , we utilized the same 64*8 H800 GPUs, completing the process in about 4 days, or roughly 80 hours. To create the SFT datasets, we use 5K GPU hours. The details are shown in Table .

@src https://arxiv.org/abs/2503.14476
@title DAPO: An Open-Source LLM Reinforcement Learning System at Scale
@section Training Details

In this work, we focus specifically on mathematical tasks to evaluate our algorithm, which can be readily transferred to other tasks. We adopt the verl framework for training. We use naive GRPO as our baseline algorithm and estimate advantages using group reward normalization.

For hyper-parameters, we utilize the AdamW optimizer with a constant learning rate of , incorporating a linear warm-up over 20 rollout steps.

For rollout, the prompt batch size is 512 and we sample 16 responses for each prompt. For training, the mini-batch size is set to 512, i.e., 16 gradient updates for each rollout step. For Overlong Reward Shaping, we set the expected maximum length as 16,384 tokens and allocate additional 4,096 tokens as the soft punish cache. Therefore, the maximum number of tokens for generation is set to 20,480 tokens.

As for the Clip-Higher mechanism, we set the clipping parameter to 0.2 and to 0.28, which effectively balance the trade-off between exploration and exploitation.

For evaluation on AIME, we repeat the evaluation set for 32 times and report avg@32 for results stability. The inference hyperparameters of evaluation are set to temperature 1.0 and topp 0.7.

@src https://arxiv.org/abs/2503.14476
@title DAPO: An Open-Source LLM Reinforcement Learning System at Scale
@section Training Dynamics

Reinforcement learning on large language models is not only a cutting-edge research direction but also an intrinsically complex systems engineering challenge, characterized by the interdependence of its various subsystems. Modifications to any single subsystem can propagate through the system, leading to unforeseen consequences due to the intricate interplay among these components. Even seemingly minor changes in initial conditions, such as variations in data and hyperparameters, can amplify through iterative reinforcement learning processes, yielding substantial deviations in outcomes. This complexity often confronts researchers with a dilemma: even after meticulous analysis and well-founded expectations that a modification will enhance specific aspects of the training process, the actual results frequently diverge from the anticipated trajectory. Therefore, monitoring of key intermediate results during experimentation is essential for swiftly identifying the sources of discrepancies and, ultimately, for refining the system.

The Length of Generated Responses is a metric closely related to training stability and performance, as shown in subfig:length . The increase in length provides the model with a larger space for exploration, allowing more complex reasoning behaviors to be sampled and gradually reinforced through training. However, it is important to note that length does not always maintain a continuous upward trend during training. In some considerable periods, it can exhibit a trend of stagnation or even decline, which has also been demonstrated in . We typically use length in conjunction with validation accuracy as indicators to assess whether an experiment is deteriorating.

The Dynamics of Reward during training has always been one of the crucial monitoring indicators in reinforcement learning, as shown in subfig:reward . In the majority of our experiments, the trend of reward increase is relatively stable and does not fluctuate or decline significantly due to adjustments in experimental settings. This indicates that, given a reliable reward signal, language models can robustly fit the distribution of training set. However, we find that the final reward on the training set often exhibits little correlation with the accuracy on the validation set, which indicates overfitting to the training set.

The Entropy of the Actor Model and Generation Probability are related to the model's exploration capability and are key metrics that we closely monitor in our experiments. Intuitively, the model's entropy needs to be maintained within an appropriate range. An excessively low entropy indicates that the probability distribution is overly sharp, leading to a loss of exploration capability. Conversely, an excessively high entropy is often associated with issues of over-exploration such as gibberish and repetitive generation. For the generation probability, the situation is exactly the opposite. As demonstrated in sec:cliphigher , by applying the Clip-Higher strategy, we effectively addressed the issue of entropy collapse. In subsequent experiments, we find that maintaining a slow upward trend in entropy is conducive to the improvement of model performance, shown in subfig:entropy and subfig:prob .
