# conclusion corpus (45 sources)

@src https://arxiv.org/abs/1706.03762
@title Attention Is All You Need
@section Conclusion

In this work, we presented the Transformer, the first sequence transduction model based entirely on attention, replacing the recurrent layers most commonly used in encoder-decoder architectures with multi-headed self-attention.

For translation tasks, the Transformer can be trained significantly faster than architectures based on recurrent or convolutional layers. On both WMT 2014 English-to-German and WMT 2014 English-to-French translation tasks, we achieve a new state of the art. In the former task our best model outperforms even all previously reported ensembles.

We are excited about the future of attention-based models and plan to apply them to other tasks. We plan to extend the Transformer to problems involving input and output modalities other than text and to investigate local, restricted attention mechanisms to efficiently handle large inputs and outputs such as images, audio and video.

Making generation less sequential is another research goals of ours.

The code we used to train and evaluate our models is available at https://github.com/tensorflow/tensor2tensor.

Acknowledgements We are grateful to Nal Kalchbrenner and Stephan Gouws for

their fruitful comments, corrections and inspiration.

@src https://arxiv.org/abs/1804.07461
@title GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding
@section Conclusion

a platform and collection of resources for evaluating and analyzing natural language understanding systems.

We find that, in aggregate, models trained jointly on our tasks see better performance than the combined performance of models trained for each task separately.

We confirm the utility of attention mechanisms and transfer learning methods such as ELMo in NLU systems, which combine to outperform the best sentence representation models on the GLUE benchmark, but still leave room for improvement.

When evaluating these models on our diagnostic dataset, we find that they fail (often spectacularly) on many linguistic phenomena, suggesting possible avenues for future work.

In sum, the question of how to design general-purpose NLU models remains unanswered, and we believe that GLUE can provide fertile soil for addressing this challenge.

@src https://arxiv.org/abs/1810.04805
@title BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
@section Conclusion

Recent empirical improvements due to transfer learning with language models have demonstrated that rich, unsupervised pre-training is an integral part of many language understanding systems. In particular, these results enable even low-resource tasks to benefit from deep unidirectional architectures. Our major contribution is further generalizing these findings to deep bidirectional architectures, allowing the same pre-trained model to successfully tackle a broad set of NLP tasks.

Appendix for "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"

We organize the appendix into three sections:

Additional implementation details for BERT are presented in Appendix ;

Additional details for our experiments are presented in Appendix ; and

Additional ablation studies are presented in Appendix .

We present additional ablation studies for BERT including:

Ablation for Different Masking Procedures.

@src https://arxiv.org/abs/1906.08237
@title XLNet: Generalized Autoregressive Pretraining for Language Understanding
@section Conclusions

XLNet is a generalized AR pretraining method that uses a permutation language modeling objective to combine the advantages of AR and AE methods. The neural architecture of XLNet is developed to work seamlessly with the AR objective, including integrating Transformer-XL and the careful design of the two-stream attention mechanism.

XLNet achieves substantial improvement over previous pretraining objectives on various tasks.

@src https://arxiv.org/abs/1907.11692
@title RoBERTa: A Robustly Optimized BERT Pretraining Approach
@section Conclusion

We carefully evaluate a number of design decisions when pretraining BERT models.

We find that performance can be substantially improved by training the model longer, with bigger batches over more data; removing the next sentence prediction objective; training on longer sequences; and dynamically changing the masking pattern applied to the training data.

Our improved pretraining procedure, which we call , achieves state-of-the-art results on GLUE, RACE and SQuAD, without multi-task finetuning for GLUE or additional data for SQuAD.

These results illustrate the importance of these previously overlooked design decisions and suggest that BERT's pretraining objective remains competitive with recently proposed alternatives.

We additionally use a novel dataset, CC-News, and release our models and code for pretraining and finetuning at: https://github.com/pytorch/fairseq.

@src https://arxiv.org/abs/2003.10555
@title ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators
@section Conclusion

We have proposed replaced token detection, a new self-supervised task for language representation learning.

The key idea is training a text encoder to distinguish input tokens from high-quality negative samples produced by an small generator network.

Compared to masked language modeling, our pre-training objective is more compute-efficient and results in better performance on downstream tasks.

It works well even when using relatively small amounts of compute, which we hope will make developing and applying pre-trained text encoders more accessible to researchers and practitioners with less access to computing resources.

We also hope more future work on NLP pre-training will consider efficiency as well as absolute performance, and follow our effort in reporting compute usage and parameter counts along with evaluation metrics.

@src https://arxiv.org/abs/2005.12872
@title End-to-End Object Detection with Transformers
@section Conclusion

We presented , a new design for object detection systems based on transformers and bipartite matching loss for direct set prediction. The approach achieves comparable results to an optimized Faster R-CNN baseline on the challenging COCO dataset. is straightforward to implement and has a flexible architecture that is easily extensible to panoptic segmentation, with competitive results. In addition, it achieves significantly better performance on large objects than Faster R-CNN, likely thanks to the processing of global information performed by the self-attention.

This new design for detectors also comes with new challenges, in particular regarding training, optimization and performances on small objects. Current detectors required several years of improvements to cope with similar issues, and we expect future work to successfully address them for .

@src https://arxiv.org/abs/2005.14165
@title Language Models are Few-Shot Learners
@section Conclusion

We presented a 175 billion parameter language model which shows strong performance on many NLP tasks and benchmarks in the zero-shot, one-shot, and few-shot settings, in some cases nearly matching the performance of state-of-the-art fine-tuned systems, as well as generating high-quality samples and strong qualitative performance at tasks defined on-the-fly. We documented roughly predictable trends of scaling in performance without using fine-tuning. We also discussed the social impacts of this class of model. Despite many limitations and weaknesses, these results suggest that very large language models may be an important ingredient in the development of adaptable, general language systems.

@src https://arxiv.org/abs/2006.11239
@title Denoising Diffusion Probabilistic Models
@section Conclusion

