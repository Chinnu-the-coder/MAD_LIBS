# function to gather information from user for specific placeholder 
def mad_libs(template,placeholders):
    filled_words={}
    # collect user input for each placeholder
    for key in placeholders:
        word=input(f"enter a/an {placeholders[key]}: ")
        filled_words[key]=word
    # fill the templates with the user input
    story=template.format(**filled_words)
    return story

# mad libs story template with placeholders
template="""Once upon a time, there was a {adjective} {noun1} who lived to {verb} everyday. One day,the {noun1} met a {adjective2} {noun2} and they became friends. Togather, they went to {place} and found a {object}."""
# Dictionary for placeholder and what type of words they should have
placeholders = {
    "adjective":"adjective",
    "noun1":"noun",
    "verb":"verb",
    "adjective2":"adjective",
    "noun2":"noun",
    "place":"place",
    "object":"object"
}
# Generate story in the MAD_LIBS
story = mad_libs(template,placeholders)
# Print the result
print("\nhere is your MAD LIBS story")
print (story)