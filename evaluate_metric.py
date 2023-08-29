import evaluate
def compute_batch_sentence_BLEU(translation_sentence_list:list, correct_sentence_list:list):
    bleu = evaluate.load("bleu")
    results = bleu.compute(predictions=translation_sentence_list, references=correct_sentence_list)
    return results['bleu']
  
def compute_batch_sentence_CHRF_plus_plus(translation_sentence_list:list, correct_sentence_list:list):
    chrf = evaluate.load("chrf")
    results = chrf.compute(predictions=translation_sentence_list, 
                           references=correct_sentence_list,
                           word_order=2)
    return results['score']