We have presented high quality image samples using diffusion models, and we have found connections among diffusion models and variational inference for training Markov chains, denoising score matching and annealed Langevin dynamics (and energy-based models by extension), autoregressive models, and progressive lossy compression. Since diffusion models seem to have excellent inductive biases for image data, we look forward to investigating their utility in other data modalities and as components in other types of generative models and machine learning systems.

@src https://arxiv.org/abs/2009.03300
@title Measuring Massive Multitask Language Understanding
@section Conclusion

We introduced a new test that measures how well text models can learn and apply knowledge encountered during pretraining. By covering 57 subjects at varying levels of difficulty, the test assesses language understanding in greater breadth and depth than previous benchmarks.

We found that it has recently become possible for models to make meaningful progress on the test, but that state-of-the-art models have lopsided performance and rarely excel at any individual task. We also showed that current models are uncalibrated and have difficulty with tasks that require calculations. Worryingly, models also perform especially poorly on socially relevant subjects including morality and law.

Our expansive test can help researchers pinpoint important shortcomings of models, making it easier to gain a clearer picture of state-of-the-art capabilities. =-1

@src https://arxiv.org/abs/2010.11929
@title An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale
@section Conclusion

We have explored the direct application of Transformers to image recognition.

Unlike prior works using self-attention in computer vision, we do not introduce image-specific inductive biases into the architecture apart from the initial patch extraction step.

Instead, we interpret an image as a sequence of patches and process it by a standard Transformer encoder as used in NLP.

This simple, yet scalable, strategy works surprisingly well when coupled with pre-training on large datasets.

Thus, matches or exceeds the state of the art on many image classification datasets, whilst being relatively cheap to pre-train.

While these initial results are encouraging, many challenges remain.

One is to apply to other computer vision tasks, such as detection and segmentation.

Our results, coupled with those in , indicate the promise of this approach.

Another challenge is to continue exploring self-supervised pre-training methods.

Our initial experiments show improvement from self-supervised pre-training, but there is still large gap between self-supervised and large-scale supervised pre-training.

Finally, further scaling of would likely lead to improved performance.

@src https://arxiv.org/abs/2011.13456
@title Score-Based Generative Modeling through Stochastic Differential Equations
@section Conclusion

We presented a framework for score-based generative modeling based on SDEs. Our work enables a better understanding of existing approaches, new sampling algorithms, exact likelihood computation, uniquely identifiable encoding, latent code manipulation, and brings new conditional generation abilities to the family of score-based generative models.

While our proposed sampling approaches improve results and enable more efficient sampling, they remain slower at sampling than GANs on the same datasets. Identifying ways of combining the stable learning of score-based generative models with the fast sampling of implicit models like GANs remains an important research direction. Additionally, the breadth of samplers one can use when given access to score functions introduces a number of hyper-parameters. Future work would benefit from improved methods to automatically select and tune these hyper-parameters, as well as more extensive investigation on the merits and limitations of various samplers.

@src https://arxiv.org/abs/2101.03961
@title Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity
@section Conclusion

Switch Transformers are scalable and effective natural language learners.

We simplify Mixture of Experts to produce an architecture that is easy to understand, stable to train and vastly more sample efficient than equivalently-sized dense models.

We find that these models excel across a diverse set of natural language tasks and in different training regimes, including pre-training, fine-tuning and multi-task training.

These advances make it possible to train models with hundreds of billion to trillion parameters and which achieve substantial speedups relative to dense T5 baselines.

We hope our work motivates sparse models as an effective architecture and that this encourages researchers and practitioners to consider these flexible models in natural language tasks, and beyond.

The authors would like to thank Margaret Li who provided months of key insights into algorithmic improvements and suggestions for empirical studies.

Hugo Larochelle for sage advising and clarifying comments on the draft,

Irwan Bello for detailed comments and careful revisions,

Colin Raffel and Adam Roberts for timely advice on neural language models and the T5 code-base,

Yoshua Bengio for advising and encouragement on research in adaptive computation,

Jascha Sohl-dickstein for interesting new directions for stabilizing new large scale models and paper revisions, and the Google Brain Team for useful discussions on the paper.

Blake Hechtman who provided invaluable help in profiling and improving the training performance of our models.

@src https://arxiv.org/abs/2102.12092
@title Zero-Shot Text-to-Image Generation
@section Conclusion

We investigate a simple approach for text-to-image generation based on an autoregressive transformer, when it is executed at scale. We find that scale can lead to improved generalization, both in terms of zero-shot performance relative to previous domain-specific approaches, and in terms of the range of capabilities that emerge from a single generative model. Our findings suggest that improving generalization as a function of scale may be a useful driver for progress on this task.

@src https://arxiv.org/abs/2103.00020
@title Learning Transferable Visual Models From Natural Language Supervision
@section Conclusion

We have investigated whether it is possible to transfer the success of task-agnostic web-scale pre-training in NLP to another domain. We find that adopting this formula results in similar behaviors emerging in the field of computer vision and discuss the social implications of this line of research. In order to optimize their training objective, CLIP models learn to perform a wide variety of tasks during pre-training. This task learning can then be leveraged via natural language prompting to enable zero-shot transfer to many existing datasets. At sufficient scale, the performance of this approach can be competitive with task-specific supervised models although there is still room for much improvement.

@src https://arxiv.org/abs/2103.14030
@title Swin Transformer: Hierarchical Vision Transformer using Shifted Windows
@section Conclusion

This paper presents Swin Transformer, a new vision Transformer which produces a hierarchical feature representation and has linear computational complexity with respect to input image size. Swin Transformer achieves the state-of-the-art performance on COCO object detection and ADE20K semantic segmentation, significantly surpassing previous best methods. We hope that Swin Transformer’s strong performance on various vision problems will encourage unified modeling of vision and language signals.

As a key element of Swin Transformer, the shifted window based self-attention is shown to be effective and efficient on vision problems, and we look forward to investigating its use in natural language processing as well.

@src https://arxiv.org/abs/2105.05233
@title Diffusion Models Beat GANs on Image Synthesis
@section Conclusion

