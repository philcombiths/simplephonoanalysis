# -*- coding: utf-8 -*-
"""
#### NOTE: distributions do not include attached diacritics for surrounding context!

Created on Feb 05 2022

@author: Philip

Example use:

# Clean input requested in console. May be spreadsheet format and include
# non IPA. Only delimited IPA will be extracted.
clean_result = cleaninput()

# Use clean input to generate simple distribution info
dist_result = simpledistributions(phones = ['xʷ', 'ʃ'], transcription_string=clean_result)

# Use distributions to determine 'overlapping' or 'complementary'
analysis_result = simplephonoanalysis(dist_result)
             
"""
import re
from collections import namedtuple

def cleaninput(delim="brackets", transcription_string=False):
    """
    Clean an IPA input.
    
    Details: input copied from a document or spreasheet for     
    phonological analysis. Extracts only IPA delineated by delimiters.

    Parameters
    ----------
    delim : STR, optional
        String delimiter for IPA transcriptions. The default is "brackets".
    transcription_string : STR, optional
        String of IPA transcriptions. Can include taps and returns
        as in spreadsheet cells. If none is given, will request input in
        console. The default is False.

    Returns
    -------
    transcription_string : STR
        String of IPA transcriptions. Multiple transcriptions separated 
        by space.

    """
    # Get transcription string
    if not transcription_string:
        transcription_string = input("Enter transcription text: ")
    else:
        # Transcription was passed to transcription_string
        pass
    
    if delim=="brackets":
        transcription_re = r"(\[.+?\])"
        transcription_list = re.findall(transcription_re, transcription_string)
        transcription_list = [re.sub(r"[\[\]]", r"", i) for i in transcription_list]
    if delim=="slashes":
        transcription_re = r"(\/.+?\/)"
        transcription_list = re.findall(transcription_re, transcription_string)
        transcription_list = [re.sub(r"[\/\/]", r"", i) for i in transcription_list]
    if delim=="quotes":
        transcription_re = r"(\".+?\")"
        transcription_list = re.findall(transcription_re, transcription_string)
        transcription_list = [re.sub(r"[\"\"]", r"", i) for i in transcription_list]
    
    transcription_string = ' '.join(transcription_list)
        
    return transcription_string
    

def simpledistributions(phones, transcription_string=False):
    """
    
    Derive simple distribution data.
    
    Details: From list of phones and string of IPA input derives simple 
    distribution data of immediate surrounding context, including word 
    boundaries.

    Parameters
    ----------
    phones : LIST
        List of strings indicating phones to compares. Compound phones
        are permitted.
    transcription_string : STR, optional
        String of IPA transcriptions without brackets or other delimiters.
        Must separate words with whitespace. Tabs or returns acceptable. If 
        none is given, will request input in console. The default is False.

    Returns
    -------
    distributions : TYPE
        DESCRIPTION.

    """
    # Get transcription string
    if not transcription_string:
        transcription_string = input("Enter transcription text: ")
    else:
        # Transcription was passed to transcription_string
        pass
    # Separate words with " "
    transcription_string_spaces = " "+re.sub(r"\s", " ", transcription_string).strip()+" "
    
    # Store results
    Distribution = namedtuple("Distribution", ['phone', 'contexts', 'formatted_contexts'])
    distributions = []
    ## Simple solution
    for phone in phones:
        context_re = re.compile(r"(.)(?:"+phone+r")(.)")
        context_list = re.findall(context_re, transcription_string_spaces)      
        print(f"Phone:{phone}")
        print(context_list)
        # format context_list
        formatted_list = [i[0].replace(' ', '#')+"__"+i[1].replace(' ', '#') for i in context_list]
        print(formatted_list)
        distributions.append(Distribution(phone, context_list, formatted_list))
    
    return distributions

def simplephonoanalysis(distributions):
    """
    
    Determine overlapping or complementary distribution.
    
    Details: From simple distribution data given by simpledistributions, 
    determines type of distribution (overlapping vs. complementary)

    Parameters
    ----------
    distributions : NAMEDTUPLE
        Distribution information from simpledistributions function.

    Returns
    -------
    distribution_type : STR
        'overlapping' or 'complementary'.

    """
    # find distribution type
    distribution_type = 'complementary'
    for phone_list in distributions:
        for dist in phone_list.contexts:
            for i in distributions:
                if i.phone==phone_list.phone:
                    continue
                if dist in i.contexts:
                    distribution_type = 'overlapping'
                    overlap = dist
                    print("Overlap found: ", overlap)
    phonenames=[i.phone for i in distributions]
    print("Result:", [i.phone for i in distributions], 
          "are in", distribution_type, "distribution.")
    return distribution_type
            

trans_string="""ʃɪp
ʃædo
xʷɑːk
xʷʊt
bwʌʃɪŋ
xʷu
bwʌʃ
oʃɪn
ʃɪ̃p
xʷɔːt
ʃep
wɪʃ
mʌxʷum
wɑʃ
tɪxʷu"""

trans_string2="""[kɑ̥tɑ́]
[ku̥su̥ʔwɑ́]
[se̥ʔé]
[ⁿdikí]
[ti̥hí]
[kíʔ]
[sijú]
[sulɑ́]
[lɑʔɑ́]
[loʔó]
[ⁿɡuʃí]
[kinó]
[ki̥sú]
[tijé]
[ʃi̥ʔí]
[tɑ̥ʔɑ́]
[tu̥ʔwɑ́]
[hɑ́ʔ]
"""

trans_string3="""[kɑ̥tɑ]
[ku̥su̥ʔwɑ]
[se̥ʔe]
[ⁿdiki]
[ti̥hi]
[kiʔ]
[siju]
[sulɑ]
[lɑʔɑ]
[loʔo]
[ⁿɡuʃi]
[kino]
[ki̥su]
[tije]
[ʃi̥ʔi]
[tɑ̥ʔɑ]
[tu̥ʔwɑ]
[hɑʔ]
"""

clean_result = cleaninput(transcription_string=trans_string3)
dist_result = simpledistributions(phones = ['i̥', 'i'], transcription_string=clean_result)
analysis_result = simplephonoanalysis(dist_result)