def expression(start, end, prefix=True):
    if start == "" and end == "":
        return [""]
    output = []
    temp = []
    group = ""
    if len(start) == len(end):
        if len(start) == 1 and prefix:
            # Came from the same prefix
            return [f"[{start[0]}-{end[0]}]"]
        elif len(start) == 1:
            if start[0] == "9":
                output.append("9")
            else:
                output.append(f"[{start[0]}-9]")
            if end[0] == "0":
                output.append("0")
            else:
                output.append(f"[0-{end[0]}]")
            return output
        digit_counter = 0
        if start[0] == end[0]:
            # There is a prefix
            while (
                digit_counter < len(start)
                and start[digit_counter] == end[digit_counter]
            ):
                group += f"{start[digit_counter]}"
                digit_counter += 1
            result_arr = expression(start[digit_counter:], end[digit_counter:])
            return [group + result for result in result_arr]
        else:
            # when no more prefix
            # To middle
            counter = len(start) - 1
            output.append(f"{start[0:counter]}")
            while counter > 0:
                output.append()
            # Middle - will always be just one group
            s = int(start[0])
            e = int(end[0])
            if e - 1 != s:
                if e - 1 == s + 1:
                    output.append(f"{end[0]-1}" + "[0-9]" * (len(start) - 1))
                else:
                    output.append(
                        f"[{start[0]+1}-{end[0]+1}]"
                        + "[0-9]" * (len(start) - 1)
                    )
            # End

            return output

    else:
        # Probably?
        new_start = "0" * (len(end) - len(start)) + start
        return expression(new_start, end, False)


def get_expression(start, end):
    return "|".join(expression(start, end))


# Testing
tests = [
    # ("0", "6", "[0-6]"),
    # ("5", "9", "[5-9]"),
    # ("3", "8", "[3-8]"),
    # ('14', '19', '1[4-9]'),
    # ('14', '25', '1[4-9]|2[0-5]'),
    # ('104', '125', '10[4-9]|11[0-9]|12[0-5]'),
    ("1004", "1215", "100[4-9]|10[1-9][0-9]|11[0-9][0-9]|120[0-9]|121[0-5]"),
    # ('1004', '1350', '100[4-9]|10[1-9][0-9]|1[1-2][0-9]|13[0-4][0-9]|1350'),
    # ('1014', '1214', '101[4-9]|10[2-9][0-9]|11[0-9][0-9]|120[0-9]|121[0-4]'),
    # ('13489', '18029',
    # '13489|1349[0-9]|13[5-9][0-9][0-9]|1[4-7][0-9][0-9][0-9]|180[0-1][0-9]|1802[0-9]'),
    # ('13489', '18479',
    # '13489|1349[0-9]|13[5-9][0-9][0-9]|1[4-7][0-9][0-9][0-9]|18[0-7][0-9][0-9][0-9]|184[0-6][0-9]|1847[0-9]'),
    # ('20040', '51092',
    # '2004[0-9]|200[5-9][0-9]|20[0-9][0-9][0-9]|2[0-9][0-9][0-9][0-9]|[3-4][0-9][0-9][0-9][0-9]|50[0-9][0-9][0-9]|510[0-8][0-9]|5109[0-2]'),
]
for num, test in enumerate(tests):
    start, end, expected = test
    res = get_expression(start, end)
    status = "SUCCESS" if res == expected else "FAILED"
    print(f"{num}) {start}, {end} -> {expected}, GOT: {res} ({status})")


# Bleh stuff
# remainder = len(start) - 1 or 1
# idx_counter = 0
# while remainder >= 1:
#     temp.extend([f"{start[idx_counter]}"] * remainder)
#     s = int(start[idx_counter])
#     e = int(end[idx_counter])
#     if e - 1 != s:
#         if s + 1 == e - 1:
#             temp.append(f"{str(s + 1)}")
#         else:
#             output.append(f"[{str(s + 1)}-{str(e - 1)}]")
#     temp.extend([f"{end[idx_counter]}"] * remainder)
#     # if result_longer:
#     #     for num in range(len(result_arr)):
#     #         if num >= 2:
#     #             return_arr.append(output[2] + result_arr[num])
#     #         else:
#     #         return_arr.append(output[num] + result_arr[num])
#     # else:
#     #     for num in range(len(output)):
#     #         if num == 0:
#     #             return_arr.append(output[0] + result_arr[0])
#     #         elif num == len(output) - 1:
#     #             return_arr.append(output[num] + result_arr[1])
#     #         else:
#     #             return_arr.append(output[num] + "[0-9]")
#     remainder -= 1
#     idx_counter += 1
#     print(
#         "OUT: ", output, "; TEMP: ", temp,
#     )
#     temp = []
# result_arr = expression(
#     start[(idx_counter):], end[(idx_counter):], False
# )
