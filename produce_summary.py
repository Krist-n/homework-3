
def file_clean_and_days_info(day_num, text_file):
    """Cleans file and seperates at |"""
    #print the number of day 
    print("Day", day_num)

    #create variable to open and search different text_files
    delivery_info = open(text_file)

    #for each line in the_file clean white space on right side and seperate (|) 
    for line in delivery_info:
        line = line.rstrip()
        words = line.split('|')
    #locates melon type, amount sold, and total
        melon = words[0]
        count = words[1]
        amount = words[2]
   
    #print info
    print(f"Delivered {count} {melon}s for total of ${amount}")
    #closes file after use
    delivery_info.close()


file_clean_and_days_info(1, "um-deliveries-20140519.txt")
file_clean_and_days_info(2, "um-deliveries-20140520.txt")
file_clean_and_days_info(3, "um-deliveries-20140521.txt")

#First edition vvvv
# the_file = open("um-deliveries-20140519.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()
