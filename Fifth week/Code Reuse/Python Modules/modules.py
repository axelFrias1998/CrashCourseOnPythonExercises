import random
import datetime

print(random.randint(1, 10))

print(random.randint(1, 10))

print(random.randint(2, 10))

print(datetime.datetime.now())

print(datetime.datetime.now() + datetime.timedelta(days=28))
#print(help(datetime.datetime))

# This is the uploader widget

#def _upload():

#    _upload_widget = fileupload.FileUploadWidget()
#
#    def _cb(change):
#        global file_contents
#        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
#        filename = change['owner'].filename
#        print('Uploaded `{}` ({:.2f} kB)'.format(
#            filename, len(decoded.read()) / 2 **10))
#        file_contents = decoded.getvalue()
#
#    _upload_widget.observe(_cb, names='data')
#    display(_upload_widget)

#_upload()

#def calculate_frequencies(file_contents):
#    # Here is a list of punctuations and uninteresting words you can use to process your text
punctuations = '''.!()-[]{};:'"\,<>/?@#$%^&*_~'''
uninteresting_words = ["de", "the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
"we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
"their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
"have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
"all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE


def generate_from_frequencies(file_contents):
    words = {}
    file_words = file_contents.split()
    for word in file_words:
        if word not in uninteresting_words:
            for letter in word:
                if letter in punctuations:
                    word = word.replace(letter, '')
            if len(word) > 0:
                if not word.lower() in words:
                    words[word.lower()] = 0
                words[word.lower()] += 1
    print(words)

generate_from_frequencies("Prueba. () . de T!exto de muchos de caracteres de prueba .")