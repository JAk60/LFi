# from helper.mistral import SentenceExtractor


# ext=SentenceExtractor()
# res=ext.apply_rule("If mission involves direct armed confrontation.","An unidentified missile has been detected on radar, approaching the fleet at high speed. Its trajectory indicates a possible direct impact. All defense systems must be activated immediately to intercept the threat.")
# print(type(res))

import pickle

# Load words from the pickle file
with open('./LFs/checkpoints/auto_trigWords/version3/Sub - mission.pkl', 'rb') as file:
    words = pickle.load(file)

# Print the words
print(words)