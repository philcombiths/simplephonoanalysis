# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 09:44:36 2021

@author: Philip

Outline:
    input transcriptions as a string. Can be multiple rows.
    input segments as list of strings to search for distributions
    for each segment
        Generate empty list to store contexts for segment
        extract each instance of preceding and following context as a labelled dictionary
        format each instance of surrounding context and append to list
             
"""
import re

def simplephonoanalysis(phones, transcription_string=True):
    # Get transcription string
    if transcription_string:
        transcription_string = input("Enter transcription text: ")
    else:
        # Transcription was passed to transcription_string
        pass
    # Separate words with " "
    transcription_string_spaces = " "+re.sub(r"\s", r" ", transcription_string).strip()+" "
    ## Simple solution
    for phone in phones:
        context_re = re.compile(r"(.)(?:"+phone+r")(.)")
        context_list = re.findall(context_re, transcription_string_spaces)
        print(f"Phone:{phone}")
        print(context_list)
        
    return context_list
    
    """
    ## More complex solution - in progress
    # Generate result dictionary
    phone_distribution_dict = dict()
    
    for phone in phones:
        context_dict = dict()
        phone_distribution_dict[phone] = context_dict
        pre_context_list = re.findall()
    """

result = simplephonoanalysis(phones = ['c', 'k', 'x'])