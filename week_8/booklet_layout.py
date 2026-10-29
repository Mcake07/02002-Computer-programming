def booklet_layout(content_pages):
    if content_pages % 4 == 0:
        empty_pages = 0
    else: 
        empty_pages = 4 - (content_pages % 4)
    total_pages = content_pages + empty_pages
    return total_pages, empty_pages