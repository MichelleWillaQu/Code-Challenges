def expression(start, end, prefix=False):
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
            result_arr = expression(
                start[digit_counter:], end[digit_counter:], True
            )
            return [group + result for result in result_arr]
        else:
            # No prefix
            remainder = len(start) - 1 or 1
            idx_counter = 0
            while remainder >= 1:
                temp.extend([f"{start[idx_counter]}"] * remainder)
                s = int(start[idx_counter])
                e = int(end[idx_counter])
                if e - 1 != s:
                    if s + 1 == e - 1:
                        temp.append(f"{str(s + 1)}")
                    else:
                        output.append(f"[{str(s + 1)}-{str(e - 1)}]")
                temp.extend([f"{end[idx_counter]}"] * remainder)
                # if result_longer:
                #     for num in range(len(result_arr)):
                #         if num >= 2:
                #             return_arr.append(output[2] + result_arr[num])
                #         else:
                #             return_arr.append(output[num] + result_arr[num])
                # else:
                #     for num in range(len(output)):
                #         if num == 0:
                #             return_arr.append(output[0] + result_arr[0])
                #         elif num == len(output) - 1:
                #             return_arr.append(output[num] + result_arr[1])
                #         else:
                #             return_arr.append(output[num] + "[0-9]")
                remainder -= 1
                idx_counter += 1
                print(
                    "OUT: ", output, "; TEMP: ", temp,
                )
                temp = []
            result_arr = expression(start[(idx_counter):], end[(idx_counter):])
            return output

    else:
        raise ("Hi")


def get_expression(start, end):
    return "|".join(expression(start, end))


# Testing
tests = [
    # ('14', '19', '1[4-9]'),
    # ('14', '25', '1[4-9]|2[0-5]'),
    # ('104', '125', '10[4-9]|11[0-9]|12[0-5]'),
    ("1004", "1215", "100[4-9]|10[1-9][0-9]|11[0-9][0-9]|120[0-9]|121[0-5]"),
    # ('1004', '1350', '100[4-9]|10[1-9][0-9]|1[1-2][0-9]|13[0-4][0-9]|1350'),
    # ('1014', '1214', '101[4-9]|10[2-9][0-9]|11[0-9][0-9]|120[0-9]|121[0-4]')
]
for num, test in enumerate(tests):
    start, end, expected = test
    res = get_expression(start, end)
    status = "SUCCESS" if res == expected else "FAILED"
    print(f"{num}) {start}, {end} -> {expected}, GOT: {res} ({status})")