We have shown that diffusion models, a class of likelihood-based models with a stationary training objective, can obtain better sample quality than state-of-the-art GANs. Our improved architecture is sufficient to achieve this on unconditional image generation tasks, and our classifier guidance technique allows us to do so on class-conditional tasks. In the latter case, we find that the scale of the classifier gradients can be adjusted to trade off diversity for fidelity. These guided diffusion models can reduce the sampling time gap between GANs and diffusion models, although diffusion models still require multiple forward passes during sampling. Finally, by combining guidance with upsampling, we can further improve sample quality on high-resolution conditional image synthesis.

@src https://arxiv.org/abs/2106.09685
@title LoRA: Low-Rank Adaptation of Large Language Models
@section Conclusion and Future Work

Fine-tuning enormous language models is prohibitively expensive in terms of the hardware required and the storage/switching cost for hosting independent instances for different tasks.

We propose LoRA, an efficient adaptation strategy that neither introduces inference latency nor reduces input sequence length while retaining high model quality.

Importantly, it allows for quick task-switching when deployed as a service by sharing the vast majority of the model parameters.

While we focused on Transformer language models, the proposed principles are generally applicable to any neural networks with dense layers.

There are many directions for future works.

1) LoRA can be combined with other efficient adaptation methods, potentially providing orthogonal improvement.

2) The mechanism behind fine-tuning or LoRA is far from clear – how are features learned during pre-training transformed to do well on downstream tasks?

We believe that LoRA makes it more tractable to answer this than full fine-tuning.

3) We mostly depend on heuristics to select the weight matrices to apply LoRA to.

Are there more principled ways to do it?

4) Finally, the rank-deficiency of MATH suggests that MATH could be rank-deficient as well, which can also be a source of inspiration for future works.

@src https://arxiv.org/abs/2112.10752
@title High-Resolution Image Synthesis with Latent Diffusion Models
@section Conclusion

We have presented latent diffusion models, a simple and efficient way to significantly improve both the

training and sampling efficiency of denoising diffusion models without

degrading their quality. Based on this and our cross-attention

conditioning mechanism, our experiments could demonstrate favorable results

compared to state-of-the-art methods across a wide range of conditional image

synthesis tasks without task-specific architectures.

This work has been supported by the German Federal Ministry for Economic Affairs and Energy within the project ’KI-Absicherung - Safe AI for automated driving’ and by the German Research Foundation (DFG) project 421703927.

@src https://arxiv.org/abs/2201.03545
@title A ConvNet for the 2020s
@section Conclusions

In the 2020s, vision Transformers, particularly hierarchical ones such as Swin Transformers, began to overtake ConvNets as the favored choice for generic vision backbones. The widely held belief is that vision Transformers are more accurate, efficient, and scalable than ConvNets. We propose s , a pure ConvNet model that can compete favorably with state-of-the-art hierarchical vision Transformers across multiple computer vision benchmarks, while retaining the simplicity and efficiency of standard ConvNets. In some ways, our observations are surprising while our model itself is not completely new — many design choices have all been examined separately over the last decade, but not collectively. We hope that the new results reported in this study will challenge several widely held views and prompt people to rethink the importance of convolution in computer vision.

Acknowledgments. We thank Kaiming He, Eric Mintun, Xingyi Zhou, Ross Girshick, and Yann LeCun for valuable discussions and feedback.

In this Appendix, we provide further experimental details ( ), robustness evaluation results ( ), more modernization experiment results ( ), and a detailed network specification ( ). We further benchmark model throughput on A100 GPUs ( ). Finally, we discuss the limitations ( ) and societal impact ( ) of our work.

@src https://arxiv.org/abs/2201.11903
@title Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
@section Conclusions

We have explored chain-of-thought prompting as a simple and broadly applicable method for enhancing reasoning in language models.

Through experiments on arithmetic, symbolic, and commonsense reasoning, we find that chain-of-thought reasoning is an emergent property of model scale that allows sufficiently large language models to perform reasoning tasks that otherwise have flat scaling curves.

Broadening the range of reasoning tasks that language models can perform will hopefully inspire further work on language-based approaches to reasoning.

@src https://arxiv.org/abs/2201.12086
@title BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation
@section Conclusion

a new VLP framework with state-of-the-art performance on a wide range of downstream vision-language tasks,

including understanding-based and generation-based tasks.

pre-trains a multimodal mixture of encoder-decoder model using a dataset bootstrapped from large-scale noisy image-text pairs by injecting diverse synthetic captions and removing noisy captions.

Our bootstrapped dataset are released to facilitate future vision-language research.

There are a few potential directions that can further enhance the performance of :

(1) Multiple rounds of dataset bootstrapping;

(2) Generate multiple synthetic captions per image to further enlarge the pre-training corpus;

(3) Model ensemble by training multiple different captioners and filters and combining their forces in CapFilt.

We hope that our paper motivates future work to focus on making improvements in both the model aspect and the data aspect,

the bread and butter of vision-language research.

@src https://arxiv.org/abs/2203.11171
@title Self-Consistency Improves Chain of Thought Reasoning in Language Models
@section Conclusion and Discussion

We introduced a simple yet effective method called self-consistency, and observed that it significantly improves accuracy in a range of arithmetic and commonsense reasoning tasks, across four large language models with varying scales.

Beyond accuracy gains, self-consistency is also useful for collecting rationales when performing reasoning tasks with language models, and for providing uncertainty estimates and improved calibration of language model outputs.

One limitation of self-consistency is that it incurs more computation cost.

In practice people can try a small number of paths (e.g., 5 or 10) as a starting point to realize most of the gains while not incurring too much cost, as in most cases the performance saturates quickly (Figure ). As part of future work, one could use self-consistency to generate better supervised data to fine-tune the model, such that the model can give more accurate predictions in a single inference run after fine-tuning.

In addition, we observed that language models can sometimes generate incorrect or nonsensical reasoning paths (e.g., the StrategyQA example in Table , the two population numbers are not exactly correct), and further work is needed to better ground models' rationale generations.

@src https://arxiv.org/abs/2205.11487
@title Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding
@section Conclusions, Limitations and Societal Impact

