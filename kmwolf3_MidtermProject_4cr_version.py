import string

def clean_line(line_str):
    cleanline = line_str
    for punc in string.punctuation:
        cleanline = cleanline.replace(punc, "")
        # print(cleanline)
    return cleanline

infile = open('dracula.txt', 'r', encoding ='utf-8')
lines = infile.read()
infile.close()

start_toc = lines.index("CONTENTS")
end_toc = lines.index("338") + 3
toc = lines[start_toc:end_toc]
# print(toc)

toc_list = toc.split('\n')

toc_text_lines = []
for list_item in toc_list:
    if len(list_item) > 0:
        toc_text_lines.append(list_item)
# print(toc_text_lines)
# print(len(toc_text_lines))

toc_chapter_titles = []
for num_line in toc_text_lines:
    clean_num = clean_line(num_line).split()
    # print(clean_num)
    last_item = clean_num[-1]
    # print(last_item)
    if last_item.isdigit():
        # print("true")
        # print(last_item)
        last_item = clean_num.pop(-1)
        toc_chapter_titles.append(clean_num)
# print(toc_chapter_titles)

clean_list = []
for toc_title in toc_chapter_titles:
    # print(toc_title)
    remove_space = "_".join(toc_title)
    # print(remove_space)
    clean_list.append(remove_space)
# print(clean_list)

ref_start = lines.index("338")
# print(ref_start)
start = lines.index("CHAPTER", ref_start)
# print(start)
end = lines.index("THE END") + 7
# print(end)
all_chapters = lines[start:end]
# print(all_chapters)

chapter_list = all_chapters.split("CHAPTER")
# print(chapter_list)

clean_chap = []
for chapter in chapter_list:
    # print(chapter)
    if len(chapter) > 0:
        chap_add = "CHAPTER" + chapter
        # print(chap_add)
        clean_chap.append(chap_add)
# print(clean_chap)

filetitle = []
count = 1
for title in clean_list:
    filename = "Dracula-Chapter-" + str(count) + "-" + title + ".txt"
    count = count + 1
    # print(filename)
    filetitle.append(filename)
# print(filetitle)

for i in range(27):
    title = filetitle[i]
    chapter = clean_chap[i]
    outfile = open(title, 'w', encoding='utf-8')
    print(chapter, file = outfile)
    outfile.close()





# Extra stuff I used for help and referencing

# count = 1
# for chapter in clean_chap:
#     # print(chapter)
#     filename = "Dracula-Chapter-" + str(count) + '.txt'
#     outfile = open(filename, 'w', encoding='utf-8')
#     print(chapter, file = outfile)
#     outfile.close()
#     count = count + 1



# pop(0)
#
# for loop over range 27


# # Example from Week08 classdemo for reference
# # makes files names that count up
# animals = ['cat', 'dog', 'shark', 'snake']
#
# count = 1
# for a in animals:
#     filename = a + "-" + str(count) + '.txt'                # avoid concatenate string with int error by making str(count) since count is a string.
#     outfile = open(filename, 'w', encoding='utf-8')
#     print("I like", a + 's', file = outfile)
#     outfile.close()
#     count = count + 1




# # W3 solution as reference- continuation of W2 where we only want the strings ending in a number in a list
# infile = open('dracula.txt', 'r', encoding='utf-8')
# lines = infile.read()
# infile.close()
#
# start = lines.index("CONTENTS")
# end = lines.index("338") + 3
# toc = lines[start:end]
# # print(toc)
#
# toc_list = toc.split('\n')
# toc_text_lines = []
# for list_item in toc_list:       # this was originally l instead of list, but I changed it because l looks way to similar to 1.
#     if len(list_item) > 0:
#         toc_text_lines.append(list_item)
# # print(toc_text_lines)
# # print(len(toc_text_lines))            # end of W2
#
# toc_chapter_titles = []
# for num_line in toc_text_lines:
#     last_item = num_line.split()[-1]
#     if last_item.isdigit():
#         # print("true")
#         # print(last_item)
#         toc_chapter_titles.append(num_line)
# print(toc_chapter_titles)
# print(len(toc_chapter_titles))




# # Example from Week08 classdemo for reference
# animals = ['cat', 'dog', 'shark', 'snake']
# fnames = ['a','b','c','d']
# count = 1
# for a in animals:
#     filename = fnames[count - 1] + "-" + str(count) + '.txt'        # [count - 1] turns count into an index
#     outfile = open(filename, 'w', encoding='utf-8')
#     print("I like", a + 's', file = outfile)
#     outfile.close()
#     count = count + 1
