from config_shield import ConfigShield, Alert
import pytest
import time

def test_detect_hallucination():
    config_shield = ConfigShield()
    response = "This is a test response."
    confidence = {'hallucination': 0.9, 'toxicity': 0.1}
    alert = config_shield.detect(response, confidence)
    assert alert.text_snippet == response
    assert alert.config_profile_id == 'default'

def test_detect_toxicity():
    config_shield = ConfigShield()
    response = "This is a test response."
    confidence = {'hallucination': 0.1, 'toxicity': 0.9}
    alert = config_shield.detect(response, confidence)
    assert alert.text_snippet == response
    assert alert.config_profile_id == 'default'

def test_detect_below_threshold():
    config_shield = ConfigShield()
    response = "This is a test response."
    confidence = {'hallucination': 0.7, 'toxicity': 0.7}
    alert = config_shield.detect(response, confidence)
    assert alert is None

def test_latency():
    config_shield = ConfigShield()
    response = "This is a test response."
    confidence = {'hallucination': 0.9, 'toxicity': 0.1}
    start_time = time.time()
    config_shield.detect(response, confidence)
    end_time = time.time()
    assert end_time - start_time < 0.2

def test_false_positive_rate():
    config_shield = ConfigShield()
    responses = ["This is a test response."] * 100
    confidences = [{'hallucination': 0.7, 'toxicity': 0.7} for _ in range(100)]
    false_positives = 0
    for response, confidence in zip(responses, confidences):
        alert = config_shield.detect(response, confidence)
        if alert:
            false_positives += 1
    assert false_positives <= 10