showcases the effectiveness of frozen large pretrained language models as text encoders for the text-to-image generation using diffusion models. Our observation that scaling the size of these language models have significantly more impact than scaling the U-Net size on overall performance encourages future research directions on exploring even bigger language models as text encoders. Furthermore, through we re-emphasize the importance of classifier-free guidance, and we introduce dynamic thresholding, which allows usage of much higher guidance weights than seen in previous works. With these novel components, produces MATH samples with unprecedented photorealism and alignment with text.

Our primary aim with is to advance research on generative methods, using text-to-image synthesis as a test bed. While end-user applications of generative methods remain largely out of scope, we recognize the potential downstream applications of this research are varied and may impact society in complex ways. On the one hand, generative models have a great potential to complement, extend, and augment human creativity . Text-to-image generation models, in particular, have the potential to extend image-editing capabilities and lead to the development of new tools for creative practitioners. On the other hand, generative methods can be leveraged for malicious purposes, including harassment and misinformation spread , and raise many concerns regarding social and cultural exclusion and bias .

These considerations inform our decision to not to release code or a public demo. In future work we will explore a framework for responsible externalization that balances the value of external auditing with the risks of unrestricted open-access.

Another ethical challenge relates to the large scale data requirements of text-to-image models, which have have led researchers to rely heavily on large, mostly uncurated, web-scraped datasets.

While this approach has enabled rapid algorithmic advances in recent years, datasets of this nature have been critiqued and contested along various ethical dimensions. For example, public and academic discourse regarding appropriate use of public data has raised concerns regarding data subject awareness and consent . Dataset audits have revealed these datasets tend to reflect social stereotypes, oppressive viewpoints, and derogatory, or otherwise harmful, associations to marginalized identity groups .

Training text-to-image models on this data risks reproducing these associations and causing significant representational harm that would disproportionately impact individuals and communities already experiencing marginalization, discrimination and exclusion within society. As such, there are a multitude of data challenges that must be addressed before text-to-image models like can be safely integrated into user-facing applications. While we do not directly address these challenges in this work, an awareness of the limitations of our training data guide our decision not to release for public use. We strongly caution against the use text-to-image generation methods for any user-facing tools without close care and attention to the contents of the training dataset.

's training data was drawn from several pre-existing datasets of image and English alt-text pairs.

A subset of this data was filtered to removed noise and undesirable content, such as pornographic imagery and toxic language.

