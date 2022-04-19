# 5.HTML
# You will receive lines of input:
# On the first line, you will receive a title of an article
# On the second line, you will receive the content of that article
# On the following lines, until you receive "end of comments" you will get the comments about the article
# Print the whole information in html format:
# The title should be in "h1" tag (<h1></h1>)
# The content in article tag (<article></article>)
# Each comment should be in div tag (<div></div>)
# For more clarification see the example below.
#
# Input
# SoftUni Article
# Some content of the SoftUni article
# some comment
# more comment
# last comment
# end of comments
#
# Output
# <h1>
#     SoftUni Article
# </h1>
# <article>
#     Some content of the SoftUni article
# </article>
# <div>
#     some comment
# </div>
# <div>
#     more comment
# </div>
# <div>
#     last comment
# </div>

article_title = input()
article_content = input()

article_list = [article_title, article_content]

while True:
    line = input()
    if line == "end of comments":
        break
    article_list.append(line)

print(f"""<h1>
    {article_list[0]}
</h1>""")
print(f"""<article>
    {article_list[1]}
</article>""")
for i in range(2, len(article_list)):
    print(f"""<div>
    {article_list[i]}
</div>""")
