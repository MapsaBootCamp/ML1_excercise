import numpy as np


def _check(y_true, y_score, pos_label):
    assert y_true.shape == y_score.shape
    if pos_label is None:
        assert 1 in y_true, 'pos_label is None and there isn\'t any 1 in y_true'
    else:
        assert pos_label in y_true, 'There is no defined pos_label in the y_true'
    
def binary_clf_roc(y_true, y_score, *, pos_label=None):
    _check(y_true, y_score, pos_label)
    if pos_label:
        y_true = y_true == pos_label
    else:
        y_true = y_true == 1
    sorted_inx = np.argsort(y_score)[::-1]
    y_score = y_score[sorted_inx]
    y_true = y_true[sorted_inx]
    threshold_idxs = np.r_[np.where(np.diff(y_score))[0], y_true.size - 1]
    
    tps = np.cumsum(y_true)[threshold_idxs]
    fps = 1 + threshold_idxs - tps
    thresholds = y_score[threshold_idxs]
    tps = np.r_[0, tps]
    fps = np.r_[0, fps]
    thresholds = np.r_[thresholds[0] + 1, thresholds]
    
    fpr = fps / fps[-1]
    tpr = tps / tps[-1]
    return fpr, tpr, thresholds
