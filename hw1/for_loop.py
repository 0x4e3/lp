# coding=utf-8


def main():
    school_scores = [
        {'school_class': '4a', 'scores': [3,4,4,5,2]},
        {'school_class': '4b', 'scores': [2,3,4,5,5]},
        {'school_class': '5c', 'scores': [4,5,2,5,3]},
    ]
    avg_score_for_school = 0
    avg_score_by_grade = {}

    for score_by_grade in school_scores:
        avg_score_by_grade[score_by_grade['school_class']] = \
            sum(score_by_grade['scores'])/len(score_by_grade['scores'])
        avg_score_for_school += \
            avg_score_by_grade[score_by_grade['school_class']]
    avg_score_for_school /= 3
    print(avg_score_for_school, avg_score_by_grade)


if __name__ == "__main__":
    main()
