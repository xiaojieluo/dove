from dove import utils

def test_markdown():
    filepath = './content/test.md'
    md = utils.Markdown(filepath)
    print(md.stream)
    # print(md)
