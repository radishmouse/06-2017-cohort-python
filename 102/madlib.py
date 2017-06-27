instruction_text = '''Please fill in the blanks below:
____(name)____'s favorite subject in school is ____(subject)____.
'''

name_prompt = 'What is name? '
subject_prompt = 'What is subject? '

final_text = "%s's favorite subject in school is %s."

print instruction_text

name = raw_input(name_prompt)
subject = raw_input(subject_prompt)

print final_text % (name, subject)