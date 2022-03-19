book_pages = int(input())
pages_read_1hr = int(input())
days_to_read_the_book = int(input())

time_to_read = book_pages / pages_read_1hr
final_time_to_read = time_to_read / days_to_read_the_book

print(int(final_time_to_read))

