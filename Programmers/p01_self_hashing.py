def solution(id_list, report, k):
    illegal_list = []
    illegal_calls = {}
    mailed_peoples = {}
    report_detail_overlap = []
    for people in id_list:
        mailed_peoples[people] = 0
    for report_detail in report:
        r_d = report_detail.split(' ')
        if r_d[1] not in illegal_calls and report_detail not in report_detail_overlap:
            illegal_calls[r_d[1]] = 1
            report_detail_overlap.append(report_detail)
        elif report_detail not in report_detail_overlap:
            illegal_calls[r_d[1]] += 1
            report_detail_overlap.append(report_detail)

    for call in illegal_calls:
        if illegal_calls[call] >= k:
            for report_detail in report_detail_overlap:
                r_d = report_detail.split(' ')
                if r_d[1] == call:
                    mailed_peoples[r_d[0]] += 1

    answer = []
    for people in mailed_peoples:
        answer.append(mailed_peoples[people])
    return answer

# [2,1,1,0]
print(solution(
            ["muzi", "frodo", "apeach", "neo"],
            ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
            2)
)

# [0,0]
print(solution(
            ["con", "ryan"],
            ["ryan con", "ryan con", "ryan con", "ryan con"],
            3)
)