400 million examples came from FIT400M (https://github.com/google-research/babeldraw/data_cards/fit400m.md , a cleaned version of the internal Alt-Text dataset. This data was filtered to removed noise and undesirable content, such as pornographic imagery and toxic language.

However, a recent audit of one of our data sources, LAION-400M , uncovered a wide range of inappropriate content including pornographic imagery, racist slurs, and harmful social stereotypes . This finding informs our assessment that is not suitable for public use at this time and also demonstrates the value of rigorous dataset audits and comprehensive dataset documentation (e.g. ) in informing consequent decisions about the model's appropriate and safe use. also relies on text encoders trained on uncurated web-scale data, and thus inherits the social biases and limitations of large language models .

While we leave an in-depth empirical analysis of social and cultural biases encoded by to future work, our small scale internal assessments reveal several limitations that guide our decision not to release at this time.

First, all generative models, including ,

, may run into danger of dropping modes of the data distribution, which may further compound the social consequence of dataset bias. Second, exhibits serious limitations when generating images depicting people. Our human evaluations found obtains significantly higher preference rates when evaluated on images that do not portray people, indicating a degradation in image fidelity. Finally, our preliminary assessment also suggests encodes several social biases and stereotypes, including an overall bias towards generating images of people with lighter skin tones and a tendency for images portraying different professions to align with Western gender stereotypes. Even when we focus generations away from people, our preliminary analysis indicates encodes a range of social and cultural biases when generating images of activities, events, and objects.

While there has been extensive work auditing image-to-text and image labeling models for forms of social bias (e.g. ), there has been comparatively less work on social bias evaluation methods for text-to-image models, with the recent exception of . We believe this is a critical avenue for future research and we intend to explore benchmark evaluations for social and cultural bias in future work—for example, exploring whether it is possible to generalize the normalized pointwise mutual information metric to the measurement of biases in image generation models. There is also a great need to develop a conceptual vocabulary around potential harms of text-to-image models that could guide the development of evaluation metrics and inform responsible model release. We aim to address these challenges in future work.

@src https://arxiv.org/abs/2205.11916
@title Large Language Models are Zero-Shot Reasoners
@section Conclusion

We have proposed , a single zero-shot prompt that elicits from large language models across a variety of reasoning tasks, in contrast to the few-shot (in-context) approach in previous work that requires hand-crafting few-shot examples per task.

Our simple method not only is the minimalist and strongest zero-shot baseline for difficult multi-step system-2 reasoning tasks that long evaded the scaling laws of LLMs, but also encourages the community to further discover similar multi-task prompts that elicit broad cognitive abilities instead of narrow task-specific skills.

@src https://arxiv.org/abs/2210.03629
@title ReAct: Synergizing Reasoning and Acting in Language Models
@section Conclusion

We have proposed – a simple yet effective method for synergizing reasoning and acting in large language models. Through a diverse set of experiments on multi-hop question-answering, fact checking, and interactive decision-making tasks, we show that leads to superior performance with interpretable decision traces. Despite the simplicity of our method, complex tasks with large action spaces require more demonstrations to learn well, which unfortunately can easily go beyond the input length limit of in-context learning. We explore the fine-tuning approach on HotpotQA with initial promising results, but learning from more high-quality human annotations will be the desiderata to further improve the performance. Scaling up with multi-task training and combining it with complementary paradigms like reinforcement learning could result in stronger agents that further unlock the potential of LLMs for more applications.

@src https://arxiv.org/abs/2210.08402
@title LAION-5B: An open large-scale dataset for training next generation image-text models
@section Conclusion

By releasing LAION-5B, a larger updated version of an openly available dataset that contains over 5 billion image-text pairs, we have further pushed the scale of open datasets for training and studying state-of-the-art language-vision models. This scale gives strong increases to zero-shot transfer and robustness.

To validate the utility of LAION-5B, we demonstrated that a subset of our dataset can be used to train SOTA CLIP models of various scale that match the strong zero-shot and robustness performance of the original models trained on closed curated data, or to fine-tune generative models like GLIDE, producing samples of good quality. The dataset thus provides opportunities in multi-language large-scale training and research of language-vision models, that were previously restricted to those having access to proprietary large datasets, to the broader research community. Finally, thanks to its large scale, even a rather strict subset filtering (driven by various criterion like NSFW, watermark presence, resolution) provides high-quality datasets that are still large enough to provide sufficient scale for the training or fine-tuning of strong specialized language-vision models.

@src https://arxiv.org/abs/2212.06817
@title RT-1: Robotics Transformer for Real-World Control at Scale
@section Conclusions, Limitations and Future Work

We presented , , a robot learning method that can effectively absorb large amounts of data and scales with data quantity and diversity. We trained on a large dataset of demonstrations containing over 130k episodes collected over the course of 17 months with 13 robots.

In our broad set of experiments, we demonstrated that our method that can perform over 700 instructions at 97% success rate and effectively generalize to new tasks, objects and environments better than previously published baselines.

We also demonstrated that can successfully absorb heterogeneous data from simulation and other robot morphologies without sacrificing original-tasks performance and while improving generalization to new scenarios.

Lastly, we showed how this level of performance and generalization allowed us to execute very long-horizon tasks in the SayCan framework, with as many as 50 steps.

While presents a promising step towards large-scale robot learning with an data-absorbent model, it comes with a number of limitations. First, it is an imitation learning method, which inherits the challenges of that class of approaches such as the fact that it may not be able to surpass the performance of the demonstrators. Second, the generalization to new instructions is limited to the combinations of previously seen concepts and is not yet able to generalize to a completely new motion that has not been seen before. Lastly, our method is presented on a large but not very dexterous set of manipulation tasks. We plan to continue extending the set of instructions that enables and generalizes to to address this challenge.

As we explore future directions for this work, we hope to scale the number of robot skills faster by developing methods that allow non-experts to train the robot via directed data collection and model prompting. While the current version of is fairly robust especially to distractor objects, its robustness to backgrounds and environments could be further improved by greatly increasing the environment diversity. We also hope to improve the reaction speeds and context retention of through scalable attention and memory.

To allow the research community to build on top of this work, we have open-sourced the code for (http://github.com/google-research/robotics_transformer , which we hope will provide researchers with a valuable resource for future research for scaling up robot learning.

@src https://arxiv.org/abs/2212.06817
@title RT-1: Robotics Transformer for Real-World Control at Scale
@section Summary and Analysis

In this section, we summarize some of our findings and propose intuition for 's high performance, generalization, and robustness.

First, ImageNet pretraining (along with Universal Sentence Encoder language embedding) has a large impact particularly on unseen tasks.

We observe that inherits some of the knowledge that results from the generality and diversity of the datasets these models were trained on.

Second, continuous actions have a large impact across all aspects of performance.

This has been previously observed and may be due to

the ability to represent more complex action distributions – the per-dimension discretization allows our model to represent complex multi-modal distributions, while the Gaussian distribution captures only a single mode.

Third, given such expressive multitask models, data diversity has a larger impact than data size.

Indeed, even datasets collected in simulated environments or from different robotic embodiments can be leveraged by , opening avenues for new regimes of data collection.

Finally, fuses language into the image pipeline early via FiLM conditioning, compared to e.g., Gato's late fusion. This enables image tokens that focus only on relevant features for the instruction at hand, which may be the cause of poor distractor performance for Gato.

Figure visualizes the attention during rollouts of .

We see that the attention is focused on relevant features and particularly on interaction between the gripper and the object of interest.

The bottleneck of attention layers such as these results in a compact representation which effectively ignores distractors and varying backgrounds.

@src https://arxiv.org/abs/2301.12597
@title BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models
@section Conclusion

a generic and compute-efficient method for vision-language pre-training that leverages frozen pre-trained image encoders and LLMs.

BLIP-2 achieves state-of-the-art performance on various vision-language tasks while having a small amount of trainable parameters during pre-training.

BLIP-2 also demonstrates emerging capabilities in zero-shot instructed image-to-text generation.

We consider BLIP-2 as an important step towards building a multimodal conversational AI agent.

@src https://arxiv.org/abs/2304.08485
@title Visual Instruction Tuning
@section Conclusion

This paper demonstrated the effectiveness of visual instruction tuning.

We presented an automatic pipeline to create language-image instruction-following data, based on which we train , a multimodal model to follow human intent to complete visual tasks. It achieves the new SoTA accuracy when fine-tuned on ScienceQA, and excellent visual chat capabilities when fine-tuned on multimodal chat data.

Besides, we present the first benchmark to study multimodal instruction-following capability.

This paper is an initial step in visual instruction tuning, and mainly focuses on real-life tasks. For more quantitative results of on academic benchmarks, please refer to the improved baselines with visual instruction tuning . We hope our work can inspire future research on building more capable multimodal models.

We thank Baolin Peng and Pan Lu for valuable discussions on instruction-tuning language models and Science QA, respectively.

We thank the LLaMA team for giving us access to their models, and open-source projects, including Alpaca and Vicuna.

This work was supported in part by NSF CAREER IIS2150012, and Institute of Information & communications Technology Planning & Evaluation(IITP) grants funded by the Korea government(MSIT) (No. 2022-0-00871, Development of AI Autonomy and Knowledge Enhancement for AI Agent Collaboration) and (No. RS-2022-00187238, Development of Large Korean Language Model Technology for Efficient Pre-training).

@src https://arxiv.org/abs/2305.20050
@title Let's Verify Step by Step
@section Conclusion

We have shown that process supervision can be used to train much more reliable reward models than outcome supervision in the domain of mathematical reasoning. We have also shown that active learning can be used to lower the cost of human data collection by surfacing only the most valuable model completions for human feedback. We release PRM800K, the full dataset of human feedback used to train our state-of-the-art reward model, with the hope that removing this significant barrier to entry will catalyze related research on the alignment of large language models. We believe that process supervision is currently under-explored, and we are excited for future work to more deeply investigate the extent to which these methods generalize.

@src https://arxiv.org/abs/2307.15818
@title RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control
@section Conclusions

In this paper, we described how vision-language-action (VLA) models could be trained by combining vision-language model (VLM) pretraining with robotic data. We then presented two instantiations of VLAs based on PaLM-E and PaLI-X, which we call -PaLM-E and -PaLI-X. These models are co-fine-tuned with robotic trajectory data to output robot actions, which are represented as text tokens. We showed that our approach results in very performant robotic policies and, more importantly, leads to a significantly better generalization performance and emergent capabilities inherited from web-scale vision-language pretraining. We believe that this simple and general approach shows a promise of robotics directly benefiting from better vision-language models, which puts the field of robot learning in a strategic position to further improve with advancements in other fields.

@src https://arxiv.org/abs/2310.11511
@title Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection
@section Conclusion

This work introduces , a new framework to enhance the quality and factuality of LLMs through retrieval on demand and self-reflection.

trains an LM to learn to retrieve, generate, and critique text passages and its own generation by predicting the next tokens from its original vocabulary as well as newly added special tokens, called reflection tokens.

further enables the tailoring of LM behaviors at test time by leveraging reflection tokens.

Our holistic evaluations on six tasks using multiple metrics demonstrate that significantly outperforms LLMs with more parameters or with conventional retrieval-augmented generation approaches.

@src https://arxiv.org/abs/2402.13753
@title LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens
@section Conclusion

In this work, we present , a method that remarkably extends the context length of LLMs to an unprecedented 2048k, while maintaining their capabilities within original shorter context window. We exploit two forms of non-uniformities in RoPE positional embedding using an efficient evolutionary search. This offers twofold benefits: it provides good initialization for fine-tuning and enables an 8 MATH context window extension without fine-tuning. Building on this, we propose a progressive extension strategy using 256k-length fine-tuned LLMs to reach a 2048k context window size without extra fine-tuning. Extensive experiments validate the effectiveness of . We envision that our -2048k models will enable many new long context applications and inspire further research.

@src https://arxiv.org/abs/2403.07974
@title LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code
@section Conclusion

In this work, we propose , a new benchmark for evaluating for code.

Our benchmark mitigates contamination issues in existing benchmarks by introducing live evaluations and emphasizing scenarios beyond code generation to account for the broader coding abilities of .

is an extensible framework, that will keep on updating with new problems, scenarios, and models.

Our evaluations reveal novel findings such as contamination detection and potential overfitting on .

We hope with serve to advance understanding of current code and also guide future research in this area through our findings.

@src https://arxiv.org/abs/2407.10671
@title Qwen2 Technical Report
@section Conclusion

This technical report has presented the Qwen2 series, a versatile suite of foundational and instruction-tuned language models, ranging from 0.5 to 72 billion parameters, including models of dense and Mixture-of-Experts architecture.

Qwen2 outperforms previous open-weight models, notably its predecessor Qwen1.5, and displays competitive performance against proprietary models across a broad spectrum of benchmarks in language understanding, generation, multilingual capabilities, coding, mathematics, and reasoning.

In this update, we have extra focus on long-context, multi-lingual, coding, mathematics capabilities and safety and responsibility.

In a commitment to fostering innovation and accessibility within the community, we have made the Qwen2 model weights openly accessible, which enables researchers and developers to harness the full potential of Qwen2 in a variety of applications and research projects. Through these efforts, we aim to contribute to the advancement of AI technologies and their positive impact on society.

@src https://arxiv.org/abs/2408.00714
@title SAM 2: Segment Anything in Images and Videos
@section Conclusion

We present a natural evolution of Segment Anything into the video domain, based on three key aspects: (i) extending the promptable segmentation task to video, (ii) equipping the SAM architecture to use memory when applied to video, and (iii) the diverse SA-V dataset for training and benchmarking video segmentation.

We believe SAM 2 marks a significant advancement in visual perception, positioning our contributions as milestones that will propel further research and applications.

We thank Alexander Kirillov and Jitendra Malik for discussions on project direction. Thanks to Andrew Huang, Sahir Gomez, Miguel Martin, Devansh Kukreja, and Somya Jain for work on the demo, and to Aohan Lin and Meng Wang for creating the dataset visualizer. We thank Shoubhik Debnath and Sagar Vaze for their work on dataset preparation. Thanks also to William Ngan and Sasha Mitts for their design expertise and to Grant Gardner and George Orlin for leading product management. We are grateful to Joelle Pineau, Daniel Bolya, Kate Saenko, Pengchuan Zhang, and Christopher Chedeau, for valuable discussions. Thanks to Rene Martinez Doehner and Baishan Guo for data support, and to our annotation engineering and management partners: Robert Kuo, Rishi Godugu, Bob Kamma, Ida Cheng, Claudette Ward, Kai Brown, Jake Kinney, Jenny Truong, and Karen Bergan. Thanks to Vispi Cassod, Parth Malani, Shiva Koduvayur, Alexander Miller, and Caleb Ho for their support with compute and infra. Finally, we thank Azita Shokrpour, Mallika Malhotra, Rodrick Shepard, Jonathan Torres, Luc Dahlin, David Soofian, Alex Bosenberg, and Amanda Kallet for project-level support.

@src https://arxiv.org/abs/2408.06072
@title CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer
@section Conclusion

In this paper, we present CogVideoX, a state-of-the-art text-to-video diffusion model. It leverages a 3D VAE and an Expert Transformer architecture to generate coherent long duration videos with significant motion. We are also exploring the scaling laws of video generation models and aim to train larger and more powerful models to generate longer and higher-quality videos, pushing the boundaries of what is achievable in text-to-video generation.

@src https://arxiv.org/abs/2408.12528
@title Show-o: One Single Transformer to Unify Multimodal Understanding and Generation
@section Conclusion

This paper proposed a unified transformer, i.e., Show-o, to unify multimodal understanding and generation. Show-o for the first time unified autoregressive and (discrete) diffusion modeling that can handle different modalities in distinct ways. Extensive experimental results demonstrated that Show-o is comparable to even better than individual expert models across a wide range of vision-language tasks. This highlighted its potential as a next-generation foundation model.

@src https://arxiv.org/abs/2410.18072
@title WorldSimBench: Towards Video Generation Models as World Simulators
@section Conclusion

In this work, we classify the functionalities of predictive models into a hierarchy and take the first step in evaluating World Simulators by proposing a dual evaluation framework called .

We conducted a comprehensive evaluation and analysis of multiple video generation models as World Simulators through both and processes.

We summarize key findings from the evaluation and hope these insights will inspire and guide future research on World Simulators.

Limitations. Although we evaluate physical rules and 3D content from the perspective of embodied intelligence, the World Simulator can be applied to more scenarios than just robots, and different scenarios have more physical representations, so how to effectively evaluate the World Simulator in other scenarios requires more exploration.

@src https://arxiv.org/abs/2412.08821
@title Large Concept Models: Language Modeling in a Sentence Representation Space
@section Conclusion and Future Work

Current best practice for large scale language modeling is to operate at the token level, i.e. to learn to predict the next tokens given a sequence of preceding tokens. There is a large body of research on improvements of , but most works concentrate on incremental changes and do not question the main underlying architecture.

In this paper, we have proposed a new architecture, named a ( ), which substantially differs from current in two aspects:

1) all modeling is performed in a high-dimensional embedding space instead of on a discrete token representation;

and 2) modeling is not instantiated in a particular language or modality, but at a higher semantic and abstract level. We have named the general form of this representation a "concept".

