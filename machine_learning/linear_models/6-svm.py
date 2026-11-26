#!/usr/bin/env python3
"""Create an SVM classifier with different kernels."""

from sklearn import svm


def get_SVM_model(name, random_state):
    """Create and return an untrained SVM model."""
    model = svm.SVC(
        kernel=name,
        random_state=random_state
    )
    return model
