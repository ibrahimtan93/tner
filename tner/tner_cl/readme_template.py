template = """
---
tags:
- generated_from_trainer
datasets:
- conll2003
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: twitter-roberta-base-dec2021-CoNLL
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9552512940390716
    - name: Recall
      type: recall
      value: 0.9628071356445641
    - name: F1
      type: f1
      value: 0.9590143324113654
    - name: Accuracy
      type: accuracy
      value: 0.9926599431486313
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# twitter-roberta-base-dec2021-CoNLL

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base-dec2021](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2021) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0412
- Precision: 0.9553
- Recall: 0.9628
- F1: 0.9590
- Accuracy: 0.9927

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 64
- eval_batch_size: 1024
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 0.11  | 25   | 0.2126          | 0.5639    | 0.6067 | 0.5845 | 0.9349   |
| No log        | 0.23  | 50   | 0.0849          | 0.8259    | 0.8612 | 0.8431 | 0.9765   |
| No log        | 0.34  | 75   | 0.0640          | 0.8752    | 0.8957 | 0.8853 | 0.9820   |
| No log        | 0.45  | 100  | 0.0572          | 0.8848    | 0.9034 | 0.8940 | 0.9832   |
| No log        | 0.57  | 125  | 0.0469          | 0.9071    | 0.9239 | 0.9155 | 0.9866   |
| No log        | 0.68  | 150  | 0.0442          | 0.9198    | 0.9278 | 0.9238 | 0.9877   |
| No log        | 0.8   | 175  | 0.0424          | 0.9192    | 0.9322 | 0.9256 | 0.9881   |
| No log        | 0.91  | 200  | 0.0407          | 0.9170    | 0.9414 | 0.9291 | 0.9891   |
| No log        | 1.02  | 225  | 0.0402          | 0.9264    | 0.9403 | 0.9333 | 0.9894   |
| No log        | 1.14  | 250  | 0.0399          | 0.9329    | 0.9446 | 0.9387 | 0.9897   |
| No log        | 1.25  | 275  | 0.0384          | 0.9278    | 0.9413 | 0.9345 | 0.9897   |
| No log        | 1.36  | 300  | 0.0363          | 0.9379    | 0.9477 | 0.9427 | 0.9906   |
| No log        | 1.48  | 325  | 0.0362          | 0.9380    | 0.9493 | 0.9436 | 0.9905   |
| No log        | 1.59  | 350  | 0.0364          | 0.9397    | 0.9497 | 0.9447 | 0.9905   |
| No log        | 1.7   | 375  | 0.0367          | 0.9324    | 0.9475 | 0.9399 | 0.9899   |
| No log        | 1.82  | 400  | 0.0372          | 0.9350    | 0.9460 | 0.9404 | 0.9899   |
| No log        | 1.93  | 425  | 0.0339          | 0.9411    | 0.9514 | 0.9462 | 0.9909   |
| No log        | 2.05  | 450  | 0.0336          | 0.9419    | 0.9529 | 0.9474 | 0.9911   |
| No log        | 2.16  | 475  | 0.0336          | 0.9447    | 0.9537 | 0.9492 | 0.9914   |
| 0.079         | 2.27  | 500  | 0.0345          | 0.9420    | 0.9566 | 0.9492 | 0.9914   |
| 0.079         | 2.39  | 525  | 0.0364          | 0.9436    | 0.9522 | 0.9479 | 0.9913   |
| 0.079         | 2.5   | 550  | 0.0340          | 0.9479    | 0.9514 | 0.9496 | 0.9916   |
| 0.079         | 2.61  | 575  | 0.0339          | 0.9481    | 0.9559 | 0.9520 | 0.9917   |
| 0.079         | 2.73  | 600  | 0.0396          | 0.9326    | 0.9504 | 0.9414 | 0.9902   |
| 0.079         | 2.84  | 625  | 0.0348          | 0.9461    | 0.9544 | 0.9502 | 0.9915   |
| 0.079         | 2.95  | 650  | 0.0359          | 0.9419    | 0.9527 | 0.9473 | 0.9908   |
| 0.079         | 3.07  | 675  | 0.0347          | 0.9434    | 0.9573 | 0.9503 | 0.9916   |
| 0.079         | 3.18  | 700  | 0.0351          | 0.9464    | 0.9566 | 0.9515 | 0.9918   |
| 0.079         | 3.3   | 725  | 0.0370          | 0.9446    | 0.9536 | 0.9491 | 0.9911   |
| 0.079         | 3.41  | 750  | 0.0358          | 0.9462    | 0.9583 | 0.9522 | 0.9917   |
| 0.079         | 3.52  | 775  | 0.0353          | 0.9483    | 0.9564 | 0.9523 | 0.9920   |
| 0.079         | 3.64  | 800  | 0.0351          | 0.9469    | 0.9564 | 0.9516 | 0.9916   |
| 0.079         | 3.75  | 825  | 0.0361          | 0.9479    | 0.9579 | 0.9529 | 0.9919   |
| 0.079         | 3.86  | 850  | 0.0370          | 0.9498    | 0.9581 | 0.9539 | 0.9918   |
| 0.079         | 3.98  | 875  | 0.0374          | 0.9460    | 0.9574 | 0.9517 | 0.9915   |
| 0.079         | 4.09  | 900  | 0.0381          | 0.9506    | 0.9594 | 0.9550 | 0.9922   |
| 0.079         | 4.2   | 925  | 0.0415          | 0.9460    | 0.9557 | 0.9509 | 0.9912   |
| 0.079         | 4.32  | 950  | 0.0390          | 0.9493    | 0.9556 | 0.9524 | 0.9917   |
| 0.079         | 4.43  | 975  | 0.0389          | 0.9483    | 0.9591 | 0.9536 | 0.9919   |
| 0.0123        | 4.55  | 1000 | 0.0379          | 0.9464    | 0.9569 | 0.9516 | 0.9918   |
| 0.0123        | 4.66  | 1025 | 0.0376          | 0.9463    | 0.9579 | 0.9521 | 0.9920   |
| 0.0123        | 4.77  | 1050 | 0.0373          | 0.9499    | 0.9571 | 0.9535 | 0.9917   |
| 0.0123        | 4.89  | 1075 | 0.0366          | 0.9520    | 0.9584 | 0.9552 | 0.9923   |
| 0.0123        | 5.0   | 1100 | 0.0374          | 0.9488    | 0.9606 | 0.9547 | 0.9923   |
| 0.0123        | 5.11  | 1125 | 0.0393          | 0.9516    | 0.9589 | 0.9552 | 0.9920   |
| 0.0123        | 5.23  | 1150 | 0.0389          | 0.9539    | 0.9603 | 0.9571 | 0.9925   |
| 0.0123        | 5.34  | 1175 | 0.0397          | 0.9486    | 0.9576 | 0.9531 | 0.9917   |
| 0.0123        | 5.45  | 1200 | 0.0397          | 0.9478    | 0.9569 | 0.9523 | 0.9919   |
| 0.0123        | 5.57  | 1225 | 0.0388          | 0.9483    | 0.9593 | 0.9537 | 0.9920   |
| 0.0123        | 5.68  | 1250 | 0.0389          | 0.9502    | 0.9606 | 0.9554 | 0.9923   |
| 0.0123        | 5.8   | 1275 | 0.0380          | 0.9547    | 0.9616 | 0.9582 | 0.9925   |
| 0.0123        | 5.91  | 1300 | 0.0391          | 0.9496    | 0.9603 | 0.9549 | 0.9924   |
| 0.0123        | 6.02  | 1325 | 0.0381          | 0.9548    | 0.9603 | 0.9575 | 0.9924   |
| 0.0123        | 6.14  | 1350 | 0.0400          | 0.9529    | 0.9596 | 0.9562 | 0.9922   |
| 0.0123        | 6.25  | 1375 | 0.0393          | 0.9544    | 0.9616 | 0.9580 | 0.9927   |
| 0.0123        | 6.36  | 1400 | 0.0419          | 0.9514    | 0.9621 | 0.9567 | 0.9924   |
| 0.0123        | 6.48  | 1425 | 0.0415          | 0.9532    | 0.9626 | 0.9579 | 0.9925   |
| 0.0123        | 6.59  | 1450 | 0.0415          | 0.952     | 0.9613 | 0.9566 | 0.9923   |
| 0.0123        | 6.7   | 1475 | 0.0399          | 0.9542    | 0.9611 | 0.9577 | 0.9925   |
| 0.0052        | 6.82  | 1500 | 0.0416          | 0.9522    | 0.9591 | 0.9556 | 0.9921   |
| 0.0052        | 6.93  | 1525 | 0.0410          | 0.9502    | 0.9599 | 0.9550 | 0.9919   |
| 0.0052        | 7.05  | 1550 | 0.0406          | 0.9507    | 0.9613 | 0.9560 | 0.9921   |
| 0.0052        | 7.16  | 1575 | 0.0400          | 0.9508    | 0.9603 | 0.9555 | 0.9923   |
| 0.0052        | 7.27  | 1600 | 0.0402          | 0.9525    | 0.9618 | 0.9571 | 0.9924   |
| 0.0052        | 7.39  | 1625 | 0.0401          | 0.9550    | 0.9633 | 0.9591 | 0.9925   |
| 0.0052        | 7.5   | 1650 | 0.0397          | 0.9555    | 0.9647 | 0.9601 | 0.9927   |
| 0.0052        | 7.61  | 1675 | 0.0412          | 0.9526    | 0.9610 | 0.9568 | 0.9922   |
| 0.0052        | 7.73  | 1700 | 0.0419          | 0.9531    | 0.9616 | 0.9574 | 0.9923   |
| 0.0052        | 7.84  | 1725 | 0.0407          | 0.9555    | 0.9621 | 0.9588 | 0.9927   |
| 0.0052        | 7.95  | 1750 | 0.0409          | 0.9551    | 0.9628 | 0.9589 | 0.9927   |
| 0.0052        | 8.07  | 1775 | 0.0413          | 0.9520    | 0.9616 | 0.9568 | 0.9924   |
| 0.0052        | 8.18  | 1800 | 0.0414          | 0.9505    | 0.9605 | 0.9555 | 0.9923   |
| 0.0052        | 8.3   | 1825 | 0.0410          | 0.9542    | 0.9605 | 0.9573 | 0.9924   |
| 0.0052        | 8.41  | 1850 | 0.0417          | 0.9553    | 0.9599 | 0.9576 | 0.9924   |
| 0.0052        | 8.52  | 1875 | 0.0418          | 0.9545    | 0.9606 | 0.9576 | 0.9923   |
| 0.0052        | 8.64  | 1900 | 0.0414          | 0.9544    | 0.9616 | 0.9580 | 0.9924   |
| 0.0052        | 8.75  | 1925 | 0.0419          | 0.9555    | 0.9620 | 0.9587 | 0.9925   |
| 0.0052        | 8.86  | 1950 | 0.0415          | 0.9544    | 0.9611 | 0.9577 | 0.9926   |
| 0.0052        | 8.98  | 1975 | 0.0413          | 0.9542    | 0.9611 | 0.9577 | 0.9926   |
| 0.0027        | 9.09  | 2000 | 0.0412          | 0.9553    | 0.9628 | 0.9590 | 0.9927   |
| 0.0027        | 9.2   | 2025 | 0.0408          | 0.9554    | 0.9630 | 0.9592 | 0.9927   |
| 0.0027        | 9.32  | 2050 | 0.0404          | 0.9545    | 0.9613 | 0.9579 | 0.9926   |
| 0.0027        | 9.43  | 2075 | 0.0407          | 0.9557    | 0.9618 | 0.9587 | 0.9926   |
| 0.0027        | 9.55  | 2100 | 0.0410          | 0.9552    | 0.9618 | 0.9585 | 0.9926   |
| 0.0027        | 9.66  | 2125 | 0.0412          | 0.9552    | 0.9620 | 0.9586 | 0.9925   |
| 0.0027        | 9.77  | 2150 | 0.0413          | 0.9557    | 0.9621 | 0.9589 | 0.9925   |
| 0.0027        | 9.89  | 2175 | 0.0413          | 0.9557    | 0.9621 | 0.9589 | 0.9925   |
| 0.0027        | 10.0  | 2200 | 0.0413          | 0.9557    | 0.9621 | 0.9589 | 0.9925   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0
- Datasets 2.3.2
- Tokenizers 0.12.1
"""