In this paper, to verify the feasibility of the high-level idea, we have assumed that a concept corresponds to a sentence in the text domain, or an equivalent speech segment, and that the embeddings are obtained by the freely available sentence encoder . With respect to the specific architecture of the , we have first shown that directly minimizing the MSE loss in the embedding space does not yield good results. We then explored several architectures based on a diffusion process: the and , as well as a which uses quantization of SONAR representations and then modeling on these discrete units.

These ablation experiments were performed with models with 1.6B parameters and focused on the generative task of continuing a sequence of sentences.

We have then scaled our models to a size of 7B parameters and instruction-finetuned them on several summarization and summary expansion tasks. We provide a detailed comparison to other public models of the same size, namely , and .

By design, a exhibits strong zero-shot generalization performance. In this paper, we trained models on English texts only, and applied them to text in other languages, without any additional training data, neither aligned nor unlabeled.

The outperforms on English and on the average over foreign languages officially supported by the .

The itself could also be trained on multilingual- and model data to acquire knowledge from these sources. We will explore this in future versions of the .

In short, all languages and modalities are first class citizens and handled equally at all stages of a .

We have observed that next sentence prediction is substantially more challenging than next token prediction.

First, given that we operate in an embedding space and at a higher semantic level, the number of possible sentences is virtually unlimited, while token vocabularies are usually in the range of 100k. Second, even given a long context, there is unavoidably more ambiguity in choosing the next sentence than the next token. And third, the usual softmax output layer over the fixed size token vocabulary provides a normalized probability distribution over all possible token continuations. Theoretically, a diffusion process should be able to learn a probability distribution over an output embedding space, but our current experimental evidence indicates that more research is needed to take full advantage of the properties of . As an example, the ability to sample multiple embeddings and associate a score would enable beam search to find the best sequence of sentences.

