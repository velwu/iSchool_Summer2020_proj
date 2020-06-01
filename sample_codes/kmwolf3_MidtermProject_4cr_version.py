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

