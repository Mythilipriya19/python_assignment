
def highest():
    score=[50, 20, 80,90]
    first=score[0]
    runner=0
    for i in score:
        if i > first:
            runner=first
            first=i
    return runner