Finally, small modeling errors could yield predictions in the embedding space which do not correspond to valid sentences, i.e. that cannot be decoded into a syntactically and semantically correct sentence. We will work on alternative concept embeddings to which would be better suited to the next sentence prediction task, and would improve modeling approaches in that concept embedding space.

We see the models and results discussed in this paper as a step towards increasing scientific diversity and a move away from current best practice in large scale language modeling.

We acknowledge that there is still a long path to reach the performance of current flagship . This will require of course further improving the core architecture, but also careful data selection and curation, extensive ablations, optimized and diverse instruction fine-tuning, and finally, scaling to models with more than 70B parameters.

We open-source the full training code of all our variants, together with a set of supporting scripts, ( to make it easy for other teams to train models.

By these means, we hope to foster research on alternative and contribute to advance the field of machine intelligence.

Technical consideration for data preparation

Since our modeling approach uses a fixed encoder and a

we decided to use pre-computed embeddings instead

of producing them on-the-fly for each training run. This allows for faster iteration on the same data mix, trading expensive GPU compute against storage capacity.

As we are storing sequences of embedding, which are fixed size tensors of 1024 floats, the storage requirements become more demanding than storing the raw text. For one terra bytes of raw text data we need to store between fifteen and twenty terra bytes of encoded data.

Overall, this trade-off in space vs compute reduces the GPU memory occupation and the compute load and lets use iterate faster.

Typically, with on single GPU we can produce around

300-400 sentence embeddings per second whereas

by loading precomputed data (potentially from remote storage)

we can load over 20 thousand embeddings per second per GPU (with around 15 CPU per GPU).

We store sequences of embeddings with 16 bits precision (FP16) in parquet datasets.

Embeddings remain aligned with the segmented texts and the

parquet binary format and library ecosystem is well suited for storing and loading efficiently such complex data structures. Parquet also lets us store extra data (such as quality metrics for each sentences) and enables non-trivial last mile data filtering and transformation.

For training the , we processed around four billion documents, generating 310 billion sentences with an average of 27 tokens per sentences for 88 characters length on average; totaling a bit more than 889 terra-bytes of raw text.

@src https://arxiv.org/abs/2412.13663
@title Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Finetuning and Inference
@section Conclusion

We present ModernBERT, an open family of encoder-only models which set a new state of the art over existing encoder models on a wide range of classification and retrieval tasks. We show that encoders benefit from both recent pretraining data scales and architecture improvements from autoregressive LLMs.

ModernBERT has a native sequence length of 8,192 tokens and incorporates recent architecture improvements, such as GeGLU layers, RoPE positional embeddings, and alternating local-global attention. ModernBERT is the first open model to feature entire model unpadding and is the first encoder designed in a hardware-aware way to maximize inference efficiency.

ModernBERT pushes the encoder state of the art forward across a wide range of benchmarks. On GLUE, ModernBERT-base is the first encoder to beat DeBERTaV3-base since its release in 2021. ModernBERT is in a class of its own in code and ColBERT-style long-context retrieval benchmarks, scoring at least 6.85 and 9.1 percentage points higher than the closest model, respectively, while remaining state-of-the-art on short-context retrieval in both single and multi-vector settings.

At the same time, ModernBERT processes short context inputs twice as fast as DeBERTaV3 and long-context inputs two times faster than the next fastest model with best-in-class memory efficiency.

ModernBERT is a generational leap over the original encoder models, with notable performance improvements over BERT and RoBERTa on both classification and retrieval tasks. ModernBERT is one of the few encoders to support long-context and programming applications, while simultaneously setting a new record in encoder inference efficiency.

@src https://arxiv.org/abs/2501.12948
@title DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
@section Conclusion, Limitation, and Future Work

We present DeepSeek-R1-Zero and DeepSeek-R1, which rely on large-scale RL to incentivize model reasoning behaviors. Our results demonstrate that pre-trained checkpoints inherently possess substantial potential for complex reasoning tasks. We believe that the key to unlocking this potential lies not in large-scale human annotation but in the provision of hard reasoning questions, a reliable verifier, and sufficient computational resources for reinforcement learning. Sophisticated reasoning behaviors, such as self-verification and reflection, appeared to emerge organically during the reinforcement learning process.

Even if DeepSeek-R1 achieves frontier results on reasoning benchmarks, it still faces several capability limitations, as outlined below:

Currently, the structural output capabilities of DeepSeek-R1 remain suboptimal compared to existing models. Moreover, DeepSeek-R1 cannot leverage tools, such as search engines and calculators, to improve the performance of output. However, as it is not hard to build an RL environment for structure output and tool use, we believe the issue will be addressed in the next version.

Token efficiency: Unlike conventional test-time computation scaling approaches, such as majority voting or Monte Carlo Tree Search (MCTS), DeepSeek-R1 dynamically allocates computational resources during inference according to the complexity of the problem at hand. Specifically, it uses fewer tokens to solve simple tasks, while generating more tokens for complex tasks. Nevertheless, there remains room for further optimization in terms of token efficiency, as instances of excessive reasoning—manifested as overthinking—are still observed in response to simpler questions.

DeepSeek-R1 is currently optimized for Chinese and English, which may result in language mixing issues when handling queries in other languages. For instance, DeepSeek-R1 might use English for reasoning and responses, even if the query is in a language other than English or Chinese. We aim to address this limitation in future updates. The limitation may be related to the base checkpoint, DeepSeek-V3-Base, mainly utilizes Chinese and English, so that it can achieve better results with the two languages in reasoning.

Prompting Engineering: When evaluating DeepSeek-R1, we observe that it is sensitive to prompts. Few-shot prompting consistently degrades its performance. Therefore, we recommend users directly describe the problem and specify the output format using a zero-shot setting for optimal results.

Due to the long evaluation times, which impact the efficiency of the RL process, large-scale RL has not been applied extensively in software engineering tasks. As a result, DeepSeek-R1 has not demonstrated a huge improvement over DeepSeek-V3 on software engineering benchmarks. Future versions will address this by implementing rejection sampling on software engineering data or incorporating asynchronous evaluations during the RL process to improve efficiency.

Beyond specific capability limitations, the pure RL methodology itself also presents inherent challenges:

Reward Hacking: The success of pure RL depends on reliable reward signals. In this study, we ensure reward reliability through a reasoning-domain rule-based reward model (RM). However, such dependable RMs are difficult to construct for certain tasks, such as writing. If the reward signal is assigned by a model instead of predefined rules, it becomes more susceptible to exploitation as training progresses, which means the policy model may find shortcuts to hack the reward model. Consequently, for complex tasks that cannot be effectively evaluated by a reliable reward model, scaling up pure RL methods remains an open challenge.

In this work, for tasks that cannot obtain a reliable signal, DeepSeek-R1 uses human annotation to create supervised data, and only conduct RL for hundreds of steps. We hope in the future, a robust reward model can be obtained to address such issues.

With the advent of pure RL methods like DeepSeek-R1, the future holds immense potential for solving any task that can be effectively evaluated by a verifier, regardless of its complexity for humans. Machines equipped with such advanced RL techniques are poised to surpass human capabilities in these domains, driven by their ability to optimize performance iteratively through trial and error. However, challenges remain for tasks where constructing a reliable reward model is inherently difficult. In such cases, the lack of a robust feedback mechanism may hinder progress, suggesting that future research should focus on developing innovative approaches to define and refine reward structures for these complex, less verifiable problems.

Furthermore, leveraging tools during the reasoning process holds significant promise. Whether it’s utilizing tools like compilers or search engines to retrieve or compute necessary information, or employing external tools—such as biological or chemical reagents, to validate final results in the real world, this integration of tool-augmented reasoning could dramatically enhance the scope and accuracy of machine-driven solutions.

@src https://arxiv.org/abs/2503.14476
@title DAPO: An Open-Source LLM Reinforcement Learning System at Scale
@section Conclusion

In this paper, we release a fully open-sourced system for large-scale LLM RL, including algorithm, code infrastructure, and dataset. The system achieves state-of-the-art large-scale LLM RL performance (AIME 50 using Qwen-32B pretrained model). We propose the Decoupled Clip and Dynamic sAmpling Policy Optimization (DAPO) algorithm, and introduce 4 key techniques to make RL powerfully effective and efficient in the long-CoT RL scenario.

Additionally, by open-sourcing the training code and dataset, we provide the broader research community and society with practical access to a scalable reinforcement learning solution, enabling all to benefit from these advancements.
